import argparse
import base64
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    from cryptography.fernet import Fernet, InvalidToken
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
except ImportError:
    Fernet = None
    InvalidToken = None
    hashes = None
    PBKDF2HMAC = None

PROJECT_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = PROJECT_DIR / 'config'
CONFIG_FILE = CONFIG_DIR / 'config.json'
KEY_FILE = CONFIG_DIR / '.encryption_key'
SALT_FILE = CONFIG_DIR / '.salt'

SENSITIVE_FIELDS = ('login.password', 'headers.cookie', 'email_smtp_password')
ENC_PREFIX = 'ENC('
KDF_ITERATIONS = 480000
MASK = '******'


def _configure_stdio() -> None:
    """将标准输出与错误输出切换为 UTF-8，避免 Windows 控制台中文乱码"""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding='utf-8', errors='replace')
        except (AttributeError, ValueError):
            pass


class CryptoTool:
    """配置加解密工具 - 与 main.py 的 SecureConfigManager 共用同一套密钥与密文格式"""

    def __init__(self, config_file: Path = CONFIG_FILE, key_file: Path = KEY_FILE, salt_file: Path = SALT_FILE) -> None:
        """
        初始化工具实例

        Args:
            config_file: 配置文件路径，默认 config/config.json
            key_file: 密钥文件路径，默认 config/.encryption_key
            salt_file: 盐值文件路径，默认 config/.salt
        """
        self.config_file = Path(config_file)
        self.key_file = Path(key_file)
        self.salt_file = Path(salt_file)
        self._fernet: Optional[Any] = None

    def available(self) -> bool:
        """
        检查 cryptography 依赖是否可用

        Returns:
            依赖齐全返回 True，缺失返回 False
        """
        return Fernet is not None and PBKDF2HMAC is not None and hashes is not None

    def _load_fernet(self) -> Any:
        """
        加载 Fernet 实例（优先环境变量主密码，其次密钥文件）

        Returns:
            已初始化的 Fernet 实例

        Raises:
            RuntimeError: 依赖缺失、盐值缺失或密钥文件缺失
        """
        if self._fernet is not None:
            return self._fernet
        if not self.available():
            raise RuntimeError('cryptography 库未安装，请运行: pip install cryptography')
        env_key = os.environ.get('CONFIG_ENCRYPTION_KEY')
        if env_key:
            if not self.salt_file.exists():
                raise RuntimeError(f'缺少盐值文件: {self.salt_file}')
            salt = self.salt_file.read_bytes()
            kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=KDF_ITERATIONS)
            key = base64.urlsafe_b64encode(kdf.derive(env_key.encode()))
        elif self.key_file.exists():
            key = self.key_file.read_bytes()
        else:
            raise RuntimeError(f'缺少密钥文件: {self.key_file}，请先执行 init 命令')
        self._fernet = Fernet(key)
        return self._fernet

    def encrypt_value(self, plaintext: str) -> str:
        """
        加密单段明文

        Args:
            plaintext: 待加密明文

        Returns:
            ENC(...) 格式密文

        Raises:
            RuntimeError: 密钥不可用
        """
        token = self._load_fernet().encrypt(str(plaintext).encode())
        return f'{ENC_PREFIX}{token.decode()})'

    def decrypt_value(self, encrypted_text: str) -> str:
        """
        解密单段密文，非 ENC(...) 格式原样返回

        Args:
            encrypted_text: 待解密文本

        Returns:
            解密后的明文；入参非密文时原样返回

        Raises:
            RuntimeError: 密钥不可用或密钥与密文不匹配
        """
        text = str(encrypted_text)
        if not (text.startswith(ENC_PREFIX) and text.endswith(')')):
            return text
        fernet = self._load_fernet()
        payload = text[len(ENC_PREFIX):-1].encode()
        try:
            return fernet.decrypt(payload).decode()
        except Exception as exc:
            if InvalidToken is not None and isinstance(exc, InvalidToken):
                raise RuntimeError('解密失败: 当前密钥与该密文不匹配')
            raise RuntimeError(f'解密失败: {type(exc).__name__}: {exc}')

    @staticmethod
    def _get_nested(data: Dict[str, Any], path: str) -> Any:
        """
        按点分路径读取嵌套字段

        Args:
            data: 配置字典
            path: 形如 login.password 的点分路径

        Returns:
            字段值，路径不存在返回 None
        """
        current = data
        for key in path.split('.'):
            if not isinstance(current, dict) or key not in current:
                return None
            current = current[key]
        return current

    @staticmethod
    def _set_nested(data: Dict[str, Any], path: str, value: Any) -> None:
        """
        按点分路径写入嵌套字段，中间层级不存在时自动创建

        Args:
            data: 配置字典
            path: 形如 login.password 的点分路径
            value: 待写入值
        """
        keys = path.split('.')
        current = data
        for key in keys[:-1]:
            if not isinstance(current.get(key), dict):
                current[key] = {}
            current = current[key]
        current[keys[-1]] = value

    def load_config(self) -> Dict[str, Any]:
        """
        读取 config.json 原始内容（不自动解密）

        Returns:
            配置字典

        Raises:
            RuntimeError: 配置文件不存在或 JSON 解析失败
        """
        if not self.config_file.exists():
            raise RuntimeError(f'配置文件不存在: {self.config_file}')
        with open(self.config_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_config(self, config: Dict[str, Any]) -> None:
        """
        原子写入 config.json（先写临时文件再替换）

        Args:
            config: 待写入配置字典

        Raises:
            RuntimeError: 写入或替换失败
        """
        tmp = self.config_file.with_name(self.config_file.name + '.tmp')
        with open(tmp, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        os.replace(tmp, self.config_file)

    def encrypt_config(self) -> List[str]:
        """
        批量加密敏感字段中的明文（幂等，已是密文的字段跳过）

        Returns:
            本次实际加密的字段路径列表

        Raises:
            RuntimeError: 配置文件或密钥不可用
        """
        config = self.load_config()
        changed = []
        for field in SENSITIVE_FIELDS:
            value = self._get_nested(config, field)
            if isinstance(value, str) and value and not value.startswith(ENC_PREFIX):
                self._set_nested(config, field, self.encrypt_value(value))
                changed.append(field)
        if changed:
            self.save_config(config)
        return changed

    def decrypt_config(self) -> Tuple[List[Tuple[str, str, str]], List[str], List[Tuple[str, str]]]:
        """
        检查敏感字段的加密状态

        Returns:
            (成功解密项列表, 仍为明文的字段列表, 解密失败项列表)
            成功解密项为 (字段路径, 密文, 明文) 三元组

        Raises:
            RuntimeError: 配置文件不可用
        """
        config = self.load_config()
        entries: List[Tuple[str, str, str]] = []
        failures: List[Tuple[str, str]] = []
        plaintext_fields: List[str] = []
        for field in SENSITIVE_FIELDS:
            value = self._get_nested(config, field)
            if not isinstance(value, str) or not value:
                continue
            if not value.startswith(ENC_PREFIX):
                plaintext_fields.append(field)
                continue
            try:
                entries.append((field, value, self.decrypt_value(value)))
            except RuntimeError as exc:
                failures.append((field, str(exc)))
        return entries, plaintext_fields, failures

    def initialize(self, password: str) -> Tuple[bool, str]:
        """
        初始化加密系统，生成 .salt 与 .encryption_key

        Args:
            password: 主密码，至少 8 个字符

        Returns:
            (是否成功, 结果说明)

        Raises:
            OSError: 密钥或盐值文件写入失败
        """
        if not self.available():
            return False, 'cryptography 库未安装，请运行: pip install cryptography'
        if len(password) < 8:
            return False, '密码长度至少需要 8 个字符'
        if self.key_file.exists():
            return False, (
                f'加密系统已初始化（密钥已存在: {self.key_file}），'
                '重建会导致现有密文失效'
            )
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=KDF_ITERATIONS)
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        self.key_file.parent.mkdir(parents=True, exist_ok=True)
        self.salt_file.write_bytes(salt)
        self.key_file.write_bytes(key)
        self._fernet = None
        return True, f'加密系统初始化完成（密钥: {self.key_file}，盐值: {self.salt_file}）'


def build_parser() -> argparse.ArgumentParser:
    """
    构建命令行参数解析器

    Returns:
        已注册全部子命令的 ArgumentParser
    """
    parser = argparse.ArgumentParser(
        prog='crypto_tool.py',
        description='配置加密解密工具（与 main.py 的 SecureConfigManager 共用同一套密钥）',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python config/crypto_tool.py decrypt-config show
  python config/crypto_tool.py encrypt "你的新密码"
  python config/crypto_tool.py decrypt "ENC(gAAAAABq...)"
  python config/crypto_tool.py encrypt-config
  python config/crypto_tool.py init --password 你的主密码
""",
    )
    subparsers = parser.add_subparsers(dest='command')

    encrypt_parser = subparsers.add_parser('encrypt', help='加密一段明文，输出 ENC(...) 字符串')
    encrypt_parser.add_argument('plaintext', help='待加密的明文')

    decrypt_parser = subparsers.add_parser('decrypt', help='解密单个 ENC(...) 字符串')
    decrypt_parser.add_argument('encrypted', help='ENC(...) 密文')

    init_parser = subparsers.add_parser('init', help='初始化加密系统，生成 .salt 与 .encryption_key')
    init_parser.add_argument('--password', '-p', required=True, help='主密码（至少 8 个字符）')

    subparsers.add_parser('encrypt-config', help='批量加密 config.json 中的明文字段')

    decrypt_config_parser = subparsers.add_parser(
        'decrypt-config',
        help='查看 config.json 中敏感字段的加解密情况'
    )
    decrypt_config_parser.add_argument('action', nargs='?', choices=['show'], help='show: 显示解密后的明文')
    decrypt_config_parser.add_argument('--show', action='store_true', help='显示解密后的明文')

    return parser


def main() -> int:
    """
    命令行入口

    Returns:
        进程退出码，0 表示成功，1 表示失败
    """
    _configure_stdio()
    parser = build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    tool = CryptoTool()

    if args.command == 'encrypt':
        try:
            print(f'{tool.encrypt_value(args.plaintext)}')
            return 0
        except RuntimeError as exc:
            print(f'❌ {exc}')
            return 1

    if args.command == 'decrypt':
        try:
            print(f'{tool.decrypt_value(args.encrypted)}')
            return 0
        except RuntimeError as exc:
            print(f'❌ {exc}')
            return 1

    if args.command == 'init':
        success, message = tool.initialize(args.password)
        print(f"{'✅' if success else '❌'} {message}")
        return 0 if success else 1

    if args.command == 'encrypt-config':
        try:
            changed = tool.encrypt_config()
        except RuntimeError as exc:
            print(f'❌ {exc}')
            return 1
        if changed:
            print(f'✅ 成功加密 {len(changed)} 个敏感字段')
            for field in changed:
                print(f'   🔒 {field}')
        else:
            print('✅ 没有需要加密的明文字段')
        return 0

    if args.command == 'decrypt-config':
        show = bool(args.show or args.action == 'show')
        try:
            entries, plaintext_fields, failures = tool.decrypt_config()
        except RuntimeError as exc:
            print(f'❌ {exc}')
            return 1
        for field, encrypted, plaintext in entries:
            print(f'📋 {field}:')
            print(f'   加密值: {encrypted}')
            print(f'   解密值: {plaintext if show else f"{MASK}（使用 decrypt-config show 查看明文）"}')
        if plaintext_fields:
            print('⚠️ 以下字段仍为明文，可执行 encrypt-config 加密:')
            for field in plaintext_fields:
                print(f'   🔓 {field}')
        for field, reason in failures:
            print(f'❌ {field}: {reason}')
        if not entries and not plaintext_fields and not failures:
            print('ℹ️ 配置文件中未找到需要处理的敏感字段')
        return 1 if failures else 0

    parser.print_help()
    return 0


if __name__ == '__main__':
    sys.exit(main())