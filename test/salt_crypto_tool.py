# -*- coding: utf-8 -*-
"""
Salt文件加密解密工具
用于管理config/.salt文件和config.json的敏感字段加解密

功能：
1. 初始化加密系统（生成salt和key）
2. 加密/解密config.json中的敏感字段
3. 验证加密状态
4. 重新加密（更换密码）

遵循 UTF-8 编码 + 简体中文规范
"""

import os
import sys
import json
import base64
from pathlib import Path
from typing import Optional, Tuple, Dict, Any

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False
    print("⚠️ 警告: cryptography库未安装，请运行: pip install cryptography")

PROJECT_DIR = Path(__file__).parent.parent
CONFIG_DIR = PROJECT_DIR / 'config'
SALT_FILE = CONFIG_DIR / '.salt'
KEY_FILE = CONFIG_DIR / '.encryption_key'
CONFIG_FILE = CONFIG_DIR / 'config.json'

# 敏感字段列表（与main.py保持一致）
_SENSITIVE_CONFIG_FIELDS = [
    'cookie.token',
    'cookie.session',
    'database.password',
    'api.secret_key',
    'auth.jwt_secret',
]


class SaltCryptoTool:
    """Salt加密解密工具类"""

    def __init__(self):
        self._fernet: Optional[Fernet] = None

    def initialize_encryption(self, password: str) -> Tuple[bool, str]:
        """
        初始化加密系统（生成salt和key）

        Args:
            password: 加密密码（至少8个字符）

        Returns:
            (成功状态, 消息)
        """
        if not CRYPTO_AVAILABLE:
            return False, 'cryptography库未安装'

        if KEY_FILE.exists():
            return True, '加密系统已初始化'

        if not password or len(password) < 8:
            return False, '密码长度至少需要8个字符'

        try:
            # 1. 生成随机salt (16字节)
            salt = os.urandom(16)
            print(f"✅ 已生成随机Salt ({len(salt)}字节)")

            # 2. 使用PBKDF2HMAC从密码派生密钥
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=480000
            )
            key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
            print(f"✅ 已从密码派生Fernet Key ({len(key)}字节)")

            # 3. 保存salt和key文件
            CONFIG_DIR.mkdir(parents=True, exist_ok=True)
            self._write_bytes(KEY_FILE, key)
            self._write_bytes(SALT_FILE, salt)
            print(f"✅ Salt已保存到: {SALT_FILE}")
            print(f"✅ Key已保存到: {KEY_FILE}")

            # 4. 初始化Fernet实例
            self._fernet = Fernet(key)

            # 5. 自动加密config.json中的敏感字段
            if CONFIG_FILE.exists():
                self._encrypt_config_file()
                print("✅ config.json敏感字段已自动加密")

            return True, '加密系统初始化成功'

        except Exception as e:
            return False, f'初始化失败: {e}'

    def load_encryption_key(self, password: Optional[str] = None) -> bool:
        """
        加载已有的加密密钥

        Args:
            password: 可选的环境变量密码（如果使用环境变量方式）

        Returns:
            是否加载成功
        """
        if not CRYPTO_AVAILABLE:
            print("❌ cryptography库未安装")
            return False

        # 方式1: 从环境变量获取
        env_key = os.environ.get('CONFIG_ENCRYPTION_KEY')
        if env_key and SALT_FILE.exists():
            try:
                with open(SALT_FILE, 'rb') as f:
                    salt = f.read()
                kdf = PBKDF2HMAC(
                    algorithm=hashes.SHA256(),
                    length=32,
                    salt=salt,
                    iterations=480000
                )
                key = base64.urlsafe_b64encode(kdf.derive(env_key.encode()))
                self._fernet = Fernet(key)
                print("✅ 从环境变量加载加密密钥成功")
                return True
            except Exception as e:
                print(f"❌ 环境变量密钥加载失败: {e}")

        # 方式2: 从key文件获取
        if KEY_FILE.exists():
            try:
                with open(KEY_FILE, 'rb') as f:
                    key = f.read()
                self._fernet = Fernet(key)
                print("✅ 从key文件加载加密密钥成功")
                return True
            except Exception as e:
                print(f"❌ Key文件加载失败: {e}")

        print("❌ 无法加载加密密钥")
        return False

    def encrypt_value(self, value: str) -> str:
        """加密单个值"""
        if not self._fernet:
            raise RuntimeError("加密器未初始化，请先调用initialize_encryption或load_encryption_key")

        encrypted = self._fernet.encrypt(value.encode())
        return f"ENC({encrypted.decode()})"

    def decrypt_value(self, encrypted_value: str) -> str:
        """解密单个值"""
        if not encrypted_value.startswith("ENC("):
            return encrypted_value

        if not self._fernet:
            raise RuntimeError("加密器未初始化")

        try:
            encrypted = encrypted_value[4:-1]
            return self._fernet.decrypt(encrypted.encode()).decode()
        except Exception as e:
            print(f"⚠️ 解密失败: {e}")
            return ""

    def encrypt_config_file(self) -> Tuple[bool, str]:
        """
        加密config.json中的所有敏感字段

        Returns:
            (成功状态, 消息)
        """
        if not CONFIG_FILE.exists():
            return False, 'config.json不存在'

        if not self._fernet:
            if not self.load_encryption_key():
                return False, '加密器未初始化'

        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                config = json.load(f)

            encrypted_count = 0
            for field_path in _SENSITIVE_CONFIG_FIELDS:
                value = self._get_nested(config, field_path)
                if value and not str(value).startswith("ENC("):
                    self._set_nested(config, field_path, self.encrypt_value(str(value)))
                    encrypted_count += 1
                    print(f"  🔒 已加密: {field_path}")

            self._write_json(CONFIG_FILE, config)
            return True, f'成功加密{encrypted_count}个敏感字段'

        except Exception as e:
            return False, f'加密失败: {e}'

    def decrypt_config_file(self) -> Tuple[bool, str]:
        """
        解密config.json中的所有敏感字段（用于查看/编辑）

        Returns:
            (成功状态, 消息)
        """
        if not CONFIG_FILE.exists():
            return False, 'config.json不存在'

        if not self._fernet:
            if not self.load_encryption_key():
                return False, '加密器未初始化'

        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                config = json.load(f)

            decrypted_count = 0
            for field_path in _SENSITIVE_CONFIG_FIELDS:
                value = self._get_nested(config, field_path)
                if value and str(value).startswith("ENC("):
                    decrypted_value = self.decrypt_value(str(value))
                    if decrypted_value:
                        self._set_nested(config, field_path, decrypted_value)
                        decrypted_count += 1
                        print(f"  🔓 已解密: {field_path}")

            self._write_json(CONFIG_FILE, config)
            return True, f'成功解密{decrypted_count}个敏感字段'

        except Exception as e:
            return False, f'解密失败: {e}'

    def check_encryption_status(self) -> Dict[str, Any]:
        """
        检查加密状态

        Returns:
            状态字典
        """
        status = {
            'crypto_available': CRYPTO_AVAILABLE,
            'salt_exists': SALT_FILE.exists(),
            'key_exists': KEY_FILE.exists(),
            'config_exists': CONFIG_FILE.exists(),
            'encrypted_fields': [],
            'plaintext_fields': [],
            'total_sensitive': len(_SENSITIVE_CONFIG_FIELDS)
        }

        if CONFIG_FILE.exists():
            try:
                with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                    config = json.load(f)

                for field_path in _SENSITIVE_CONFIG_FIELDS:
                    value = self._get_nested(config, field_path)
                    if value:
                        if str(value).startswith("ENC("):
                            status['encrypted_fields'].append(field_path)
                        else:
                            status['plaintext_fields'].append(field_path)
            except Exception as e:
                status['error'] = str(e)

        return status

    def reencrypt_with_new_password(self, old_password: str, new_password: str) -> Tuple[bool, str]:
        """
        使用新密码重新加密（需要旧密码验证）

        Args:
            old_password: 旧密码
            new_password: 新密码（至少8个字符）

        Returns:
            (成功状态, 消息)
        """
        if not new_password or len(new_password) < 8:
            return False, '新密码长度至少需要8个字符'

        # 1. 先用旧密码解密所有字段
        if not self.load_encryption_key(old_password):
            return False, '旧密码验证失败'

        success, msg = self.decrypt_config_file()
        if not success:
            return False, f'解密失败: {msg}'

        # 2. 删除旧的salt和key文件
        if KEY_FILE.exists():
            KEY_FILE.unlink()
        if SALT_FILE.exists():
            SALT_FILE.unlink()

        # 3. 用新密码重新初始化并加密
        return self.initialize_encryption(new_password)

    def _get_nested(self, obj: Dict, path: str) -> Any:
        """获取嵌套字典值"""
        keys = path.split('.')
        current = obj
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None
        return current

    def _set_nested(self, obj: Dict, path: str, value: Any):
        """设置嵌套字典值"""
        keys = path.split('.')
        current = obj
        for key in keys[:-1]:
            if key not in current or not isinstance(current[key], dict):
                current[key] = {}
            current = current[key]
        current[keys[-1]] = value

    @staticmethod
    def _write_bytes(filepath: Path, data: bytes):
        """写入二进制文件"""
        with open(filepath, 'wb') as f:
            f.write(data)

    @staticmethod
    def _write_json(filepath: Path, data: Dict):
        """写入JSON文件"""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


def print_status(status: Dict):
    """打印加密状态报告"""
    print("\n" + "=" * 60)
    print("📊 加密状态报告")
    print("=" * 60)

    print(f"\n🔐 加密库: {'✅ 已安装' if status['crypto_available'] else '❌ 未安装'}")
    print(f"🧂 Salt文件: {'✅ 存在' if status['salt_exists'] else '❌ 不存在'}")
    print(f"🔑 Key文件: {'✅ 存在' if status['key_exists'] else '❌ 不存在'}")
    print(f"📄 Config文件: {'✅ 存在' if status['config_exists'] else '❌ 不存在'}")

    print(f"\n📋 敏感字段统计:")
    print(f"   总计: {status['total_sensitive']} 个")
    print(f"   ✅ 已加密: {len(status['encrypted_fields'])} 个")
    print(f"   ❌ 未加密: {len(status['plaintext_fields'])} 个")

    if status['encrypted_fields']:
        print(f"\n   已加密字段:")
        for field in status['encrypted_fields']:
            print(f"     🔒 {field}")

    if status['plaintext_fields']:
        print(f"\n   ⚠️ 未加密字段:")
        for field in status['plaintext_fields']:
            print(f"     🔓 {field}")

    print("\n" + "=" * 60)


def main():
    """主函数 - 命令行接口"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Salt文件加密解密工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  # 初始化加密系统
  py salt_crypto_tool.py init --password mysecretpassword

  # 查看加密状态
  py salt_crypto_tool.py status

  # 加密config.json
  py salt_crypto_tool.py encrypt

  # 解密config.json（查看明文）
  py salt_crypto_tool.py decrypt

  # 更换密码
  py salt_crypto_tool.py reencrypt --old-password oldpass --new-password newpass

环境变量方式:
  export CONFIG_ENCRYPTION_KEY="your-password"
  py salt_crypto_tool.py encrypt
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='可用命令')

    # init 命令
    init_parser = subparsers.add_parser('init', help='初始化加密系统')
    init_parser.add_argument('--password', '-p', required=True, help='加密密码（至少8个字符）')

    # status 命令
    subparsers.add_parser('status', help='查看加密状态')

    # encrypt 命令
    subparsers.add_parser('encrypt', help='加密config.json')

    # decrypt 命令
    subparsers.add_parser('decrypt', help='解密config.json')

    # reencrypt 命令
    reencrypt_parser = subparsers.add_parser('reencrypt', help='更换加密密码')
    reencrypt_parser.add_argument('--old-password', required=True, help='当前密码')
    reencrypt_parser.add_argument('--new-password', required=True, help='新密码')

    args = parser.parse_args()

    tool = SaltCryptoTool()

    if args.command == 'init':
        success, msg = tool.initialize_encryption(args.password)
        print(f"{'✅' if success else '❌'} {msg}")
        sys.exit(0 if success else 1)

    elif args.command == 'status':
        status = tool.check_encryption_status()
        print_status(status)

    elif args.command == 'encrypt':
        success, msg = tool.encrypt_config_file()
        print(f"{'✅' if success else '❌'} {msg}")
        sys.exit(0 if success else 1)

    elif args.command == 'decrypt':
        success, msg = tool.decrypt_config_file()
        print(f"{'✅' if success else '❌'} {msg}")
        print("⚠️ 注意: 解密后请及时重新加密！")
        sys.exit(0 if success else 1)

    elif args.command == 'reencrypt':
        success, msg = tool.reencrypt_with_new_password(args.old_password, args.new_password)
        print(f"{'✅' if success else '❌'} {msg}")
        sys.exit(0 if success else 1)

    else:
        parser.print_help()


if __name__ == '__main__':
    main()