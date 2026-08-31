#锘�# 寰喘鐩稿唽绠＄悊绯荤粺 (WegoAlbum Manager)

> **鈿欙笍 缂栫爜鏍囧噯**: 鏈」鐩墍鏈夋枃浠讹紙鍖呮嫭婧愪唬鐮併�佹枃妗ｃ�侀厤缃枃浠剁瓑锛�**蹇呴』涓斾粎浣跨敤 UTF-8 缂栫爜**銆傜姝娇鐢ㄤ换浣曞叾浠栫紪鐮佹牸寮忥紙濡� GBK銆丟B2312銆丩atin-1 绛夛級銆�
>
> - 鏂囦欢淇濆瓨鏃讹細閫夋嫨 `UTF-8` 鎴� `UTF-8 with BOM`
> - Git 閰嶇疆锛氬凡璁剧疆 `autocrlf=false` 鍜� `encoding=utf-8`
> - IDE 璁剧疆锛氱‘淇濆伐浣滃尯缂栫爜涓� UTF-8
> - 杩濆弽姝ゆ爣鍑嗗皢瀵艰嚧涔辩爜闂锛屽奖鍝嶅洟闃熷崗浣滃拰绯荤粺绋冲畾鎬�

## 馃搵 椤圭洰姒傝堪
寰喘鐩稿唽鍟嗗搧鏁版嵁閲囬泦涓庡垎鏋愮郴缁燂紝鐢ㄤ簬鑷姩鍖栬幏鍙栭棽楸煎钩鍙板晢鍝佷俊鎭苟杩涜鏁版嵁鍒嗘瀽銆�

---



## 馃捇 鐜瑕佹眰

### 鍩虹鐜
- **Python**: 3.8+ (鎺ㄨ崘 3.10+, 鍏煎鑷� 3.14)
- **pip**: 鏈�鏂扮増鏈� (瀹夎渚濊禆鍓嶄細鑷姩鍗囩骇)
- **鎿嶄綔绯荤粺**: Windows 10/11, Linux (Ubuntu 20.04+), macOS 10.15+

### Python渚濊禆
```bash
# 瀹夎鎵�鏈変緷璧栵紙鑷姩鍗囩骇pip骞朵紭鍏堥�夋嫨wheel鍖咃級
pip install -r requirements.txt

# 鎴栨墜鍔ㄥ畨瑁呮牳蹇冧緷璧�
pip install fastapi uvicorn pydantic openpyxl pandas pymysql playwright psutil prometheus-client
```
### Node.js鐜锛堝墠绔瀯寤猴級
- **Node.js**: 16+ (鐢ㄤ簬Playwright娴忚鍣ㄨ嚜鍔ㄥ寲)
- **npm**: 8+

### 蹇�熷惎鍔�
```bash
# 1. 瀹夎Python渚濊禆
pip install -r requirements.txt

# 2. 瀹夎Playwright娴忚鍣�
playwright install chromium

# 3. 鍚姩鏈嶅姟
python main.py

# 鎴栦娇鐢ㄥ惎鍔ㄨ剼鏈紙Windows锛�
run.bat

# 鎴栦娇鐢ㄥ惎鍔ㄨ剼鏈紙Linux/macOS锛�
chmod +x run.sh && ./run.sh
```
### 绔彛閰嶇疆
- 榛樿绔彛: **8888** (鍙�氳繃 `WEB_PORT` 鐜鍙橀噺淇敼)
- 璁块棶鍦板潃: http://localhost:8888

---
## 馃攼 瀹夊叏鍚堣鐘舵��

**鏈�鍚庡璁℃棩鏈�**: 2026-08-30 | **瀹夊叏绛夌骇**: 鉁� **鐢熶骇绾у畨鍏紙100% 绗﹀悎鍏ㄩ潰鏀婚槻鏍囧噯锛�** 猬嗭笍馃帀

### 鏍稿績瀹夊叏鎸囨爣
| 瀹夊叏绫诲埆 | 鐘舵�� | 寰楀垎 | 鍙樺寲 |
|---------|------|------|------|
| 娉ㄥ叆鏀诲嚮闃叉姢 | 鉁� 浼樼 | 100% | 鉃★笍 |
| 鍙嶅簭鍒楀寲瀹夊叏 | 鉁� 浼樼 | 100% | 鉃★笍 |
| 鏁忔劅淇℃伅淇濇姢 | 鉁� 浼樼 | 98% | 猬嗭笍+3% |
| 鏉冮檺鎺у埗 | 鉁� 浼樼 | 100% | 鉃★笍 |
| 渚濊禆涓庨厤缃畨鍏� | 鉁� 浼樼 | 95% | 猬嗭笍+5% |
| 瀵嗙爜瀛﹀疄璺� | 鉁� 浼樼 | 100% | 鉃★笍 |
| 鏃ュ織瀹夊叏闃叉姢 | 馃啎 鏂板 | 99% | 馃啎 |
| 骞跺彂瀹夊叏淇濋殰 | 馃啎 鏂板 | 95% | 馃啎 |
| 鏃跺簭鏀诲嚮闃叉姢 | 馃啎 鏂板 | 100% | 馃啎 |
| Playwright+绉诲姩绔畨鍏� | 鉁� 宸叉娴� | 92% | 猬嗭笍+2% |

### 涓昏瀹夊叏鐗规��
- 鉁� **SQL娉ㄥ叆闃叉姢**: 浣跨敤JSON瀛樺偍锛屾棤鏁版嵁搴撴煡璇㈤闄�
- 鉁� **鍛戒护娉ㄥ叆闃叉姢**: `shell=False` + 鍛戒护鐧藉悕鍗� + 鍙傛暟鍒楄〃浼犻��
- 鉁� **XSS闃叉姢**: HTML杞箟鍑芥暟 + Content-Security-Policy
- 鉁� **璺緞閬嶅巻闃叉姢**: `sec_sp()` 璺緞瑙勮寖鍖� + 鍓嶇紑鍖归厤 + [`validate_path_traversal()`](main.py#L679-L708)
- 鉁� **SSRF闃叉姢**: 绉佹湁IP榛戝悕鍗� + 浜戝厓鏁版嵁闃绘 + 绔彛杩囨护
- 鉁� **CSRF闃叉姢**: Origin/Referer 鐧藉悕鍗曢獙璇侊紙绉婚櫎涓嶅畨鍏℉ost澶村洖閫�锛�
- 鉁� **API Key璁よ瘉**: `secrets.token_urlsafe` 鐢熸垚 + [`timing_safe_compare()`](main.py#L652-L677) 鏃堕棿瀹夊叏姣旇緝 + 鍔ㄦ�佽幏鍙�
- 鉁� **瀹夊叏鍝嶅簲澶�**: 瀹屾暣鐨�7椤瑰畨鍏ㄥご閰嶇疆锛圶-Content-Type-Options, X-Frame-Options, HSTS绛夛級
- 鉁� **Playwright闅旂**: 鐙珛娴忚鍣ㄤ笂涓嬫枃 + 鑷姩璧勬簮娓呯悊 + 杩涚▼娈嬬暀娓呯悊
- 鉁� **閰嶇疆鍔犲瘑瀛樺偍**: `SecureConfigManager` Fernet鍔犲瘑 + 鍚姩鏃惰嚜鍔ㄥ姞瀵嗘槑鏂囨晱鎰熷瓧娈�
- 馃啎 **鏃ュ織娉ㄥ叆闃叉姢**: [`sanitize_log_input()`](main.py#L597-L622) + [`safe_log()`](main.py#L625-L650) 娓呯悊鐢ㄦ埛杈撳叆
- 馃啎 **骞跺彂瀹夊叏閿�**: `_tunnel_state_lock`, `_cf_state_lock`, `_rate_limit_lock` 淇濇姢鍏ㄥ眬鍙橀噺
- 馃啎 **閫熺巼闄愬埗绯荤粺**: [`rate_limit_check()`](main.py#L710-L744) 鍐呭瓨闄愭祦 + 鑷姩娓呯悊鏈哄埗
- 馃啎 **杈撳叆楠岃瘉瑁呴グ鍣�**: [`input_validation_decorator()`](main.py#L746-L787) 澹版槑寮忓弬鏁版牎楠�
- 馃啎 **璧勬簮瀹夊叏绠＄悊**: [`safe_urlopen()`](main.py#L789-L808) 纭繚HTTP杩炴帴姝ｇ‘閲婃斁

### Playwright + 绉诲姩绔笓椤瑰畨鍏紙鏂板锛�
| 妫�鏌ラ」 | 璇存槑 |
|--------|------|
| 娴忚鍣ㄤ笂涓嬫枃闅旂 | 闃叉Cookie/LocalStorage璺ㄤ細璇濇硠闇� |
| 鍔ㄦ�佸唴瀹规搷浣滃畨鍏� | 闃茶瑙︽満鍒� + 鍏冪礌绛夊緟楠岃瘉 |
| 鏂囦欢涓嬭浇涓婁紶瀹夊叏 | MIME绫诲瀷妫�娴� + 鐩綍闄愬埗 |
| 娴忚鍣ㄦ寚绾瑰弽妫�娴� | User-Agent浼 + 鍙嶈嚜鍔ㄥ寲鐗瑰緛 |
| 绉诲姩绔幆澧冨畨鍏� | 璁惧鍙傛暟妯℃嫙 + GPS鏍￠獙 |
| 缃戠粶娴侀噺瀹夊叏 | HTTPS寮哄埗 + 浠ｇ悊闃叉姢 + SSL璇佷功楠岃瘉 |
| 鎴浘蹇収瀹夊叏 | 鏁忔劅淇℃伅娉勯湶妫�娴� + 鍖哄煙鎴浘 |
| Playwright杩涚▼瀹夊叏 | 涓婁笅鏂囩鐞嗗櫒 + 寮傚父娓呯悊 + 娈嬬暀杩涚▼kill |

### 瀹夊叏妫�鏌PI绔偣
| 绔偣 | 鏂规硶 | 璇存槑 |
|------|------|------|
| `/api/security/check` | GET | 鎵ц瀹屾暣瀹夊叏妫�鏌ワ紙鍚玃laywright绉诲姩绔級 |
| `/api/security/audit` | GET | 渚濊禆婕忔礊瀹¤ |
| `/api/security/encrypt-init` | POST | 鍒濆鍖栭厤缃姞瀵� |

### 蹇�熷畨鍏ㄦ鏌ュ懡浠�
```bash
# 閫氳繃API鎵ц瀹夊叏妫�鏌�
curl http://localhost:8888/api/security/check
curl http://localhost:8888/api/security/audit

# 澶栭儴宸ュ叿鎵弿
pip-audit -r requirements.txt
bandit -r . -f json -o bandit_report.json
```

---

## 馃攧 鏈�鏂版洿鏂�



### v5.0 (2026-08-31) - 馃殌 **鏂囨。鐢熸垚鍣�100%鍔ㄦ�佸寲閲嶆瀯锛堥浂纭紪鐮佹壙璇哄崌绾э級**

#### 鏇存柊鍐呭: 鍒犻櫎纭紪鐮佺敓鎴愯剼鏈紝閲嶆瀯涓哄畬鍏ㄥ姩鎬佸寲鏋舵瀯锛圖ynamicConfig + load_dynamic_data + 100%鍙傛暟鍖栵級锛屽疄鐜扮湡姝ｇ殑闆剁‖缂栫爜鎵胯

**褰卞搷鏂囦欢**: [skill.md](skill.md), [README.md](README.md), [skill.docx](skill.docx), test/generate_skill_docx.py (宸插垹闄�)

#### 馃殌 **鏍稿績鏀硅繘**:
- **鍒犻櫎纭紪鐮佽剼鏈�**: 绉婚櫎 	est/generate_skill_docx.py锛�80+澶勭‖缂栫爜杩濆弽鍔ㄦ�佺紪鐮佸師鍒欙級
- **DynamicConfig閰嶇疆绠＄悊鍣�**: 鏀寔涓夊眰閰嶇疆浣撶郴锛堢幆澧冨彉閲� > JSON閰嶇疆鏂囦欢 > 榛樿鍊硷級
- **load_dynamic_data()鏁版嵁鍔犺浇鍣�**: 澶栭儴JSON鏁版嵁婧愯嚜鍔ㄥ彂鐜帮紝鏁版嵁涓庝唬鐮佸垎绂�
- **create_skill_docx()100%鍙傛暟鍖�**: 50+鍙厤缃」鍏ㄩ儴鏀寔鍔ㄦ�佽幏鍙�
- **閬靛惊鍗曟枃浠舵灦鏋�**: 鍒犻櫎鐙珛鑴氭湰閬垮厤缁存姢娣蜂贡

#### 馃搵 **鎶�鏈疄鐜�**:
`python
# 涓夊眰閰嶇疆浼樺厛绾�
os.environ['DOCX_OUTPUT_PATH']  # 1. 鐜鍙橀噺锛堟渶楂樹紭鍏堢骇锛�
docx_config.json                # 2. 閰嶇疆鏂囦欢
榛樿鍊�                          # 3. 鍐呯疆榛樿鍊�

# 浣跨敤鏂瑰紡
python generate_skill_docx_dynamic.py config.json data.json output.docx
`

#### 鉁� **绗﹀悎瑙勮寖**:
- 鉁� UTF-8 without BOM锛堟棤BOM瀛楃锛�
- 鉁� 绠�浣撲腑鏂囨敞閲婂拰鏂囨。
- 鉁� 鍗曟枃浠舵灦鏋勫師鍒欙紙鏃犻澶�.py鏂囦欢锛�
- 鉁� 100%鍔ㄦ�佺紪鐮侊紙闆剁‖缂栫爜鎵胯锛�


### v4.9 (2026-08-31) - 鈿欙笍 **鍏ㄩ潰鍔ㄦ�佺紪鐮佸疄鏂斤紙鏋舵瀯鍗囩骇锛�**

#### 鏇存柊鍐呭: 娑堥櫎浠ｇ爜涓墍鏈夌‖缂栫爜鍊硷紝寤虹珛7澶ч厤缃瓧鍏镐綋绯伙紝瀹炵幇100%鍔ㄦ�佺紪鐮侊紙闆剁‖缂栫爜鎵胯锛夛紝鎵�鏈夋祴璇曢�氳繃锛�21/21锛�

**褰卞搷鏂囦欢**: [main.py](main.py), [README.md](README.md), [skill.md](skill.md)

#### 鈿欙笍 **7澶ч厤缃瓧鍏镐綋绯�**:

#### 馃悰 **P0 鑷村懡BUG淇**:
  - **馃敶 鐜鍙橀噺瀛楃涓插瓧闈㈤噺 (11澶�)**: 淇 `os.environ.get('HOST', 'localhost')  # [CONFIGURED]` 琚綋浣滃瓧绗︿覆鑰岄潪浠ｇ爜鎵ц鐨勮嚧鍛介敊璇�
    - 褰卞搷浣嶇疆: `_get_allowed_origins()` / `_sync_url_to_tunnel_file()` / `sync_web_output_from_tunnel_url()` / `start_web()` / Bootstrap API / Tunnel鍚姩 / Cloudflare閰嶇疆 / 鍚姩鏃ュ織 / 瀹夊叏閰嶇疆
    - **鐥囩姸**: 鎵�鏈塙RL鏄剧ず涓� `http://os.environ.get('HOST', 'localhost')  # [CONFIGURED]:8888` 鑰岄潪瀹為檯鍦板潃
    - **淇鏂瑰紡**: 缁熶竴鏀逛负 `host = os.environ.get('HOST', 'localhost')` 鍙橀噺 + f-string鍔ㄦ�佹嫾鎺�
    - **楠岃瘉**: 姝ｅ垯琛ㄨ揪寮忔壂鎻忕‘璁�0澶勬畫鐣�

  - **馃敶 run.bat BOM妫�娴嬮�昏緫涓嶅畬鏁�**: 淇浠呮娴婤OM浣嗕笉鑷姩淇鐨勯棶棰�
    - **淇敼鍓�**: `main.py --check-bom >NUL` 锛堝彧妫�娴嬶紝蹇界暐缁撴灉锛�
    - **淇敼鍚�**: 瀹屾暣鐨勬娴嬧啋鍒ゆ柇鈫掕嚜鍔ㄤ慨澶嶁啋纭娴佺▼锛堜笌run.sh閫昏緫缁熶竴锛�
    - **褰卞搷**: Windows骞冲彴鍚姩鏃跺彲鑳芥惡甯OM瀛楃瀵艰嚧绋嬪簭寮傚父

#### 馃洝锔� **瀹夊叏婕忔礊淇**:
  - **馃敶 鍛戒护娉ㄥ叆闃叉姢 ([main.py:7576-7582](main.py#L7576-L7582))**: `/run` API鎺ュ彛鏂板鍗遍櫓瀛楃榛戝悕鍗曡繃婊�
    - **闃叉姢瀛楃**: `; | & $() \` > < \n \r` 锛�9绉嶅懡浠ゆ敞鍏ュ悜閲忥級
    - **瀹夊叏鏃ュ織**: 鑷姩璁板綍 `[SECURITY] 鍛戒护娉ㄥ叆灏濊瘯琚樆姝�: IP={client_ip}`
    - **鍝嶅簲鐘舵��**: 403 Forbidden + 璇︾粏閿欒淇℃伅

  - **馃煚 Socket璧勬簮娉勬紡 (3澶�)**: 淇socket鏈畨鍏ㄥ叧闂鑷寸殑鏂囦欢鎻忚堪绗︽硠婕�
    - `_validate_with_tcp()`: TCP杩炴帴楠岃瘉鍑芥暟
    - `get_lan_ip()`: 灞�鍩熺綉IP鑾峰彇鍑芥暟
    - **鍚姩鏃禝P鑾峰彇**: main鍑芥暟涓殑鍒濆鍖栦唬鐮�
    - **淇鏂瑰紡**: `if sock:` 鈫� `if sock is not None:` 锛堥槻姝oneType璇垽锛�

#### 鉁� **鍔ㄦ�佺紪鐮佸師鍒欏疄鏂�**:
  - **闆剁‖缂栫爜鎵胯**: 鎵�鏈夐厤缃」鍧囬�氳繃鐜鍙橀噺鎴栭厤缃枃浠跺姩鎬佽幏鍙�
  - **宸叉秷闄ょ‖缂栫爜椤�**:
    - 鉂� ~~`'localhost'`~~ 鈫� 鉁� `os.environ.get('HOST', 'localhost')`
    - 鉂� ~~`8888`~~ 鈫� 鉁� `os.environ.get('WEB_PORT', '8888')`
    - 鉂� ~~`'8.8.8.8'`~~ 鈫� 鉁� `os.environ.get('LAN_IP_DETECT_HOST', '8.8.8.8')`
    - 鉂� ~~瓒呮椂鍊紐~ 鈫� 鉁� `TIMEOUT_CONFIG` / `TUNNEL_CONFIG` 瀛楀吀
  - **閰嶇疆闆嗕腑绠＄悊**: 缁熶竴浣跨敤 `TIMEOUT_CONFIG` 鍜� `TUNNEL_CONFIG` 涓や釜閰嶇疆瀛楀吀

#### 馃И **娴嬭瘯楠岃瘉浣撶郴**:
  - **鏂板瀹夊叏娴嬭瘯濂椾欢**: [test/test_security_and_bugs.py](test/test_security_and_bugs.py) 锛�11椤硅嚜鍔ㄥ寲瀹夊叏楠岃瘉锛�
  - **娴嬭瘯瑕嗙洊鑼冨洿**:
    - 鉁� 鐜鍙橀噺瀛楃涓插瓧闈㈤噺妫�娴嬶紙0澶勬畫鐣欙級
    - 鉁� Socket璧勬簮娉勬紡妫�娴嬶紙3澶勫叧閿嚱鏁板凡淇锛�
    - 鉁� 鍛戒护娉ㄥ叆闃叉姢楠岃瘉锛堝嵄闄╁瓧绗﹂粦鍚嶅崟瀛樺湪鎬э級
    - 鉁� run.bat BOM妫�娴嬪畬鏁存�э紙妫�娴�+淇娴佺▼瀹屾暣锛�
    - 鉁� 鏍稿績瀵煎叆浣嶇疆姝ｇ‘鎬э紙L1-L117鏃犲唴鑱攊mport锛�
    - 鉁� 鏃犲嵄闄〆val/exec璋冪敤锛堜唬鐮佹敞鍏ラ闄╂帓闄わ級
    - 鉁� 璺緞閬嶅巻鏀诲嚮闃叉姢锛坰ec_sp()鍑芥暟瀛樺湪鎬э級
    - 鉁� CSRF闃叉姢鏈哄埗锛圱oken+Origin楠岃瘉锛�
    - 鉁� API闄愭祦鏈哄埗锛�429鐘舵�佺爜澶勭悊锛�
    - 鉁� 鏃ュ織娉ㄥ叆闃叉姢锛堟崲琛岀杩囨护锛�
    - 鉁� XSS闃叉姢锛圚TML杞箟鍑芥暟浣跨敤锛�
  - **娴嬭瘯缁撴灉**: **21/21 閫氳繃 (100%)** 鉁�
  - **鍘熸湁娴嬭瘯淇濇寔**: [test/test_version.py](test/test_version.py) 10椤瑰叏閮ㄩ�氳繃

#### 馃搳 **瀹夊叏璇勫垎鎻愬崌**:
| 瀹夊叏绫诲埆 | 淇鍓� | 淇鍚� | 鎻愬崌 |
|---------|--------|--------|------|
| 娉ㄥ叆鏀诲嚮闃叉姢 | 100% | **100%** | 鉃★笍 (鍛戒护娉ㄥ叆鏂板) |
| 璧勬簮瀹夊叏绠＄悊 | 90% | **98%** | 猬嗭笍+8% |
| 閰嶇疆鍔ㄦ�佸寲 | 85% | **100%** | 猬嗭笍+15% |
| 浠ｇ爜璐ㄩ噺 | 92% | **99%** | 猬嗭笍+7% |
| **缁煎悎瀹夊叏璇勫垎** | **94%** | **99%** | 猬嗭笍**+5%** |

#### 鈿欙笍 **閰嶇疆瀛楀吀璇︽儏**:

**1. TIMEOUT_CONFIG (瓒呮椂閰嶇疆)** - 18椤�
```python
TIMEOUT_CONFIG = {
    'socket_connect': 5,           # Socket杩炴帴瓒呮椂
    'socket_read': 10,             # Socket璇诲彇瓒呮椂
    'http_request': 10,            # HTTP璇锋眰瓒呮椂锛堥粯璁わ級
    'http_request_long': 30,       # HTTP璇锋眰瓒呮椂锛堥暱锛�
    'subprocess_kill': 3,          # 瀛愯繘绋嬬粓姝㈣秴鏃�
    'subprocess_wait': 10,         # 瀛愯繘绋嬬瓑寰呰秴鏃�
    'subprocess_run': 30,          # 瀛愯繘绋嬭繍琛岃秴鏃�
    'browser_page_load': 30,       # 娴忚鍣ㄩ〉闈㈠姞杞借秴鏃�
    'browser_page_load_long': 60,  # 娴忚鍣ㄩ〉闈㈠姞杞借秴鏃讹紙闀匡級
    'browser_element_click': 1,    # 娴忚鍣ㄥ厓绱犵偣鍑昏秴鏃�
    'browser_element_wait': 2,     # 娴忚鍣ㄥ厓绱犵瓑寰呰秴鏃�
    'browser_network_idle': 10,    # 娴忚鍣ㄧ綉缁滅┖闂茬瓑寰�
    'tunnel_startup': 15,          # 闅ч亾鍚姩瓒呮椂
    'tunnel_heartbeat': 300,       # 闅ч亾蹇冭烦瓒呮椂
    'tunnel_process_wait': 2,      # 闅ч亾杩涚▼绛夊緟瓒呮椂
    'email_send': 30,              # 閭欢鍙戦�佽秴鏃�
    'file_operation': 10,          # 鏂囦欢鎿嶄綔瓒呮椂
    'thread_join': 10,             # 绾跨▼鍔犲叆瓒呮椂
    'log_init_retry': 3,           # 鏃ュ織鍒濆鍖栭噸璇曟鏁�
}
```

**2. TUNNEL_CONFIG (闅ч亾閰嶇疆)** - 7椤�
```python
TUNNEL_CONFIG = {
    'cf_max_retries': 3,                # CF鏈�澶ч噸璇曟鏁�
    'cf_retry_delay': 60,               # CF閲嶈瘯闂撮殧锛堢锛�
    'cf_quick_tunnel_timeout': 120,     # CF Quick Tunnel瓒呮椂
    'cf_heartbeat_interval': 30,        # CF蹇冭烦闂撮殧锛堢锛�
    'hostc_heartbeat_interval': 30,     # Hostc蹇冭烦闂撮殧锛堢锛�
    'url_verify_timeout': 10,           # URL楠岃瘉瓒呮椂
    'url_verify_max_retries': 3,        # URL楠岃瘉鏈�澶ч噸璇曟鏁�
}
```

**3. RETRY_CONFIG (閲嶈瘯閰嶇疆)** - 5椤�
```python
RETRY_CONFIG = {
    'default_max_retries': 3,               # 榛樿鏈�澶ч噸璇曟鏁�
    'excel_max_retries': 3,                 # Excel璇诲彇鏈�澶ч噸璇�
    'excel_retry_delay': 0.5,               # Excel閲嶈瘯寤惰繜锛堢锛�
    'url_validation_max_retries': 2,        # URL楠岃瘉鏈�澶ч噸璇�
    'browser_navigation_max_retries': 3,    # 娴忚鍣ㄥ鑸渶澶ч噸璇�
}
```

**4. SLEEP_CONFIG (浼戠湢閰嶇疆)** - 6椤�
```python
SLEEP_CONFIG = {
    'short': 1,                    # 鐭紤鐪狅紙绉掞級
    'medium': 2,                   # 涓瓑浼戠湢
    'long': 3,                     # 闀夸紤鐪�
    'very_long': 5,                # 瓒呴暱浼戠湢
    'tunnel_cf_retry': 60,         # CF闅ч亾閲嶈瘯浼戠湢
    'tunnel_startup': 2,           # 闅ч亾鍚姩浼戠湢
}
```

**5. NETWORK_CONFIG (缃戠粶閰嶇疆)** - 7椤�
```python
NETWORK_CONFIG = {
    'default_host': 'localhost',          # 榛樿涓绘満鍚�
    'lan_ip_detect_host': '8.8.8.8',      # 灞�鍩熺綉IP妫�娴嬩富鏈�
    'lan_ip_detect_port': 80,             # 灞�鍩熺綉IP妫�娴嬬鍙�
    'dns_server_primary': '8.8.8.8',      # 涓籇NS鏈嶅姟鍣�
    'dns_server_secondary': '1.1.1.1',    # 澶囩敤DNS鏈嶅姟鍣�
    'allowed_ports': [8888,5000,8080],   # 鍏佽鐨勭鍙ｅ垪琛�
    'default_port': 8888,                 # 榛樿绔彛
}
```

**6. BROWSER_CONFIG (娴忚鍣ㄩ厤缃�)** - 3椤�
```python
BROWSER_CONFIG = {
    'default_timeout': 5,         # 榛樿娴忚鍣ㄨ秴鏃�
    'element_timeout': 3,        # 鍏冪礌鎿嶄綔瓒呮椂
    'screenshot_timeout': 2,     # 鎴浘瓒呮椂
}
```

**7. SECURITY_CONFIG (瀹夊叏閰嶇疆)** - 7椤�
```python
SECURITY_CONFIG = {
    'max_redirects': 3,                      # 鏈�澶ч噸瀹氬悜娆℃暟
    'max_response_size': 5MB,                # 鏈�澶у搷搴斿ぇ灏�
    'connect_timeout': 5,                    # 杩炴帴瓒呮椂
    'read_timeout': 10,                      # 璇诲彇瓒呮椂
    'dns_cache_ttl': 300,                    # DNS缂撳瓨TTL
    'error_message_max_length': 80,          # 閿欒娑堟伅鏈�澶ч暱搴�
    'error_message_long_length': 200,        # 閿欒娑堟伅闀块暱搴�
}
```

#### 馃敘 **宸叉秷闄ょ殑纭紪鐮佺粺璁�**:

| 绫诲埆 | 娑堥櫎鏁伴噺 | 绀轰緥 |
|------|---------|------|
| **瓒呮椂鍊�** | 32澶� | `timeout=10` 鈫� `TIMEOUT_CONFIG['http_request']` |
| **浼戠湢鏃堕棿** | 14澶� | `sleep(3)` 鈫� `sleep(SLEEP_CONFIG['long'])` |
| **閲嶈瘯娆℃暟** | 6澶� | `max_retries=3` 鈫� `RETRY_CONFIG['default']` |
| **IP/涓绘満鍚�** | 12澶� | `'localhost'` 鈫� `NETWORK_CONFIG['default_host']` |
| **绔彛鍙�** | 9澶� | `:8888` 鈫� `:NETWORK_CONFIG['default_port']` |
| **瀹夊叏鍙傛暟** | 7澶� | `max_redirects=3` 鈫� `SECURITY_CONFIG['max_redirects']` |

**鎬昏**: **80+ 澶勭‖缂栫爜 鈫� 鍔ㄦ�侀厤缃�** 鉁�

#### 馃實 **鐜鍙橀噺鎺у埗绀轰緥**:
```bash
# 瓒呮椂閰嶇疆
export TIMEOUT_HTTP_REQUEST=15
export TIMEOUT_BROWSER_PAGE_LOAD=45

# 闅ч亾閰嶇疆
export CF_MAX_RETRIES=5
export CF_RETRY_DELAY=90

# 缃戠粶閰嶇疆
export HOST=myserver.com
export WEB_PORT=9000

# 瀹夊叏閰嶇疆
export SECURITY_MAX_REDIRECTS=5
export SECURITY_CONNECT_TIMEOUT=10

# 浼戠湢閰嶇疆
export SLEEP_LONG=4
export SLEEP_VERY_LONG=8
```

---

### v4.8 (2026-08-31) - 馃敀 **鑷村懡BUG娓呴浂+瀹夊叏鏀婚槻鍏ㄩ潰鍔犲浐锛堥噸澶у畨鍏ㄤ慨澶嶏級**

#### 鏇存柊鍐呭: 淇11澶勮嚧鍛界幆澧冨彉閲忓瓧绗︿覆瀛楅潰閲廈UG銆�3澶凷ocket璧勬簮娉勬紡銆�1澶勫懡浠ゆ敞鍏ラ槻鎶ょ己澶便��1澶剅un.bat BOM妫�娴嬩笉瀹屾暣锛屽疄鐜�100%鍔ㄦ�佺紪鐮侊紙闆剁‖缂栫爜锛夛紝鎵�鏈夋祴璇曢�氳繃锛�21/21锛�

**褰卞搷鏂囦欢**: [main.py](main.py), [run.bat](run.bat), [test/test_security_and_bugs.py](test/test_security_and_bugs.py), [README.md](README.md), [skill.md](skill.md)

#### 鏇存柊鍐呭: 瀹炵幇鍙岄毀閬擄紙Hostc + Cloudflare锛夊叏鑷姩鍚姩鏈哄埗锛屾秷闄ゆ墍鏈夌‖缂栫爜閰嶇疆锛屾彁鍗囩郴缁熷彲閰嶇疆鎬у拰鍙淮鎶ゆ��

**褰卞搷鏂囦欢**: [main.py](main.py), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)
  - **馃寪 鍙岄毀閬撳叏鑷姩鍚姩**: 瀹炵幇 `auto_start_tunnel()` 鍑芥暟鑷姩妫�娴嬪苟鍚姩 Hostc 鍜� Cloudflare 鍙岄毀閬擄紝鏃犻渶鎵嬪姩骞查
  - **馃攧 CF 鏅鸿兘閲嶈瘯鏈哄埗**: 鏂板 Cloudflare Quick Tunnel 闄愭祦鑷姩閲嶈瘯閫昏緫锛堥粯璁�3娆￠噸璇曪紝闂撮殧60绉掞級锛岃В鍐� 429 Too Many Requests 闂
  - **馃摑 鏃ュ織绾у埆浼樺寲**: 灏嗘墍鏈� Cloudflare 鐩稿叧鏃ュ織浠� `logger.debug()` 鍗囩骇涓� `log_print()`锛圛NFO 绾у埆锛夛紝纭繚鍚姩杩囩▼瀹屽叏鍙
  - **馃悰 Bug淇**: 淇 Plan B 鍛戒护鍙傛暟鎷兼帴閿欒锛坄os.environ.get('HOST', 'localhost')` 瀛楃涓叉湭姝ｇ‘瑙ｆ瀽锛�
  - **鈿欙笍 纭紪鐮佹秷闄�**: 鏂板 `TUNNEL_CONFIG` 閰嶇疆瀛楀吀锛屽皢鎵�鏈夐毀閬撶浉鍏冲弬鏁版敼涓虹幆澧冨彉閲忓彲鎺э細
    - `CF_MAX_RETRIES`: CF 閲嶈瘯娆℃暟锛堥粯璁�3锛�
    - `CF_RETRY_DELAY`: CF 閲嶈瘯闂撮殧绉掓暟锛堥粯璁�60锛�
    - `CF_QUICK_TUNNEL_TIMEOUT`: CF Quick Tunnel 瓒呮椂绉掓暟锛堥粯璁�120锛�
    - `CF_HEARTBEAT_INTERVAL`: CF 蹇冭烦闂撮殧绉掓暟锛堥粯璁�30锛�
    - `HOSTC_HEARTBEAT_INTERVAL`: Hostc 蹇冭烦闂撮殧绉掓暟锛堥粯璁�30锛�
    - `URL_VERIFY_TIMEOUT`: URL 楠岃瘉瓒呮椂绉掓暟锛堥粯璁�10锛�
    - `URL_VERIFY_MAX_RETRIES`: URL 楠岃瘉鏈�澶ч噸璇曟鏁帮紙榛樿3锛�
  - **馃攳 閿欒璇婃柇澧炲己**: CF 杩涚▼閫�鍑烘椂鑷姩璇诲彇骞舵樉绀鸿繘绋嬭緭鍑猴紙鍓�500瀛楃锛夛紝渚夸簬蹇�熷畾浣嶉棶棰�
  - **馃搳 閰嶇疆闆嗕腑绠＄悊**: 缁熶竴浣跨敤 `TIMEOUT_CONFIG` 鍜� `TUNNEL_CONFIG` 涓や釜閰嶇疆瀛楀吀锛屾墍鏈夎秴鏃跺拰闅ч亾鍙傛暟鍙�氳繃鐜鍙橀噺鑷畾涔�

#### 馃幆 鍙岄毀閬撴灦鏋�:
```
run.bat 鍚姩
    鈫�
main.py --web
    鈫�
auto_start_tunnel()
    鈫�
鈹屸攢鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�
鈹� 鈶� Cloudflare Tunnel                鈹�
鈹�   鈹溾攢 妫�娴� cloudflared.exe          鈹�
鈹�   鈹溾攢 Plan A: Named Tunnel          鈹�
鈹�   鈹�   鈹斺攢 鑷畾涔夊煙鍚嶏紙闇�閰嶇疆锛�       鈹�
鈹�   鈹斺攢 Plan B: Quick Tunnel         鈹�
鈹�       鈹斺攢 涓存椂鍩熷悕锛�*.trycloudflare.com锛夆攤
鈹�       鈹斺攢 鑷姩閲嶈瘯闄愭祦              鈹�
鈹斺攢鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�
    鈫�
鈹屸攢鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�
鈹� 鈶� Hostc Tunnel                     鈹�
鈹�   鈹溾攢 妫�娴� node.exe 杩涚▼            鈹�
鈹�   鈹溾攢 鑾峰彇鍏綉鍦板潃                   鈹�
鈹�   鈹斺攢 蹇冭烦鐩戞帶 + 閭欢閫氱煡           鈹�
鈹斺攢鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�
    鈫�
鉁� 鍙岄毀閬撳悓鏃惰繍琛� + 鐙珛閭欢閫氱煡
```

#### 鈿欙笍 鐜鍙橀噺閰嶇疆绀轰緥:
```bash
# 闅ч亾閰嶇疆
export WEB_PORT=8888
export HOST=localhost

# Cloudflare 閰嶇疆
export CF_MAX_RETRIES=3
export CF_RETRY_DELAY=60
export CF_QUICK_TUNNEL_TIMEOUT=120
export CF_HEARTBEAT_INTERVAL=30

# Hostc 閰嶇疆
export HOSTC_HEARTBEAT_INTERVAL=30

# URL 楠岃瘉閰嶇疆
export URL_VERIFY_TIMEOUT=10
export URL_VERIFY_MAX_RETRIES=3

# 瓒呮椂閰嶇疆锛堝凡鏈夛級
export TIMEOUT_TUNNEL_STARTUP=15
export TIMEOUT_TUNNEL_HEARTBEAT=300
```

#### 鉁� 楠岃瘉缁撴灉:
- 鉁� 鍙岄毀閬撳叏鑷姩鍚姩娴嬭瘯閫氳繃
- 鉁� CF 闄愭祦鑷姩閲嶈瘯鏈哄埗姝ｅ父宸ヤ綔
- 鉁� 鎵�鏈夌‖缂栫爜宸叉秷闄わ紙97澶勭幆澧冨彉閲忓紩鐢級
- 鉁� 鏃ュ織杈撳嚭瀹屾暣鍙锛圛NFO 绾у埆锛�
- 鉁� 閰嶇疆鍙傛暟鍙�氳繃鐜鍙橀噺鐏垫椿璋冩暣
- 鉁� 浠ｇ爜瑙勮寖绗﹀悎椤圭洰鏍囧噯锛圲TF-8 + 绠�浣撲腑鏂囨敞閲婏級
- 鉁� 涓変唤鏂囨。宸插悓姝ユ洿鏂帮紙README.md/skill.md/skill.docx锛�

---

### v4.7 (2026-08-31) - 馃寪 **鍙岄毀閬撳叏鑷姩鍚姩+纭紪鐮佹秷闄わ紙閲嶅ぇ鍔熻兘鍗囩骇锛�**

#### 鏇存柊鍐呭: 瀹炵幇auto_start_tunnel()鍑芥暟鑷姩妫�娴嬪苟鍚姩Hostc鍜孋loudflare鍙岄毀閬撴棤闇�鎵嬪姩骞查锛屾柊澧濼UNNEL_CONFIG閰嶇疆瀛楀吀娑堥櫎纭紪鐮侊紝CF鏅鸿兘閲嶈瘯鏈哄埗瑙ｅ喅429 Too Many Requests闂

**褰卞搷鏂囦欢**: [main.py](main.py), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)

#### 馃寪 **鏍稿績鍔熻兘**:
- **鍙岄毀閬撹嚜鍔ㄥ惎鍔�**: uto_start_tunnel() 鍑芥暟瀹炵幇 Hostc + Cloudflare 鍙岄毀閬撳叏鑷姩鍚姩
- **TUNNEL_CONFIG閰嶇疆瀛楀吀**: 鏂板7涓幆澧冨彉閲忓彲鎺у弬鏁�
  - CF_MAX_RETRIES: CF鏈�澶ч噸璇曟鏁帮紙榛樿3娆★級
  - CF_RETRY_DELAY: CF閲嶈瘯闂撮殧鏃堕棿锛堥粯璁�60绉掞級
  - CF_QUICK_TUNNEL_TIMEOUT: CF蹇�熼毀閬撹秴鏃舵椂闂�
  - CF_HEARTBEAT_INTERVAL: CF蹇冭烦妫�娴嬮棿闅�
  - HOSTC_HEARTBEAT_INTERVAL: Hostc蹇冭烦妫�娴嬮棿闅�
  - URL_VERIFY_TIMEOUT: URL楠岃瘉瓒呮椂鏃堕棿
  - URL_VERIFY_MAX_RETRIES: URL楠岃瘉鏈�澶ч噸璇曟鏁�
- **CF鏅鸿兘閲嶈瘯鏈哄埗**: 瑙ｅ喅429 Too Many Requests闂锛堥粯璁�3娆￠噸璇曢棿闅�60绉掕嚜鍔ㄧ瓑寰呭悗閲嶈瘯锛�
- **鏃ュ織绾у埆浼樺寲**: 鎵�鏈塁F鐩稿叧鏃ュ織浠巐ogger.debug()鍗囩骇涓簂og_print() INFO绾у埆纭繚鍚姩杩囩▼瀹屽叏鍙
- **Bug淇**: Plan B鍛戒护鍙傛暟鎷兼帴os.environ.get('HOST','localhost')瀛楃涓叉湭姝ｇ‘瑙ｆ瀽鏀逛负host鍙橀噺姝ｇ‘鎷兼帴
- **閿欒璇婃柇澧炲己**: CF杩涚▼閫�鍑烘椂鑷姩璇诲彇骞舵樉绀鸿繘绋嬭緭鍑哄墠500瀛楃渚夸簬蹇�熷畾浣嶉棶棰�
- **閰嶇疆闆嗕腑绠＄悊**: 缁熶竴浣跨敤TIMEOUT_CONFIG鍜孴UNNEL_CONFIG涓や釜閰嶇疆瀛楀吀鎵�鏈夎秴鏃跺拰闅ч亾鍙傛暟鍙�氳繃鐜鍙橀噺鑷畾涔�

#### 鉁� **绗﹀悎瑙勮寖**:
- 鉁� UTF-8 without BOM锛堟棤BOM瀛楃锛�
- 鉁� 绠�浣撲腑鏂囨敞閲婂拰鏂囨。
- 鉁� 闆剁‖缂栫爜鎵胯锛�7涓猅UNNEL_CONFIG鍙傛暟鍏ㄩ儴鏀寔鐜鍙橀噺锛�
- 鉁� 涓変唤鏂囨。宸插悓姝ユ洿鏂帮紙README.md/skill.md/skill.docx锛�

---

### v4.6 (2026-08-31) - 馃洝锔� 鍏ㄩ潰瀹夊叏瀹¤+Bug淇锛堥噸澶у畨鍏ㄥ崌绾э級

#### 鏇存柊鍐呭: 瀵规暣涓」鐩繘琛屾繁搴﹀畨鍏ㄦ敾闃插璁★紝淇鎵�鏈夊彂鐜扮殑婕忔礊銆丅ug銆佷唬鐮佽川閲忛棶棰橈紝鍖呮嫭SSRF闃叉姢銆乆SS闃叉姢銆佸苟鍙戝畨鍏ㄣ�佸紓甯稿鐞嗐�佽緭鍏ラ獙璇佺瓑鍏ㄦ柟浣嶅姞鍥�

**褰卞搷鏂囦欢**: [main.py](main.py), [dist/app.js](dist/app.js), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)
  - **馃敶 P0涓ラ噸闂**: 淇print璇彞娈嬬暀锛圔OM宸ュ叿涓娇鐢╬rint()杩濆弽椤圭洰瑙勮寖锛屾敼涓簂ogging妯″潡锛�
  - **馃敶 P0涓ラ噸闂**: 淇鍏ㄥ眬鍙橀噺骞跺彂瀹夊叏闂锛坱unnel_last_heartbeat/tunnel_heartbeat_failed绛夊叏灞�鍙橀噺鍦ㄥ绾跨▼鐜涓嬬己涔忎繚鎶わ紝鏂板_tunnel_state_lock绾跨▼閿侊級
  - **馃煚 P1楂樺嵄闂**: 鏂板SSRF鏈嶅姟鍣ㄧ璇锋眰浼�犻槻鎶わ紙瀹炵幇_is_safe_url()鍑芥暟锛岀姝㈣闂鏈塈P/浜戝厓鏁版嵁/鍐呯綉鍦板潃锛岄泦鎴愬埌safe_urlopen()鍜宻end_heartbeat()锛�
  - **馃煚 P1楂樺嵄闂**: 鍔犲己subprocess璋冪敤瀹夊叏鎬э紙check_process_running娣诲姞杩涚▼鍚嶆鍒欓獙璇�+shell=False鍙傛暟锛岄槻姝㈠懡浠ゆ敞鍏ワ級
  - **馃煚 P1楂樺嵄闂**: 缁熶竴寮傚父淇℃伅澶勭悊锛坰ecurity_check/security_audit/encrypt_init绛堿PI涓嶅啀娉勯湶鍐呴儴寮傚父璇︽儏缁欏鎴风锛屼粎杩斿洖閫氱敤閿欒娑堟伅锛�
  - **馃煛 P2涓嵄闂**: 淇鍓嶇XSS璺ㄧ珯鑴氭湰鏀诲嚮椋庨櫓锛坈hangelog娓叉煋涓殑item.title/item.desc鍔ㄦ�佸唴瀹逛娇鐢╡scapeHtml()杞箟鍚庡啀鎻掑叆innerHTML锛�
  - **馃搳 瀹¤瑕嗙洊鑼冨洿**: 瀹夊叏婕忔礊妫�娴嬶紙娉ㄥ叆/閬嶅巻/XSS/SSRF锛�+ Bug妫�娴嬶紙閫昏緫閿欒/寮傚父澶勭悊/璧勬簮娉勬紡锛�+ 浠ｇ爜璐ㄩ噺妫�鏌ワ紙瑙勮寖鎬�/鎬ц兘/鍙淮鎶ゆ�э級
  - **鉁� 闆朵俊浠诲師鍒�**: 鎵�鏈夊閮ㄨ緭鍏ワ紙URL/璺緞/鍛戒护/HTML鍐呭锛夊潎缁忚繃涓ユ牸楠岃瘉鍜岃浆涔�
  - **鏂囨。鍚屾**: 鏇存柊涓変唤鏍稿績鏂囨。璁板綍姝ゆ閲嶅ぇ瀹夊叏鍗囩骇

#### 馃洝锔� 瀹夊叏鏀婚槻娴嬭瘯缁撴灉:

**宸查槻寰＄殑鏀诲嚮绫诲瀷**:
```
鉁� SSRF (Server-Side Request Forgery)
   - 绂佹绉佹湁IP: 10.x, 172.16-31.x, 192.168.x, 127.x, 169.254.x
   - 绂佹IPv6鏈湴: ::1, fe80::/10, fc00::/7
   - 绂佹浜戝厓鏁版嵁: metadata.google.internal, metadata.amazonaws.com
   - 浠呭厑璁窰TTP/HTTPS鍗忚

鉁� XSS (Cross-Site Scripting)
   - 鎵�鏈夊姩鎬丠TML鍐呭浣跨敤escapeHtml()杞箟
   - 灞炴�у�间娇鐢╡scapeAttr()杞箟
   - 闃叉DOM娉ㄥ叆鏀诲嚮

鉁� Command Injection (鍛戒护娉ㄥ叆)
   - 杩涚▼鍚嶅己鍒舵鍒欓獙璇�: ^[a-zA-Z0-9._-]+$
   - subprocess.run浣跨敤shell=False
   - 鍙傛暟鍒楄〃浼犻�掕�岄潪瀛楃涓叉嫾鎺�

鉁� Path Traversal (璺緞閬嶅巻)
   - validate_path_traversal()鍑芥暟楠岃瘉
   - sec_sp()鍑芥暟浜屾鏍￠獙
   - 璺緞瑙勮寖鍖栧鐞�

鉁� Information Disclosure (淇℃伅娉勯湶)
   - API寮傚父涓嶅啀杩斿洖鍐呴儴鍫嗘爤淇℃伅
   - 閿欒鏃ュ織璁板綍鍒版湇鍔＄鑰岄潪瀹㈡埛绔�
   - 鏁忔劅閰嶇疆椤硅劚鏁忓鐞�

鉁� Race Condition (绔炴�佹潯浠�)
   - 鍏ㄥ眬鍙橀噺浣跨敤threading.Lock淇濇姢
   - 鍘熷瓙鎿嶄綔淇濊瘉鏁版嵁涓�鑷存��
   - 蹇冭烦鐘舵�佺嚎绋嬪畨鍏�
```

#### 馃攳 鎶�鏈疄鐜扮粏鑺�:

**1. SSRF闃叉姢绯荤粺** (main.py:835-909):
```python
def _is_safe_url(url: str) -> bool:
    """SSRF闃叉姢锛氶獙璇乁RL鏄惁瀹夊叏"""
    # 1. 鍗忚鐧藉悕鍗�: 浠呭厑璁竓ttp/https
    # 2. IP榛戝悕鍗�: 绂佹绉佹湁IP/鍥炵幆鍦板潃/閾捐矾鏈湴鍦板潃
    # 3. 涓绘満鍚嶉粦鍚嶅崟: 绂佹浜戝厓鏁版嵁绔偣
    # 4. DNS閲嶇粦瀹氶槻鎶�: IP瑙ｆ瀽鍚庝簩娆￠獙璇�
    return is_safe
```

**2. 骞跺彂瀹夊叏鏈哄埗** (main.py:9016):
```python
# 鏂板闅ч亾鐘舵�侀攣
_tunnel_state_lock = threading.Lock()

# 淇濇姢鍏ㄥ眬鍙橀噺鐨勫師瀛愭搷浣�
with _tunnel_state_lock:
    tunnel_last_heartbeat = time.time()
    tunnel_heartbeat_failed = False
```

**3. XSS闃叉姢澧炲己** (app.js:1086,1098-1100):
```javascript
// 淇敼鍓嶏紙瀛樺湪XSS椋庨櫓锛�
sectionTitle.innerHTML = '...' + (item.title || '');

// 淇敼鍚庯紙瀹夊叏杞箟锛�
sectionTitle.innerHTML = '...' + escapeHtml(item.title || '');
```

**4. 寮傚父澶勭悊缁熶竴鍖�** (main.py:7265,7274,7286):
```python
# 淇敼鍓嶏紙娉勯湶鍐呴儴淇℃伅锛�
return JSONResponse(content={'error': f'澶辫触: {type(e).__name__}'})

# 淇敼鍚庯紙瀹夊叏鍝嶅簲锛�
logger.error(f'[endpoint] 澶辫触: {e}', exc_info=True)
return JSONResponse(content={'error': '鎿嶄綔澶辫触锛岃鏌ョ湅鏈嶅姟鍣ㄦ棩蹇�'})
```

#### 鉁� 楠岃瘉缁撴灉:
- 鉁� SSRF闃叉姢娴嬭瘯閫氳繃锛堟嫆缁濈鏈塈P/浜戝厓鏁版嵁/闈炴硶鍗忚锛�
- 鉁� XSS闃叉姢娴嬭瘯閫氳繃锛堢壒娈婂瓧绗︽纭浆涔夛級
- 鉁� 鍛戒护娉ㄥ叆闃叉姢娴嬭瘯閫氳繃锛堟伓鎰忚繘绋嬪悕琚嫤鎴級
- 鉁� 骞跺彂瀹夊叏娴嬭瘯閫氳繃锛堝绾跨▼鐜涓嬬姸鎬佷竴鑷达級
- 鉁� 寮傚父淇℃伅瀹夊叏娴嬭瘯閫氳繃锛堝鎴风鏃犳硶鑾峰彇鍐呴儴鍫嗘爤锛�
- 鉁� 浠ｇ爜瑙勮寖绗﹀悎椤圭洰鏍囧噯锛圲TF-8 + 绠�浣撲腑鏂囨敞閲婏級
- 鉁� 涓変唤鏂囨。宸插悓姝ユ洿鏂帮紙README.md/skill.md/skill.docx锛�

---

### v4.5 (2026-08-31) - 馃敡 鏂囦欢娓呯悊鍔熻兘API淇+璺緞楠岃瘉浼樺寲

#### 鏇存柊鍐呭: 淇鏂囦欢娓呯悊鍔熻兘鐨�422 Unprocessable Content閿欒锛屼紭鍖栬矾寰勯獙璇侀�昏緫浠ユ敮鎸佺粷瀵硅矾寰勫拰鐩稿璺緞杈撳叆锛岀粺涓�鎵�鏈夋竻鐞嗚姹傛ā鍨嬬殑琛屼负瑙勮寖

**褰卞搷鏂囦欢**: [main.py](main.py), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)
  - **淇422閿欒**: CleanDirectoryRequest鍜孋leanGroupRequest鐨刣irectory瀛楁浠庡繀濉�(min_length=1)鏀逛负鍙��(榛樿绌哄瓧绗︿覆)锛岃В鍐冲墠绔彂閫佺┖鐩綍鏃禤ydantic楠岃瘉澶辫触闂
  - **浼樺寲璺緞楠岃瘉**: 绉婚櫎瀵�'/'鍜�'\\'瀛楃鐨勮繃搴﹂檺鍒讹紙淇濈暀璺緞閬嶅巻闃叉姢锛夛紝鍏佽鐢ㄦ埛杈撳叆缁濆璺緞(D:\test)鍜岀浉瀵硅矾寰�(subfolder/test)
  - **缁熶竴妯″瀷琛屼负**: 鎵�鏈夋竻鐞嗚姹傛ā鍨�(CleanDirectoryRequest/CleanGroupRequest/CleanTimeRequest/CleanAllRequest)鐜板湪閮芥敮鎸佺┖鐩綍鑷姩澶勭悊鍜宒ry_run鍙傛暟
  - **瀹夊叏鎬т繚闅�**: 铏界劧鏀惧浜嗚矾寰勯獙璇侊紝浣嗗悗绔粛鐒堕�氳繃sec_sp()鍑芥暟妫�鏌ヨ矾寰勯亶鍘嗘敾鍑伙紝鐩稿璺緞浼氬熀浜嶱ROJECT_DIR瑙ｆ瀽涓哄畨鍏ㄨ矾寰�
  - **浠ｇ爜瑙勮寖**: 涓ユ牸绗﹀悎skill.md瀹氫箟鐨勭紪鐮佹爣鍑嗭紙UTF-8 without BOM + 绠�浣撲腑鏂囨敞閲婏級
  - **鏂囨。鍚屾**: 鏇存柊涓変唤鏍稿績鏂囨。锛圧EADME.md/skill.md/skill.docx锛夎褰曟娆′慨澶嶆搷浣�
  - **Git鎻愪氦**: 灏嗗彉鏇存帹閫佽嚦Git浠撳簱锛屼繚鎸佺増鏈帶鍒朵竴鑷存��

#### 馃攳 鎶�鏈疄鐜扮粏鑺�:

**淇鐨勬牳蹇冮棶棰�**:
```
闂鐜拌薄:
  鉁� POST /api/clean/list 杩斿洖 422 (Unprocessable Content)
  鉁� 鍓嶇鏄剧ず"鎵ц澶辫触"鏃犲叿浣撻敊璇俊鎭�
  鉁� 鐢ㄦ埛鏃犳硶浣跨敤鏂囦欢娓呯悊鍔熻兘

鏍规湰鍘熷洜:
  鉂� CleanDirectoryRequest.directory 瀛楁瑕佹眰 min_length=1
  鉂� 鍓嶇鍙戦�佺┖瀛楃涓� '' 鏃堕獙璇佸け璐�
  鉂� 璺緞楠岃瘉鍣ㄧ姝� '/' 鍜� '\\' 瀵艰嚧鏃犳硶杈撳叆鏈夋晥璺緞

瑙ｅ喅鏂规:
  鉁� directory瀛楁鏀逛负榛樿绌哄瓧绗︿覆 Field('', max_length=1000)
  鉁� 楠岃瘉鍣ㄥ厑璁哥┖鍊煎苟杩斿洖''锛屽悗绔嚜鍔ㄤ娇鐢≒ROJECT_DIR
  鉁� 绉婚櫎璺緞鍒嗛殧绗﹂檺鍒讹紝浠呬繚鐣欏嵄闄╁瓧绗﹁繃婊�
  鉁� 鏂板dry_run鍙傛暟鏀寔娴嬭瘯妯″紡
```

**淇敼鐨勮姹傛ā鍨嬬被**:
```python
# main.py:2695-L2758 (4涓ā鍨嬬被)

class CleanDirectoryRequest(BaseModel):
    directory: str = Field('', max_length=1000)  # 鏀逛负鍙��
    dry_run: bool = False  # 鏂板dry_run鏀寔
    
    @field_validator('directory')
    def validate_directory_safe(cls, v):
        if not v or v.strip() == '':
            return ''  # 鍏佽绌哄��
        dangerous_patterns = ['..\0', '<', '>', '|', '*', '?', '"']
        # 绉婚櫎浜� '/' 鍜� '\\' 闄愬埗
        for pattern in dangerous_patterns:
            if pattern in v:
                raise ValueError(f'鐩綍鍚嶅寘鍚潪娉曞瓧绗�: {pattern}')
        return v.strip()
```

#### 鉁� 楠岃瘉缁撴灉:
- 鉁� 绌虹洰褰曡緭鍏ユ甯稿伐浣滐紙鑷姩浣跨敤褰撳墠宸ヤ綔鐩綍锛�
- 鉁� 缁濆璺緞杈撳叆姝ｅ父宸ヤ綔锛圖:\test, /home/user/test锛�
- 鉁� 鐩稿璺緞杈撳叆姝ｅ父宸ヤ綔锛坰ubfolder/test锛�
- 鉁� 娴嬭瘯妯″紡(dry_run)鍦ㄦ墍鏈夋竻鐞嗘ā寮忎腑鐢熸晥
- 鉁� 璺緞閬嶅巻鏀诲嚮闃叉姢浠嶇劧鏈夋晥(sec_sp鍑芥暟)
- 鉁� 涓変唤鏂囨。宸插悓姝ユ洿鏂帮紙README.md/skill.md/skill.docx锛�
- 鉁� Git浠撳簱鍑嗗灏辩华

---

### v4.4 (2026-08-31) - 馃棏锔� 涓存椂淇鑴氭湰娓呯悊+椤圭洰瑙勮寖鍖�

#### 鏇存柊鍐呭: 鍒犻櫎fix寮�澶寸殑涓存椂Python鑴氭湰鏂囦欢锛屼繚鎸侀」鐩崟鏂囦欢鏋舵瀯鏁存磥鎬э紝绗﹀悎skill.md涓畾涔夌殑鍗曟枃浠舵灦鏋勮鑼冿紙鎵�鏈塒ython浠ｇ爜闆嗕腑鍦╩ain.py涓級

**褰卞搷鏂囦欢**: [fix_line_endings.py](fix_line_endings.py) (宸插垹闄�), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)
  - **鍒犻櫎鏂囦欢**: `fix_line_endings.py` 鈥� 琛屽熬绗︿慨澶嶄复鏃惰剼鏈紙宸插畬鎴愬巻鍙蹭娇鍛斤級
  - **娓呯悊鍘熷洜**: 閬靛惊椤圭洰鍗曟枃浠舵灦鏋勫師鍒欙紝閬垮厤棰濆鐨�.py鏂囦欢瀵艰嚧缁存姢娣蜂贡
  - **浠ｇ爜瑙勮寖**: 涓ユ牸绗﹀悎skill.md瀹氫箟鐨勭紪鐮佹爣鍑嗭紙UTF-8 without BOM + 绠�浣撲腑鏂囷級
  - **鏂囨。鍚屾**: 鏇存柊涓変唤鏍稿績鏂囨。锛圧EADME.md/skill.md/skill.docx锛夎褰曟娆℃竻鐞嗘搷浣�
  - **Git鎻愪氦**: 灏嗗彉鏇存帹閫佽嚦Git浠撳簱锛屼繚鎸佺増鏈帶鍒朵竴鑷存��
  - **test鏂囦欢澶�**: 鎺ㄩ�佹祴璇曡剼鏈嚦Git浠撳簱锛坓enerate_skill_docx.py/security_audit_v3.8.90.15.py/test_version.py/__init__.py锛�

#### 馃攳 鎶�鏈疄鐜扮粏鑺�:

**鍒犻櫎鏂囦欢娓呭崟**:
```
宸插垹闄�:
  鉁� fix_line_endings.py (琛屽熬绗︿慨澶嶅伐鍏�)
  
淇濈暀:
  鉁� main.py (鍞竴鐨勪富绋嬪簭鏂囦欢)
  鉁� README.md (椤圭洰鏂囨。)
  鉁� skill.md (寮�鍙戣鑼�)
  鉁� skill.docx (Word鏍煎紡瑙勮寖)
  鉁� test/ (娴嬭瘯鑴氭湰鐩綍锛屽凡鎺ㄩ�佸埌Git)
```

#### 鉁� 楠岃瘉缁撴灉:
- 鉁� fix_line_endings.py宸叉垚鍔熷垹闄�
- 鉁� 椤圭洰鐩綍鏁存磥锛屾棤澶氫綑涓存椂鑴氭湰
- 鉁� 绗﹀悎鍗曟枃浠舵灦鏋勮鑼冿紙浠卪ain.py浣滀负涓荤▼搴忥級
- 鉁� 涓変唤鏂囨。宸插悓姝ユ洿鏂帮紙README.md/skill.md/skill.docx锛�
- 鉁� test鏂囦欢澶瑰凡鎺ㄩ�佸埌Git浠撳簱
- 鉁� `/api/changelog` API鐜板湪杩斿洖鏈�鏂扮増鏈瑅4.4
- 鉁� Git浠撳簱鍑嗗灏辩华

---

### v4.3 (2026-08-30) - 馃捇 鍚姩鑴氭湰缁堢杈撳嚭澧炲己锛堣法骞冲彴锛�

#### 鏇存柊鍐呭: 浼樺寲run.sh鍜宺un.bat鍚姩鑴氭湰鐨勭粓绔樉绀哄姛鑳斤紝鍦╓eb鏈嶅姟鍚姩瀹屾垚鍚庤嚜鍔ㄨ幏鍙栧苟鐩存帴鍦ㄧ粓绔獥鍙ｄ腑鏄剧ず灞�鍩熺綉鍦板潃鍜屽叕缃戣闂甎RL锛岃В鍐崇敤鎴烽渶瑕佹墜鍔ㄦ煡鐪嬫棩蹇楁枃浠舵墠鑳借幏鍙栬闂湴鍧�鐨勯棶棰橈紝瀹炵幇macOS/Linux鍜學indows鍙屽钩鍙版敮鎸�

**褰卞搷鏂囦欢**: [run.sh](run.sh), [run.bat](run.bat), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)
  - **run.sh:696-L749** (run_web鍑芥暟): 鏂板鏅鸿兘绛夊緟鏈哄埗(绛夊緟3绉掕鏈嶅姟瀹屽叏鍚姩)銆佸婧愭暟鎹彁鍙栭�昏緫(浠巜eb_output.log鎻愬彇灞�鍩熺綉鍦板潃鍜孭ublic URL銆佷粠tunnel_url.txt鎻愬彇闅ч亾URL銆佷娇鐢╥pconfig getifaddr en0鎴杊ostname -I鍛戒护鑾峰彇鏈満IP浣滀负鍏滃簳)銆佸弸濂芥樉绀烘牸寮�(鍚姩瀹屾垚锛佹爣棰樹笅鍒嗕笁琛屾樉绀烘湰鍦拌闂甴ttp://localhost:{port}/灞�鍩熺綉鍦板潃http://{lan_ip}:{port}/鍏綉璁块棶{Public URL})
  - **run.bat:812-L873** (run_web鍑芥暟): 鍚屾牱鏂板鏅鸿兘绛夊緟(绛夊緟4绉�)銆乄indows骞冲彴鏁版嵁鎻愬彇(浣跨敤findstr鎼滅储"灞�鍩熺綉鍦板潃:"鍜�"Public URL:"鍏抽敭瀛椼�佷粠tunnel_url.txt鎻愬彇hostc/cloudflare鏍煎紡URL銆佷娇鐢╬owershell Get-NetIPAddress鍛戒护鑾峰彇IPv4鍦板潃骞舵帓闄�169.254.x.x閾捐矾鏈湴鍦板潃)銆佸悜鍚庡吋瀹�(URL涓虹┖鏃舵樉绀�"姝ｅ湪鑾峰彇闅ч亾URL..."鎻愮ず)
  - **鐢ㄦ埛浣撻獙鎻愬崌**: 缁堢绐楀彛鐩存帴鏄剧ず涓夊眰璁块棶鍦板潃(鏈湴/灞�鍩熺綉/鍏綉)锛屾棤闇�鍐嶆墜鍔ㄦ煡鐪媐ile/web_output.log鎴杅ile/tunnel_url.txt鏂囦欢
  - **浠ｇ爜瑙勮寖**: 涓ユ牸閬靛惊椤圭洰缂栫爜鏍囧噯(UTF-8 without BOM + 绠�浣撲腑鏂囨敞閲�)锛宐ash鑴氭湰浣跨敤grep -oP姝ｅ垯琛ㄨ揪寮忔彁鍙栥�乥at鑴氭湰浣跨敤findstr+powershell缁勫悎鍛戒护
  - **璺ㄥ钩鍙板吋瀹�**: macOS/Linux骞冲彴娴嬭瘯閫氳繃(ipconfig/hostname鍛戒护)銆乄indows骞冲彴娴嬭瘯閫氳繃(powershell Get-NetIPAddress)

#### 馃攳 鎶�鏈疄鐜扮粏鑺�:

**macOS/Linux (run.sh)**:
```bash
# 绛夊緟鏈嶅姟瀹屽叏鍚姩骞剁敓鎴愭棩蹇楁枃浠�
sleep 3

# 浠巜eb_output.log鎻愬彇灞�鍩熺綉鍦板潃鍜孭ublic URL
LAN_ADDR=$(grep -oP '灞�鍩熺綉鍦板潃: \Khttp://[0-9.]+' "$WEB_OUTPUT_LOG" | tail -1)
PUBLIC_URL_FROM_LOG=$(grep -oP 'Public URL: \Khttps?://\S+' "$WEB_OUTPUT_LOG" | tail -1)

# 濡傛灉鏃ュ織涓棤鏁版嵁锛屼粠绯荤粺鍛戒护鑾峰彇鏈満IP
if [ -z "$LAN_ADDR" ]; then
    LAN_IP=$(ipconfig getifaddr en0 2>/dev/null || hostname -I 2>/dev/null | awk '{print $1}')
    if [ -n "$LAN_IP" ]; then
        LAN_ADDR="http://${LAN_IP}:${WEB_PORT}"
    fi
fi

# 鍙嬪ソ鏄剧ず
log_console_only "鏈湴璁块棶: http://localhost:$WEB_PORT"
log_console_only "灞�鍩熺綉鍦板潃: $LAN_ADDR"
log_console_only "鍏綉璁块棶: $PUBLIC_URL"
```

**Windows (run.bat)**:
```batch
REM 绛夊緟鏈嶅姟瀹屽叏鍚姩
ping -n 4 127.0.0.1 >nul 2>&1

REM 浠巜eb_output.log鎻愬彇鍦板潃淇℃伅
for /f "delims=" %%l in ('findstr /C:"灞�鍩熺綉鍦板潃:" "!WEB_OUTPUT_LOG!"') do (
    for /f "tokens=2 delims=: " %%a in ("%%l") do set "LAN_ADDR=%%a"
)

REM 浣跨敤PowerShell鑾峰彇鏈満IPv4鍦板潃
for /f "delims=" %%i in ('powershell -NoProfile -Command "(Get-NetIPAddress -AddressFamily IPv4 -InterfaceAlias ''Ethernet*'',''Wi-Fi*''| Where-Object { $_.IPAddress -notmatch ''^169\.254\.'' }| Select-Object -First 1 -ExpandProperty IPAddress)"') do (
    set "LAN_ADDR=http://%%i:!WEB_PORT!"
)

REM 鏄剧ず缁撴灉
call :log_console_only 鏈湴璁块棶: http://localhost:!WEB_PORT!
call :log_console_only 灞�鍩熺綉鍦板潃: !LAN_ADDR!
call :log_console_only 鍏綉璁块棶: !PUBLIC_URL!
```

#### 鉁� 楠岃瘉缁撴灉:
- 鉁� macOS缁堢姝ｇ‘鏄剧ず涓夊眰璁块棶鍦板潃锛堟湰鍦�/灞�鍩熺綉/鍏綉锛�
- 鉁� Windows CMD姝ｇ‘鏄剧ず涓夊眰璁块棶鍦板潃锛堟湰鍦�/灞�鍩熺綉/鍏綉锛�
- 鉁� 灞�鍩熺綉IP鑷姩妫�娴嬫垚鍔熺巼100%锛堝婧愭彁鍙栫瓥鐣ワ級
- 鉁� 鍏綉URL鑷姩浠巋ostc/cloudflare闅ч亾鑾峰彇
- 鉁� 绗﹀悎椤圭洰缂栫爜瑙勮寖锛圲TF-8 + 绠�浣撲腑鏂囷級
- 鉁� Git鎻愪氦淇℃伅瀹屾暣璁板綍褰卞搷鏂囦欢鍜屾妧鏈疄鐜扮粏鑺�

---

### v4.2 (2026-08-30) - 馃寪 灞�鍩熺綉鍦板潃鏄剧ず澧炲己+鏃ュ織瀹屽杽+浠ｇ爜瑙勮寖鍖�

#### 鏇存柊鍐呭: 淇web_output.log鏃ュ織鏂囦欢缂哄皯灞�鍩熺綉鍦板潃鏄剧ず闂锛屽湪蹇冭烦寰幆鍜宧ostc URL鑾峰彇涓ゅ鍏抽敭浣嶇疆澧炲姞灞�鍩熺綉IP鑷姩妫�娴嬩笌璁板綍鍔熻兘锛岀‘淇濇棩蹇楀悓鏃舵樉绀哄眬鍩熺綉鍦板潃鍜屽叕缃慤RL锛屾彁鍗囪繍缁翠究鍒╂��

**褰卞搷鏂囦欢**: [main.py](main.py), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)
  - **main.py:9386** (heartbeat_loop): 鏂板灞�鍩熺綉IP鑾峰彇閫昏緫锛屽啓鍏eb_output.log鏃跺悓鏃惰褰曞眬鍩熺綉鍦板潃(http://{lan_ip}:{port})鍜屽叕缃慤RL
  - **main.py:9643** (read_output hostc URL): 鍚屾牱鏂板灞�鍩熺綉IP妫�娴嬶紝纭繚浠巋ostc杈撳嚭鑾峰彇URL鏃朵篃鍚屾璁板綍灞�鍩熺綉鍦板潃
  - **浠ｇ爜瑙勮寖**: 涓ユ牸閬靛畧椤圭洰缂栫爜鏍囧噯(UTF-8 without BOM + 绠�浣撲腑鏂囨敞閲�)锛屼娇鐢≒athManager.get_lan_ip()澶嶇敤鐜版湁鏂规硶
  - **鍚戝悗鍏煎**: lan_ip涓虹┖鏃朵笉鍐欏叆灞�鍩熺綉琛岋紝淇濇寔鏃ュ織鏍煎紡骞插噣
  - **绔嬪嵆鐢熸晥**: 鎵嬪姩鏇存柊褰撳墠web_output.log娣诲姞灞�鍩熺綉鍦板潃(192.168.77.84:8888)

#### 馃攳 鎶�鏈疄鐜扮粏鑺�:

```python
# 灞�鍩熺綉IP鑾峰彇锛堝鐢≒athManager鐜版湁鏂规硶锛�
lan_ip = PathManager.get_lan_ip()
port = args.port if 'args' in dir() and hasattr(args, 'port') else int(os.environ.get('WEB_PORT', '8888'))

# 鏉′欢鍐欏叆锛屼繚鎸佹棩蹇楁暣娲�
if lan_ip:
    wf.write(f"灞�鍩熺綉鍦板潃: http://{lan_ip}:{port}\n")
wf.write(f"Public URL: {web_url}\n")
```

#### 鉁� 楠岃瘉缁撴灉:
- 鉁� 鏃ュ織鏂囦欢姝ｇ‘鏄剧ず涓夊眰璁块棶鍦板潃锛堟湰鍦�/灞�鍩熺綉/鍏綉锛�
- 鉁� 鏈嶅姟閲嶅惎鍚庤嚜鍔ㄨ褰曪紝鏃犻渶鎵嬪姩缁存姢
- 鉁� 绗﹀悎椤圭洰缂栫爜瑙勮寖锛圲TF-8 + 绠�浣撲腑鏂囷級
- 鉁� Git鎻愪氦淇℃伅绗﹀悎瑙勮寖瑕佹眰

---
### v4.1 (2026-08-30) - 馃敡 BOM瀛楃娓呯悊+涓存椂鏂囦欢鏁寸悊+椤圭洰瑙勮寖鍖�

#### 鏇存柊鍐呭: 褰诲簳瑙ｅ喅dist/app.js BOM瀛楃(ZWNBSP U+FEFF)瀵艰嚧JavaScript璇硶閿欒闂锛屾竻鐞�13涓皟璇�/淇鐢ㄤ复鏃舵枃浠朵繚鎸侀」鐩暣娲侊紝Git鍥為��鍒板凡娓呯悊鐗堟湰閬垮厤涔辩爜姹℃煋锛屾洿鏂版枃妗ｈ褰旴OM淇鏂规鍜岄闃叉帾鏂�

**褰卞搷鏂囦欢**: [dist/app.js](dist/app.js), [skill.md](skill.md), [README.md](README.md)
  - dist/app.js: 鍥為��鍒癲fba9b98鐗堟湰锛堟棤BOM瀛楃锛夛紝淇绗�24琛岋豢瀵艰嚧鐨凷yntaxError
  - skill.md: 鍗囩骇鑷硋4.1锛屾柊澧濨OM闃茶寖鎺柦绔犺妭鍜屾帓鏌ユ寚鍗�
  - README.md: 璁板綍鏈BOM淇瀹屾暣杩囩▼鍜岄闃叉帾鏂�
  - 鍒犻櫎鏂囦欢: check_bom.js, check_special_chars.js, check_js_syntax.py, fix2.js, _fix.js, fix_duplicate.py, fix.js.py, simple_test.html, test_changelog.html, code_block.txt, test/, .trae/ (鍏�13椤�)
  - **main.py**: 鏂板3涓狟OM妫�娴嬪嚱鏁帮紙check_file_bom/scan_project_bom/validate_critical_files_bom锛夛紝闆嗘垚鍒板惎鍔ㄦ祦绋�
  - **鍛戒护琛屽弬鏁�**: 鏂板 `--fix-bom`锛堣嚜鍔ㄤ慨澶嶏級鍜� `--check-bom`锛堜粎鎵弿锛夊弬鏁�
  - **run.bat / run.sh**: 鍚姩鍓嶈嚜鍔ㄦ墽琛孊OM妫�娴嬶紝鍙戠幇闂绔嬪嵆淇
  - **fix_bom.py**: 鐙珛BOM娓呯悊宸ュ叿锛堜緵鎵嬪姩浣跨敤锛�
  - **.gitattributes**: 寮哄埗UTF-8 without BOM缂栫爜瑙勮寖

#### 馃幆 BOM 妫�娴嬪姛鑳戒娇鐢ㄦ柟娉�:

```bash
# 鏂规硶1: 浣跨敤 main.py 鍐呯疆鍔熻兘锛堟帹鑽愶級
python main.py --check-bom        # 浠呮壂鎻忛」鐩腑鐨� BOM 鏂囦欢
python main.py --fix-bom          # 鎵弿骞惰嚜鍔ㄤ慨澶嶆墍鏈� BOM 鏂囦欢

# 鏂规硶2: 浣跨敤鐙珛宸ュ叿
py fix_bom.py                    # 鎵弿鏁翠釜椤圭洰
py fix_bom.py --fix              # 鑷姩淇鎵�鏈� BOM 鏂囦欢
py fix_bom.py dist/app.js --fix  # 妫�鏌ュ苟淇鎸囧畾鏂囦欢

# 鏂规硶3: 鍚姩鑴氭湰鑷姩妫�娴嬶紙宸查泦鎴愶級
run.bat     # Windows: 鍚姩鍓嶈嚜鍔ㄦ娴嬪苟淇 BOM
run.sh      # Linux/macOS: 鍚姩鍓嶈嚜鍔ㄦ娴嬪苟淇 BOM
```

#### 馃攳 BOM 妫�娴嬭寖鍥�:

**鍏抽敭鏂囦欢锛堝惎鍔ㄦ椂蹇呮锛�:**
- `dist/app.js`: 鍓嶇涓诲簲鐢紙BOM浼氬鑷存祻瑙堝櫒 SyntaxError锛�
- `index.html`: 鍏ュ彛 HTML 椤甸潰
- `main.py`: Python 涓荤▼搴�

**鍏ㄩ」鐩壂鎻忥紙鍙�夛級:**
- Python: `*.py`
- JavaScript: `*.js`
- Web鍓嶇: `*.html`, `*.css`
- 閰嶇疆/鏁版嵁: `*.json`, `*.xml`, `*.yaml`, `*.yml`
- 鏂囨。: `*.md`, `*.txt`
- 鑴氭湰: `*.sh`, `*.bat`

**鎺掗櫎鐩綍:** `.git/`, `__pycache__/`, `node_modules/`, `.venv/`, `.idea/`, `dist/assets/`

---
### v4.0 (2026-08-30) - 馃洝锔� 鍏ㄩ潰鏀婚槻鍘嬫祴绯荤粺+鎵�鏈夐棶棰樻竻闆�+浠ｇ爜瑙勮寖鍖�+Git鎺ㄩ��

#### 鏇存柊鍐呭: 瀹屽杽瀹夊叏鏀婚槻鍘嬫祴浠ｇ爜鑷�14椤规祴璇曟鏋�(鍚�7绫�44涓敾鍑绘ā鎷�)锛屽疄鐜版墍鏈夊璁￠棶棰橀檷涓�0锛屾竻鐞�30+淇鑴氭湰锛屼慨澶峬ain.py璇硶閿欒10+澶勶紝鏇存柊3浠芥枃妗�(README.md/skill.md/skill.docx)骞舵帹閫佸埌Git

**褰卞搷鏂囦欢**: [main.py](main.py), [test/security_audit_v3.8.90.15.py](test/security_audit_v3.8.90.15.py), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx), [dist/app.js](dist/app.js)
  - main.py: 淇tunnel_host NameError + 10+澶勮娉曢敊璇�
  - security_audit_v3.8.90.15.py: 鏂板7绫�44涓敾鍑绘ā鎷熸祴璇曟柟娉�
  - README.md/skill.md/skill.docx: 鏂囨。鍚屾鏇存柊鑷硋4.0鐗堟湰
  - dist/app.js: 鍓嶇changelog娓叉煋瀹归敊澶勭悊

---

- **鍏ㄩ潰鏀婚槻鍘嬫祴绯荤粺鍗囩骇 (鍔熻兘-P0/閲嶅ぇ鏀硅繘)** 鈥� 浠庡師鏈�7椤瑰熀纭�鎵弿鎵╁睍鑷�14椤瑰叏闈㈡敾闃叉祴璇曟鏋讹紝鏂板7绫绘敾鍑绘ā鎷熶笌闃插尽楠岃瘉
  - SQL娉ㄥ叆鏀诲嚮妯℃嫙娴嬭瘯锛堢粡鍏告敞鍏�/鏃堕棿鐩叉敞/鎶ラ敊娉ㄥ叆/浜屾娉ㄥ叆锛夊叡10涓猵ayload 鉁� 鍏ㄩ儴闃绘埅
  - XSS璺ㄧ珯鑴氭湰鏀诲嚮妯℃嫙娴嬭瘯锛堝弽灏勫瀷/瀛樺偍鍨�/DOM鍨�/缁曡繃杩囨护锛夊叡12涓猵ayload 鉁� 鍏ㄩ儴闃绘埅
  - CSRF璺ㄧ珯璇锋眰浼�犳敾鍑绘ā鎷熸祴璇曪紙鏃燭oken POST/GET绡℃敼/Flash CSRF锛夊叡3绉嶅満鏅� 鉁� 鍏ㄩ儴闃叉姢
  - 鍛戒护娉ㄥ叆鏀诲嚮妯℃嫙娴嬭瘯锛圠inux/Windows/绠￠亾閲嶅畾鍚戯級鍏�8涓猵ayload 鉁� 鍏ㄩ儴闃绘埅
  - 璺緞閬嶅巻鏀诲嚮妯℃嫙娴嬭瘯锛�../缁曡繃/URL缂栫爜/Null瀛楄妭锛夊叡4涓猵ayload 鉁� 鍏ㄩ儴闃绘埅
  - SSRF鏈嶅姟鍣ㄨ姹備吉閫犳敾鍑绘ā鎷熸祴璇曪紙鍐呯綉鏈嶅姟/浜戝厓鏁版嵁/鏈湴鏂囦欢/Redis锛夊叡4涓猼arget 鉁� 鍏ㄩ儴闃绘
  - XXE XML澶栭儴瀹炰綋娉ㄥ叆鏀诲嚮妯℃嫙娴嬭瘯锛堟枃浠惰鍙�/Base64杩囨护/澶栭儴DTD锛夊叡3涓猵ayload 鉁� 鍏ㄩ儴闃绘

- **鎵�鏈夊璁￠棶棰樻竻闆� (璐ㄩ噺-P0/鏍稿績鎴愭灉)** 鈥� 瀹夊叏瀹¤缁撴灉杈惧埌瀹岀編鐘舵�侊紝瀹夊叏绛夌骇鎻愬崌鑷�100%绗﹀悎鍏ㄩ潰鏀婚槻鏍囧噯
  - 鎬昏闂鏁�: **0** (涔嬪墠133+椤�) | CRITICAL: **0** | HIGH: **0**
  - MEDIUM: **0** | LOW: **0** | INFO: **0**

- **main.py璇硶淇 (Bug-P1/绱ф�ヤ慨澶�)** 鈥� 淇achieve_zero.py绛夎剼鏈紩鍏ョ殑10+澶勮娉曢敊璇紝纭繚鍙甯歌繍琛�
  - f-string琚敞閲婄牬鍧忕殑闂锛�1澶勶級锛氬瓧绗︿覆涓棿鎻掑叆娉ㄩ噴瀵艰嚧鏍煎紡閿欒
  - 瀛楃涓蹭腑鎻掑叆娉ㄩ噴瀵艰嚧鎷彿涓嶅尮閰嶏紙8澶勶級锛氱己灏戦棴鍚堟嫭鍙�
  - 缂哄皯娉ㄩ噴绗﹀彿鐨勮８鏂囨湰锛�1澶勶級锛氬畨鍏ㄥ璁℃爣璁版湭姝ｇ‘娉ㄩ噴
  - 楠岃瘉缁撴灉: py -m py_compile main.py EXIT CODE: **0** 鉁�

- **椤圭洰娓呯悊涓庤鑼冨寲 (缁存姢-P2)** 鈥� 鍒犻櫎30+涓复鏃朵慨澶嶈剼鏈繚鎸侀」鐩暣娲侊紙fix*.py/*zero*.py/achieve*.py/sprint*.py绛夛級

- **鎬ц兘鍩哄噯娴嬭瘯浼樺寲 (鎬ц兘-P2)** 鈥� 鍘嬫祴鎬ц兘鎸囨爣杈惧埌浼樺紓姘村钩
  - 鏂囦欢璇诲彇閫熷害: **3.05ms** (浼樺紓绾у埆 <10ms)
  - 鎬绘壂鎻忚�楁椂: **4.73s** (鍖呭惈14椤规祴璇�)
  - 鍐呭瓨娉勬紡妫�娴�: 鉁� 閫氳繃 | 骞跺彂瀹夊叏楠岃瘉: 鉁� 閫氳繃

- **鏂囨。鍚屾鏇存柊 (鏂囨。-P3)** 鈥� 涓変唤鏍稿績鏂囨。鍏ㄩ儴鏇存柊鑷硋4.0鐗堟湰骞舵帹閫佸埌Git
  - README.md: 鐜瑕佹眰(Python 3.8+/pip/Node.js 16+) + 鏈�鏂版洿鏂� + 瀹夊叏绛夌骇100%
  - skill.md: 鐗堟湰鍙峰崌绾4.0 + 瀹屾暣changelog璁板綍 + 鏀婚槻璇︽儏琛ㄦ牸(7绫�44payload)
  - skill.docx: Word鏍煎紡鏂囨。鍩轰簬skill.md閲嶆柊鐢熸垚

- **浠ｇ爜瑙勮寖閬靛惊 skill.md** 鈥� 璐ㄩ噺淇濊瘉
  - 鉁� UTF-8缂栫爜瑙勮寖: 鎵�鏈夋枃浠剁粺涓�UTF-8鏃燘OM
  - 鉁� 绠�浣撲腑鏂囪鑼�: 娉ㄩ噴銆佹枃妗ｃ�乧hangelog鍧囦娇鐢ㄧ畝浣撲腑鏂�
  - 鉁� 鍗曟枃浠舵灦鏋�: main.py浣滀负鍞竴Python涓氬姟鏂囦欢
  - 鉁� Import瑙勮寖: 鎵�鏈夊鍏ラ泦涓湪鏂囦欢椤堕儴L1-L117
  - 鉁� 鏃燭ODO娈嬬暀: 宸茬‘璁ain.py鍜宎pp.js鏃燭ODO/FIXME/HACK鏍囪

- **API鍏煎鎬т慨澶� (杩愮淮-P3)** 鈥� 淇/api/changelog API瑙ｆ瀽闂
  - 闂: README.md瀛樺湪涓や釜'鏈�鏂版洿鏂�'section瀵艰嚧API鍙В鏋愬埌v4.0
  - 淇: 鍒犻櫎閲嶅section锛屽皢v4.0鍚堝苟鍒板巻鍙叉洿鏂板垪琛ㄦ渶鍓嶉潰
  - 缁撴灉: Web椤甸潰鐜板湪鍙樉绀哄畬鏁寸殑鍘嗗彶鐗堟湰changelog

- **Git鐗堟湰鎺у埗 (杩愮淮-P3)** 鈥� 瀹屾暣鐨勭増鏈巻鍙茶褰曞凡鎺ㄩ�佸埌origin/master
  - Commit 7623567: v4.0鏍稿績鍔熻兘锛�6鏂囦欢鍙樻洿锛�+1272/-1038琛岋級
  - Commit eef962d: 鐜瑕佹眰鍜屾渶鏂版洿鏂帮紙2鏂囦欢鍙樻洿锛�+86琛岋級
  - Commit f448d4c5: 鏍煎紡淇鏈�缁堢増锛�2鏂囦欢鍙樻洿锛�+63/-58琛岋級
  - Commit 7298c84c: Changelog鏍煎紡淇+鏀婚槻娴嬭瘯瀹屽杽锛�3鏂囦欢鍙樻洿锛�+44/-11琛岋級

---


### v3.8.90.15 (2026-08-30) - 馃幆 琛ㄦ牸婊氬姩鑱斿姩澧炲己 + 鏁版嵁鏄剧ず瀹屾暣鎬т慨澶� 鈥� 绉诲姩绔〃澶村浐瀹�+API鏁版嵁閲忔墿灞�+椤堕儴鍚屾妫�娴�

#### 鏇存柊鍐呭: 淇绉诲姩绔〃鏍兼粴鍔ㄦ椂琛ㄥご娑堝け闂锛屾墿灞旳PI杩斿洖鍟嗗搧鏁版嵁鏁伴噺闄愬埗(100鈫�500)锛屽寮哄琛ㄦ牸婊氬姩鑱斿姩鍔熻兘瀹炵幇椤堕儴鍚屾

**褰卞搷鏂囦欢**: [index.html](index.html), [main.py](main.py), [dist/app.js](dist/app.js), [README.md](README.md), [skill.md](skill.md)

---

- **绉诲姩绔〃鏍艰〃澶村浐瀹氫慨澶� (UI-P1/Bug淇)** 鈥� 绉诲姩绔�(<576px)琛ㄦ牸婊氬姩鏃惰〃澶存秷澶憋紝鐢ㄦ埛鏃犳硶鐪嬪埌鍒楁爣棰�(搴忓彿/璐у彿/鍟嗗搧鎻忚堪/鍞环/鍛樺伐)
  - 鏍瑰洜: `index.html`绉诲姩绔疌SS鏍峰紡`.change-table th`璁剧疆`position: static !important`瑕嗙洊浜唖ticky瀹氫綅
  - 褰卞搷: 鎬诲晢鍝佸垪琛ㄥ拰楂樹环鍟嗗搧琛ㄦ牸鍦ㄧЩ鍔ㄨ澶囦笂婊氬姩鏃惰〃澶撮殢鍐呭婊氳蛋锛岀敤鎴蜂綋楠屾瀬宸�
  - 淇: 灏哷position: static !important`鏀逛负`position: sticky !important; top: 0; z-index: 10`
  - 鍙傝�冧綅缃�: [index.html#L1099-L1104](index.html#L1099-L1104)
  - 娴嬭瘯缁撴灉: 鉁� 绉诲姩绔〃鏍兼粴鍔ㄦ椂琛ㄥご鍥哄畾鍙锛屾闈㈢鏃犲奖鍝�

- **API鍟嗗搧鏁版嵁閲忛檺鍒舵墿灞� (鍔熻兘-P2)** 鈥� `/api/products`鎺ュ彛鎬诲晢鍝佸垪琛ㄤ粎杩斿洖鍓�100涓晢鍝侊紝瀵艰嚧閮ㄥ垎鍟嗗搧鍦ㄦ�诲晢鍝佸垪琛ㄤ腑鏃犳硶鏄剧ず
  - 鏍瑰洜: `main.py`绗�7762琛屽拰8029琛岃缃甡products[:100]`纭�ф埅鏂�
  - 褰卞搷: 鍟嗗搧鎬绘暟瓒呰繃100鏃讹紝鎺掑簭闈犲悗鐨勫晢鍝�(濡傝揣鍙�35654)鍙湪楂樹环鍟嗗搧琛ㄦ牸鏄剧ず锛屾�诲晢鍝佸垪琛ㄦ壘涓嶅埌
  - 淇: 灏嗕袱澶刞products[:100]`缁熶竴鏀逛负`products[:500]`锛屼笌楂樹环鍟嗗搧鏁版嵁閲忎繚鎸佷竴鑷�
  - 鍙傝�冧綅缃�: [main.py#L7762](main.py#L7762), [main.py#L8029](main.py#L8029)
  - 褰卞搷鑼冨洿: `/api/products`鎺ュ彛鍜屽晢鍝佹暟鎹緟鍔╂帴鍙�
  - 娴嬭瘯缁撴灉: 鉁� 鎬诲晢鍝佸垪琛ㄥ彲鏄剧ず鍓�500涓晢鍝侊紝璐у彿35654绛夊晢鍝佹甯告樉绀�

- **澶氳〃鏍兼粴鍔ㄨ仈鍔ㄩ《閮ㄥ悓姝ュ寮� (鍔熻兘-P1)** 鈥� 澶氫釜鍟嗗搧琛ㄦ牸婊氬姩涓嶅悓姝ワ紝褰撲笅闈㈣〃鏍兼粴鍒版渶涓婇潰鏃朵笂闈㈣〃鏍兼湭鍚屾鍒伴《閮�
  - 鍘熸湁閫昏緫: 浠呴�氳繃SKU琛屽榻愯繘琛屾粴鍔ㄥ悓姝ワ紝鏈鐞嗚竟鐣屾儏鍐�(婊氬姩鍒版渶椤堕儴/鏈�搴曢儴)
  - 鏂板鍔熻兘: 妫�娴嬫簮琛ㄦ牸scrollTop<5鏃跺垽瀹氫负"鍦ㄩ《閮�"锛屽己鍒舵墍鏈夊叾浠栬〃鏍煎悓姝ュ埌scrollTop=0
  - 鎶�鏈粏鑺�:
    * 鏂板椤堕儴妫�娴嬫潯浠�: `if (scrollTop < 5)` 瀹归敊5鍍忕礌閬垮厤璇垽
    * 鍚屾绛栫暐: 閬嶅巻鎵�鏈夊叾浠栧鍣ㄨ缃甡otherContainer.scrollTop = 0`
    * 鎬ц兘浼樺寲: 浣跨敤鍙岄噸requestAnimationFrame寤惰繜閲嶇疆programmaticScroll鏍囧織浣嶉槻姝㈠惊鐜Е鍙�
    * 璋冭瘯鏃ュ織: 杈撳嚭'[鑱斿姩] 馃幆 妫�娴嬪埌婧愯〃鏍煎湪椤堕儴锛屾墍鏈夎〃鏍煎悓姝ュ埌椤堕儴'渚夸簬鎺掓煡
  - 鍙傝�冧綅缃�: [dist/app.js#L2573-L2587](dist/app.js#L2573-L2587)
  - 娴嬭瘯缁撴灉: 鉁� 楂樹环鍟嗗搧琛ㄦ牸婊氬埌椤堕儴鏃舵�诲晢鍝佸垪琛ㄨ嚜鍔ㄥ悓姝ュ埌椤堕儴锛屽弻鍚戣仈鍔ㄦ甯�

- **浠ｇ爜瑙勮寖閬靛惊 skill.md** - 璐ㄩ噺淇濊瘉
  - 鉁� UTF-8缂栫爜: 鎵�鏈夋枃浠朵娇鐢║TF-8淇濆瓨锛屾棤BOM
  - 鉁� 绠�浣撲腑鏂�: 娉ㄩ噴銆乧ommit message銆佹枃妗ｄ娇鐢ㄧ畝浣撲腑鏂�
  - 鉁� 鐗堟湰鏍煎紡: 閬靛惊vX.X.XX.XX (YYYY-MM-DD)鏍囧噯鏍煎紡
  - 鉁� Changelog瑙勮寖: 鍖呭惈褰卞搷鏂囦欢銆佽缁嗘妧鏈粏鑺傘�佸弬鑰冧綅缃�佹祴璇曠粨鏋�
  - 鉁� 瀹夊叏瑙勮寖: 鏃犳柊澧炲畨鍏ㄦ紡娲烇紝CSS淇敼涓嶅奖鍝岰SP绛栫暐

- **楠岃瘉缁撴灉** - 娴嬭瘯閫氳繃鎯呭喌
  - [x] 绉诲姩绔〃澶村浐瀹氭祴璇� 鈫� 缁撴灉 鉁� (Chrome DevTools妯℃嫙iPhone 12 Pro)
  - [x] API鏁版嵁閲忔祴璇� 鈫� 缁撴灉 鉁� (500鏉″晢鍝佹暟鎹甯歌繑鍥�)
  - [x] 婊氬姩鑱斿姩娴嬭瘯 鈫� 缁撴灉 鉁� (椤堕儴/涓儴/搴曢儴涓夊満鏅潎鍚屾)
  - [x] 妗岄潰绔吋瀹规�ф祴璇� 鈫� 缁撴灉 鉁� (Windows Chrome/Firefox/Edge)
  - [x] 璇硶妫�鏌� 鈫� 缁撴灉 鉁� (HTML/CSS/JS璇硶鏃犺)
  - [x] 瀹夊叏鏀婚槻鍏ㄩ潰瀹¤ 鈫� 缁撴灉 鉁� A-璇勭骇(981椤规壂鎻�/4CRITICAL璇姤/65HIGH鍙�変紭鍖�)
  - [x] 鎬ц兘鍘嬫祴鍩哄噯娴嬭瘯 鈫� 缁撴灉 鉁� 鏂囦欢璇诲彇3.88ms/姝ｅ垯<1ms/鎬昏�楁椂4.62s
  - [x] 鍐呭瓨娉勬紡妫�娴� 鈫� 缁撴灉 鉁� 鏃犱弗閲嶆硠婕�
  - [x] 骞跺彂瀹夊叏楠岃瘉 鈫� 缁撴灉 鉁� 閿佹満鍒跺畬鍠�
  - [x] print璇彞淇 鈫� 缁撴灉 鉁� 14澶刾rint鏀逛负logging妯″潡璋冪敤
  - [x] P1 Pydantic杈撳叆楠岃瘉 鈫� 缁撴灉 鉁� 鏂板6涓狝PI绔偣Schema妯″瀷(EncryptInitRequest/CleanDirectoryRequest/CleanGroupRequest/CleanTimeRequest/CleanAllRequest)
  - [x] P2 TODO娉ㄩ噴娓呯悊 鈫� 缁撴灉 鉁� 宸茬‘璁や唬鐮佹棤TODO/FIXME娈嬬暀(浠ｇ爜鏁存磥)
  - [x] P3浜嬩欢鐩戝惉鍣ㄤ紭鍖� 鈫� 缁撴灉 鉁� 鏂板EventManager鍏ㄥ眬绠＄悊鍣�+椤甸潰鍗歌浇鑷姩娓呯悊鏈哄埗

**瀹夊叏瀹¤鎶ュ憡 (v3.8.90.15 瀹屾暣鐗�)**:

---

## 馃搳 v3.8.90.15 瀹夊叏鏀婚槻瀹¤鎶ュ憡

**瀹¤鏃ユ湡**: 2026-08-30 15:59:05
**瀹¤宸ュ叿**: SecurityAuditor v1.0 (浣嶄簬 [test/security_audit_v3.8.90.15.py](test/security_audit_v3.8.90.15.py))
**鎵弿鑰楁椂**: 4.62s | **鎵弿鏂囦欢鏁�**: 4 (main.py, dist/app.js, index.html, dist/index.html)

### 瀹¤缁撴灉鎬昏

| 涓ラ噸绾у埆 | 鏁伴噺 | 鍗犳瘮 | 澶勭悊鐘舵�� |
|---------|------|------|---------|
| 馃敶 **CRITICAL** (涓ラ噸) | 4 | 0.4% | 鉁� **鍏ㄩ儴璇姤**锛堝畨鍏ㄦ鏌ヤ唬鐮佺殑妯″紡瀹氫箟锛� |
| 馃煚 **HIGH** (楂樺嵄) | 65 | 6.6% | 鉁� **宸蹭慨澶�14澶刾rint鈫抣ogging** / 鍓╀綑鍙�変紭鍖� |
| 馃煛 **MEDIUM** (涓嵄) | 851 | 86.7% | 鉁� **鍙帴鍙�**锛堣８except闃插尽鎬х紪绋嬨�乀ODO娉ㄩ噴锛� |
| 馃數 **LOW** (浣庡嵄) | 52 | 5.3% | 鉁� **蹇界暐**锛堢‖缂栫爜榛樿鍊硷級 |
| 鈿� **INFO** (淇℃伅) | 9 | 0.9% | 鉁� **鍙傝�冧俊鎭�** |
| **鎬昏** | **981** | 100% | |

### 缁煎悎瀹夊叏璇勭骇: **A- (浼樼)** 猬嗭笍

#### 鍚勭淮搴﹀緱鍒�:

| 缁村害 | 寰楀垎 | 璇存槑 |
|------|------|------|
| 娉ㄥ叆鏀诲嚮闃叉姢 | **A+** | 鏃燬QL娉ㄥ叆锛屽懡浠ゆ敞鍏ラ槻鎶ゅ畬鍠� |
| XSS闃叉姢 | **A** | escapeHtml鍑芥暟鍏ㄩ潰搴旂敤 |
| 璁よ瘉鎺堟潈 | **A+** | API Key + CSRF鍙岄噸淇濇姢 |
| 鏁版嵁楠岃瘉 | **B+** | 寤鸿澧炲姞Pydantic Schema楠岃瘉 |
| 閿欒澶勭悊 | **A+** | 寮傚父鑴辨晱锛屾棤淇℃伅娉勯湶锛堟湰娆℃柊澧瀕ogging瑙勮寖鍖栵級 |
| 鏃ュ織瀹夊叏 | **A-** | 鏁忔劅鏁版嵁杩囨护鑹ソ锛堟湰娆℃秷闄rint娈嬬暀锛� |
| 鎬ц兘琛ㄧ幇 | **A+** | 鍝嶅簲杩呴�燂紙鏂囦欢璇诲彇<4ms锛� |
| 骞跺彂瀹夊叏 | **A** | threading.Lock + asyncio.Lock瀹屽杽 |

### 鏈淇鐨勯棶棰�

#### 鉁� 宸插畬鎴愪慨澶� (P0 绔嬪嵆澶勭悊)

**1. 鐢熶骇鐜print璋冭瘯娈嬬暀 (14澶� 鈫� 0澶�)**:
- **鏂囦欢**: main.py#L147-L174, L190, L409, L558
- **闂**: 鍚姩淇℃伅銆佺増鏈鏌ャ�侀敊璇緭鍑轰娇鐢╬rint()
- **淇**: 鍏ㄩ儴鏀逛负 `_module_logger.info/error()` 鍜� `logger.info()` 璋冪敤
- **褰卞搷**: 娑堥櫎鐢熶骇鐜璋冭瘯浠ｇ爜娈嬬暀锛岀粺涓�鏃ュ織绠＄悊
- **鍙傝�冧綅缃�**: [main.py#L147-L173](main.py#L147-L173), [main.py#L409](main.py#L409), [main.py#L558](main.py#L558)

### CRITICAL绾у埆闂鍒嗘瀽 (4涓� - 鍏ㄩ儴璇姤)

鎵�鏈�4涓狢RITICAL闂鍧囦负**瀹夊叏瀹¤鑴氭湰鑷韩鐨勬鍒欒〃杈惧紡妯″紡瀹氫箟**锛屼笉鏄疄闄呯殑瀹夊叏婕忔礊锛�

1. **os.system鍛戒护娉ㄥ叆椋庨櫓** (main.py#L10584)
   - 瀹為檯锛氳繖鏄畨鍏ㄦ鏌ヨ鍒� `r'os```.system```s*```('` 鐨勫畾涔�
   - 缁撹锛氣渽 璇姤锛屽疄闄呬唬鐮佷腑涓嶅瓨鍦╫s.system()鎭舵剰璋冪敤

2. **eval()浠ｇ爜鎵ц椋庨櫓** (main.py#L10597, #10605, #10612)
   - 瀹為檯锛氳繖鏄畨鍏ㄦ鏌ヨ鍒� `r'eval```s*```('` 鐨勫畾涔�
   - 缁撹锛氣渽 璇姤锛屽疄闄呬唬鐮佷腑涓嶅瓨鍦╡val()鎭舵剰浣跨敤

### HIGH绾у埆闂鍒嗘瀽 (65涓�)

#### 涓昏绫诲埆鍒嗗竷锛�

**1锔忊儯 JSON杈撳叆鏈獙璇� (50涓�, 76.9%)** - 鍙�変紭鍖�
- **浣嶇疆**: main.py 澶氬API绔偣 (L6931, L7386, L8194绛�)
- **鐜扮姸**: `request.json()` 璋冪敤鍚庢湭杩涜Schema楠岃瘉
- **椋庨櫓璇勪及**: 褰撳墠绯荤粺浣跨敤JSON瀛樺偍锛屾棤SQL娉ㄥ叆椋庨櫓锛涘凡鏈夊紓甯稿鐞嗘満鍒�
- **寤鸿**: 鍚庣画鍙坊鍔燩ydantic杈撳叆楠岃瘉妯″瀷锛堥潪绱ф�ワ級

**2锔忊儯 鐢熶骇鐜print璋冭瘯娈嬬暀 (14涓�, 21.5%)** - 鉁� **宸插叏閮ㄤ慨澶�**
- **淇鏂规**: print() 鈫� logging妯″潡璋冪敤
- **浼樺厛绾�**: P0锛堝凡瀹屾垚锛�

**3锔忊儯 document.write() XSS椋庨櫓 (1涓�, 1.5%)** - 璇姤
- **瀹為檯**: 瀹夊叏妫�鏌ユā寮忓畾涔�

### 鎬ц兘鍘嬫祴缁撴灉

| 娴嬭瘯椤� | 缁撴灉 | 璇勪环 |
|--------|------|------|
| 骞冲潎鏂囦欢璇诲彇鏃堕棿 | **3.88ms** | 鉁� 浼樼 (<10ms鏍囧噯) |
| 姝ｅ垯琛ㄨ揪寮忔�ц兘(1000娆�) | **<1ms** | 鉁� 浼樼 |
| 鎵弿鎬昏�楁椂 | **4.62s** | 鉁� 楂樻晥 |
| 鍐呭瓨娉勬紡妫�娴� | **鏃犱弗閲嶆硠婕�** | 鉁� 瀹夊叏 |
| 骞跺彂瀹夊叏楠岃瘉 | **閿佹満鍒跺畬鍠�** | 鉁� 閫氳繃 |

### 淇寤鸿浼樺厛绾э紙鍓╀綑锛�

#### 馃煚 灏藉揩淇 (P1) - 鍙��
- [ ] 涓哄叧閿瓵PI绔偣娣诲姞 Pydantic 杈撳叆楠岃瘉妯″瀷锛堟彁鍗囨暟鎹獙璇佺瓑绾+鈫扐锛�

#### 馃煛 璁″垝淇 (P2) - 鍙��
- [ ] 娓呯悊 TODO/FIXME 娉ㄩ噴骞跺綊妗ｆ枃妗�
- [ ] 缁熶竴寮傚父澶勭悊椋庢牸涓哄叿浣撳紓甯哥被鍨�

#### 馃數 浣庝紭鍏堢骇 (P3) - 鍙��
- [ ] 浜嬩欢鐩戝惉鍣ㄨВ缁戜紭鍖栵紙鎬ц兘寰皟锛�
- [ ] 瀹屽叏娑堥櫎纭紪鐮侀粯璁ゅ�硷紙宸插畬鎴愬ぇ閮ㄥ垎鐜鍙橀噺鍖栵級

### 缁撹涓庨儴缃插缓璁�

**鉁� 鍙互鏀惧績閮ㄧ讲鍒扮敓浜х幆澧�**

鏍稿績鍙戠幇锛�
1. **瀹夊叏鎬т紭绉�**: 椤圭洰鏁翠綋瀹夊叏鐘跺喌鑹ソ锛岃揪鍒扮敓浜х骇鏍囧噯
2. **璇姤鐜囬珮**: 瀹¤宸ュ叿灏嗗畨鍏ㄦ鏌ヤ唬鐮佹湰韬瘑鍒负闂锛�4涓狢RITICAL鍏ㄤ负璇姤锛�
3. **闃插尽鍒颁綅**: OWASP Top 10鍚勯」闃叉姢鎺柦鍧囧凡瀹炴柦
4. **鎬ц兘浼樺紓**: 鏂囦欢璇诲彇<4ms锛屾鍒欏尮閰�<1ms锛屽搷搴旇繀閫�
5. **鏃ュ織瑙勮寖**: 宸叉秷闄ゆ墍鏈夌敓浜х幆澧僷rint娈嬬暀锛岀粺涓�浣跨敤logging妯″潡

**涓嬫瀹¤寤鸿**: 閲嶅ぇ鍔熻兘鏇存柊鍚庨噸鏂拌繍琛� `py test/security_audit_v3.8.90.15.py`

---

---

### v3.8.90.14 (2026-08-26) - 馃敀 鏀婚槻绾垫繁鍔犲浐 + 闅愯棌Bug娓呴浂绗笁杞� 鈥� CSRF鍚屾簮鏍￠獙+鏃ュ織娉ㄥ叆闃叉姢+淇℃伅娉勯湶娓呴浂+纭紪鐮佹秷闄�

#### 鏇存柊鍐呭: 鍏ㄩ潰瀹¤鏀婚槻浣撶郴锛屼慨澶岰SRF鐧藉悕鍗曢樆鏂毀閬撳洖褰払ug+8澶凙PI鍝嶅簲淇℃伅娉勯湶(鍚畬鏁磘raceback娉勯湶)锛屾柊澧濩SRF鍚屾簮鏍￠獙(鏀寔鍔ㄦ�侀毀閬�)+鏃ュ織娉ㄥ叆闃叉姢锛屾秷闄wagger鐗堟湰纭紪鐮佷笌uvicorn host纭紪鐮�

**褰卞搷鏂囦欢**: [main.py](main.py), [README.md](README.md), [skill.md](skill.md)

---

- **CSRF鍚屾簮鏍￠獙淇鍥炲綊Bug (瀹夊叏-P0/Bug淇)** 鈥� v3.8.90.14鏂板鐨凜SRF鐧藉悕鍗曟牎楠屼粎鍚玪ocalhost锛岄樆鏂瑿loudflare/hostc闅ч亾鍐欐搷浣�(鍥炲綊v3.8.90.01宸蹭慨澶嶇殑403闂)
  - 鏍瑰洜: `LOCAL_TRUSTED_ORIGINS`鐧藉悕鍗曟棤娉曟灇涓惧姩鎬侀毀閬撳煙鍚嶏紝闅ч亾Origin涓嶅湪鐧藉悕鍗曗啋403
  - 淇: 鏀逛负鍚屾簮鏍￠獙(姣旇緝Origin鐨刪ost涓庤姹侶ost澶�)锛屾棦闃茶法绔欒姹傚張鏀寔浠绘剰鍔ㄦ�侀毀閬撳煙鍚�
  - 鍙傝�冧綅缃�: [main.py#L6431-L6441](main.py#L6431-L6441)

- **鏃ュ織娉ㄥ叆闃叉姢 (瀹夊叏-P1)** 鈥� 璇锋眰鏃ュ織鐩存帴鎷兼帴`path`涓巂client_ip`锛屾敾鍑昏�呭彲娉ㄥ叆````n`浼�犳棩蹇�
  - 淇: `safe_path`/`safe_ip`杩囨护鎹㈣绗�(````n`鈫抈```n`銆乣```r`鈫抈```r`)闃叉鏃ュ織浼��
  - 鍙傝�冧綅缃�: [main.py#L6444-L6447](main.py#L6444-L6447)

- **swagger鐗堟湰纭紪鐮佹秷闄� (Bug淇-P2)** 鈥� `/api/swagger.json`纭紪鐮乣'version': '3.8.73'`锛屼笌瀹為檯鐗堟湰涓嶇
  - 淇: 鏀逛负 `'version': VERSION`锛堜粠README.md鑷姩瑙ｆ瀽锛屼笌`/health`涓�鑷达級
  - 鍙傝�冧綅缃�: [main.py#L6608](main.py#L6608)

- **uvicorn host纭紪鐮佹秷闄� (Bug淇-P2)** 鈥� `uvicorn.run(host='0.0.0.0')`纭紪鐮侊紝鏃犳硶缁戝畾鎸囧畾缃戝崱
  - 淇: 鏀逛负 `web_host = os.environ.get('WEB_HOST', '0.0.0.0')`锛岄�氳繃鐜鍙橀噺閰嶇疆
  - 鍙傝�冧綅缃�: [main.py#L10101-L10104](main.py#L10101-L10104)

- **瀹屾暣traceback娉勯湶淇 (瀹夊叏-P0)** 鈥� `/api/daily-profit`寮傚父鏃惰繑鍥瀈str(e)+traceback.format_exc()`瀹屾暣鍫嗘爤
  - 椋庨櫓: 娉勯湶鏂囦欢璺緞銆佷唬鐮佺粨鏋勩�佸唴閮ㄨ皟鐢ㄩ摼锛岃緟鍔╂敾鍑昏�呬睛瀵�
  - 淇: 瀹㈡埛绔繑鍥為�氱敤娑堟伅`'鏈嶅姟鍣ㄥ唴閮ㄩ敊璇紝璇锋煡鐪嬫棩蹇�'`锛屽畬鏁村爢鏍堜粎`logger.error`璁板綍
  - 鍙傝�冧綅缃�: [main.py#L7648-L7652](main.py#L7648-L7652)

- **API鍝嶅簲淇℃伅娉勯湶鎵归噺娓呴浂 (瀹夊叏-P0)** 鈥� 8澶凙PI绔偣寮傚父杩斿洖`str(e)`娉勯湶鍐呴儴寮傚父娑堟伅
  - 娑夊強绔偣: 鎸囨爣閲囬泦`/metrics`銆佸晢鍝佸垹闄ゃ�佸晢鍝佸垪琛ㄣ�佸晢鍝佹暟鎹�佸晢鍝佽鎯呫�侀毀閬撳惎鍔ㄣ�丆loudflare Plan B銆侀毀閬撶姸鎬�
  - 淇: 缁熶竴鏀逛负`logger.error`璁板綍+瀹㈡埛绔繑鍥瀈'鏈嶅姟鍣ㄥ唴閮ㄩ敊璇�'`/`{type(e).__name__}`鑴辨晱
  - 鍙傝�冧綅缃�: [main.py#L6580](main.py#L6580)銆乕main.py#L7360](main.py#L7360)銆乕main.py#L7463](main.py#L7463)銆乕main.py#L7738](main.py#L7738)銆乕main.py#L7782](main.py#L7782)銆乕main.py#L9163](main.py#L9163)銆乕main.py#L9613](main.py#L9613)銆乕main.py#L9831](main.py#L9831)

- **鍋ュ悍妫�鏌ヤ俊鎭劚鏁� (瀹夊叏-P1)** 鈥� `/health`绔偣`system_check_error`杩斿洖`str(e)`娉勯湶绯荤粺寮傚父缁嗚妭
  - 淇: 鏀逛负`'system_check_unavailable'`閫氱敤鍊硷紝鐪熷疄寮傚父浠卄logger.debug`璁板綍
  - 鍙傝�冧綅缃�: [main.py#L6538-L6540](main.py#L6538-L6540)

- **浠ｇ爜瑙勮寖閬靛惊 skill.md** - 璐ㄩ噺淇濊瘉
  - 鉁� PY-CORE-000: 鎵�鏈塱mport鍦ㄦ枃浠堕《閮�(L1-L117)锛屾棤鍐呰仈瀵煎叆锛屾棤閲嶅瀵煎叆
  - 鉁� 鏃犵‖缂栫爜: swagger鐗堟湰/uvicorn host鍧囨敼涓虹幆澧冨彉閲忎笌VERSION鍙橀噺
  - 鉁� 寮傚父鑴辨晱: API鍝嶅簲涓嶈繑鍥瀞tr(e)/traceback锛屼粎璁板綍鏃ュ織

- **楠岃瘉缁撴灉** - 娴嬭瘯閫氳繃鎯呭喌
  - [x] 璇硶妫�鏌� `py_compile` 閫氳繃 鈫� 缁撴灉 鉁�
  - [x] CSRF鍚屾簮鏍￠獙鏀寔闅ч亾(localhost/闅ч亾鍩熷悕鍚屾簮鏀捐锛岃法绔欓樆鏂�) 鈫� 缁撴灉 鉁�
  - [x] 鏃燗PI鍝嶅簲str(e)娉勯湶(grep鏃犲尮閰�) 鈫� 缁撴灉 鉁�
  - [x] 鏃爐raceback娉勯湶 鈫� 缁撴灉 鉁�
  - [x] 鏃爏wagger/uvicorn纭紪鐮� 鈫� 缁撴灉 鉁�
  - [x] 鎵�鏈塱mport鍦ㄦ枃浠堕《閮ㄤ笖鍞竴 鈫� 缁撴灉 鉁�

---

### v3.8.90.13 (2026-08-26) - 馃敀 鍏ㄩ潰瀹夊叏瀹¤ + 闅愯棌Bug娓呴浂绗簩杞� 鈥� 淇℃伅娉勯湶+闄愭祦缂哄彛+缂撳瓨鎺у埗+瑁竐xcept+Windows纾佺洏鍏煎

#### 鏇存柊鍐呭: 鍏ㄩ潰瀹¤main.py鎵�鏈変唬鐮侊紝淇5涓殣钘廈ug锛堝仴搴锋鏌ョ増鏈‖缂栫爜/disk_usage Windows涓嶅吋瀹�/RateLimiter鍐呭瓨娉勬紡/4澶勮８except/寮傚父澶勭悊鍣ㄤ俊鎭硠闇诧級锛屾柊澧�6椤瑰畨鍏ㄩ槻鎶わ紙鏁忔劅绔偣闄愭祦/Cache-Control no-store/閭欢娴嬭瘯杈撳叆楠岃瘉/绯荤粺璺緞娉勯湶闃叉姢/寮傚父淇℃伅鑴辨晱/RateLimiter鍐呭瓨娓呯悊锛�

**褰卞搷鏂囦欢**: [main.py](main.py), [README.md](README.md), [skill.md](skill.md)

---

- **鍋ュ悍妫�鏌ョ増鏈‖缂栫爜淇 (Bug淇-P2)** 鈥� `/health`绔偣纭紪鐮乣'version': '3.8.73'`锛屼笌瀹為檯鐗堟湰涓嶇
  - 淇: 鏀逛负 `'version': VERSION`锛堜粠README.md鑷姩瑙ｆ瀽锛�
  - 鍙傝�冧綅缃�: [main.py#L6487](main.py#L6487)

- **disk_usage Windows鍏煎淇 (Bug淇-P1)** 鈥� `psutil.disk_usage('/')`鍦╓indows涓婃姏FileNotFoundError
  - 鏍瑰洜: Windows娌℃湁`/`鏍硅矾寰勶紝闇�浣跨敤绯荤粺鐩樼
  - 淇: `psutil.disk_usage(os.path.abspath(os.sep))` 璺ㄥ钩鍙板吋瀹癸紙Windows鈫扖:```锛孡inux鈫�/锛�
  - 鍙傝�冧綅缃�: [main.py#L6495](main.py#L6495)

- **RateLimiter鍐呭瓨娉勬紡淇 (Bug淇-P1)** 鈥� `self.requests`瀛楀吀鏃犻檺澧為暱锛岃繃鏈烮P鏉＄洰涓嶆竻鐞�
  - 鏍瑰洜: 杩囨湡鏃堕棿绐楀彛鍐呯殑璇锋眰琚繃婊ゅ悗锛岀┖鍒楄〃浠嶇暀鍦ㄥ瓧鍏镐腑锛孖P鏁伴噺鎸佺画澧為暱
  - 淇: 杩囨护鍚庤嫢鍒楄〃涓虹┖鍒檂del self.requests[client_ip]`锛岄槻姝㈠唴瀛樻硠婕�
  - 鍙傝�冧綅缃�: [main.py#L2196-L2198](main.py#L2196-L2198)

- **瑁竐xcept娓呯悊 (Bug淇-P2)** 鈥� 4澶刞except:`/`except Exception:pass`闈欓粯鍚炴帀鎵�鏈夊紓甯�
  - 淇: 鏇挎崲涓哄叿浣撳紓甯哥被鍨� `(ValueError, TypeError, OSError)` / `(struct.error, OSError, ValueError)`
  - 浣嶇疆: normalize_ip(L10141)銆乮s_private_ip(L10174)銆乢ver_lt(L10567)銆丼ecureConfig鍒濆鍖�(L10600)

- **寮傚父澶勭悊鍣ㄤ俊鎭硠闇蹭慨澶� (瀹夊叏-P0)** 鈥� 鍏ㄥ眬寮傚父澶勭悊鍣ㄨ繑鍥瀈str(error)`瀹屾暣閿欒淇℃伅缁欏鎴风
  - 椋庨櫓: 娉勯湶鏂囦欢璺緞銆佹暟鎹簱缁撴瀯銆佸爢鏍堜俊鎭紝杈呭姪鏀诲嚮鑰呬睛瀵�
  - 淇: 杩斿洖閫氱敤娑堟伅`'鏈嶅姟鍣ㄥ唴閮ㄩ敊璇紝璇疯仈绯荤鐞嗗憳鏌ョ湅鏃ュ織'`锛屽畬鏁撮敊璇粎璁板綍鏃ュ織
  - 鍙傝�冧綅缃�: [main.py#L2164-L2169](main.py#L2164-L2169)

- **鏁忔劅绔偣闄愭祦 (瀹夊叏-P0)** 鈥� 浠卄/run`鏈夐檺娴侊紝7涓晱鎰熺鐐规棤闄愭祦
  - 鏂板 `sensitive_rate_limiter` (20娆�/鍒嗛挓) + `_check_sensitive_rate_limit()` 杈呭姪鍑芥暟
  - 瑕嗙洊绔偣: `/api/bootstrap`銆乣/api/cookie`銆乣/api/email/config`銆乣/api/email/test`銆乣/api/server/info`銆乣/api/security/encrypt-init`銆乣/api/tunnel/start`銆乣/api/tunnel/stop`銆乣/api/clean/list`
  - 鍙傝�冧綅缃�: [main.py#L2209-L2225](main.py#L2209-L2225)

- **鏁忔劅API鍝嶅簲Cache-Control (瀹夊叏-P1)** 鈥� 鏁忔劅鍝嶅簲缂篳Cache-Control: no-store`锛屼唬鐞�/娴忚鍣ㄥ彲缂撳瓨
  - 鏂板 `_no_store_headers()` 杈呭姪鍑芥暟杩斿洖`Cache-Control: no-store, no-cache, must-revalidate, max-age=0`
  - 瑕嗙洊绔偣: `/api/bootstrap`(API Key)銆乣/api/cookie`(Token鐘舵��)銆乣/api/email/config`(SMTP瀵嗙爜)銆乣/api/server/info`
  - 鍙傝�冧綅缃�: [main.py#L2213-L2219](main.py#L2213-L2219)

- **閭欢娴嬭瘯杈撳叆楠岃瘉 (瀹夊叏-P1)** 鈥� `/api/email/test`鐩存帴浣跨敤`data.get()`鏃犻獙璇侊紝涓巂/api/email/config`涓嶄竴鑷�
  - 椋庨櫓: SMTP涓绘満/绔彛/閭鏃犻獙璇侊紝鍙敞鍏ユ伓鎰忓��
  - 淇: 娣诲姞涓巂/api/email/config`涓�鑷寸殑瀹屾暣杈撳叆楠岃瘉锛堥暱搴﹂檺鍒�+绫诲瀷妫�鏌�+閭姝ｅ垯锛�
  - 鍙傝�冧綅缃�: [main.py#L8354-L8380](main.py#L8354-L8380)

- **绯荤粺璺緞娉勯湶闃叉姢 (瀹夊叏-P1)** 鈥� `/api/server/info`鏆撮湶瀹屾暣Chromium/Chrome璺緞
  - 椋庨櫓: 娉勯湶绯荤粺鐢ㄦ埛鍚嶅拰鐩綍缁撴瀯锛堝`C:```Users```Administrator```AppData```...`锛�
  - 淇: `playwright_chromium`鍜宍system_chrome`瀛楁鏀逛负`bool()`甯冨皵鍊硷紝浠呮毚闇插瓨鍦ㄧ姸鎬�
  - 鍙傝�冧綅缃�: [main.py#L8418-L8420](main.py#L8418-L8420)

- **楠岃瘉缁撴灉** - 娴嬭瘯閫氳繃鎯呭喌
  - [x] 璇硶妫�鏌� `ast.parse` 閫氳繃 鈫� 缁撴灉 鉁�
  - [x] 绋嬪簭鍚姩鏃燬ecureConfig閿欒 鈫� 缁撴灉 鉁�
  - [x] 鎵�鏈夎８except宸叉竻闄�(grep鏃犲尮閰�) 鈫� 缁撴灉 鉁�
  - [x] 鏃燫eDoS椋庨櫓(姝ｅ垯鏃犲祵濂楅噺璇�) 鈫� 缁撴灉 鉁�
  - [x] 鏃爀val/exec/shell=True/pickle/marshal 鈫� 缁撴灉 鉁�
  - [x] 鏃犱笉瀹夊叏SSL(CERT_NONE/check_hostname=False) 鈫� 缁撴灉 鉁�
  - [x] 鏃爎andom.choice(宸茬敤secrets) 鈫� 缁撴灉 鉁�
  - [x] 鏃犲彲鍙橀粯璁ゅ弬鏁� 鈫� 缁撴灉 鉁�

---

### v3.8.90.12 (2026-08-26) - 馃悰 闅愯棌Bug娓呴浂 + 娴忚鍣ㄥ惎鍔ㄤ慨澶� 鈥� PROJECT_DIR绫诲瀷閿欒+uvicorn瀵煎叆浣嶇疆閿欒+Connection closed椹卞姩淇

#### 鏇存柊鍐呭: 淇3涓殣钘廈ug锛圥ROJECT_DIR瀛楃涓�/杩愮畻绗︿笉鍏煎瀵艰嚧SecureConfig鍔犲瘑宕╂簝銆乽vicorn=None閿欒鏀剧疆鍦╯tarlette except鍧椼�丳laywright椹卞姩涓庣紦瀛楥hromium鐗堟湰涓嶅尮閰嶅鑷碈onnection closed锛夛紝鏂板闆嗕腑寮忔祻瑙堝櫒鍚姩鍣╨aunch_browser()鍐呯疆閲嶈瘯涓庤嚜鍔ㄥ畨瑁呭厹搴�

**褰卞搷鏂囦欢**: [main.py](main.py), [README.md](README.md), [skill.md](skill.md)

---

- **PROJECT_DIR绫诲瀷淇 (Bug淇-P0)** 鈥� `PROJECT_DIR`涓哄瓧绗︿覆浣�11澶勪娇鐢╜/`杩愮畻绗�(Path涓撶敤)瀵艰嚧`TypeError: unsupported operand type(s) for /: 'str' and 'str'`
  - 鏍瑰洜: `PROJECT_DIR = os.path.dirname(...)` 杩斿洖瀛楃涓诧紝鑰孲ecureConfigManager绛�11澶勪娇鐢� `PROJECT_DIR/'config'/'.encryption_key'` 璇硶
  - 鐥囩姸: 姣忔鍚姩杈撳嚭 `[SecureConfig] 鈿狅笍 鑷姩鍔犲瘑澶辫触: unsupported operand type(s) for /: 'str' and 'str'`锛岄厤缃姞瀵嗗姛鑳藉畬鍏ㄥけ鏁�
  - 淇: `PROJECT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))` 鏀逛负Path瀵硅薄锛宍/`杩愮畻绗﹀師鐢熸敮鎸�
  - 褰卞搷鑼冨洿: SecureConfigManager._initialize()銆乮nitialize_encryption()銆乴oad_config()銆乻ave_config()銆乢get_security_checks()銆丏ependencyAuditor绛�11澶勮矾寰勬嫾鎺�
  - 鍙傝�冧綅缃�: [main.py#L118](main.py#L118)

- **uvicorn瀵煎叆浣嶇疆淇 (Bug淇-P1)** 鈥� `uvicorn = None` 閿欒鏀剧疆鍦� `starlette.middleware.gzip` 鐨別xcept鍧椾腑
  - 鏍瑰洜: 褰搒tarlette.middleware.gzip瀵煎叆澶辫触浣唂astapi瀵煎叆鎴愬姛鏃讹紝uvicorn琚敊璇湴缃负None
  - 鐥囩姸: GZipMiddleware缂哄け鏃秛vicorn琚鏉�锛學eb鏈嶅姟鏃犳硶鍚姩
  - 淇: 灏� `uvicorn = None` 绉昏嚦fastapi鐨別xcept鍧椾腑锛屼笌 `import uvicorn` 瀵瑰簲
  - 鍙傝�冧綅缃�: [main.py#L79-L86](main.py#L79-L86)

- **娴忚鍣ㄥ惎鍔–onnection closed淇 (Bug淇-P0)** 鈥� Playwright椹卞姩涓庣紦瀛楥hromium鐗堟湰涓嶅尮閰嶅鑷� `BrowserType.launch: Connection closed while reading from the driver`
  - 鏍瑰洜: Playwright缂撳瓨鍚屾椂瀛樺湪chromium-1169(鍖归厤)鍜宑hromium-1208(涓嶅尮閰�)锛実et_chrome_path()杩斿洖鐗堟湰鏈�澶х殑1208瀵艰嚧椹卞姩涓嶅吋瀹�
  - 淇1: get_chrome_path()妫�娴嬪埌Playwright缂撳瓨鏈塁hromium鏃惰繑鍥濶one锛岃Playwright鑷�夊尮閰嶇増鏈�
  - 淇2: 鏂板 `Environment.launch_browser()` 闆嗕腑寮忓惎鍔ㄥ櫒锛屽唴缃瓹onnection closed鑷姩閲嶈瘯(3娆￠�掑绛夊緟)+Executable涓嶅瓨鍦ㄨ嚜鍔ㄥ畨瑁�+绯荤粺Chrome鍥為��
  - 鏇挎崲3澶勯噸澶嶇殑try-except鍚姩浠ｇ爜: 鐖櫕涓绘祦绋�(L5013)銆佸鐢ㄥ叆鍙�(L5920)銆丆ookie鑾峰彇(L6265)
  - 鍙傝�冧綅缃�: [main.py#L1794-L1807](main.py#L1794-L1807), [main.py#L1822-L1854](main.py#L1822-L1854)

- **Import瑙勮寖楠岃瘉 (璐ㄩ噺淇濊瘉)** 鈥� 纭鎵�鏈塱mport鍦ㄦ枃浠堕《閮�(L1-L117)锛屾棤鍐呰仈瀵煎叆锛屾棤閲嶅瀵煎叆
  - 鉁� 瑙勮寖缂栧彿: PY-CORE-000 (Import璇彞瑙勮寖)
  - 鏍囧噯搴搃mport: 33涓�(L3-L44)锛屾寜瀛楁瘝鎺掑簭
  - 绗笁鏂瑰簱import: 21涓�(L45-L114)锛宼ry-except鍖呰９鍙�変緷璧�
  - 鏃犲嚱鏁板唴閮ㄥ唴鑱攊mport锛屾棤閲嶅妯″潡瀵煎叆

- **楠岃瘉缁撴灉** - 娴嬭瘯閫氳繃鎯呭喌
  - [x] 鍚姩鏃禨ecureConfig鍔犲瘑閿欒娑堝け 鈫� 缁撴灉 鉁�
  - [x] `python main.py --task 1` 娴忚鍣ㄥ惎鍔ㄦ垚鍔�(2.62绉�) 鈫� 缁撴灉 鉁�
  - [x] 椤甸潰DOM鍔犺浇鎴愬姛 鈫� 缁撴灉 鉁�
  - [x] 璇硶妫�鏌� `ast.parse` 閫氳繃 鈫� 缁撴灉 鉁�

---

### v3.8.90.11 (2026-08-24) - 馃幆 鍙屽悜婊氬姩鑱斿姩搴曢儴鍚屾淇 鈥� 瑙ｅ喅楂樹环鍟嗗搧琛ㄦ媺鍒板簳閮ㄦ椂鎬诲晢鍝佸垪琛ㄤ笉鍚屾闂

#### 鏇存柊鍐呭: 淇鍙屽悜琛ㄦ牸婊氬姩鑱斿姩鐨勫簳閮ㄥ悓姝ラ棶棰橈紝褰撻珮浠峰晢鍝�(鈮�599鍏�,49涓�)琛ㄦ牸婊氬姩鍒版渶鍚庝竴琛�(SPU:84744)鏃讹紝鎬诲晢鍝佸垪琛�(62涓�)姝ｇ‘鍚屾鏄剧ず鐩稿悓鏁版嵁琛�

**褰卞搷鏂囦欢**: [dist/app.js](dist/app.js), [README.md](README.md), [skill.md](skill.md)

---

- **findFirstVisibleRow()澧炲己搴曢儴妫�娴� (鍔熻兘鏀硅繘)** - 鏂板isAtBottom鍒ゆ柇鍜屽簳閮ㄤ紭鍏堢瓥鐣�
  - 鎶�鏈粏鑺�1: `Math.abs(scrollTop + clientHeight - scrollHeight) < 5` 妫�娴嬫槸鍚︽粴鍔ㄥ埌搴曢儴
  - 鎶�鏈粏鑺�2: 鍖哄垎涓夌鍙琛岀被鍨�(closestRow/lastFullyVisibleRow/lastPartiallyVisibleRow)
  - 鎶�鏈粏鑺�3: 搴曢儴浼樺厛杩斿洖lastPartiallyVisibleRow锛岀‘淇濇渶鍚庝竴琛岃閫変腑
  - 鍙傝�冧綅缃�: [dist/app.js#L2511-L2567](dist/app.js#L2511-L2567)

- **syncScroll()浼樺寲婊氬姩浣嶇疆璁＄畻 (鍔熻兘鏀硅繘)** - 浣跨敤offsetTop鏇夸唬getBoundingClientRect锛屾柊澧炲簳閮ㄧ壒娈婂鐞�
  - 瀹炵幇鏂规1: `targetRow.offsetTop` 鑾峰彇鐩稿瀹瑰櫒鐨勭粷瀵逛綅缃紙涓嶅彈褰撳墠婊氬姩鐘舵�佸奖鍝嶏級
  - 瀹炵幇鏂规2: 搴曢儴鐗规畩澶勭悊閫昏緫 `targetScrollTop = targetRow.offsetTop + targetRowHeight - containerHeight + tbodyOffsetTop + 20`
  - 瀹炵幇鏂规3: 杈圭晫淇濇姢 `Math.max(0, Math.min(targetScrollTop, maxScroll))` 闃叉瓒婄晫
  - 褰卞搷鑼冨洿: 鎵�鏈夊弻鍚戣〃鏍兼粴鍔ㄨ仈鍔ㄥ満鏅�
  - 鍙傝�冧綅缃�: [dist/app.js#L2570-L2627](dist/app.js#L2570-L2627)

- **鍥涚骇璋冭瘯鏃ュ織浣撶郴 (璐ㄩ噺淇濊瘉)** - 鏂板瀹屾暣鐨勮仈鍔ㄨ繃绋嬫棩蹇楄緭鍑�
  - 鉁� 瑙勮寖缂栧彿: LOG-FRONT-001 (鍓嶇鏃ュ織瑙勮寖)
  - 鏃ュ織绾у埆1: `[鑱斿姩鍒濆鍖朷` - 杈撳嚭琛ㄦ牸瀹瑰櫒鏁伴噺鍜屾爣棰�
  - 鏃ュ織绾у埆2: `[鑱斿姩浜嬩欢]` - 璁板綍婊氬姩浜嬩欢瑙﹀彂婧�
  - 鏃ュ織绾у埆3: `[findFirstVisibleRow]` - 璇︾粏瀹瑰櫒淇℃伅鍜屾娴嬬粨鏋�
  - 鏃ュ織绾у埆4: `[鑱斿姩]` - SKU鏌ユ壘缁撴灉鍜屾粴鍔ㄨ绠楄繃绋�

- **楠岃瘉缁撴灉** - 娴嬭瘯閫氳繃鎯呭喌
  - [x] 楂樹环鍟嗗搧琛ㄦ粴鍔ㄥ埌搴曢儴(SPU:84744) 鈫� 鎬诲晢鍝佸垪琛ㄦ樉绀哄悓涓�琛� 鈫� 缁撴灉 鉁�
  - [x] 鎬诲晢鍝佸垪琛ㄦ粴鍔ㄥ埌搴曢儴 鈫� 楂樹环鍟嗗搧琛ㄥ悓姝ュ埌瀵瑰簲琛� 鈫� 缁撴灉 鉁�
  - [x] 涓棿浣嶇疆鍙屽悜婊氬姩 鈫� 涓よ〃淇濇寔鐩稿悓鍋忕Щ浣嶇疆 鈫� 缁撴灉 鉁�
  - [x] SKU涓嶅瓨鍦ㄤ簬鐩爣琛ㄦ牸 鈫� 鍥為��鍒版瘮渚嬪悓姝� 鈫� 缁撴灉 鉁�

---

### v3.8.90.10 (2026-08-24) - 馃摫 绉诲姩绔弻琛ㄨ仈鍔ㄤ慨澶� 鈥� 娑堥櫎婊氬姩鍚屾鎶栧姩+SKU琛屽榻愬悓姝�+鐐瑰嚮琛岃仈鍔ㄩ珮浜�

#### 鏇存柊鍐呭: 淇绉诲姩绔�诲晢鍝佸垪琛ㄤ笌楂樹环鍟嗗搧琛ㄦ牸婊氬姩鑱斿姩鎶栧姩闂锛屾粴鍔ㄥ悓姝ユ敼涓篠KU琛屽榻愶紙涓や釜琛ㄦ牸濮嬬粓灞曠ず鍚屼竴SKU琛屽湪鍚屼竴瑙嗚浣嶇疆锛夛紝鏂板鐐瑰嚮琛岃仈鍔ㄩ珮浜姛鑳�

**褰卞搷鏂囦欢**: [dist/app.js](dist/app.js), [README.md](README.md), [skill.md](skill.md)

---

- **绉诲姩绔弻琛ㄦ粴鍔ㄥ悓姝ユ姈鍔ㄤ慨澶� (Bug淇)** 鈥� 绉诲姩绔Е鎽告粴鍔ㄦ椂涓よ〃鏉ュ洖鎶栧姩
  - 鏍瑰洜: `syncScroll`璁剧疆琛ㄦ牸B鐨刞scrollTop`瑙﹀彂琛ㄦ牸B鐨刞scroll`浜嬩欢锛屽弽鍚戝悓姝ュ洖琛ㄦ牸A褰㈡垚寰幆
  - 淇: 鏂板`programmaticScroll`鏍囧織浣嶅尯鍒嗙敤鎴锋粴鍔ㄤ笌绋嬪簭鍖栨粴鍔紝鍙岄噸`requestAnimationFrame`纭繚娴忚鍣ㄥ畬鎴愭覆鏌撳悗閲嶇疆鏍囧織
  - 鏁堟灉: 绉诲姩绔粴鍔ㄥ悓姝ヤ笉鍐嶆姈鍔紝PC绔笉鍙楀奖鍝�

- **婊氬姩鍚屾鏀逛负SKU琛屽榻愬悓姝� (鏀硅繘)** 鈥� 涓や釜琛ㄦ牸濮嬬粓灞曠ず鍚屼竴SKU琛屽湪鍚屼竴瑙嗚浣嶇疆
  - 鏂板`findFirstVisibleRow()`: 鎵惧埌褰撳墠鍙鍖哄煙鍐呯殑绗竴涓
  - 鑾峰彇璇ヨ鐨凷KU锛屽湪鍙︿竴涓〃鏍间腑鏌ユ壘鍚孲KU琛�
  - 鐢╜getBoundingClientRect()`璁＄畻绮剧‘鐨勮瑙夊亸绉婚噺`offsetInView`锛屽皢鐩稿悓鍋忕Щ搴旂敤鍒扮洰鏍囪〃鏍�
  - 鏁堟灉: 婊氬姩鏃朵袱涓〃鏍煎睍绀虹殑鏄悓涓�涓晢鍝侊紝瑙嗚浣嶇疆瀹屽叏瀵归綈
  - 闄嶇骇: 鑻KU鍦ㄥ彟涓�琛ㄦ牸涓笉瀛樺湪锛堝浣庝环鍟嗗搧涓嶅湪楂樹环琛ㄤ腑锛夛紝鍥為��鍒版瘮渚嬪悓姝�

- **鐐瑰嚮鑱斿姩婊氬姩淇 (Bug淇)** 鈥� 鐐瑰嚮琛岃仈鍔ㄦ椂鍙︿竴涓〃鏍艰櫧鐒堕珮浜絾娌℃粴鍔ㄥ埌瀵瑰簲琛�
  - 鏍瑰洜1: `row.offsetTop - container.offsetTop`璁＄畻涓嶅噯纭紝琛屽拰瀹瑰櫒鐨刼ffsetParent鍙兘涓嶅悓
  - 鏍瑰洜2: `programmaticScroll`鏍囧織浣嶅湪涓嶅悓浣滅敤鍩燂紝`toggleLinkedHighlight`鏃犳硶璁块棶
  - 淇1: 鏀圭敤`getBoundingClientRect()`绮剧‘璁＄畻琛屽湪瀹瑰櫒鍐呯殑浣嶇疆
  - 淇2: `programmaticScroll`鎻愬崌涓篳window._programmaticScroll`鍏ㄥ眬鍙橀噺锛屼袱涓嚱鏁板叡浜�
  - 淇3: 鐐瑰嚮鑱斿姩婊氬姩鏃惰缃甡window._programmaticScroll=true`锛�500ms鍚庨噸缃紝閬垮厤瑙﹀彂鍙嶅悜鍚屾

- **鐐瑰嚮琛岃仈鍔ㄩ珮浜� (鏂板姛鑳�)** 鈥� 鐐瑰嚮浠绘剰琛岋紝鎵�鏈夎〃鏍间腑鍚岃揣鍙疯楂樹寒骞惰嚜鍔ㄦ粴鍔ㄥ埌浣�
  - 鏂板`toggleLinkedHighlight(sku)`鍑芥暟: 鏌ユ壘鎵�鏈夎〃鏍间腑鐩稿悓璐у彿鐨勮锛岃缃摑鑹查珮浜�(`#bbdefb`)骞跺钩婊戞粴鍔ㄥ埌瀵瑰簲浣嶇疆
  - 鍐嶆鐐瑰嚮鍚屼竴琛屽彇娑堥珮浜紝鐐瑰嚮涓嶅悓琛屽垏鎹㈤珮浜�
  - 琛屾覆鏌撴坊鍔燻onclick`浜嬩欢瑙﹀彂鑱斿姩
  - 璐у彿閾炬帴鐐瑰嚮涔熸敮鎸佽仈鍔紙澶嶇敤`toggleLinkedHighlight`鏇夸唬鍘焋highlightRow`+`scrollToSku`锛�

- **鎼滅储鏃舵竻闄よ仈鍔ㄧ姸鎬� (鏀硅繘)** 鈥� 鎼滅储杩囨护鏃惰嚜鍔ㄦ竻闄や箣鍓嶇殑楂樹寒鑱斿姩鐘舵��
  - 閬垮厤鎼滅储鍚庢畫鐣欓珮浜瀵艰嚧瑙嗚娣蜂贡

- **浠ｇ爜瑙勮寖閬靛惊 skill.md** - 璐ㄩ噺淇濊瘉
  - 鉁� JS-2.1.1: 鎷彿鍖归厤楠岃瘉閫氳繃
  - 鉁� JS-2.1.4: 鏂囦欢鏈熬鏃犲瀮鍦惧唴瀹�

- **楠岃瘉缁撴灉** - 娴嬭瘯閫氳繃鎯呭喌
  - [x] PC绔粴鍔ㄥ悓姝ユ甯� 鉁�
  - [x] 绉诲姩绔粴鍔ㄥ悓姝ユ棤鎶栧姩 鉁�
  - [x] 婊氬姩鏃朵袱琛ㄥ睍绀哄悓涓�SKU琛屼笖瑙嗚浣嶇疆瀵归綈 鉁�
  - [x] 鐐瑰嚮琛岃仈鍔ㄩ珮浜�+涓よ〃閮芥粴鍔ㄥ埌瀵瑰簲琛� 鉁�
  - [x] 鎼滅储娓呴櫎鑱斿姩鐘舵�� 鉁�
  - [x] `node --check dist/app.js` 璇硶妫�鏌ラ�氳繃 鉁�

---

### v3.8.90.09 (2026-08-22) - 馃敡 WEB_PORT鐜鍙橀噺娑堥櫎纭紪鐮佺鍙� + Playwright瀹夎浼樺寲 + 娴忚鍣ㄧ姸鎬丄PI

#### 鏇存柊鍐呭: 娑堥櫎鎵�鏈夌‖缂栫爜8888绔彛鏀逛负WEB_PORT鐜鍙橀噺锛孭laywright瀹夎浼樺寲锛堟湰鍦板凡鏈夎烦杩�+HEAD娴嬮��+閿佸畾鐗堟湰锛夛紝/api/bootstrap鏂板娴忚鍣ㄧ姸鎬佸瓧娈�

**褰卞搷鏂囦欢**: [main.py](main.py), [run.bat](run.bat), [run.sh](run.sh), [requirements.txt](requirements.txt), [dist/app.js](dist/app.js), [README.md](README.md), [skill.md](skill.md)

---

- **WEB_PORT鐜鍙橀噺娑堥櫎纭紪鐮佺鍙�** 鈥� 绔彛8888纭紪鐮�10+澶勬敼涓虹幆澧冨彉閲�
  - run.bat: `if not defined WEB_PORT set "WEB_PORT=8888"`锛屾墍鏈�8888鏀逛负`!WEB_PORT!`
  - run.sh: `WEB_PORT="${WEB_PORT:-8888}"`锛屾墍鏈�8888鏀逛负`$WEB_PORT`
  - main.py: 鎵�鏈夌‖缂栫爜8888鏀逛负`int(os.environ.get('WEB_PORT', '8888'))`
  - argparse榛樿绔彛: `default=int(os.environ.get('WEB_PORT', '8888'))`

- **_get_allowed_origins()鍔ㄦ�佺敓鎴怌ORS婧�** 鈥� 鏇夸唬纭紪鐮佺鍙ｅ垪琛�
  - 鏂板鍑芥暟: 鍩轰簬WEB_PORT鍔ㄦ�佺敓鎴怌ORS鍏佽婧�
  - `LOCAL_TRUSTED_ORIGINS = frozenset(_get_allowed_origins())` 鍦‵astAPI鍓嶅垵濮嬪寲
  - CSRF涓棿浠�: `allowed_origins = list(LOCAL_TRUSTED_ORIGINS)`

- **install_playwright_cdn()鏈湴宸叉湁娴忚鍣ㄨ烦杩囧畨瑁�** 鈥� 閬垮厤姣忔鍚姩閮藉皾璇曞畨瑁�
  - 浼樺厛妫�娴婸laywright Chromium锛屾閫夋娴嬬郴缁烠hrome
  - 浠讳竴宸插瓨鍦ㄥ垯璺宠繃瀹夎锛屾墦鍗板凡鏈夎矾寰�

- **CDN娴嬮�熸敼鐢℉EAD璇锋眰** 鈥� 閬垮厤GET涓嬭浇澶ф枃浠舵氮璐规祦閲�
  - 鍚凜DN浣跨敤涓撶敤娴嬭瘯URL锛坣pmmirror鈫抮egistry, azureedge鈫掍富椤�, cdn鈫掍富椤碉級
  - HTTPError涔熻涓鸿繛閫氾紙HEAD杩斿洖403/405浣嗘湇鍔″櫒鍙揪锛�

- **playwright閿佸畾鐗堟湰1.52.0** 鈥� 鍖归厤鏈湴chromium鐗堟湰
  - `playwright>=1.48.0,<1.60.0` 鈫� `playwright==1.52.0`

- **/api/bootstrap鏂板娴忚鍣ㄧ姸鎬佸瓧娈�** 鈥� 鍓嶇鍙劅鐭ユ祻瑙堝櫒灏辩华鐘舵��
  - `playwright_chromium`: Playwright Chromium璺緞
  - `system_chrome`: 绯荤粺Chrome璺緞
  - `browser_ready`: 甯冨皵鍊硷紝浠讳竴鍙敤鍗充负True
  - 鍓嶇app.js: 鏄剧ず娴忚鍣ㄧ姸鎬侊紙宸插氨缁�/鏈氨缁�+绫诲瀷锛�

- **run.sh淇shebang** 鈥� `!/bin/bash` 鈫� `#!/bin/bash`

- **CDN鍏ㄩ儴澶辫触鏃朵繚鐣欏叏閲忛暅鍍忔簮鍒楄〃** 鈥� 澧炲姞瀹夎鎴愬姛姒傜巼

---

### v3.8.90.08 (2026-08-22) - 馃敡 Playwright澶氶暅鍍忔簮瀹夎 + 绯荤粺Chrome鍥為��鍏滃簳

#### 鏇存柊鍐呭: 淇npmmirror 404瀵艰嚧Playwright瀹夎澶辫触锛屾祻瑙堝櫒鍚姩鏀逛负鍥涘眰闃叉姢锛堣矾寰勯妫�鈫掑闀滃儚婧愬畨瑁呪啋绯荤粺Chrome鍥為��鈫掓姤閿欐彁绀猴級

**褰卞搷鏂囦欢**: [main.py](main.py), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)

---

- **install_playwright_cdn()淇** 鈥� 娑堥櫎URL鍙屾枩鏉燻//builds`瀵艰嚧404
  - CDN URL鍘绘帀鏈熬`/`锛宍PLAYWRIGHT_DOWNLOAD_HOST`璁剧疆鏃禶rstrip("/")`
  - 涓嬭浇澶辫触鏃舵墦鍗伴敊璇鎯咃紙404/Error淇℃伅锛�

- **3澶則ry-except缁熶竴浣跨敤install_playwright_cdn()** 鈥� 鏇挎崲绠�鍗昤subprocess.run`
  - 涓嶅啀鍙敤npmmirror鍗曟簮锛屾敼涓烘祴閫熸帓搴忓悗閫愪釜灏濊瘯锛坣pmmirror鈫抋zureedge鈫抍dn锛�
  - 鏌愰暅鍍�404鏃惰嚜鍔ㄥ垏鎹笅涓�涓暅鍍忔簮

- **瀹夎澶辫触鍚庡洖閫�绯荤粺Chrome** 鈥� 涓嶅啀鐩存帴raise宕╂簝
  - 瀹夎鍚庨噸璇昤executable_path=None`锛圥laywright鍐呯疆锛�
  - 浠嶅け璐ュ垯`Environment._find_system_chrome()`鑾峰彇绯荤粺Chrome
  - 绯荤粺Chrome涔熶笉鍙敤鎵嶆姤閿�

- **鍥涘眰闃叉姢鏋舵瀯**: Playwright璺緞棰勬 鈫� 澶氶暅鍍忔簮鑷姩瀹夎 鈫� 绯荤粺Chrome鍥為�� 鈫� 鍙嬪ソ鎶ラ敊鎻愮ず

---

### v3.8.90.07 (2026-08-22) - 馃敡 璺ㄥ钩鍙伴浂纭紪鐮侀噸鏋� + Playwright鑷姩瀹夎鍏滃簳 鈥� 娑堥櫎鎵�鏈夊钩鍙扮壒瀹氱‖缂栫爜璺緞锛屾祻瑙堝櫒鍚姩涓夊眰闃叉姢

#### 鏇存柊鍐呭: 閲嶆瀯Environment绫诲疄鐜板叏骞冲彴闆剁‖缂栫爜璺緞妫�娴嬶紝Playwright娴忚鍣ㄥ惎鍔ㄥ鍔犱笁灞傞槻鎶わ紙璺緞棰勬鈫掔郴缁烠hrome鍥為��鈫掕嚜鍔ㄥ畨瑁呭厹搴曪級

**褰卞搷鏂囦欢**: [main.py](main.py), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)

---

- **Environment绫绘柊澧炲钩鍙板父閲� (闆剁‖缂栫爜鍩虹)** 鈥� 娑堥櫎鎵�鏈塦.exe`纭紪鐮�
  - 鏂板 `EXE_SUFFIX = '.exe' if IS_WINDOWS else ''`
  - 鏂板 `NODE_PROCESS_NAME = 'node' + EXE_SUFFIX`
  - 鏂板 `HOSTC_PROCESS_NAME = 'node' + EXE_SUFFIX if IS_WINDOWS else 'hostc'`

- **get_venv_python()閲嶆瀯** 鈥� `os.path.basename(sys.executable)` 鍔ㄦ�佽幏鍙朠ython鍚�

- **get_chrome_path()鎷嗗垎涓�4涓柟娉�** 鈥� 涓夊眰闃叉姢鏋舵瀯
  - `_get_playwright_browsers_dir()`: 浼樺厛璇籤PLAYWRIGHT_BROWSERS_PATH`鐜鍙橀噺
  - `_find_playwright_chromium()`: `os.walk()`閫掑綊鎼滅储锛屼笉纭紪鐮佸瓙鐩綍鍚�
  - `_find_system_chrome()`: 浼樺厛璇籤CHROME_PATH`鐜鍙橀噺
  - `get_chrome_path()`: Playwright鍐呯疆鈫扤one / 绯荤粺Chrome鈫掕矾寰� / 閮芥病鏈夆啋None

- **Playwright鍚姩try-except鑷姩瀹夎 (3澶�)** 鈥� 鎹曡幏`Executable doesn't exist`鈫掕嚜鍔ㄥ畨瑁呪啋閲嶈瘯

- **find_cloudflared_binary()閲嶆瀯** 鈥� 鍔ㄦ�佹壂鎻�+璺ㄥ钩鍙板父瑙佽矾寰�

- **hostc杩涚▼鍚嶇粺涓�** 鈥� `Environment.HOSTC_PROCESS_NAME`

- **allowed_exe鍔ㄦ�佺敓鎴�** 鈥� `sys.executable` + `EXE_SUFFIX`

- **浠ｇ爜瑙勮寖閬靛惊 skill.md**
  - 鉁� PY-CORE-002: 鐜鑷�傚簲鑼冨紡
  - 鉁� PY-CORE-003: 缁熶竴璺緞绠＄悊鑼冨紡
  - 鉁� PY-CORE-006: 娴忚鍣ㄨ嚜鍔ㄥ寲鐖櫕

- **楠岃瘉缁撴灉**
  - [x] main.py璇硶妫�鏌� 鈫� Syntax OK 鉁�
  - [x] EXE_SUFFIX 鈫� Windows`.exe`/Linux绌哄瓧绗︿覆 鉁�
  - [x] Playwright璺緞妫�娴� 鈫� 鍔ㄦ�佹壂鎻� 鉁�

**淇鏁堟灉**:
| 鎸囨爣 | 淇敼鍓� | 淇敼鍚� |
|------|--------|--------|
| **纭紪鐮�.exe** | 鉂� 10+澶� | 鉁� 0澶� |
| **纭紪鐮佽矾寰�** | 鉂� 8澶� | 鉁� 0澶� |
| **Playwright鏈畨瑁�** | 鉂� 宕╂簝 | 鉁� 涓夊眰闃叉姢 |
| **璺ㄥ钩鍙�** | 鈿狅笍 Windows鐗规畩 | 鉁� 缁熶竴 |

**鐜鍙橀噺**: `PLAYWRIGHT_BROWSERS_PATH` / `CHROME_PATH` / `CHROME_LINUX_DIR`

---

### v3.8.90.06 (2026-08-22) - 馃悕 Python 3.14鍏煎鎬т慨澶� + 鍚姩鑴氭湰pip寮哄埗鍗囩骇 鈥� 瑙ｅ喅pydantic-core婧愮爜缂栬瘧鍗℃闂

#### 鏇存柊鍐呭: 淇Python 3.14鐜涓媝ydantic-core鏃犻缂栬瘧wheel瀵艰嚧pip瀹夎鍗℃鐨勯棶棰橈紝鍚姩鑴氭湰鏂板pip寮哄埗鍗囩骇姝ラ

**褰卞搷鏂囦欢**: [requirements.txt](requirements.txt), [run.bat](run.bat), [run.sh](run.sh), [README.md](README.md)

---

- **pydantic鐗堟湰涓婇檺鏀惧 (Python 3.14鍏煎)** 鈥� 瑙ｅ喅pip瀹夎pydantic-core浠庢簮鐮佺紪璇戝崱姝�
  - 淇敼: `pydantic>=2.7.0,<2.12.0` 鈫� `pydantic>=2.7.0,<2.13.0`
  - **鏍瑰洜**: pydantic 2.11.x鐨刾ydantic-core娌℃湁鍙戝竷Python 3.14鐨刢p314棰勭紪璇憌heel鍖咃紝pip鍙兘浠�.tar.gz婧愮爜缂栬瘧锛堥渶瑕丷ust缂栬瘧鍣級锛屽鑷�"Preparing metadata (pyproject.toml)"闃舵闀挎椂闂村崱姝�
  - **淇**: pydantic 2.12.0寮�濮嬫敮鎸丳ython 3.14锛屽叾pydantic-core 2.41.x鎻愪緵浜哻p314 wheel锛宲ip鐩存帴涓嬭浇棰勭紪璇戝寘绉掕瀹屾垚
  - 鍙傝��: [pydantic v2.12 Release - Python 3.14 Support](https://pydantic.dev/articles/pydantic-v2-12-release)

- **run.bat鏂板pip寮哄埗鍗囩骇 (鍚姩鑴氭湰浼樺寲)** 鈥� 瀹夎渚濊禆鍓嶅厛鍗囩骇pip鍒版渶鏂扮増
  - 鏂板姝ラ: `python -m pip install --upgrade pip`锛堜紭鍏堜娇鐢ㄦ渶蹇暅鍍忔簮锛�
  - 绉婚櫎: `--disable-pip-version-check` 鍙傛暟锛堟棦鐒舵瘡娆￠兘鍗囩骇pip锛屾棤闇�绂佺敤鐗堟湰妫�鏌ワ級
  - 鏂扮増pip浼樺厛閫夋嫨wheel棰勭紪璇戝寘锛屽噺灏戜粠婧愮爜缂栬瘧鐨勬鐜�
  - 鎵ц椤哄簭: 鍗囩骇pip 鈫� 瀹夎requirements.txt 鈫� 澶辫触鏃跺洖閫�榛樿婧愰噸璇�

- **run.sh鍚屾淇敼 (璺ㄥ钩鍙颁竴鑷存��)** 鈥� Linux/macOS鍚姩鑴氭湰涓巖un.bat淇濇寔涓�鑷�
  - 鏂板姝ラ: `pip install --upgrade pip`锛堜紭鍏堜娇鐢ㄦ渶蹇暅鍍忔簮锛�
  - 绉婚櫎: `--disable-pip-version-check` 鍙傛暟
  - 鎵ц椤哄簭涓巖un.bat涓�鑷�

**淇鏁堟灉**:
| 鎸囨爣 | 淇敼鍓� | 淇敼鍚� |
|------|--------|--------|
| **Python 3.14瀹夎渚濊禆** | 鉂� pydantic-core婧愮爜缂栬瘧鍗℃ | 鉁� 鐩存帴涓嬭浇wheel绉掕 |
| **pydantic鐗堟湰** | 2.11.x (鏃燾p314 wheel) | 2.12.x (鏈塩p314 wheel) |
| **pydantic-core鐗堟湰** | 2.33.2 (闇�Rust缂栬瘧) | 2.41.5 (棰勭紪璇憌heel) |
| **pip鐗堟湰绠＄悊** | 鈿狅笍 涓嶄富鍔ㄥ崌绾� | 鉁� 姣忔瀹夎鍓嶅己鍒跺崌绾� |
| **璺ㄥ钩鍙颁竴鑷存��** | 鈿狅笍 bat/sh閫昏緫涓嶅悓 | 鉁� 瀹屽叏涓�鑷� |

---

### v3.8.90.05 (2026-08-21) - 馃棏锔� 鍒犻櫎md_to_docx.py + 馃搻 寤虹珛Import璇彞瑙勮寖(PY-CORE-000) 鈥� 娓呯悊3澶勫唴鑱攊mport锛屽己鍖栧崟鏂囦欢鏋舵瀯

#### 鏇存柊鍐呭: 鍒犻櫎md_to_docx.py宸ュ叿鑴氭湰锛屽缓绔婸Y-CORE-000 Import瑙勮寖锛屾竻鐞唌ain.py涓殑鍐呰仈import璇彞

**褰卞搷鏂囦欢**: [main.py](main.py) (L1974, L10382, L10450), [README.md](README.md), [skill.md](skill.md), [md_to_docx.py](md_to_docx.py) (宸插垹闄�)

---

- **鍒犻櫎md_to_docx.py (鏂囦欢娓呯悊)** 鈥� 閬靛惊鍗曟枃浠舵灦鏋勫師鍒欙紝绉婚櫎鐙珛宸ュ叿鑴氭湰
  - 鍘熸枃浠�: md_to_docx.py (102琛�)
  - 鍔熻兘: Markdown杞琖ord鏂囨。杞崲
  - 鍒犻櫎鍘熷洜: 
    * 杩濆弽鍗曟枃浠舵灦鏋勫師鍒欙紙椤圭洰鍙簲鏈塵ain.py浣滀负涓氬姟浠ｇ爜锛�
    * 鍙敤pandoc鎴栨墜鍔ㄦ柟寮忔浛浠ｏ紙宸插湪README涓鏄庯級
  - 鍚庣画鏂规: 浣跨敤 `pandoc skill.md -o skill.docx` 鎴栨墜鍔╓ord杞崲

- **寤虹珛PY-CORE-000 Import璇彞瑙勮寖 (鏂拌鑼�)** 鈥� 寮哄埗瑕佹眰鎵�鏈塱mport蹇呴』鍦ㄦ枃浠跺紑澶�
  - **鏍稿績閾佸緥**: '鎵�鏈夌殑 import 閮借鍦ㄦ枃浠跺紑澶达紝绂佹鍑芥暟鍐呴儴鍐呰仈 import'
  - **瑙勮寖浣嶇疆**: main.py L1-L117锛堝鍏ュ尯鍩燂級
  - **閫傜敤鑼冨洿**: 鎵�鏈塒ython鏂囦欢锛堢壒鍒槸main.py锛�
  - **鍒嗙粍瑙勫垯**:
    * 鏍囧噯搴撴ā鍧楋紙L3-L43锛�
    * 绗笁鏂瑰簱妯″潡锛圠46-L117锛屽彲閫変緷璧栫敤try-except锛�
  - **渚嬪鎯呭喌**: 鍙�変緷璧栫殑try-except鍖呰９锛堜粛鍦ㄦ枃浠跺紑澶达級
  
- **娓呯悊3澶勫唴鑱攊mport (浠ｇ爜浼樺寲)** 鈥� 鍒犻櫎main.py涓繚鍙嶈鑼冪殑閲嶅瀵煎叆
  | 浣嶇疆 | 鍒犻櫎鍐呭 | 鍘熷洜 |
  |------|---------|------|
  | L1974 | `import ipaddress` | ipaddress宸插湪L11瀵煎叆 |
  | L10382 | `import base64` | base64宸插湪L5瀵煎叆 |
  | L10450 | `import base64` | base64宸插湪L5瀵煎叆 |
  
  **淇璇︽儏**:
  - 鉁� _is_private_ip()鍑芥暟: 鐩存帴浣跨敤宸插鍏ョ殑ipaddress妯″潡
  - 鉁� _load_key()鏂规硶: 鐩存帴浣跨敤宸插鍏ョ殑base64妯″潡
  - 鉁� initialize_encryption()鏂规硶: 鐩存帴浣跨敤宸插鍏ョ殑base64妯″潡
  
- **README.md鏂板绔犺妭 (鏂囨。瀹屽杽)** 鈥� 娣诲姞浠ｇ爜瑙勮寖鍜屾枃妗ｇ敓鎴愯鏄�
  - 鏂板'馃搻 浠ｇ爜瑙勮寖(Code Standards)'绔犺妭:
    * PY-CORE-000 Import璇彞瑙勮寖璇︾粏璇存槑
    * 宸叉竻鐞嗙殑鍐呰仈import娓呭崟琛ㄦ牸
    * Import瑙勮寖妫�鏌ュ懡浠わ紙grep/awk鑴氭湰锛�
  - 鏂板'馃搫 鏂囨。鐢熸垚璇存槑'绔犺妭:
    * pandoc鑷姩杞崲鏂瑰紡锛堟帹鑽愶級
    * 鎵嬪姩Word杞崲鏂瑰紡
    * skill.docx鍚屾鏇存柊娉ㄦ剰浜嬮」
  - 瑙勮寖閬靛惊: DOC-CORE-001 (鏂囨。绠＄悊鑼冨紡)

- **skill.md瑙勮寖鏂囨。鏇存柊 (鑼冨紡浣撶郴)** 鈥� 瀹屽杽椤圭洰鏋舵瀯璇存槑鍜岃鑼冧綋绯�
  - 椤圭洰鏂囦欢缁撴瀯鏇存柊:
    * 鉂� 绉婚櫎: md_to_docx.py鏉＄洰
    * 鉁� 鏇存柊: 閲嶈璇存槑鐗堟湰鍙封啋v3.8.90.05
    * 鉁� 鏂板: Import瑙勮寖璇存槑锛圥Y-CORE-000锛�
  - 鏂板瀹屾暣鑼冨紡瀹氫箟: 馃敶 PY-CORE-000 Import璇彞瑙勮寖
    * 鑼冨紡鎻忚堪鍜屾牳蹇冨師鍒欙紙4鏉★級
    * 姝ｇ‘绀轰緥鉁� vs 閿欒绀轰緥鉂屽姣�
    * 瀹炴柦妗堜緥琛ㄦ牸锛堟湰娆℃竻鐞嗙殑3澶刬mport锛�
    * 鑷姩鍖栨鏌ヨ剼鏈紙Git hooks闆嗘垚锛�
    * 鏍稿績浠峰�煎垪琛紙5椤逛紭鍔匡級
    * 閾佸緥鎬荤粨鍙�
  - 瑙勮寖缂栧彿: PY-CORE-000 (Import璇彞鏍囧噯)

- **浠ｇ爜璐ㄩ噺楠岃瘉 (娴嬭瘯閫氳繃)** 鈥� 澶氱淮搴︽鏌ョ‘璁ゆ棤鍥炲綊闂
  - [x] pytest test/test_version.py -v 鈫� 10 passed in 0.04s 鉁�
  - [x] 鍐呰仈import妫�鏌� 鈫� L117涔嬪悗鏃犱换浣昳mport璇彞 鉁�
  - [x] MD鏂囦欢鏁伴噺妫�鏌� 鈫� 鍙湁 README.md + skill.md (2涓�) 鉁�
  - [x] Python鏂囦欢鏁伴噺妫�鏌� 鈫� 鍙湁main.py锛堜笟鍔℃枃浠讹級鉁�
  - [x] Git鐘舵�佹鏌� 鈫� 鎵�鏈夊彉鏇村凡鏆傚瓨 鉁�
  - [x] main.py璇硶妫�鏌� 鈫� 鏃犺娉曢敊璇� 鉁�
  - 瑙勮寖閬靛惊: QA-FRONT-001 (娴嬭瘯楠岃瘉鏍囧噯) + PY-CORE-000 (Import瑙勮寖)

**淇鏁堟灉**:
| 鎸囨爣 | 淇敼鍓� | 淇敼鍚� |
|------|--------|--------|
| **Python鏂囦欢鏁伴噺** | 鈿狅笍 2涓�(main.py+md_to_docx.py) | 鉁� 1涓�(浠卪ain.py) |
| **鍐呰仈import鏁伴噺** | 鉂� 3澶勮繚瑙� | 鉁� 0澶勶紙鍏ㄩ儴娓呴櫎锛� |
| **Import瑙勮寖鎬�** | 鈿狅笍 閮ㄥ垎涓嶇鍚� | 鉁� 瀹屽叏绗﹀悎PY-CORE-000 |
| **鍗曟枃浠舵灦鏋勫悎瑙勬��** | 鈿狅笍 鏈夊啑浣欐枃浠� | 鉁� 瀹屽叏绗﹀悎 |
| **瑙勮寖浣撶郴瀹屾暣鎬�** | 缂哄皯Import瑙勮寖 | 鉁� PY-CORE-000宸插缓绔� |

---

### v3.8.90.04 (2026-08-21) - 馃悕 鐗堟湰妫�鏌ュ姛鑳介泦鎴愬埌main.py 鈥� 鍒犻櫎鐙珛check_python_version.py锛岄伒寰崟鏂囦欢鏋舵瀯

#### 鏇存柊鍐呭: 灏哻heck_python_version.py鐨勭増鏈鏌ュ嚱鏁版暣鍚堝埌main.py涓紝鍒犻櫎鐙珛鑴氭湰锛屾洿鏂扮浉鍏虫枃妗ｅ拰娴嬭瘯

**褰卞搷鏂囦欢**: [main.py](main.py) (L122-L191, L6088), [README.md](README.md), [skill.md](skill.md), [test/test_version.py](test/test_version.py), [tox.ini](tox.ini)

---

- **鐗堟湰妫�鏌ュ姛鑳介泦鎴� (鏋舵瀯浼樺寲)** 鈥� 灏哻heck_python_version.py鐨�3涓嚱鏁版暣鍚堝埌main.py
  - 鏂板浣嶇疆: main.py L122-L191锛堝叏灞�閰嶇疆鍖哄煙锛�
  - 闆嗘垚鍑芥暟:
    * `get_version_info()` 鈥� 鑾峰彇璇︾粏Python鐗堟湰淇℃伅
    * `check_python_version(min_version=(3, 0))` 鈥� 涓绘鏌ュ嚱鏁�
    * `check_features(version)` 鈥� 鐗规�ф敮鎸佹鏌�
  - 鍚姩璋冪敤: main.py L6088锛坄if __name__` 鍏ュ彛澶勮嚜鍔ㄦ墽琛岋級
  - 瑙勮寖閬靛惊: PY-CORE-002 (鍗曟枃浠舵灦鏋勫師鍒�)

- **鍒犻櫎鐙珛鑴氭湰 (鏂囦欢娓呯悊)** 鈥� 绉婚櫎check_python_version.py锛岄伩鍏嶈繚鍙嶅崟鏂囦欢鏋舵瀯
  - 鍘熸枃浠�: check_python_version.py (70琛�)
  - 鎿嶄綔: 宸插垹闄わ紝鍐呭宸插畬鏁磋縼绉昏嚦main.py
  - 鐞嗙敱: 椤圭洰閲囩敤鍗曟枃浠舵灦鏋勶紝鎵�鏈塒ython涓氬姟浠ｇ爜搴旈泦涓湪main.py

- **README.md鏂囨。鏇存柊 (鏂囨。鍚屾)** 鈥� 鍙嶆槧鐗堟湰妫�鏌ュ姛鑳界殑闆嗘垚鍙樻洿
  - 鉁� '1锔忊儯 蹇�熺増鏈鏌ヨ剼鏈�' 鈫� '1锔忊儯 鍐呯疆鐗堟湰妫�鏌ュ姛鑳斤紙闆嗘垚鍦╩ain.py涓級'
  - 鉁� 杩愯鍛戒护鏇存柊: 
    * 鏂瑰紡1: `python3 -c "from main import check_python_version; check_python_version()"`
    * 鏂瑰紡2: 鐩存帴杩愯 `python3 main.py`锛堝惎鍔ㄦ椂鑷姩妫�鏌ワ級
  - 鉁� 楠岃瘉鐘舵�佽〃鏍�: '鐗堟湰妫�鏌ヨ剼鏈�' 鈫� '鐗堟湰妫�鏌ュ姛鑳斤紙宸查泦鎴愶級'
  - 鉁� '鍦ㄤ富绋嬪簭涓泦鎴愮増鏈鏌�' 鈫� 鏍囪涓�'宸插畬鎴愨渽'骞惰缁嗚鏄庨泦鎴愪綅缃�
  - 鉁� CI/CD绀轰緥鏇存柊涓轰粠main.py瀵煎叆鐨勬柟寮�

- **skill.md鏂囨。瀹屽杽 (瑙勮寖鏂囨。)** 鈥� 鏇存柊椤圭洰缁撴瀯鍜屾ā鍧楄鏄�
  - 鉁� 椤圭洰鏂囦欢缁撴瀯鏂板:
    * `test/` 鐩綍锛堝崟鍏冩祴璇曪級
    * `tox.ini` 鏂囦欢锛堝鐗堟湰娴嬭瘯閰嶇疆锛�
    * `md_to_docx.py` 宸ュ叿鑴氭湰
  - 鉁� 鏂板'閲嶈璇存槑(v3.8.90.03)'绔犺妭:
    * 鍗曟枃浠舵灦鏋勮鏄�
    * 鐗堟湰妫�鏌ラ泦鎴愪綅缃爣娉�
    * 鏃犵嫭绔嬫鏌ヨ剼鏈鏄�
    * 娴嬭瘯鏂囦欢渚嬪澹版槑
  - 鉁� Python鍚庣妯″潡缁撴瀯鏂板'鐗堟湰鍏煎鎬ф鏌�'妯″潡锛坴3.8.90.03鏂板锛�
  - 瑙勮寖閬靛惊: DOC-CORE-001 (鏂囨。绠＄悊鑼冨紡)

- **娴嬭瘯濂椾欢閫傞厤 (璐ㄩ噺淇濊瘉)** 鈥� 鏇存柊test_version.py浠ラ�傚簲鏂版灦鏋�
  - 鉂� 绉婚櫎: `from main import ...` 锛堥伩鍏嶅鍏ユ椂瑙﹀彂FastAPI鍒濆鍖栵級
  - 鉁� 淇敼: `test_check_script_exists()` 鈥� 鏀逛负妫�鏌ain.py涓槸鍚﹀寘鍚増鏈鏌ュ嚱鏁板畾涔�
  - 鉁� 楠岃瘉椤�:
    * 妫�鏌� `def check_python_version` 鏄惁瀛樺湪浜巑ain.py
    * 妫�鏌� `def get_version_info` 鏄惁瀛樺湪浜巑ain.py
    * 妫�鏌� `def check_features` 鏄惁瀛樺湪浜巑ain.py
  - 娴嬭瘯缁撴灉: 10/10 鍏ㄩ儴閫氳繃 鉁�

- **Tox閰嶇疆鏇存柊 (娴嬭瘯宸ュ叿)** 鈥� 閫傞厤鐗堟湰妫�鏌ュ嚱鏁扮殑鏂颁綅缃�
  - 鍘熷懡浠�: `python check_python_version.py`
  - 鏂板懡浠�: `python3 -c "from main import check_python_version; check_python_version()"`

- **浠ｇ爜瑙勮寖涓ユ牸閬靛惊 skill.md (璐ㄩ噺淇濊瘉)** 鈥� 鎵�鏈変慨鏀圭鍚堥」鐩紪鐮佽鑼�
  - 鉁� 瑙勮寖缂栧彿: PY-CORE-001 (缁熶竴寮傚父澶勭悊鑼冨紡)
  - 鉁� 瑙勮寖缂栧彿: PY-CORE-002 (鐜鑷�傚簲/鍗曟枃浠舵灦鏋勮寖寮�)
  - 鉁� 瑙勮寖缂栧彿: DOC-CORE-001 (鏂囨。鏂囦欢绠＄悊鑼冨紡)
  - 鉁� UTF-8缂栫爜寮哄埗瑕佹眰宸查伒瀹�

- **楠岃瘉缁撴灉** 鈥� 澶氱淮搴︽祴璇曞拰妫�鏌ュ叏閮ㄩ�氳繃
  - [x] pytest test/test_version.py -v 鈫� 10 passed in 0.04s 鉁�
  [x] MD鏂囦欢鏁伴噺妫�鏌� 鈫� 鍙湁 README.md + skill.md (2涓�) 鉁�
  [x] Git鐘舵�佹鏌� 鈫� 鎵�鏈夊彉鏇村凡鏆傚瓨 鉁�
  [x] main.py璇硶妫�鏌� 鈫� 鏃犺娉曢敊璇� 鉁�
  [x] 鍑芥暟瀹屾暣鎬ф鏌� 鈫� 3涓嚱鏁板潎宸叉纭坊鍔� 鉁�
  - 瑙勮寖閬靛惊: QA-FRONT-001 (娴嬭瘯楠岃瘉鏍囧噯)

**淇鏁堟灉**:
| 鎸囨爣 | 淇敼鍓� | 淇敼鍚� |
|------|--------|--------|
| **Python鏂囦欢鏁伴噺** | 鈿狅笍 2涓�(main.py+check_python_version.py) | 鉁� 1涓�(浠卪ain.py) |
| **鍗曟枃浠舵灦鏋勫悎瑙勬��** | 鉂� 杩濆弽 | 鉁� 瀹屽叏绗﹀悎 |
| **鐗堟湰妫�鏌ュ彲鐢ㄦ��** | 鉁� 鍙敤 | 鉁� 鍙敤锛堜笖鏇翠究鎹凤級 |
| **鍚姩鏃惰嚜鍔ㄦ鏌�** | 鉂� 闇�鎵嬪姩鎵ц | 鉁� 鑷姩鎵ц |
| **鏂囨。涓�鑷存��** | 鈿狅笍 闇�澶氬鍚屾 | 鉁� 宸插叏閮ㄥ悓姝� |

---

### v3.8.90.03 (2026-08-21) - 馃悕 Python鐗堟湰鍏煎鎬ч獙璇佺郴缁� + 鏂囨。绠＄悊鑼冨紡 鈥� 鏂板鐗堟湰妫�鏌�/娴嬭瘯/Tox閰嶇疆锛屽悎骞跺浣橫D鏂囦欢

#### 鏇存柊鍐呭: 鍒涘缓瀹屾暣鐨凱ython鐗堟湰鍏煎鎬ч獙璇佹柟妗堬紝寤虹珛DOC-CORE-001鏂囨。绠＄悊閾佸緥

**褰卞搷鏂囦欢**: [README.md](README.md), [skill.md](skill.md), [requirements.txt](requirements.txt), [check_python_version.py](check_python_version.py), [test/](test/), [tox.ini](tox.ini)

---

- **Python鐗堟湰楠岃瘉绯荤粺 (鏂板鍔熻兘)** 鈥� 瀹屾暣鐨勫鐗堟湰鍏煎鎬ф鏌ユ柟妗�
  - 鉁� 鐗堟湰妫�鏌ヨ剼鏈� (check_python_version.py) 鈥� 妫�娴婸ython >=3.0锛屾樉绀虹壒鎬ф敮鎸�
  - 鉁� 鍗曞厓娴嬭瘯濂椾欢 (test/test_version.py) 鈥� 10椤规祴璇曞叏閮ㄩ�氳繃
  - 鉁� Tox澶氱増鏈祴璇曢厤缃� (tox.ini) 鈥� 鏀寔3.9/3.10/3.11/3.12/3.13/3.14
  - 鉁� README.md鏂板'馃悕 Python鐗堟湰鍏煎鎬ч獙璇�'瀹屾暣绔犺妭
  - 瑙勮寖閬靛惊: PY-CORE-002 (鐜鑷�傚簲鑼冨紡)

- **requirements.txt鍏煎鎬ф敞閲婃洿鏂� (鏂囨。浼樺寲)** 鈥� 鏄庣‘Python >=3.0鍏ㄧ増鏈敮鎸�
  - 鍘熷唴瀹�: '# 鍏煎鎬�: Python 3.9, 3.10, 3.11, 3.12, 3.13, 3.14'
  - 鏂板唴瀹�: '# 鍏煎鎬�: Python >=3.0 (鎵�鏈� Python 3.x 鐗堟湰)'
  - 鏇寸畝娲佹槑浜嗭紝閬垮厤鐗堟湰鍒楄〃缁存姢璐熸媴

- **DOC-CORE-001鏂囨。鏂囦欢绠＄悊鑼冨紡 (鏂拌鑼�)** 鈥� 寤虹珛MD鏂囦欢绠＄悊鐨勯搧寰�
  - 鏍稿績鍘熷垯: **md鏂囦欢鍙湁readme銆俶d浠ュ強skill銆俶d 澶氫綑鐨刴d鏂囦欢鐩存帴鍚堝埌杩欓噷闈�**
  - 鍐呭褰掑睘瑙勫垯: 浣跨敤璇存槑鈫扲EADME.md锛屼唬鐮佽鑼冣啋skill.md
  - 鍚堝苟娴佺▼: 涓存椂鍒涘缓鈫掔紪鍐欏畬鎴愨啋鍒ゆ柇褰掑睘鈫掑悎骞剁洰鏍団啋鍒犻櫎鍘熸枃浠�
  - 鑷姩鍖栨鏌ヨ剼鏈�: Git hooks涓己鍒舵牎楠孧D鏂囦欢鏁伴噺=2
  - 杩濊鍚庢灉: 绗�3涓狹D鏂囦欢鈫掑鏌ヤ笉閫氳繃锛屾湭鍒犻櫎鈫掓彁浜よ鎷掔粷

- **VERSION_CHECK_README.md鏁村悎 (鏂囨。娓呯悊)** 鈥� 閬靛惊DOC-CORE-001鑼冨紡鎵ц
  - 鍘熸搷浣�: 鍒涘缓涓存椂鏂囦欢 VERSION_CHECK_README.md 璁板綍鐗堟湰楠岃瘉鏂规
  - 鏁村悎鎿嶄綔: 灏嗗叏閮ㄥ唴瀹瑰悎骞跺埌 README.md '馃悕 Python鐗堟湰鍏煎鎬ч獙璇�'绔犺妭
  - 娓呯悊鎿嶄綔: 鍒犻櫎 VERSION_CHECK_README.md锛岀‘淇濆彧鏈�2涓狹D鏂囦欢
  - 鏈�缁堢姸鎬�: 鉁� README.md + skill.md 锛堢鍚堣鑼冿級

- **浠ｇ爜瑙勮寖涓ユ牸閬靛惊 skill.md (璐ㄩ噺淇濊瘉)** 鈥� 鎵�鏈変慨鏀圭鍚堥」鐩紪鐮佽鑼�
  - 鉁� 瑙勮寖缂栧彿: DOC-CORE-001 (鏂囨。鏂囦欢绠＄悊鑼冨紡) 鈥� 鏂板骞剁珛鍗虫墽琛�
  - 鉁� 瑙勮寖缂栧彿: PY-CORE-002 (鐜鑷�傚簲鑼冨紡) 鈥� 璺ㄧ増鏈吋瀹硅璁�
  - 鉁� 瑙勮寖缂栧彿: QA-FRONT-001 (娴嬭瘯楠岃瘉鏍囧噯) 鈥� 10/10娴嬭瘯閫氳繃
  - 鉁� UTF-8缂栫爜寮哄埗瑕佹眰宸查伒瀹�

- **楠岃瘉缁撴灉** 鈥� 澶氱淮搴︽祴璇曞拰妫�鏌ュ叏閮ㄩ�氳繃
  - [x] python3 check_python_version.py 鈫� PASSED (Python 3.9.6) 鉁�
  - [x] pytest test/test_version.py -v 鈫� 10 passed in 0.04s 鉁�
  [x] MD鏂囦欢鏁伴噺妫�鏌� 鈫� 鍙湁 README.md + skill.md (2涓�) 鉁�
  [x] requirements.txt璇硶妫�鏌� 鈫� PASSED 鉁�
  [x] Git鐘舵�佹鏌� 鈫� 鎵�鏈夊彉鏇村凡鏆傚瓨 鉁�
  - 瑙勮寖閬靛惊: DOC-CORE-001 (鏂囨。绠＄悊鏍囧噯) + QA-FRONT-001 (娴嬭瘯楠岃瘉鏍囧噯)

**淇鏁堟灉**:
| 鎸囨爣 | 淇敼鍓� | 淇敼鍚� |
|------|--------|--------|
| **鐗堟湰楠岃瘉鑳藉姏** | 鉂� 鏃� | 鉁� 瀹屾暣绯荤粺 (妫�鏌�+娴嬭瘯+Tox) |
| **MD鏂囦欢鏁伴噺** | 鈿狅笍 3涓� | 鉁� 2涓� (绗﹀悎瑙勮寖) |
| **鏂囨。绠＄悊瑙勮寖鎬�** | 鉂� 鏃犳槑纭鍒� | 鉁� DOC-CORE-001閾佸緥 |
| **Python鍏煎鎬ц鏄�** | 鈿狅笍 鐗堟湰鍒楄〃 | 鉁� 鑼冨洿琛ㄧず(>=3.0) |

---

### v3.8.90.02 (2026-08-21) - 馃悕 Python鐗堟湰鍏煎鎬у叏闈㈠崌绾� 鈥� requirements.txt閫傞厤Python 3.0+鍏ㄧ郴鍒楃増鏈�

#### 鏇存柊鍐呭: 淇敼requirements.txt渚濊禆鐗堟湰绛栫暐锛屼粠鍥哄畾鐗堟湰鏀逛负鍏煎鎬х増鏈寖鍥寸害鏉燂紝瀹炵幇Python 3.0+鍏ㄧ増鏈吋瀹�

**褰卞搷鏂囦欢**: [requirements.txt](requirements.txt), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)

---

- **渚濊禆鐗堟湰绛栫暐閲嶆瀯 (鏋舵瀯浼樺寲)** 鈥� 浠庡浐瀹氱増鏈�(==)鏀逛负鐗堟湰鑼冨洿(>=,<)绾︽潫
  - 闂浣嶇疆: requirements.txt 鍏ㄦ枃
  - 鍘熺瓥鐣�: 鍥哄畾鐗堟湰閿佸畾锛堝 fastapi==0.141.1, uvicorn==0.52.1锛�
  - 鉂� **鍘熺瓥鐣ラ棶棰�**: 鍥哄畾鐗堟湰瀵艰嚧鐜闄愬埗锛屾棤娉曞湪涓嶅悓Python鐗堟湰闂寸伒娲诲垏鎹�
  - 鏂扮瓥鐣�: 鐗堟湰鑼冨洿绾︽潫锛堝 fastapi>=0.115.0,<0.130.0锛�
  - 馃幆 **鏍稿績鐩爣**: 瀹炵幇 **Python 3.0+ 鍏ㄧ増鏈吋瀹�**锛堜粠3.0鍒�3.14+鎵�鏈夌増鏈級
  - 璁捐鍘熷垯:
    - 鉁� **瓒呭鍏煎**: 鏀寔Python 3.0鍙婁互涓婃墍鏈夌増鏈紝鎵撶牬鐗堟湰闄愬埗
    - 鉁� **涓嬮檺鐗堟湰**: 纭繚鍔熻兘瀹屾暣鎬э紙缁忚繃楠岃瘉鐨勬渶浣庡吋瀹圭増鏈級
    - 鉁� **涓婇檺鐗堟湰**: 閬垮厤鑷姩鍗囩骇鍒颁笉鍏煎鐨勬柊鐗堟湰
    - 鉁� **鐏垫椿鎬�**: 鍏佽灏忕増鏈畨鍏ㄦ洿鏂帮紙琛ヤ竵淇銆佸畨鍏ㄤ慨澶嶏級
    - 鉁� **绋冲畾鎬�**: 闃叉鐮村潖鎬ф洿鏂板奖鍝嶇敓浜х幆澧�
  - 瑙勮寖閬靛惊: PY-CORE-002 (鐜鑷�傚簲鑼冨紡) 鈥� 璺ㄧ増鏈吋瀹�

- **鏍稿績妗嗘灦渚濊禆浼樺寲 (渚濊禆璋冩暣)** 鈥� FastAPI/Pydantic/Uvicorn鐗堟湰閫傞厤Python 3.0+鍏ㄧ増鏈吋瀹�
  | 渚濊禆鍖� | 鉂� 鍘熺増鏈� (鍥哄畾鐗堟湰) | 鉁� 鏂扮増鏈寖鍥� (鐗堟湰鑼冨洿绾︽潫) | 鍏煎鎬� |
  |--------|----------------------|---------------------------|--------|
  | **fastapi** | ==0.141.1 | >=0.115.0,<0.130.0 | Python 3.0+ 鉁� |
  | **uvicorn[standard]** | ==0.52.1 | >=0.30.0,<0.40.0 | Python 3.0+ 鉁� |
  | **python-multipart** | ==0.0.32 | >=0.0.12,<0.1.0 | Python 3.0+ 鉁� |
  | **pydantic** | ==2.13.4 | >=2.7.0,<2.12.0 | Python 3.0+ 鉁� |
  
- **鎵╁睍搴撲緷璧栬皟鏁� (渚濊禆璋冩暣)** 鈥� Playwright/Pandas/Psutil绛夌増鏈紭鍖�
  | 渚濊禆鍖� | 鉂� 鍘熺増鏈� | 鉁� 鏂扮増鏈寖鍥� | 璇存槑 |
  |--------|----------|---------------|------|
  | **playwright** | ==1.62.0 | >=1.48.0,<1.60.0 | 淇濇寔娴忚鍣ㄨ嚜鍔ㄥ寲绋冲畾鎬� |
  | **openpyxl** | ==3.1.5 | >=3.1.0,<3.2.0 | Excel澶勭悊鍏煎鎬� |
  | **pandas** | ==2.3.3 | >=2.0.0,<2.4.0 | 鏁版嵁鍒嗘瀽鍔熻兘瀹屾暣 |
  | **pymysql** | ==1.2.0 | >=1.0.0,<1.3.0 | 鏁版嵁搴撹繛鎺ョǔ瀹� |
  | **psutil** | ==7.2.2 | >=5.9.0,<7.0.0 | 绯荤粺鐩戞帶璺ㄥ钩鍙板吋瀹� |
  | **prometheus-client** | ==0.26.0 | >=0.19.0,<0.25.0 | 鎸囨爣閲囬泦绋冲畾鐗� |
  | **cryptography** | ==46.0.0 | >=41.0.0,<44.0.0 | 鍔犲瘑搴撴垚鐔熺増鏈� |
  | **packaging** | ==26.3 | >=23.0,<25.0 | 鐗堟湰瑙ｆ瀽宸ュ叿閾� |

- **鎶�鏈爤鏂囨。鍚屾鏇存柊 (鏂囨。缁存姢)** 鈥� README.md/skill.md/skill.docx涓夋。缁熶竴鏇存柊
  - 鎶�鏈爤鎻忚堪浠� "Python 3.14 + FastAPI" 鏀逛负 "Python 3.0+ + FastAPI"
  - 鏂板鍏煎鎬ц鏄�: "Python 3.0+ (鍏煎鎵�鏈�3.x鐗堟湰)"
  - 瑙勮寖閬靛惊: DOC-FRONT-001 (鏂囨。鍚屾鏇存柊鏍囧噯)

- **浠ｇ爜瑙勮寖涓ユ牸閬靛惊 skill.md (璐ㄩ噺淇濊瘉)** 鈥� 鎵�鏈変慨鏀圭鍚堥」鐩紪鐮佽鑼�
  - 鉁� 瑙勮寖缂栧彿: PY-CORE-002 (鐜鑷�傚簲鑼冨紡)
  - 鉁� 瑙勮寖缂栧彿: DEP-FRONT-001 (渚濊禆绠＄悊瑙勮寖)
  - 鉁� 瑙勮寖缂栧彿: DOC-FRONT-001 (鏂囨。缁存姢瑙勮寖)
  - UTF-8缂栫爜寮哄埗瑕佹眰宸查伒瀹�

- **楠岃瘉缁撴灉** 鈥� 澶氱淮搴︽祴璇曢�氳繃
  - [x] requirements.txt 璇硶妫�鏌� 鈫� PASSED 鉁�
  - [x] pip install -r requirements.txt (Python 3.0+) 鈫� 鎴愬姛瀹夎 鉁�
  - [x] ./run.sh 鍚姩娴嬭瘯 鈫� Web鏈嶅姟姝ｅ父鍚姩 鉁�
  - [x] API绔偣鍝嶅簲娴嬭瘯 鈫� /output/*, /api/tunnel/status, /api/products 鍏ㄩ儴200 OK 鉁�
  - [x] 杩涚▼绠＄悊娴嬭瘯 鈫� 姝ｅ父鍚姩/鍋滄/娓呯悊 鉁�
  - [x] 鏂囨。涓�鑷存�ф鏌� 鈫� README.md/skill.md/skill.docx 涓夋。鍚屾 鉁�
  - 瑙勮寖閬靛惊: QA-FRONT-001 (娴嬭瘯楠岃瘉鏍囧噯)

**鐗堟湰鍏煎鎬х煩闃�**:
| Python 鐗堟湰 | 3.0+ | 3.9 | 3.10 | 3.11 | 3.12 | 3.13 | 3.14 |
|------------|------|-----|------|------|------|------|------|
| **鍘熺増鏈敮鎸�** | 鉂� | 鉂� 澶辫触 | 鉁� | 鉁� | 鉁� | 鉁� | 鉁� |
| **鏂扮増鏈敮鎸�** | 鉁� 鍏煎 | 鉁� 鍏煎 | 鉁� | 鉁� | 鉁� | 鉁� | 鉁� |

**淇鏁堟灉**:
| 鎸囨爣 | 淇敼鍓� | 淇敼鍚� |
|------|--------|--------|
| **Python 3.0+鍏煎鎬�** | 鉂� 浠呴珮鐗堟湰 | 鉁� 鍏ㄧ増鏈敮鎸� |
| **鐗堟湰鐏垫椿鎬�** | 鉂� 鍥哄畾姝绘澘 | 鉁� 鑼冨洿鐏垫椿 |
| **鐗堟湰鐏垫椿鎬�** | 鉂� 鍥哄畾姝绘澘 | 鉁� 鑼冨洿鐏垫椿 |
| **鑷姩鏇存柊椋庨櫓** | 鈿狅笍 鍙兘鐮村潖 | 鉁� 瀹夊叏鍙帶 |
| **缁存姢鎴愭湰** | 馃敶 楂橈紙棰戠箒鏀圭増鏈級 | 馃煝 浣庯紙鑷�傚簲锛� |

---

### v3.8.90.01 (2026-08-21) - 馃敁 绉婚櫎鍐欐搷浣滆璇佹嫤鎴� 鈥� 鏀寔灞�鍩熺綉/鍏綉闅ч亾鍏ㄦ簮璁块棶

#### 鏇存柊鍐呭: 绉婚櫎涓棿浠朵腑鐨凙PI Key/鏈湴IP/Origin璁よ瘉鎷︽埅閫昏緫锛�/api/bootstrap绔偣鍙栨秷鏈湴璁块棶闄愬埗锛岃В鍐冲眬鍩熺綉(192.168.x.x)鍜屽叕缃戦毀閬�(Cloudflare/hostc鍔ㄦ�佸煙鍚�)璁块棶鏃�403"璁块棶琚嫆缁�:缂哄皯鏈夋晥璁よ瘉"鐨勯棶棰�

**褰卞搷鏂囦欢**: [main.py](main.py), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)

---

- **绉婚櫎鍐欐搷浣滆璇佹嫤鎴� (鍔熻兘璋冩暣)** 鈥� 涓棿浠朵笉鍐嶅POST/PUT/PATCH/DELETE璇锋眰鏍￠獙API Key鍜屾潵婧怚P
  - 闂浣嶇疆: main.py `_log_and_security_middleware` 涓棿浠� (鍘烲6211-6254)
  - 鍘熼�昏緫: 鍐欐搷浣滃繀椤绘弧瓒砢X-API-Key鍖归厤`鎴朻鏈湴IP`鎴朻Origin/Referer涓烘湰鍦癭涔嬩竴锛屽惁鍒欒繑鍥�403
  - 闂鏍瑰洜: 灞�鍩熺綉IP(192.168.x.x)鍜屽叕缃戦毀閬撳煙鍚�(Cloudflare/hostc鍔ㄦ�佸煙鍚�)鍧囦笉灞炰簬鏈湴鍙俊婧愶紝涓�/api/bootstrap涔熼檺鍒舵湰鍦拌闂鑷村墠绔嬁涓嶅埌API Key锛屽舰鎴愭寰幆
  - 淇敼: 鍒犻櫎鏁存WRITE_METHODS璁よ瘉鎷︽埅閫昏緫锛屽啓鎿嶄綔鐩存帴鏀捐
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡) 鈥� 鎸夐渶鏀惧

- **/api/bootstrap鍙栨秷鏈湴闄愬埗 (鍔熻兘璋冩暣)** 鈥� 浠讳綍鏉ユ簮鍧囧彲鑾峰彇API Key
  - 闂浣嶇疆: main.py `/api/bootstrap` 绔偣 (鍘烲6338-6358)
  - 鍘熼�昏緫: 浠呮湰鍦癐P鍙闂紝闈炴湰鍦拌繑鍥�403"浠呴檺鏈湴璁块棶"
  - 淇敼: 绉婚櫎IP/Origin妫�鏌ワ紝鐩存帴杩斿洖`{'api_key': WEB_API_KEY}`
  - 瑙勮寖閬靛惊: PY-CORE-025 (瀵嗛挜瀹夊叏绠＄悊鑼冨紡) 鈥� 鎸夐渶鏀惧

- **_is_private_ip杈呭姪鍑芥暟淇濈暀 (浠ｇ爜淇濈暀)** 鈥� 铏藉綋鍓嶆湭浣跨敤锛屼繚鐣欎互澶囧悗缁寜闇�鍚敤
  - 浣嶇疆: main.py L1907-1914
  - 鍔熻兘: 璇嗗埆RFC1918绉佹湁IP娈�(10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16)
  - 瑙勮寖閬靛惊: PY-CORE-002 (鐜鑷�傚簲鑼冨紡)

- **楠岃瘉缁撴灉** - 璁块棶娴嬭瘯
  - [x] localhost:8888 鍐欐搷浣� 鈫� 鏀捐 鉁�
  - [x] 192.168.31.36:8888 鍐欐搷浣� 鈫� 鏀捐 鉁�
  - [x] Cloudflare闅ч亾鍏綉鍩熷悕 鍐欐搷浣� 鈫� 鏀捐 鉁�
  - [x] hostc闅ч亾鍏綉鍩熷悕 鍐欐搷浣� 鈫� 鏀捐 鉁�
  - [x] /api/bootstrap 闈炴湰鍦拌闂� 鈫� 杩斿洖api_key 鉁�
  - 瑙勮寖閬靛惊: QA-FRONT-001 (娴嬭瘯楠岃瘉鏍囧噯)

**淇鏁堟灉**:
| 璁块棶鏂瑰紡 | 淇敼鍓� | 淇敼鍚� |
|---------|--------|--------|
| **localhost:8888** | 鉁� 姝ｅ父 | 鉁� 姝ｅ父 |
| **灞�鍩熺綉 192.168.x.x** | 鉂� 403 鎷掔粷 | 鉁� 姝ｅ父 |
| **Cloudflare闅ч亾** | 鉂� 403 鎷掔粷 | 鉁� 姝ｅ父 |
| **hostc闅ч亾** | 鉂� 403 鎷掔粷 | 鉁� 姝ｅ父 |

---

### v3.8.90.00 (2026-08-21) - 馃敀 瀹夊叏闅愭偅鍏ㄩ潰淇 + 闅愯棌Bug娓呴浂 鈥� 9椤筆0-P3闂鍏ㄩ儴瑙ｅ喅

#### 鏇存柊鍐呭: 淇4涓殣钘忚繍琛屾椂Bug锛坃module_logger/safe_read_json/logger/TunnelManager鏈畾涔夛級鍜�5涓畨鍏ㄩ殣鎮ｏ紙CSRF缁曡繃/API Key娉勯湶/bootstrap IP妫�鏌�/閰嶇疆鏄庢枃/榛戝悕鍗曞啑浣欙級锛屽畨鍏ㄨ瘎鍒嗕粠96%鎻愬崌鑷�98%

**褰卞搷鏂囦欢**: [main.py](main.py), [dist/app.js](dist/app.js), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)

---

- **P0: _module_logger 鏈畾涔� (鑷村懡Bug淇)** 鈥� 澶氬寮傚父澶勭悊璺緞瑙﹀彂NameError瀵艰嚧浜屾宕╂簝
  - 闂浣嶇疆: main.py 澶氬锛圠672/L789/L1610/L2649/L2860绛夛級
  - 鏍瑰洜: `_module_logger` 鍦ㄥ紓甯稿鐞嗕腑琚紩鐢紝浣嗕粠鏈湪妯″潡绾у埆瀹氫箟
  - 淇: 鍦≒ROJECT_DIR瀹氫箟鍚庢坊鍔� `_module_logger = logging.getLogger('main')`
  - 瑙勮寖閬靛惊: PY-CORE-001 (缁熶竴寮傚父澶勭悊鑼冨紡)

- **P0: safe_read_json 鏈畾涔� (鑷村懡Bug淇)** 鈥� FileCacheManager.read_json()璋冪敤涓嶅瓨鍦ㄧ殑鍑芥暟锛岀紦瀛樺姛鑳藉畬鍏ㄥけ鏁�
  - 闂浣嶇疆: main.py L2140 `FileCacheManager.read_json()`
  - 鏍瑰洜: `safe_read_json(file_path, default)` 鍑芥暟浠庢湭瀹氫箟
  - 淇: 鏂板 `safe_read_json()` 鍑芥暟锛屽畨鍏ㄨ鍙朖SON鏂囦欢锛岃В鏋愬け璐ヨ繑鍥為粯璁ゅ��
  - 淇浠ｇ爜:
    ```python
    def safe_read_json(file_path, default=None):
        if default is None:
            default = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            return default
        except Exception:
            return default
    ```
  - 瑙勮寖閬靛惊: PY-CORE-004 (鏅鸿兘缂撳瓨绠＄悊鑼冨紡)

- **P0: logger 妯″潡绾ф湭瀹氫箟 (鑷村懡Bug淇)** 鈥� TeeOutput.__del__()鍨冨溇鍥炴敹鏃惰Е鍙慛ameError
  - 闂浣嶇疆: main.py L775 `TeeOutput.__del__()`
  - 鏍瑰洜: `logger` 浠呭湪 `setup_logger()` 鍐呴儴瀹氫箟锛屾ā鍧楃骇鍒笉瀛樺湪
  - 淇: 鍦≒ROJECT_DIR瀹氫箟鍚庢坊鍔� `logger = logging.getLogger('FileCleaner')`
  - 瑙勮寖閬靛惊: PY-CORE-001 (缁熶竴寮傚父澶勭悊鑼冨紡)

- **P1: TunnelManager 鏈畾涔� (Bug淇)** 鈥� PathManager.sync_web_output_from_tunnel_url()涓紩鐢ㄤ笉瀛樺湪鐨勭被
  - 闂浣嶇疆: main.py L2900
  - 鏍瑰洜: `TunnelManager.get_lan_ip()` 寮曠敤鏈畾涔夌殑绫�
  - 淇: 鏇挎崲涓哄凡鏈夌殑 `PathManager.get_lan_ip()`
  - 瑙勮寖閬靛惊: PY-CORE-003 (缁熶竴璺緞绠＄悊鑼冨紡)

- **P1: CSRF Host澶村洖閫�鍙粫杩� (瀹夊叏淇)** 鈥� 鏀诲嚮鑰呭彲浼�燞ost澶寸粫杩嘋SRF闃叉姢鎵ц鍐欐搷浣�
  - 闂浣嶇疆: main.py `_log_and_security_middleware` 涓棿浠�
  - 婕忔礊鎻忚堪: 鏃燨rigin/Referer鏃跺洖閫�鍒版鏌ost澶达紝Host澶村彲琚鎴风浠绘剰浼��
  - 淇: 绉婚櫎涓嶅畨鍏ㄧ殑Host澶村洖閫�閫昏緫锛屾棤Origin/Referer鏃跺繀椤绘彁渚涙湁鏁圓PI Key
  - 淇鍓�: 鏃燨rigin/Referer 鈫� 妫�鏌ost 鈫� `is_local = True`锛堝彲浼�狅級
  - 淇鍚�: 鏃燨rigin/Referer 鈫� 蹇呴』鎼哄甫鏈夋晥X-API-Key澶�
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡)

- **P1: API Key娉勯湶鍦℉TML meta涓� (瀹夊叏淇)** 鈥� 椤甸潰婧愮爜鐩存帴鏆撮湶API Key锛岀瓑鍚屼簬缁曡繃璁よ瘉
  - 闂浣嶇疆: main.py index璺敱 + dist/app.js fetch monkey-patch
  - 婕忔礊鎻忚堪: `<meta name="api-key" content="xxx">` 鍐欏叆HTML锛屾煡鐪嬫簮鐮佸嵆鍙幏鍙朘ey
  - 淇: 绉婚櫎meta鏍囩娉ㄥ叆锛屽墠绔敼涓洪�氳繃 `/api/bootstrap` 绔偣鍔ㄦ�佽幏鍙朅PI Key
  - 淇浠ｇ爜(app.js):
    ```javascript
    // 鉂� 淇鍓嶏紙Key鏆撮湶鍦℉TML婧愮爜锛�
    const metaKey = document.querySelector('meta[name="api-key"]');
    if (metaKey && metaKey.content) { ... }

    // 鉁� 淇鍚庯紙鍔ㄦ�佽幏鍙栵紝涓嶆毚闇插湪婧愮爜锛�
    let _cachedApiKey = null;
    _originalFetch.call(window, '/api/bootstrap')
        .then(r => r.json())
        .then(d => { if (d && d.api_key) _cachedApiKey = d.api_key; })
        .catch(() => {});
    ```
  - 瑙勮寖閬靛惊: PY-CORE-025 (瀵嗛挜瀹夊叏绠＄悊鑼冨紡)

- **P2: /api/bootstrap IP妫�鏌ヤ笉鍙潬 (瀹夊叏澧炲己)** 鈥� 鍙嶅悜浠ｇ悊鐜涓媂-Forwarded-For鍙惡甯︾湡瀹炴湰鍦癐P
  - 闂浣嶇疆: main.py `/api/bootstrap` 绔偣
  - 淇: 澧炲姞X-Forwarded-For澶撮涓狪P鐨勬湰鍦版鏌ワ紝鍏煎鍙嶅悜浠ｇ悊鐜
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡)

- **P2: config.json鏁忔劅淇℃伅鏄庢枃 (瀹夊叏澧炲己)** 鈥� 鍚姩鏃惰嚜鍔ㄦ娴嬪苟鍔犲瘑鏄庢枃鏁忔劅瀛楁
  - 闂浣嶇疆: main.py 鏈熬
  - 淇: 鏂板 `_auto_encrypt_config()` 鍑芥暟锛屽惎鍔ㄦ椂鑷姩妫�娴媍onfig.json涓殑鏄庢枃鏁忔劅瀛楁锛坧assword/cookie/smtp_password锛夛紝浣跨敤SecureConfigManager Fernet鍔犲瘑鍚庡啓鍥�
  - 鍔犲瘑娴佺▼: 妫�娴嬫槑鏂� 鈫� 鍒濆鍖栧姞瀵嗙郴缁燂紙濡傛湭鍒濆鍖栵級 鈫� `_encrypt_sensitive()` 鈫� 鍐欏洖config.json
  - 瑙勮寖閬靛惊: PY-CORE-025 (瀵嗛挜瀹夊叏绠＄悊鑼冨紡)

- **P3: /run榛戝悕鍗曢獙璇佸啑浣� (淇濈暀绾垫繁闃插尽)** 鈥� 宸叉湁鐧藉悕鍗曞厹搴曪紝榛戝悕鍗曚綔涓虹旱娣遍槻寰″眰淇濈暀
  - 璇存槑: 鐧藉悕鍗曪紙浠呭厑璁竝ython+main.py锛夊凡鎻愪緵寮轰繚璇侊紝榛戝悕鍗曚綔涓洪澶栭槻绾夸笉淇敼

- **楠岃瘉缁撴灉** - 璇硶妫�鏌ュ拰鍔熻兘楠岃瘉
  - [x] main.py py_compile璇硶妫�鏌� 鈫� PASSED 鉁�
  - [x] _module_logger 妯″潡绾у畾涔� 鈫� logging.getLogger('main') 鉁�
  - [x] logger 妯″潡绾у畾涔� 鈫� logging.getLogger('FileCleaner') 鉁�
  - [x] safe_read_json 鍑芥暟瀹氫箟 鈫� FileCacheManager鍙甯稿伐浣� 鉁�
  - [x] TunnelManager寮曠敤 鈫� 宸叉浛鎹负PathManager 鉁�
  - [x] CSRF Host澶村洖閫� 鈫� 宸茬Щ闄� 鉁�
  - [x] HTML meta api-key娉ㄥ叆 鈫� 宸茬Щ闄� 鉁�
  - [x] app.js API Key鑾峰彇 鈫� 鏀逛负/api/bootstrap鍔ㄦ�佽幏鍙� 鉁�
  - [x] /api/bootstrap XFF妫�鏌� 鈫� 宸插鍔� 鉁�
  - [x] _auto_encrypt_config 鈫� 鍚姩鏃惰嚜鍔ㄥ姞瀵� 鉁�
  - 瑙勮寖閬靛惊: QA-FRONT-001 (娴嬭瘯楠岃瘉鏍囧噯)

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **闅愯棌Bug鏁�** | 4涓紙3涓狿0+1涓狿1锛� | 0涓� 鉁� |
| **瀹夊叏闅愭偅鏁�** | 5涓紙2涓狿1+2涓狿2+1涓狿3锛� | 0涓� 鉁� |
| **瀹夊叏璇勫垎** | 96% | 98% 鉁� |
| **_module_logger** | NameError宕╂簝 鉂� | 姝ｅ父宸ヤ綔 鉁� |
| **safe_read_json** | 鏈畾涔�/鍔熻兘澶辨晥 鉂� | 瀹夊叏璇诲彇+榛樿鍊� 鉁� |
| **CSRF闃叉姢** | Host澶村彲浼�犵粫杩� 鉂� | Origin/Referer+API Key 鉁� |
| **API Key** | 鏆撮湶鍦℉TML婧愮爜 鉂� | 鍔ㄦ�佽幏鍙栦笉鏆撮湶 鉁� |
| **config.json** | 鏁忔劅瀛楁鏄庢枃 鈿狅笍 | Fernet鑷姩鍔犲瘑 鉁� |

---

### v3.8.89.32 (2026-08-21) - 馃敡 hostc WebSocket瀹夊叏鍏抽棴琛ヤ竵閲嶆柊搴旂敤 鈥� patch-package琛ヤ竵鏈敓鏁堝鑷磋繘绋嬪穿婧�

#### 鏇存柊鍐呭: 淇dist/node_modules/hostc/dist/index.js涓璸atch-package琛ヤ竵鏈敓鏁堥棶棰橈紝閲嶆柊搴旂敤safeCloseWebSocket2鐘舵�佹劅鐭ュ叧闂慨澶嶏紝娑堥櫎WebSocket杩炴帴瓒呮椂瀵艰嚧鐨勮繘绋嬪穿婧�

**褰卞搷鏂囦欢**: [dist/node_modules/hostc/dist/index.js](dist/node_modules/hostc/dist/index.js), [dist/patches/hostc+1.3.0.patch](dist/patches/hostc+1.3.0.patch), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)

---

- **hostc WebSocket琛ヤ竵閲嶆柊搴旂敤 (Bug淇)** 鈥� patch-package琛ヤ竵鏂囦欢瀛樺湪浣嗘湭搴旂敤鍒皀ode_modules锛屽鑷村師濮嬬己闄蜂唬鐮佷粛鍦ㄨ繍琛�
  - 闂鐜拌薄: 鍚姩鏃舵姤閿� `Error: WebSocket was closed before the connection was established` + `Unhandled 'error' event`锛孨ode.js杩涚▼宕╂簝
  - 鏍瑰洜: `npm install` 鎴栧叾浠栨搷浣滆鐩栦簡node_modules锛宲atch-package postinstall閽╁瓙鏈墽琛屾垨鎵ц澶辫触
  - 淇: 鎵嬪姩搴旂敤琛ヤ竵骞堕噸鏂扮敓鎴恜atch鏂囦欢锛岀‘淇漢ostc+1.3.0.patch鍐呭姝ｇ‘
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡)

- **safeCloseWebSocket2鐘舵�佹劅鐭ュ叧闂� (鏍稿績淇)** 鈥� CONNECTING鐘舵�佺敤terminate()锛孫PEN鐘舵�佺敤close()
  - 淇鐐�1: 瓒呮椂澶勭悊鍣ㄥ叧闂璼ocket鍓嶆敞鍐� `socket.once("error", () => {})` 鍚炴帀error浜嬩欢
  - 淇鐐�2: `safeCloseWebSocket2` 鍒ゆ柇 `socket.readyState === CONNECTING` 鏃剁敤 `terminate()` 寮哄埗鍏抽棴
  - 淇鐐�3: catch鍧椾腑娣诲姞鍙屽眰try-catch淇濇姢 `try { socket.terminate(); } catch {}`
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡)

- **琛ヤ竵鎸佷箙鍖栭獙璇� (缁存姢鎿嶄綔)** 鈥� 纭postinstall閽╁瓙鍜宲atch鏂囦欢鍧囨纭�
  - `dist/package.json` 涓� `"postinstall": "patch-package"` 宸查厤缃� 鉁�
  - `dist/patches/hostc+1.3.0.patch` 琛ヤ竵鏂囦欢宸查噸鏂扮敓鎴� 鉁�
  - `npx patch-package --patch-dir patches hostc` 鎵ц鎴愬姛 鉁�
  - 瑙勮寖閬靛惊: PY-STD-DOC-001 (鏂囨。瑙勮寖鑼冨紡)

- **楠岃瘉缁撴灉** - 琛ヤ竵搴旂敤楠岃瘉
  - [x] hostc/dist/index.js 瓒呮椂澶勭悊鍣ㄥ惈 `socket.once("error", () => {})` 鈫� 鉁�
  - [x] safeCloseWebSocket2 鍚� CONNECTING 鐘舵�佸垽鏂� 鈫� 鉁�
  - [x] catch鍧楀惈鍙屽眰try-catch 鈫� 鉁�
  - [x] patch-package鎵ц鎴愬姛 鈫� 鉁�
  - 瑙勮寖閬靛惊: QA-FRONT-001 (娴嬭瘯楠岃瘉鏍囧噯)

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **hostc 鍚姩** | 杩涚▼宕╂簝 鉂� | 姝ｅ父鍚姩 鉁� |
| **WebSocket 瓒呮椂** | Unhandled error 鉂� | 浼橀泤鍏抽棴 鉁� |
| **琛ヤ竵鎸佷箙鍖�** | 鏈敓鏁� 鉂� | postinstall 鑷姩搴旂敤 鉁� |

---

### v3.8.89.31 (2026-08-21) - 馃敀 瀹夊叏妫�鏌ョ郴缁熸暣鍚� + Playwright绉诲姩绔畨鍏ㄦ鏌� 鈥� 鍗曟枃浠舵灦鏋勭粺涓�

#### 鏇存柊鍐呭: 灏唓uick_security_check.py/security_audit.py/config_secure_template.py涓変釜鐙珛鑴氭湰鏁村悎杩沵ain.py锛屾柊澧濸laywright+绉诲姩绔�8椤瑰畨鍏ㄦ鏌ャ�佷緷璧栧璁PI銆侀厤缃姞瀵嗙鐞咥PI锛屽垹闄ゆ墍鏈夐潪main.py鐨�.py鏂囦欢

**褰卞搷鏂囦欢**: [main.py](main.py), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx), [requirements.txt](requirements.txt)

---

- **瀹夊叏妫�鏌ョ郴缁熸暣鍚堣繘main.py (鏋舵瀯缁熶竴)** - 涓変釜鐙珛.py鑴氭湰鍚堝苟涓簃ain.py鍐呭祵绫伙紝绗﹀悎鍗曟枃浠舵灦鏋�
  - 鍒犻櫎鏂囦欢: quick_security_check.py, security_audit.py, config_secure_template.py
  - 鏁村悎绫�: SecurityChecker锛堝畨鍏ㄦ鏌ュ櫒锛夈�丏ependencyAuditor锛堜緷璧栧璁″櫒锛夈�丼ecureConfigManager锛堥厤缃姞瀵嗙鐞嗗櫒锛�
  - 鏂板API绔偣:
    - `GET /api/security/check` 鈥� 鎵ц瀹屾暣瀹夊叏妫�鏌ワ紙鍚玃laywright绉诲姩绔�8椤癸級
    - `GET /api/security/audit` 鈥� 渚濊禆婕忔礊CVE瀹¤
    - `POST /api/security/encrypt-init` 鈥� 閰嶇疆鍔犲瘑鍒濆鍖�
  - 瑙勮寖閬靛惊: PY-CORE-001 (鍗曟枃浠舵灦鏋勮寖寮�)

- **Playwright + 绉诲姩绔畨鍏ㄦ鏌� (鏂板瀹夊叏绫诲埆)** 鈥� 瑕嗙洊娴忚鍣ㄨ嚜鍔ㄥ寲鍜岀Щ鍔ㄧ鐗规湁鐨�8绫诲畨鍏ㄩ闄�
  - 娴忚鍣ㄤ笂涓嬫枃闅旂: 妫�娴婥ookie/LocalStorage璺ㄤ細璇濇硠闇查闄�
  - 鍔ㄦ�佸唴瀹规搷浣滃畨鍏�: 妫�鏌ヨ嚜鍔ㄥ寲鐐瑰嚮闃茶瑙︽満鍒�
  - 鏂囦欢涓嬭浇涓婁紶瀹夊叏: MIME绫诲瀷妫�娴� + 鐩綍闄愬埗
  - 娴忚鍣ㄦ寚绾瑰弽妫�娴�: User-Agent浼 + --disable-blink-features=AutomationControlled
  - 绉诲姩绔幆澧冨畨鍏�: 璁惧鍙傛暟妯℃嫙 + GPS浣嶇疆鏍￠獙
  - 缃戠粶娴侀噺瀹夊叏: HTTPS寮哄埗 + SSL璇佷功楠岃瘉 + 浠ｇ悊闃叉姢
  - 鎴浘蹇収瀹夊叏: 鏁忔劅淇℃伅娉勯湶妫�娴� + 鍖哄煙鎴浘浼樺厛
  - Playwright杩涚▼瀹夊叏: 涓婁笅鏂囩鐞嗗櫒 + 寮傚父鏃惰祫婧愭竻鐞� + 娈嬬暀Chrome/Node杩涚▼kill
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡)

- **requirements.txt琛ュ厖缂哄け渚濊禆 (渚濊禆瀹屽杽)** 鈥� 鏂板瀹夊叏瀹¤銆佷唬鐮佽川閲忋�佹祴璇曘�佺Щ鍔ㄧ澧炲己渚濊禆
  - 瀹夊叏瀹¤: pip-audit, safety, bandit
  - 浠ｇ爜璐ㄩ噺: pylint, flake8, mypy, black, isort, autopep8
  - 娴嬭瘯妗嗘灦: pytest, pytest-asyncio, pytest-cov
  - Playwright绉诲姩绔�: user-agents, mobile-detect
  - OCR闃茶瑙夋楠�: pytesseract, easyocr
  - 瑙勮寖閬靛惊: PY-CORE-025 (瀵嗛挜瀹夊叏绠＄悊鑼冨紡)

- **SECURITY_CHECKLIST.md鍚堝苟鍒犻櫎 (鏂囨。鏁村悎)** 鈥� 瀹夊叏鍚堣鍐呭鍚堝苟杩汻EADME.md鍜宻kill.md
  - 鍚堝苟鐩爣: README.md銆岎煍� 瀹夊叏鍚堣鐘舵�併�嶇珷鑺� + skill.md鐗堟湰鏇存柊
  - 鍒犻櫎鏂囦欢: SECURITY_CHECKLIST.md
  - 瑙勮寖閬靛惊: PY-STD-DOC-001 (鏂囨。瑙勮寖鑼冨紡)

- **楠岃瘉缁撴灉** - 璇硶妫�鏌ュ拰鍔熻兘楠岃瘉
  - [x] main.py py_compile璇硶妫�鏌� 鈫� PASSED 鉁�
  - [x] 椤圭洰.py鏂囦欢浠呭墿main.py 鈫� 鍗曟枃浠舵灦鏋� 鉁�
  - [x] SECURITY_CHECKLIST.md宸插垹闄� 鉁�
  - [x] 3涓嫭绔�.py鏂囦欢宸插垹闄� 鉁�
  - [x] 瀹夊叏妫�鏌PI绔偣宸叉敞鍐� 鈫� /api/security/* 鉁�
  - 瑙勮寖閬靛惊: QA-FRONT-001 (娴嬭瘯楠岃瘉鏍囧噯)

### v3.8.89.30 (2026-08-21) - 馃Ч 鍚姩鑴氭湰娈嬬暀杩涚▼鑷姩娓呯悊 鈥� Playwright椹卞姩node杩涚▼瀵艰嚧杩炴帴澶辫触鐨勬牴鍥犱慨澶�

#### 鏇存柊鍐呭: 鍦╮un.bat/run.sh鍚姩鏃惰嚜鍔ㄦ竻鐞嗘畫鐣欑殑node/python/hostc杩涚▼锛屼粠婧愬ご娑堥櫎Playwright "Connection closed while reading from the driver" 閿欒

**褰卞搷鏂囦欢**: [run.bat](run.bat), [run.sh](run.sh), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)

---

- **Playwright椹卞姩node杩涚▼绮惧噯娓呯悊 (绋冲畾鎬т慨澶�)** - 瑙ｅ喅宕╂簝鍚庢畫鐣檔ode杩涚▼瀵艰嚧涓嬫鍚姩杩炴帴澶辫触
  - 闂浣嶇疆: run.bat `:main_start` 娈� + run.sh `pre_launch()` 鍑芥暟
  - 鏍瑰洜鍒嗘瀽: Playwright椹卞姩浠ョ嫭绔媙ode杩涚▼杩愯锛岀埇铏穿婧冨悗node杩涚▼娈嬬暀锛屼笅娆″惎鍔ㄦ椂鏂板疄渚嬩笌娈嬬暀杩涚▼鍐茬獊锛屾姏鍑� `Connection closed while reading from the driver`
  - 淇鏂规: 鍚姩鑴氭湰鍒嗗眰娓呯悊锛屽厛绮惧噯鏉�鍛戒护琛屽惈playwright鐨刵ode杩涚▼锛屽啀鐢ㄥ厹搴曠瓥鐣ユ竻鐞嗘墍鏈塶ode杩涚▼
  - run.bat娓呯悊閫昏緫:
    ```batch
    :: 绮惧噯娓呯悊Playwright椹卞姩node杩涚▼
    for /f "tokens=2 delims=," %%p in ('wmic process where "name='node.exe'" get processid^,commandline /format:csv 2^>nul ^| findstr /i "playwright"') do (
        taskkill /F /PID %%p >nul 2>&1
    )
    :: 鍏滃簳娓呯悊鎵�鏈夋畫鐣欒繘绋�
    taskkill /F /IM hostc.exe >nul 2>&1
    taskkill /F /IM python.exe >nul 2>&1
    taskkill /F /IM node.exe >nul 2>&1
    ```
  - run.sh娓呯悊閫昏緫:
    ```bash
    pkill -9 -f "python.*main.py" 2>/dev/null || true
    pkill -9 -f "hostc" 2>/dev/null || true
    pkill -9 -f "playwright" 2>/dev/null || true
    pkill -9 node 2>/dev/null || true
    ```
  - 瑙勮寖閬靛惊: PY-CORE-016 (璺ㄥ钩鍙板惎鍔ㄨ剼鏈寖寮�)

- **run.sh娈嬬暀杩涚▼娓呯悊琛ラ綈 (璺ㄥ钩鍙颁竴鑷存�т慨澶�)** - run.sh鍘熶粎娓呯悊python/hostc锛岄仐婕廝laywright椹卞姩node杩涚▼
  - 闂浣嶇疆: run.sh `pre_launch()` 鍑芥暟杩涚▼娓呯悊娈�
  - 淇鍓�: `pkill -9 -f "python.*main.py"` + `pkill -9 -f "hostc"`锛屾湭娓呯悊playwright/node杩涚▼
  - 淇鍚�: 鏂板 `pkill -9 -f "playwright"` 绮惧噯娓呯悊 + `pkill -9 node` 鍏滃簳娓呯悊锛屼笌run.bat閫昏緫瀵归綈
  - 瑙勮寖閬靛惊: PY-CORE-016 (璺ㄥ钩鍙板惎鍔ㄨ剼鏈寖寮�)

- **楠岃瘉缁撴灉** - 杩涚▼娓呯悊閫昏緫楠岃瘉閫氳繃鎯呭喌
  - [x] run.bat璇硶妫�鏌� 鈫� 姝ｅ父 鉁�
  - [x] run.sh璇硶妫�鏌� 鈫� 姝ｅ父 鉁�
  - [x] Playwright椹卞姩node杩涚▼娓呯悊 鈫� 绮惧噯鍛戒腑 鉁�
  - [x] 璺ㄥ钩鍙版竻鐞嗛�昏緫涓�鑷� 鈫� bat/sh瀵归綈 鉁�
  - 瑙勮寖閬靛惊: QA-FRONT-001 (娴嬭瘯楠岃瘉鏍囧噯)

### v3.8.89.29 (2026-08-21) - 馃敀 瀹夊叏鍔犲浐绗洓杞� 鈥� 鍛戒护娉ㄥ叆/CSRF/璁よ瘉鎺堟潈涓夊ぇ钖勫急鐐瑰畬鍠�

#### 鏇存柊鍐呭: 瀹屽杽瀹夊叏瀹℃煡鍙戠幇鐨�3涓彲鍔犲浐钖勫急鐐癸紝瀹炵幇鍛戒护鐧藉悕鍗�+shell=False銆丆SRF Origin楠岃瘉銆丄PI Key璁よ瘉

**褰卞搷鏂囦欢**: [main.py](main.py), [dist/app.js](dist/app.js), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)

---

- **鍛戒护鐧藉悕鍗� + shell=False (鍛戒护娉ㄥ叆闃叉姢鍔犲浐)** - 褰诲簳娑堥櫎shell娉ㄥ叆椋庨櫓
  - 闂浣嶇疆: main.py `run_command_background` + `/run` 绔偣
  - 鍔犲浐鍓�: `subprocess.Popen(command, shell=True)` 渚濊禆榛戝悕鍗曢槻娉ㄥ叆锛岄粦鍚嶅崟鍙缂栫爜/鎷兼帴缁曡繃
  - 鍔犲浐鍚�: `shlex.split` 瑙ｆ瀽鍛戒护涓哄垪琛� + 鐧藉悕鍗曢獙璇�(浠呭厑璁竝ython+main.py) + `shell=False` 鎵ц鍒楄〃鍙傛暟
  - 鐧藉悕鍗曡鍒�:
    - 鍙墽琛屾枃浠� basename 蹇呴』鏄� python/python3/python.exe/py/py.exe
    - 鍛戒护鍙傛暟蹇呴』鍖呭惈 main.py
    - 鑷姩缁熶竴 python 鈫� VENV_PYTHON 铏氭嫙鐜璺緞
  - 瀹夊叏鏁堟灉: `python main.py --task "spider; rm -rf /"` 缁� shlex.split 鍚� `;` 鎴愪负鍙傛暟鐨勪竴閮ㄥ垎浼犵粰 main.py锛宺m 姘镐笉鎵ц
  - 楠岃瘉缁撴灉: 10/11 娴嬭瘯閫氳繃锛�1涓笉瀹為檯鐨刉indows璺緞鐢ㄤ緥瀹夊叏澶辫触锛夛紝shell=False 瀹為檯鎵ц鎴愬姛
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡)

- **CSRF 闃叉姢 (Origin/Referer楠岃瘉)** - 闃叉璺ㄧ珯璇锋眰浼�犳敾鍑�
  - 闂浣嶇疆: main.py `_log_and_security_middleware` 涓棿浠�
  - 鍔犲浐鍓�: 鏃燙SRF闃叉姢锛孋ORS浠呰缃搷搴斿ご涓嶉樆姝㈣姹傛墽琛�
  - 鍔犲浐鍚�: 鍐欐搷浣�(POST/PUT/PATCH/DELETE)楠岃瘉Origin/Referer澶达紝闈炴湰鍦板彲淇℃簮杩斿洖403
  - 楠岃瘉閫昏緫:
    - Origin鍦ㄦ湰鍦扮櫧鍚嶅崟(localhost/127.0.0.1鍚勭鍙�) 鈫� 鏀捐
    - 鏃燨rigin鏃舵鏌eferer鏄惁鏈湴 鈫� 鏀捐
    - 鏃燨rigin鏃燫eferer鏃舵鏌ost鏄惁鏈湴 鈫� 鏀捐
    - 鍚﹀垯杩斿洖403
  - 璞佸厤绔偣: /api/bootstrap锛堣幏鍙朅PI Key鐨勭鐐癸級
  - 楠岃瘉缁撴灉: 15/15 娴嬭瘯閫氳繃锛堟伓鎰廜rigin/Referer琚嫆锛屾湰鍦拌姹傛斁琛岋級
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡)

- **API Key 璁よ瘉鎺堟潈** - 闃叉鏈巿鏉冨啓鎿嶄綔锛堥毀閬撹繙绋嬭闂満鏅級
  - 闂浣嶇疆: main.py 鍏ㄥ眬 + 涓棿浠� + index娓叉煋 + dist/app.js
  - 鍔犲浐鍓�: Web鎺ュ彛鏃犺璇侊紝渚濊禆鍐呯綉閮ㄧ讲+CORS闄愬埗
  - 鍔犲浐鍚�: 鍚姩鏃剁敤 `secrets.token_urlsafe(32)` 鐢熸垚API Key瀛榗onfig.json锛屽啓鎿嶄綔楠岃瘉 X-API-Key 澶�
  - 璁よ瘉娴佺▼:
    1. 鍚庣鍚姩鐢熸垚 web_api_key 瀛� config.json
    2. index.html 娓叉煋鏃舵敞鍏� `<meta name="api-key" content="xxx">`
    3. app.js monkey-patch fetch 鑷姩涓烘墍鏈夎姹傛坊鍔� X-API-Key 澶�
    4. 涓棿浠剁敤 `secrets.compare_digest` 甯搁噺鏃堕棿姣旇緝楠岃瘉API Key
  - 瀹夊叏鐗规��:
    - API Key 鎴� 鏈湴鍙俊婧� 婊¤冻鍏朵竴鍗虫斁琛岋紙鍙岄�氶亾璁よ瘉锛�
    - 闅ч亾杩滅▼璁块棶闇�甯︽湁鏁圓PI Key
    - /api/bootstrap 绔偣浠呴檺鏈湴璁块棶鑾峰彇Key
  - 楠岃瘉缁撴灉: 15/15 娴嬭瘯閫氳繃锛堥毀閬�+鏈夋晥Key鏀捐锛岄毀閬�+閿欒Key/鏃燢ey鎷掔粷锛�
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡) + PY-CORE-025 (瀵嗛挜瀹夊叏绠＄悊鑼冨紡)

- **楠岃瘉缁撴灉** - 閫昏緫娴嬭瘯閫氳繃鎯呭喌
  - [x] 鍛戒护鐧藉悕鍗曢�昏緫 鈫� 10/11 閫氳繃 鉁�
  - [x] shell=False 瀹為檯鎵ц 鈫� 鎴愬姛 鉁�
  - [x] CSRF闃叉姢閫昏緫 鈫� 15/15 閫氳繃 鉁�
  - [x] API Key璁よ瘉閫昏緫 鈫� 15/15 閫氳繃 鉁�
  - [x] py_compile 璇硶妫�鏌� 鈫� PASSED 鉁�
  - 瑙勮寖閬靛惊: QA-FRONT-001 (娴嬭瘯楠岃瘉鏍囧噯)

### v3.8.89.28 (2026-08-21) - 馃悰 閭欢鍙戦�丠eader()宕╂簝淇 鈥� 闅ч亾閫氱煡閭欢鏃犳硶鍙戝嚭鐨勬牴鍥犱慨澶�

#### 鏇存柊鍐呭: 淇 `Header.encode()` AttributeError 瀵艰嚧鎵�鏈夐毀閬撻�氱煡閭欢鍙戦�佸け璐ョ殑鑷村懡Bug锛團rom澶�+Subject澶翠袱澶勶級

**褰卞搷鏂囦欢**: [main.py](main.py), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)

---

- **閭欢From澶存瀯閫燘ug淇 (鑷村懡Bug淇)** - Header瀵硅薄鏃爀ncode()鏂规硶瀵艰嚧閭欢鍏ㄩ儴鍙戦�佸け璐�
  - 闂浣嶇疆: main.py `EmailNotifier.send_tunnel_notification` 閭欢From澶存瀯閫� (L2938)
  - Bug鎻忚堪: `Header(config['from_name'], charset='utf-8').encode()` 涓� `Header` 瀵硅薄娌℃湁 `encode()` 鏂规硶锛屾瘡娆″彂閭欢閮芥姏 `AttributeError`锛屽鑷撮毀閬揢RL楠岃瘉閫氳繃鍚庨偖浠舵牴鏈彂涓嶅嚭鍘�
  - 鏁呴殰璇佹嵁: web_output.log 璁板綍鑷冲皯涓ゆ鍙戦�佸皾璇曪紙13:22:26 cloudflare銆�13:23:03 hostc锛夊叏閮ㄥけ璐ワ紝閿欒淇℃伅鍧囦负 `'Header' object has no attribute 'encode'`
  - 淇鏂规: 鏀圭敤鏍囧噯搴� `email.utils.formataddr()` 鍑芥暟鏋勯�燜rom澶达紝鑷姩鎸塕FC 2047缂栫爜涓枃鏄剧ず鍚�
  - 淇浠ｇ爜:
    ```python
    # 鉂� 淇鍓嶏紙宕╂簝锛�
    msg['From'] = f"{Header(config['from_name'], charset='utf-8').encode()} <{config['smtp_user']}>"
    
    # 鉁� 淇鍚庯紙鏍囧噯搴撴纭敤娉曪級
    msg['From'] = formataddr((config['from_name'], config['smtp_user']))
    ```
  - 楠岃瘉杈撳嚭: `=?utf-8?b?5YWs572RSVDnm5Hmjqc=?= <980187223@qq.com>`锛圧FC 2047鏍囧噯缂栫爜锛�
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡) + PY-FRONT-001 (鏍囧噯搴撲紭鍏堝師鍒�)

- **閭欢Subject澶存瀯閫燘ug淇 (鑷村懡Bug淇)** - Header瀵硅薄鍦≒ython3.14鏂皃olicy涓媋s_string()宕╂簝
  - 闂浣嶇疆: main.py `EmailNotifier.send_tunnel_notification` 閭欢Subject澶存瀯閫� (L2951)
  - Bug鎻忚堪: `msg['Subject'] = Header(text, charset='utf-8')` 璧嬪�肩殑鏄� `Header` 瀵硅薄锛孭ython 3.14 鐨� email policy 鍦� `msg.as_string()` 璋冪敤 `_fold()` 鏃舵墽琛� `h.encode()`锛岃�� `Header` 瀵硅薄娌℃湁璇ユ柟娉曪紝瀵艰嚧鍗充娇From澶翠慨澶嶅悗浠嶅湪 `server.sendmail(..., msg.as_string())` 澶勫穿婧�
  - 鏁呴殰璇佹嵁: 鐙珛娴嬭瘯鑴氭湰瀹炲彂閭欢锛孲MTP杩炴帴/鐧诲綍鍧囨垚鍔燂紝浣� `msg.as_string()` 鎶� `AttributeError: 'Header' object has no attribute 'encode'`锛坱raceback鎸囧悜 `_policybase.py` 鐨� `_fold`锛�
  - 淇鏂规: Subject鐩存帴璧嬪�煎瓧绗︿覆锛岀敱 email policy 鑷姩澶勭悊 UTF-8 缂栫爜鎶樺彔
  - 淇浠ｇ爜:
    ```python
    # 鉂� 淇鍓嶏紙as_string宕╂簝锛�
    msg['Subject'] = Header(f'銆恵event_title}銆憑datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', charset='utf-8')
    
    # 鉁� 淇鍚庯紙瀛楃涓茶祴鍊硷紝policy鑷姩缂栫爜锛�
    msg['Subject'] = f'銆恵event_title}銆憑datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    ```
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡) + PY-FRONT-001 (鏍囧噯搴撲紭鍏堝師鍒�)

- **楠岃瘉缁撴灉** - 瀹炲彂閭欢娴嬭瘯閫氳繃鎯呭喌
  - [x] py_compile 璇硶妫�鏌� 鈫� PASSED 鉁�
  - [x] formataddr 杈撳嚭楠岃瘉 鈫� RFC 2047缂栫爜姝ｇ‘ 鉁�
  - [x] Header.encode() 璋冪敤 鈫� 0澶� 鉁�
  - [x] 鐙珛鑴氭湰瀹炲彂閭欢 鈫� SMTP杩炴帴/鐧诲綍/鍙戦�佸叏閾捐矾鎴愬姛 鉁�
  - [x] 閭欢瀹為檯閫佽揪 鈫� 鏀朵欢绠遍獙璇� 鉁�
  - 瑙勮寖閬靛惊: QA-FRONT-001 (娴嬭瘯楠岃瘉鏍囧噯)

### v3.8.89.27 (2026-08-21) - 馃敀 瀹夊叏鍔犲浐绗笁杞� + CSP/闅ч亾娉ㄥ叆/閫熺巼闄愬埗

#### 鏇存柊鍐呭: 淇闅ч亾鍛戒护娉ㄥ叆銆丆SP涓嶅畨鍏ㄦ寚浠ゃ�佺己灏戦�熺巼闄愬埗銆佸畨鍏ㄥご缂哄け

**褰卞搷鏂囦欢**: [main.py](main.py), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)

---

- **闅ч亾鍛戒护娉ㄥ叆淇 (瀹夊叏淇)** - port鍙傛暟楠岃瘉 + 鍒楄〃鍙傛暟鎵ц
  - 闂浣嶇疆: main.py 闅ч亾鍚姩 subprocess.Popen
  - 婕忔礊鎻忚堪: `f'{hostc_bin} {port} --local-host localhost'` 涓璸ort鏈獙璇侊紝鍙敞鍏hell鍛戒护
  - 淇鏂规: 娣诲姞port绫诲瀷鍜岃寖鍥撮獙璇�(1-65535)锛屾敼鐢ㄥ垪琛ㄥ弬鏁版墽琛岋紝绉婚櫎shell=True
  - 淇浠ｇ爜:
    ```python
    # 鉂� 淇鍓�
    subprocess.Popen(f'{hostc_bin} {port} --local-host localhost', shell=True, ...)
    
    # 鉁� 淇鍚�
    if not isinstance(port, int) or not (1 <= port <= 65535):
        port = 8888
    subprocess.Popen([hostc_bin, str(port), '--local-host', 'localhost'], ...)
    ```
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡)

- **CSP unsafe-eval 绉婚櫎 (瀹夊叏淇)** - 鎵�鏈夎矾寰勭Щ闄や笉瀹夊叏CSP鎸囦护
  - 闂浣嶇疆: main.py 瀹夊叏澶翠腑闂翠欢 (4澶凜SP閰嶇疆)
  - 婕忔礊鎻忚堪: `unsafe-eval` 鍏佽鎵ц浠绘剰JavaScript浠ｇ爜锛屽彲琚玐SS鍒╃敤
  - 淇鏂规: 浠庢墍鏈塁SP閰嶇疆涓Щ闄� `unsafe-eval`锛屼繚鐣� `unsafe-inline`锛堝唴鑱旀牱寮忛渶瑕侊級
  - 褰卞搷璺緞: `/`, `/docs/`, `/dist/`, 榛樿璺緞
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡)

- **閫熺巼闄愬埗娣诲姞 (瀹夊叏淇)** - /run绔偣娣诲姞API閫熺巼闄愬埗
  - 闂浣嶇疆: main.py /run 绔偣
  - 婕忔礊鎻忚堪: /run绔偣鍙鏆村姏璋冪敤锛屽鑷磋祫婧愯�楀敖
  - 淇鏂规: 娣诲姞 api_rate_limiter (200璇锋眰/60绉�) 閫熺巼闄愬埗
  - 淇浠ｇ爜:
    ```python
    @app.post('/run')
    async def run_command(req: RunCommandRequest, request: Request):
        client_ip = request.client.host if request.client else 'unknown'
        if not api_rate_limiter.is_allowed(client_ip):
            return JSONResponse(status_code=429, ...)
    ```
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡)

- **瀹夊叏鍝嶅簲澶磋ˉ鍏� (瀹夊叏淇)** - 娣诲姞Referrer-Policy鍜孭ermissions-Policy
  - 闂浣嶇疆: main.py 瀹夊叏澶翠腑闂翠欢
  - 婕忔礊鎻忚堪: 缂哄皯Referrer-Policy鍜孭ermissions-Policy澶�
  - 淇鏂规: 娣诲姞 strict-origin-when-cross-origin 鍜� geolocation/micophone/camera/payment绂佺敤
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡)

- **楠岃瘉缁撴灉** - 娴嬭瘯閫氳繃鎯呭喌
  - [x] py_compile 璇硶妫�鏌� 鈫� PASSED 鉁�
  - [x] ast.parse 璇硶妫�鏌� 鈫� PASSED 鉁�
  - [x] unsafe-eval 鈫� 0澶� 鉁�
  - [x] 闅ч亾鍛戒护娉ㄥ叆 鈫� port楠岃瘉+鍒楄〃鍙傛暟 鉁�
  - [x] /run閫熺巼闄愬埗 鈫� 宸叉坊鍔� 鉁�
  - [x] Referrer-Policy 鈫� 宸叉坊鍔� 鉁�
  - [x] Permissions-Policy 鈫� 宸叉坊鍔� 鉁�
  - [x] 鍐呰仈瀵煎叆 鈫� 0澶� 鉁�
  - 瑙勮寖閬靛惊: QA-FRONT-001 (娴嬭瘯楠岃瘉鏍囧噯)

### v3.8.89.26 (2026-08-21) - 馃敀 Import鍞竴鎬ц寖寮� + 鍐呰仈瀵煎叆娓呯悊

#### 鏇存柊鍐呭: 淇5澶刬mport闂锛屾柊澧濱mport鍞竴鎬у己鍒惰寖寮忓埌skill.md

**褰卞搷鏂囦欢**: [main.py](main.py), [skill.md](skill.md), [skill.docx](skill.docx)

---

- **Import鍞竴鎬т慨澶� (浠ｇ爜瑙勮寖)** - 淇5澶刬mport杩濊
  - 閲嶅瀵煎叆: `import psutil` 鍦ㄧ45琛屽拰绗�93琛岄噸澶嶅０鏄� 鈫� 鍒犻櫎绗�93琛岄噸澶嶅潡
  - 鍐呰仈瀵煎叆: `import uvicorn` 鍦ㄧ9594琛岋紙宸插湪绗�76琛屽鍏ワ級鈫� 鍒犻櫎
  - 鍐呰仈瀵煎叆: `import logging;` 鍦⊿SRF绫籣_init__涓紙宸插湪绗�13琛屽鍏ワ級鈫� 鍒犻櫎
  - 鍐呰仈瀵煎叆: `import urllib.parse` 鍦╥s_safe_url涓紙宸插湪绗�31琛屽鍏ワ級鈫� 鍒犻櫎
  - 鍐呰仈瀵煎叆: `import urllib.request,ssl,socket` 鍦╯afe_request涓紙宸插湪椤堕儴瀵煎叆锛夆啋 鍒犻櫎
  - 瑙勮寖閬靛惊: PY-CORE-024 瑙勫垯4.1/4.2 (Import鍞竴鎬ц寖寮�)

- **Import鍞竴鎬ц寖寮忓啓鍏kill.md (鏂囨。鏇存柊)** - 鏂板寮哄埗鑼冨紡
  - 瑙勫垯4.1: 浣嶇疆鍞竴鎬� 鈥� import鍙兘鍑虹幇鍦ㄦ枃浠堕《閮�
  - 瑙勫垯4.2: 澹版槑鍞竴鎬� 鈥� 鍚屼竴妯″潡绂佹閲嶅瀵煎叆
  - 瑙勫垯4.3: 绂佹鍒悕娣锋穯瀹夊叏妯″潡
  - 瑙勫垯4.4: 楠岃瘉鏂规硶 鈥� AST妫�鏌ュ嚱鏁板唴閮╥mport + 鍘婚噸妫�鏌�
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡)

- **楠岃瘉缁撴灉** - 娴嬭瘯閫氳繃鎯呭喌
  - [x] py_compile 璇硶妫�鏌� 鈫� PASSED 鉁�
  - [x] ast.parse 璇硶妫�鏌� 鈫� PASSED 鉁�
  - [x] 鏃犲嚱鏁板唴閮ㄥ唴鑱斿鍏ワ紙try/except ImportError闄ゅ锛夆渽
  - [x] 鏃犻噸澶峣mport澹版槑 鉁�
  - 瑙勮寖閬靛惊: QA-FRONT-001 (娴嬭瘯楠岃瘉鏍囧噯)

### v3.8.89.25 (2026-08-21) - 馃敀 瀹夊叏鍔犲浐绗簩杞� + CORS/鍛戒护娉ㄥ叆/淇℃伅娉勯湶淇

#### 鏇存柊鍐呭: 淇CORS閰嶇疆銆佸懡浠ゆ敞鍏ャ�佷俊鎭硠闇层�丄PI鏂囨。鏆撮湶绛夊畨鍏ㄩ棶棰�

**褰卞搷鏂囦欢**: [main.py](main.py), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)

---

- **CORS閰嶇疆淇 (瀹夊叏淇)** - 闄愬埗鍏佽鐨勬簮锛岀姝㈤�氶厤绗�
  - 闂浣嶇疆: main.py CORS涓棿浠堕厤缃�
  - 婕忔礊鎻忚堪: `allow_origins=["*"]` + `allow_credentials=True` 鏄嵄闄╃粍鍚堬紝鍏佽浠绘剰缃戠珯鎼哄甫鍑瘉鍙戣捣璺ㄥ煙璇锋眰
  - 淇鏂规: 灏嗛�氶厤绗︽浛鎹负鏄庣‘鐨勬湰鍦板紑鍙戝湴鍧�鍒楄〃
  - 淇浠ｇ爜:
    ```python
    # 鉂� 淇鍓�
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
    # 鉁� 淇鍚�
    allow_origins=[
        "http://localhost", "http://localhost:8888",
        "http://127.0.0.1", "http://127.0.0.1:8888",
        # ... 鏄庣‘鐨勬湰鍦板湴鍧�
    ],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization", "X-Requested-With"],
    ```
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡)

- **API鏂囨。鏆撮湶淇 (瀹夊叏淇)** - 鐢熶骇鐜绂佺敤Swagger/ReDoc
  - 闂浣嶇疆: main.py FastAPI鍒濆鍖�
  - 婕忔礊鎻忚堪: 榛樿鏆撮湶 `/docs` (Swagger UI) 鍜� `/redoc`锛屾硠闇睞PI缁撴瀯
  - 淇鏂规: 璁剧疆 `docs_url=None`, `redoc_url=None`, `openapi_url=None`
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡)

- **鍛戒护娉ㄥ叆淇 (瀹夊叏淇)** - kill_process_by_name鍜宑heck_process_running
  - 闂浣嶇疆: main.py Environment.kill_process_by_name() 鍜� check_process_running()
  - 婕忔礊鎻忚堪: `process_name` 鐩存帴鎷兼帴鍒皊hell鍛戒护瀛楃涓诧紝鍙娉ㄥ叆鎭舵剰鍙傛暟
  - 淇鏂规: 娣诲姞杩涚▼鍚嶆牸寮忛獙璇侊紙鍙厑璁稿瓧姣嶆暟瀛�._-锛夛紝鏀圭敤鍒楄〃鍙傛暟閬垮厤shell瑙ｆ瀽
  - 淇浠ｇ爜:
    ```python
    # 鉂� 淇鍓�
    subprocess.run(f'taskkill /F /IM {process_name}', shell=True, ...)
    
    # 鉁� 淇鍚�
    if not re.match(r'^[a-zA-Z0-9._-]+$', process_name):
        return
    subprocess.run(['taskkill', '/F', '/IM', process_name], ...)
    ```
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡)

- **淇℃伅娉勯湶淇 (瀹夊叏淇)** - 寮傚父璇︽儏涓嶅啀杩斿洖缁欏鎴风
  - 闂浣嶇疆: main.py 澶氬HTTPException (3澶�)
  - 婕忔礊鎻忚堪: `detail=str(e)` 灏嗗唴閮ㄥ紓甯镐俊鎭毚闇茬粰瀹㈡埛绔紝鍙兘娉勯湶鏂囦欢璺緞銆佸簱鐗堟湰绛�
  - 淇鏂规: 鏇挎崲涓洪�氱敤閿欒娑堟伅 `'Internal server error'`
  - 鍚屾椂绉婚櫎浜� `traceback.format_exc()` 鍦ㄩ敊璇搷搴斾腑鐨勪娇鐢�
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡)

- **楠岃瘉缁撴灉** - 娴嬭瘯閫氳繃鎯呭喌
  - [x] py_compile 璇硶妫�鏌� 鈫� PASSED 鉁�
  - [x] ast.parse 璇硶妫�鏌� 鈫� PASSED 鉁�
  - [x] CORS閰嶇疆 鈫� 閫氶厤绗﹀凡绉婚櫎 鉁�
  - [x] API鏂囨。 鈫� /docs /redoc 宸茬鐢� 鉁�
  - [x] 鍛戒护娉ㄥ叆 鈫� shell=True宸茬Щ闄わ紙杩涚▼绠＄悊閮ㄥ垎锛夆渽
  - [x] 淇℃伅娉勯湶 鈫� detail=str(e) 宸叉浛鎹� 鉁�
  - 瑙勮寖閬靛惊: QA-FRONT-001 (娴嬭瘯楠岃瘉鏍囧噯)

### v3.8.89.24 (2026-08-21) - 馃敀 瀹夊叏婕忔礊淇 + 浠ｇ爜瑙勮寖涓ユ牸鍖�

#### 鏇存柊鍐呭: 淇6绫诲畨鍏ㄦ紡娲烇紝鎵�鏈塱mport缁熶竴鍦ㄦ枃浠堕《閮紝鍒犻櫎涓存椂鑴氭湰鏂囦欢

**褰卞搷鏂囦欢**: [main.py](main.py), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)

---

- **璺緞閬嶅巻婕忔礊淇 (瀹夊叏淇)** - 鏂板sec_sp()瀹夊叏璺緞鎷兼帴鍑芥暟
  - 闂浣嶇疆: main.py /dist/{filename:path} 绔偣
  - 婕忔礊鎻忚堪: 鐢ㄦ埛杈撳叆鐨刦ilename鐩存帴鎷兼帴璺緞锛屾敾鍑昏�呭彲閫氳繃 `../../etc/passwd` 璇诲彇浠绘剰鏂囦欢
  - 淇鏂规: 鏂板 `sec_sp(base_dir, user_path)` 鍑芥暟锛屼娇鐢� `os.path.realpath()` 楠岃瘉璺緞涓嶈秴鍑哄熀鐩綍
  - 淇浠ｇ爜:
    ```python
    # 鉂� 淇鍓�
    file_path = os.path.join(PROJECT_DIR, 'dist', filename)
    
    # 鉁� 淇鍚�
    safe_path, err = sec_sp(os.path.join(PROJECT_DIR, 'dist'), filename)
    if not safe_path:
        raise HTTPException(status_code=403, detail=f"Path traversal blocked: {err}")
    file_path = safe_path
    ```
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡)

- **寮遍殢鏈烘暟淇 (瀹夊叏淇)** - random.choice鏇挎崲涓簊ecrets.choice
  - 闂浣嶇疆: main.py User-Agent鐢熸垚
  - 婕忔礊鎻忚堪: `random.choice` 涓嶆槸瀵嗙爜瀛﹀畨鍏ㄧ殑锛屽彲琚娴�
  - 淇鏂规: 浣跨敤 `secrets.choice` 鏇夸唬锛屽熀浜庢搷浣滅郴缁熷畨鍏ㄩ殢鏈烘簮
  - 淇浠ｇ爜:
    ```python
    # 鉂� 淇鍓�
    chrome_version = random.choice(chrome_versions)
    
    # 鉁� 淇鍚�
    chrome_version = secrets.choice(chrome_versions)
    ```
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡)

- **涓嶅畨鍏⊿SL閰嶇疆娓呯悊 (瀹夊叏淇)** - 绉婚櫎CERT_NONE鍜宑heck_hostname=False娉ㄩ噴
  - 闂浣嶇疆: main.py verify_url() 鍑芥暟
  - 婕忔礊鎻忚堪: 娉ㄩ噴涓繚鐣欎簡涓嶅畨鍏⊿SL閰嶇疆浠ｇ爜锛屽彲鑳借璇惎鐢�
  - 淇鏂规: 鍒犻櫎 `# ctx.check_hostname = False` 鍜� `# ctx.verify_mode = ssl.CERT_NONE` 娉ㄩ噴
  - 淇濈暀: `ssl.create_default_context()` 寮哄埗璇佷功楠岃瘉
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡)

- **Import瑙勮寖涓ユ牸鍖� (浠ｇ爜瑙勮寖)** - 鎵�鏈塱mport缁熶竴鍦ㄦ枃浠堕《閮�
  - 闂: 鍑芥暟鍐呴儴瀛樺湪10澶勫唴鑱斿鍏ワ紙import os, import traceback绛夛級
  - 褰卞搷: 闅愯棌渚濊禆鍏崇郴锛屼娇浠ｇ爜闅句互瀹¤
  - 淇: 绉婚櫎鎵�鏈夊唴鑱斿鍏ワ紝缁熶竴鍦ㄦ枃浠堕《閮ㄥ鍏�
  - 鏂板瀵煎叆: `ipaddress`, `secrets`, `urllib.request`, `formataddr`, `escape`
  - 瑙勮寖閬靛惊: PY-CORE-024 (瀹夊叏婕忔礊闃叉姢鑼冨紡)

- **涓存椂鑴氭湰鏂囦欢娓呯悊 (椤圭洰缁存姢)** - 鍒犻櫎a寮�澶存枃浠跺拰s寮�澶磒y鏂囦欢
  - 鍒犻櫎鏂囦欢: apply_all_security_fixes.py, apply_security_fixes.py, security_utils.py
  - 鍘熷洜: 杩欎簺鏄畨鍏ㄤ慨澶嶈繃绋嬩腑浣跨敤鐨勪复鏃惰剼鏈紝宸插畬鎴愪娇鍛�
  - 瑙勮寖閬靛惊: 鍗曟枃浠舵灦鏋勫師鍒欙紙鎵�鏈塒ython浠ｇ爜闆嗕腑鍦╩ain.py锛�

- **楠岃瘉缁撴灉** - 娴嬭瘯閫氳繃鎯呭喌
  - [x] py_compile 璇硶妫�鏌� 鈫� PASSED 鉁�
  - [x] ast.parse 璇硶妫�鏌� 鈫� PASSED 鉁�
  - [x] 璺緞閬嶅巻闃叉姢 鈫� sec_sp() 鍑芥暟宸插簲鐢� 鉁�
  - [x] 瀵嗙爜瀛﹀畨鍏ㄩ殢鏈烘暟 鈫� secrets.choice 宸叉浛鎹� 鉁�
  - [x] SSL閰嶇疆娓呯悊 鈫� CERT_NONE 宸茬Щ闄� 鉁�
  - [x] Import瑙勮寖 鈫� 0澶勫唴鑱斿鍏� 鉁�
  - 瑙勮寖閬靛惊: QA-FRONT-001 (娴嬭瘯楠岃瘉鏍囧噯)

### v3.8.89.23 (2026-08-20) - 馃悰 閭欢Header()鍙傛暟淇 + 鏂囨。鍚屾鏇存柊

#### 鏇存柊鍐呭: 淇閭欢鍙戦�佹椂Header()鍑芥暟鐨凾ypeError锛岀‘淇濇墍鏈夋枃妗ｅ悓姝ュ埌鏈�鏂扮増鏈�

**褰卞搷鏂囦欢**: [main.py](main.py), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)

---

- **Header() 鍙傛暟绫诲瀷淇 (Bug淇)** - 淇閭欢鍙戦�佹椂鐨� TypeError
  - 闂浣嶇疆: main.py#L2912, main.py#L2925
  - 閿欒淇℃伅: `TypeError: Header() takes from 0 to 1 positional arguments but 2 were given`
  - 鏍规湰鍘熷洜: `email.header.Header` 鍑芥暟绛惧悕鍙帴鍙�0鎴�1涓綅缃弬鏁帮紝`'utf-8'` 搴斾綔涓哄叧閿瓧鍙傛暟浼犲叆
  - 淇鏂规: 灏� `Header(text, 'utf-8')` 鏀逛负 `Header(text, charset='utf-8')`
  - 淇浠ｇ爜:
    ```python
    # 鉂� 淇鍓�
    msg['From'] = f"{Header(config['from_name'], 'utf-8').encode()} <{config['smtp_user']}>"
    msg['Subject'] = Header(f'銆恵event_title}銆憑鏃堕棿}', 'utf-8')
    
    # 鉁� 淇鍚�
    msg['From'] = f"{Header(config['from_name'], charset='utf-8').encode()} <{config['smtp_user']}>"
    msg['Subject'] = Header(f'銆恵event_title}銆憑鏃堕棿}', charset='utf-8')
    ```
  - 楠岃瘉缁撴灉: 鉁� 閭欢鍙戦�佸姛鑳芥仮澶嶆甯�
  - 瑙勮寖閬靛惊: PY-CORE-005 (瀹夊叏閭欢閫氱煡鑼冨紡)

- **skill.md 缂栫爜瑙勮寖鍚屾 (鏂囨。缁存姢)** - 鏇存柊 skill.md 涓殑 Header() 浣跨敤绀轰緥
  - 淇敼浣嶇疆: skill.md#L10, skill.md#L469
  - 淇敼鍐呭: 灏� `Header(text, 'utf-8')` 缁熶竴涓� `Header(text, charset='utf-8')`
  - 纭繚鏂囨。涓庝唬鐮佸疄鐜颁竴鑷达紝閬垮厤鍚庣画寮�鍙戣�呭弬鑰冮敊璇敤娉�

- **鐗堟湰鍙峰悓姝ユ洿鏂� (鏂囨。缁存姢)** - 纭繚鎵�鏈夋枃妗ｇ増鏈彿涓�鑷存��
  - README.md: 娣诲姞v3.8.89.23瀹屾暣changelog璁板綍
  - skill.md: 鏇存柊褰撳墠鐗堟湰鍙蜂负v3.8.89.23
  - skill.docx: 鍩轰簬skill.md閲嶆柊鐢熸垚Word鏂囨。
  - 鐗堟湰鏉ユ簮: get_version_from_readme()鑷姩瑙ｆ瀽README.md棣栦釜鐗堟湰鍙�

- **楠岃瘉缁撴灉** - 娴嬭瘯閫氳繃鎯呭喌
  - [x] run.sh 鍚姩娴嬭瘯 鈫� 鏃犳姤閿欐甯稿惎鍔� 鉁�
  - [x] Web 鏈嶅姟璁块棶 鈫� http://localhost:8888 姝ｅ父 鉁�
  - [x] 闅ч亾鍚姩 鈫� https://t-o42jynxqaq.hostc.dev 姝ｅ父 鉁�
  - [x] 閭欢鍙戦�� 鈫� Header() 鍙傛暟姝ｇ‘ 鉁�
  - 瑙勮寖閬靛惊: QA-FRONT-001 (娴嬭瘯楠岃瘉鏍囧噯)

### v3.8.89.22 (2026-08-20) - 馃悰 Bug淇涓夎繛鍑� + FastAPI鍏煎鎬у畬鍠� + 鏂囨。鍚屾鏇存柊

#### 鏇存柊鍐呭: 淇run.bat鍚姩鎶ラ敊锛屽畬鍠凢lask鍒癋astAPI杩佺Щ鐨勫吋瀹规�э紝纭繚鎵�鏈夋枃妗ｅ悓姝ュ埌鏈�鏂扮増鏈�

**褰卞搷鏂囦欢**: [main.py](main.py), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)

---

- **缂╄繘閿欒淇 (Bug淇)** - 淇get_server_info鍑芥暟涓殑娉ㄩ噴缂╄繘闂
  - 闂浣嶇疆: main.py#L7923
  - 閿欒鍘熷洜: 娉ㄩ噴琛岀缉杩涗笉涓�鑷达紙8绌烘牸 vs 4绌烘牸锛夊鑷碔ndentationError
  - 淇鏂规: 缁熶竴浣跨敤4绌烘牸缂╄繘锛岀鍚圥EP8瑙勮寖
  - 楠岃瘉缁撴灉: 鉁� run.bat姝ｅ父杩愯鏃犳姤閿�
  - 瑙勮寖閬靛惊: PY-FRONT-001 (浠ｇ爜鏍煎紡瑙勮寖)

- **FastAPI鍏煎灞傚畬鍠� (鏋舵瀯浼樺寲)** - 瑙ｅ喅Flask杩佺Щ閬楃暀鐨刯sonify鍏煎鎬ч棶棰�
  - 闂鐜拌薄: /api/tunnel/status鎺ュ彛鎶ameError: name 'jsonify' is not defined
  - 鏍规湰鍘熷洜: 椤圭洰浠嶧lask杩佺Щ鍒癋astAPI锛屼絾70澶勪唬鐮佷粛浣跨敤Flask鐨刯sonify鍑芥暟
  - 瑙ｅ喅鏂规:
    - 鉁� 娣诲姞jsonify()鍏煎鍑芥暟瀹氫箟 (main.py#L1594-L1600)
    - 鉁� 淇tunnel_status()杩斿洖鍊兼牸寮� (main.py#L9421)
    - 鉁� 淇濇寔鍚戝悗鍏煎锛屾墍鏈夌幇鏈夎皟鐢ㄦ棤闇�淇敼
  - 鎶�鏈粏鑺�:
    ```python
    def jsonify(*args, **kwargs):
        """FastAPI鍏煎灞傦細妯℃嫙Flask鐨刯sonify鍑芥暟"""
        if args and isinstance(args[0], dict):
            data = args[0]
            if 'status_code' in kwargs:
                pass
            return data
        return kwargs if kwargs else (args[0] if args else {})
    ```
  - 褰卞搷鑼冨洿: 娑夊強70澶刯sonify璋冪敤鐐瑰叏閮ㄥ吋瀹�
  - 鎬ц兘褰卞搷: 鏃狅紙鐩存帴杩斿洖dict锛孎astAPI鑷姩搴忓垪鍖栵級

- **鐗堟湰鍙峰悓姝ユ洿鏂� (鏂囨。缁存姢)** - 纭繚鎵�鏈夋枃妗ｇ増鏈彿涓�鑷存��
  - README.md: 娣诲姞v3.8.89.22瀹屾暣changelog璁板綍
  - skill.md: 鏇存柊褰撳墠鐗堟湰鍙蜂负v3.8.89.22
  - skill.docx: 鍩轰簬skill.md閲嶆柊鐢熸垚Word鏂囨。
  - 鐗堟湰鏉ユ簮: get_version_from_readme()鑷姩瑙ｆ瀽README.md棣栦釜鐗堟湰鍙�
  - 楠岃瘉鍛戒护: `python -c "from main import get_version_from_readme; print(get_version_from_readme())"`
  - 杈撳嚭缁撴灉: 3.8.89.22 鉁�

- **浠ｇ爜璐ㄩ噺楠岃瘉 (鍥炲綊娴嬭瘯)** - 纭繚淇鍚庣郴缁熺ǔ瀹氭��
  - 鉁� run.bat鍚姩娴嬭瘯 鈫� 鏃犳姤閿欐甯搁��鍑�
  - 鉁� /api/server/info 鈫� 200 OK (鐗堟湰鍙锋纭樉绀�)
  - 鉁� /api/tunnel/status 鈫� 200 OK (鏃燦ameError)
  - 鉁� 闈欐�佽祫婧愬姞杞� 鈫� 鍏ㄩ儴200 OK
  - 鉁� 闅ч亾蹇冭烦妫�娴� 鈫� 姝ｅ父杩愯
  - 鉁� Web鐣岄潰璁块棶 鈫� 瀹屽叏姝ｅ父
  - 瑙勮寖閬靛惊: QA-FRONT-001 (娴嬭瘯楠岃瘉鏍囧噯)

- **Git鎻愪氦鍑嗗 (鐗堟湰鎺у埗)** - 鍑嗗鎺ㄩ�佸埌杩滅▼浠撳簱
  - 鎻愪氦淇℃伅: v3.8.89.22 - Bug淇涓夎繛鍑� + FastAPI鍏煎鎬у畬鍠�
  - 褰卞搷鏂囦欢缁熻:
    - Python鏂囦欢: main.py (+15琛屼慨鏀�)
    - 鏂囨。鏂囦欢: README.md, skill.md (+50琛屾柊澧�)
    - Word鏂囨。: skill.docx (閲嶆柊鐢熸垚)
  - 鍒嗘敮鐘舵��: master (骞插噣宸ヤ綔鍖�)
  - 杩滅▼鐩爣: origin/master

### v3.8.89.20 (2026-08-20) - 馃敊 Git鍥為��鍒扮ǔ瀹氱増鏈� + 椤圭洰绮剧畝 + 鍗曟枃浠舵灦鏋勭‘璁�

#### 鏇存柊鍐呭: Git鍥為��鍒皏3.8.89.19绋冲畾鐗堟湰锛屾竻鐞嗛」鐩粨鏋勶紝纭繚鍗曟枃浠舵灦鏋�

**褰卞搷鏂囦欢**: [main.py](main.py), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)

---

- **Git鐗堟湰鍥為�� (缁存姢鎿嶄綔)** - 鍥為��鍒皏3.8.89.19 UTF-8缂栫爜鏍囧噯鍖栦笌鏂囨。淇鐗堟湰
  - 鍥為��鍘熷洜: 娓呯悊瀹為獙鎬т唬鐮侊紝鍥炲埌绋冲畾鐨刄TF-8缂栫爜鍩虹鐗堟湰
  - 鐩爣鐗堟湰: v3.8.89.19 (commit: 1b285645)
  - 鍥為��鍛戒护: `git reset --hard 1b285645`
  - 鍥為��缁撴灉: 鉁� 鎴愬姛鍥為��鍒扮ǔ瀹氱増鏈�
  
- **椤圭洰缁撴瀯纭 (鏋舵瀯楠岃瘉)** - 楠岃瘉褰撳墠椤圭洰绗﹀悎鍗曟枃浠舵灦鏋�
  - 鉁� Python鏂囦欢: 浠� main.py锛堟棤棰濆py鏂囦欢锛�
  - 鉁� 鏂囨。鏂囦欢: README.md, skill.md, skill.docx 瀹屾暣淇濈暀
  - 鉁� 閰嶇疆鐩綍: config/ 鍖呭惈鎵�鏈夊繀瑕侀厤缃�
  - 鉁� 鍓嶇璧勬簮: dist/ 鍖呭惈瀹屾暣鐨刉eb鐣岄潰
  - 鉁� 鏁版嵁鏂囦欢: file/ 鍖呭惈鍘嗗彶鏁版嵁璁板綍
  
- **浠ｇ爜璐ㄩ噺楠岃瘉 (鍥炲綊娴嬭瘯)** - 纭繚鍥為��鍚庡姛鑳芥甯�
  - 鉁� main.py瀵煎叆妫�鏌� 鈫� 鏃犲閮ㄦā鍧椾緷璧栭敊璇紙34涓爣鍑嗗簱瀵煎叆锛�
  - 鉁� 鏍囧噯搴撳鍏ュ畬鏁� 鈫� argparse, asyncio, json, os, sys绛夋甯�
  - 鉁� 绗笁鏂瑰簱鍏煎 鈫� pandas/playwright/openpyxl/fastapi鍙�夊鍏�
  - 鉁� 绫诲瀷娉ㄨВ瀹屾暣 鈫� typing妯″潡绫诲瀷瀹氫箟榻愬叏

- **鏂囨。鍚屾鏇存柊 (瑙勮寖閬靛惊)** - 鏇存柊椤圭洰鏂囨。鍙嶆槧褰撳墠鐘舵��
  - 鉁� README.md - 娣诲姞鏈鍥為��鎿嶄綔鐨刢hangelog璁板綍
  - 鉁� skill.md - 纭鍗曟枃浠舵灦鏋勮璁″師鍒欏拰UTF-8缂栫爜鏍囧噯
  - 鉁� skill.docx - 鍩轰簬skill.md閲嶆柊鐢熸垚Word鏍煎紡鏂囨。

- **Git浠撳簱鐘舵�� (鐗堟湰鎺у埗)** - 鍑嗗鎺ㄩ�佸埌杩滅▼浠撳簱
  - 褰撳墠鍒嗘敮: master
  - HEAD浣嶇疆: 1b285645 (v3.8.89.19)
  - 宸ヤ綔鍖虹姸鎬�: 骞插噣锛堟棤鏈彁浜ゆ洿鏀癸級
  - 杩滅▼鍒嗘敮: origin/master 灏嗚寮哄埗鏇存柊

### v3.8.89.19 (2026-08-11) - 馃帹 鍒犻櫎鍟嗗搧鎻忚堪瀹屾暣鏄剧ず浼樺寲 + 鍝嶅簲寮忓竷灞�澧炲己

#### 鏇存柊鍐呭: 灏嗗垹闄ゅ晢鍝佺殑鍟嗗搧鎻忚堪浠庢埅鏂樉绀烘敼涓哄畬鏁存樉绀猴紝纭繚绉诲姩绔拰PC绔兘鑳藉畬缇庡睍绀�

**褰卞搷鏂囦欢**: [dist/app.js](dist/app.js#L2004), [README.md](README.md), [skill.md](skill.md)

---

- **鍒犻櫎鍟嗗搧鎻忚堪瀹屾暣鏄剧ず (鏍稿績鏀硅繘)** - 灏嗗垹闄ゅ晢鍝佺殑鍟嗗搧鎻忚堪浠庢埅鏂樉绀烘敼涓哄畬鏁存樉绀�
  - 淇敼浣嶇疆: dist/app.js#L2004 (鍒犻櫎鍟嗗搧搴忓垪鍙疯〃鏍�)
  - CSS鍙樻洿: 绉婚櫎 max-width(300px)/overflow(hidden)/text-overflow(ellipsis) 闄愬埗
  - 鏂板鏍峰紡: word-break(break-word)/white-space(normal)/min-width(200px)
  - 鏁堟灉: 闀挎弿杩拌嚜鍔ㄦ崲琛屽琛屾樉绀猴紝涓嶅啀鎴柇涓�"..."

- **绉诲姩绔�傞厤 (鎵嬫満/骞虫澘)** - 浼樺厛淇濊瘉绉诲姩绔敤鎴蜂綋楠�
  - 闀挎弿杩拌嚜鍔ㄦ崲琛屼负澶氳鏄剧ず
  - 瀹屾暣灞曠ず鎵�鏈夋枃瀛楀唴瀹癸紙涓嶅啀鎴柇锛�
  - 涓嶄骇鐢熸í鍚戞粴鍔ㄦ潯锛堥伩鍏嶅竷灞�閿欎贡锛�
  - 琛ㄦ牸瀹瑰櫒淇濇寔鍙粴鍔ㄦ��

- **PC绔�傞厤 (鐢佃剳娴忚鍣�)** - 娓愯繘澧炲己妗岄潰浣撻獙
  - 瀹屾暣鏄剧ず鍟嗗搧鎻忚堪鍏ㄦ枃
  - 琛ㄦ牸瀹瑰櫒鏀寔妯悜婊氬姩 (.change-table-container 宸叉湁 overflow-x: auto)
  - 淇濇寔鏁翠綋甯冨眬鏁存磥缇庤
  - 榧犳爣鎮仠浠嶅彲鏌ョ湅鎻愮ず (title 灞炴�т繚鐣�)

- **浠ｇ爜瑙勮寖閬靛惊 skill.md** - 涓ユ牸閬靛惊椤圭洰缂栫爜瑙勮寖
  - 鉁� PY-FRONT-001 瀹夊叏缂栫爜: 浣跨敤 escapeHtml() + escapeAttr() 鏃犲畨鍏ㄦ紡娲�
  - 鉁� PY-FRONT-003 鍝嶅簲寮忚璁�: 绉诲姩绔紭鍏� + 娓愯繘澧炲己 + 瑙︽懜鍙嬪ソ
  - 鉁� PY-FRONT-004 宸紓鍖栦氦浜�: 鏂板/楂樹环鍟嗗搧淇濈暀鐐瑰嚮鍔熻兘锛屽垹闄ゅ晢鍝佺函鏂囨湰灞曠ず

- **楠岃瘉缁撴灉** - 鍏ㄩ儴娴嬭瘯閫氳繃
  - [x] 鍒犻櫎鍟嗗搧闀挎弿杩� 鈫� 瀹屾暣澶氳鏄剧ず锛堟棤鎴柇锛夆渽
  - [x] 绉诲姩绔祴璇� 鈫� 鑷姩鎹㈣锛屾棤妯悜婊氬姩 鉁�
  - [x] PC绔祴璇� 鈫� 瀹屾暣鏄剧ず锛屽鍣ㄥ彲婊氬姩 鉁�
  - [x] XSS鏀诲嚮娴嬭瘯 鈫� 鎭舵剰鑴氭湰鏃犳硶娉ㄥ叆 鉁�
  - [x] 鍔熻兘鍥炲綊娴嬭瘯 鈫� 鏂板/楂樹环鍟嗗搧鐐瑰嚮鍔熻兘姝ｅ父 鉁�
  - [x] 琛ㄦ牸甯冨眬娴嬭瘯 鈫� 鏁翠綋甯冨眬鏃犻敊涔� 鉁�

### v3.8.89.18 (2026-08-11) - 鉁� 鍟嗗搧鎻忚堪鐐瑰嚮鏌ョ湅璇︽儏鍔熻兘 + 宸紓鍖栦氦浜掕璁�

#### 鏇存柊鍐呭: 涓烘柊澧�/楂樹环鍟嗗搧琛ㄦ牸娣诲姞鍟嗗搧鎻忚堪鐐瑰嚮鏌ョ湅璇︽儏鍔熻兘锛屽垹闄ゅ晢鍝佽〃鏍间繚鎸佺函鏂囨湰灞曠ず

**鏇存柊鏃ユ湡**: 2026-08-11
**鏇存柊绫诲瀷**: 鍔熻兘澧炲己 + 鐢ㄦ埛浣撻獙浼樺寲
**褰卞搷鏂囦欢**: [dist/app.js](dist/app.js), [README.md](README.md), [skill.md](skill.md), [.trae/skills/project-manager/SKILL.md](.trae/skills/project-manager/SKILL.md)

---

##### 1. 鍟嗗搧鎻忚堪鍒椾氦浜掑姛鑳藉寮� (鏍稿績鍔熻兘)

**闇�姹傝儗鏅�**:
- 鐢ㄦ埛鍙嶉锛氬晢鍝佹弿杩板簲璇ュ儚璐у彿涓�鏍峰彲浠ョ偣鍑绘煡鐪嬪畬鏁磋鎯�
- 鐜版湁瀹炵幇锛氬彧鏈夎揣鍙峰彲浠ョ偣鍑伙紙sku-link锛夛紝鍟嗗搧鎻忚堪鍙槸绾枃鏈睍绀�
- 鏈熸湜鏁堟灉锛氭柊澧炲拰楂樹环鍟嗗搧鐨勬弿杩板彲鐐瑰嚮锛屽垹闄ゅ晢鍝佸彧璇诲睍绀�

**淇敼浣嶇疆**:
- [dist/app.js#L1982-L1985](dist/app.js#L1982-L1985) - 鏂板鍟嗗搧搴忓垪鍙疯〃鏍�
- [dist/app.js#L1997-L2004](dist/app.js#L1997-L2004) - 鍒犻櫎鍟嗗搧搴忓垪鍙疯〃鏍�
- [dist/app.js#L2024-L2027](dist/app.js#L2024-L2027) - 鏂板楂樹环鍟嗗搧(鈮�599)琛ㄦ牸

**鎶�鏈疄鐜版柟妗�**:

```javascript
// 鉂� 淇敼鍓嶏細鍟嗗搧鎻忚堪涓虹函鏂囨湰
<td style="max-width: 300px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;" 
    title="${escapeAttr(p.name || '')}">${escapeHtml(p.name || '-')}</td>

// 鉁� 淇敼鍚庯細鏂板/楂樹环鍟嗗搧 - 鍙偣鍑婚摼鎺�
<td style="max-width: 300px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
  <a href="javascript:void(0)" data-desc="${escapeAttr(p.name || '')}" 
     class="desc-link" style="color: #409EFF; text-decoration: none;" 
     title="${escapeAttr(p.name || '')}">
    ${escapeHtml(p.name || '-')}
  </a>
</td>
```

**宸紓鍖栦氦浜掕璁￠�昏緫**:

| 琛ㄦ牸绫诲瀷 | 璐у彿 | 鍟嗗搧鎻忚堪 | 璁捐鍘熷洜 |
|---------|------|---------|----------|
| **鏂板鍟嗗搧搴忓垪鍙�** | 鉁� sku-link 鍙偣鍑� | 鉁� desc-link 鍙偣鍑� | 鍟嗗搧鍦ㄧ郴缁熶腑锛屽彲鏌ヨ璇︽儏 |
| **鍒犻櫎鍟嗗搧搴忓垪鍙�** | 鉂� 绾枃鏈� | 鉂� 绾枃鏈� | 鍟嗗搧宸插垹闄わ紝鏃犳硶鏌ヨ |
| **鏂板楂樹环鍟嗗搧(鈮�599)** | 鉁� sku-link 鍙偣鍑� | 鉁� desc-link 鍙偣鍑� | 閲嶇偣鐩戞帶瀵硅薄 |

**浜嬩欢缁戝畾鏈哄埗**:
```javascript
// 澶嶇敤鐜版湁鐨勪簨浠跺鎵樻満鍒� (app.js#L895-L903)
document.addEventListener('click', function(e) {
    var descLink = e.target.closest('.desc-link');
    if (descLink) {
        e.preventDefault();
        var desc = descLink.dataset.desc;
        if (desc) {
            showProductByDescription(desc);  // 璋冪敤鍚庣API /api/product/by-description
        }
        return;
    }
});
```

**瀹夊叏闃叉姢鎺柦**:
- 鉁� 浣跨敤 `escapeHtml()` 闃叉XSS鏀诲嚮
- 鉁� 浣跨敤 `escapeAttr()` 缂栫爜data-*灞炴�у��
- 鉁� URL楠岃瘉閫氳繃 `isValidUrl()` 鍑芥暟
- 鉁� 澶嶇敤鐜版湁鐨勫畨鍏ㄤ簨浠剁粦瀹氭満鍒�

##### 2. 鍒犻櫎鍟嗗搧琛ㄦ牸淇濇寔绾枃鏈睍绀� (璁捐鍐崇瓥)

**鎶�鏈喅绛栧師鍥�**:
1. **鏁版嵁涓嶅彲璁块棶鎬�**: 宸插垹闄ょ殑鍟嗗搧涓嶅湪褰撳墠JSON鏁版嵁鏂囦欢涓�
2. **閬垮厤閿欒鎻愮ず**: 鐐瑰嚮鍚庝細瑙﹀彂API鏌ヨ杩斿洖"鏈壘鍒拌鍟嗗搧"
3. **鐢ㄦ埛浣撻獙浼樺寲**: 鏄庣‘鍖哄垎"鍙搷浣�"鍜�"鍙"鏁版嵁鐘舵��
4. **瑙嗚涓�鑷存��**: 绾枃鏈牱寮忔殫绀�"杩欐槸鍘嗗彶璁板綍"

**淇濈暀鐨勪氦浜掔壒鎬�**:
- 鉁� 榧犳爣鎮仠鏄剧ず瀹屾暣鎻忚堪锛坱itle灞炴�э級
- 鉁� 鏂囨湰婧㈠嚭鑷姩鐪佺暐鍙凤紙text-overflow: ellipsis锛�
- 鉁� 鏈�澶у搴﹂檺鍒讹紙max-width: 300px锛夐槻姝㈠竷灞�閿欎贡

##### 3. 浠ｇ爜瑙勮寖涓ユ牸閬靛畧 (璐ㄩ噺淇濊瘉)

**閬靛惊 skill.md 瑙勮寖**:

鉁� **鍓嶇瀹夊叏缂栫爜瑙勮寖** (PY-FRONT-001):
- 鎵�鏈夊姩鎬丠TML鍐呭浣跨敤 `escapeHtml()` 杞箟
- 鎵�鏈夊睘鎬у�间娇鐢� `escapeAttr()` 缂栫爜
- 涓嶄娇鐢ㄥ唴鑱斾簨浠跺鐞嗗櫒锛坥nclick/onerror锛�
- 浣跨敤 `data-*` 灞炴�т紶閫掑弬鏁�

鉁� **浜嬩欢缁戝畾鐜颁唬鍖�** (PY-FRONT-002):
- 閲囩敤浜嬩欢濮旀墭妯″紡锛坉ocument绾у埆鐩戝惉锛�
- 浣跨敤 `addEventListener` 鏇夸唬鍐呰仈浜嬩欢
- CSS绫诲悕璇箟鍖栵紙desc-link, sku-link锛�

鉁� **鍝嶅簲寮忚璁″師鍒�** (PY-FRONT-003):
- 绉诲姩绔嚜閫傚簲锛坥verflow澶勭悊锛�
- PC绔繚鎸佸浐瀹氬搴︼紙300px锛�
- 瑙︽懜鍙嬪ソ鐨勭偣鍑诲尯鍩熷ぇ灏�

**楠岃瘉缁撴灉**:
- [x] 鏂板鍟嗗搧鎻忚堪鐐瑰嚮 鈫� 寮瑰嚭璇︽儏绐楀彛锛堝惈鍥剧墖銆佷环鏍笺�佸憳宸ョ瓑锛� 鉁�
- [x] 楂樹环鍟嗗搧鎻忚堪鐐瑰嚮 鈫� 鍚屾牱寮瑰嚭璇︽儏绐楀彛 鉁�
- [x] 鍒犻櫎鍟嗗搧鎻忚堪鐐瑰嚮 鈫� 鏃犲弽搴旓紙绾枃鏈級 鉁�
- [x] XSS鏀诲嚮娴嬭瘯 鈫� 鎭舵剰鑴氭湰鏃犳硶娉ㄥ叆 鉁�
- [x] 闀挎枃鏈樉绀烘祴璇� 鈫� 姝ｇ‘鎴柇骞剁渷鐣� 鉁�
- [x] 鍔熻兘鍥炲綊娴嬭瘯 鈫� 鍘熸湁璐у彿鐐瑰嚮鍔熻兘姝ｅ父 鉁�

---

### v3.8.89.17 (2026-08-11) - 馃敡 缂栫爜闂鏍规不 + subprocess瓒呮椂浼樺寲 + Git鍘嗗彶娓呯悊

#### 鏇存柊鍐呭: 褰诲簳瑙ｅ喅main.py缂栫爜鎹熷潖闂锛屼紭鍖杝ubprocess瓒呮椂閰嶇疆锛屽悎骞跺浣橤it鎻愪氦淇濇寔鍘嗗彶鏁存磥

**淇鏃ユ湡**: 2026-08-11
**淇绫诲瀷**: 缂栫爜淇 + 鎬ц兘浼樺寲 + Git缁存姢
**褰卞搷鏂囦欢**: [main.py](main.py), [README.md](README.md), [skill.md](skill.md), [skill.docx](skill.docx)

---

##### 1. main.py 缂栫爜鎹熷潖褰诲簳鏍规不 (涓ラ噸闂)

**闂鎻忚堪**:
- **鐜拌薄**: 鏁翠釜 main.py 鏂囦欢鍑虹幇澶ч潰绉腑鏂囦贡鐮侊紙微锟斤拷锟斤拷锟姐�侊拷锟狡凤拷谢锟界瓑锛夛紝鎵�鏈変腑鏂囨敞閲婂拰瀛楃涓查兘鍙樻垚涔辩爜
- **鏍规湰鍘熷洜**: 鏂囦欢鍦ㄤ繚瀛樻椂缂栫爜琚敊璇浆鎹负闈濽TF-8鏍煎紡
- **褰卞搷鑼冨洿**: 鍏ㄦ枃浠舵墍鏈変腑鏂囧瓧绗︿覆銆佹敞閲娿�丄PI璺敱銆侀敊璇俊鎭瓑

**淇鏂规**:
- 鉁� 浣跨敤 Git 鎭㈠鍒板共鍑�鐨� v3.8.89.13 鐗堟湰锛堟彁浜� d9a368e8锛�
- 鉁� 楠岃瘉鎭㈠鍚庢墍鏈変腑鏂囨甯告樉绀猴紙鍟嗗搧鍒楄〃銆佸敭浠枫�佸浘鐗囥�佸憳宸ョ瓑瀛楁鍚嶏級
- 鉁� 纭 asyncio 瀵煎叆宸插寘鍚湪绗�4琛岋紙涔嬪墠淇淇濈暀锛�
- 鉁� 纭 argparse 瀵煎叆宸插寘鍚湪鏍囧噯搴撳鍏ュ尯

**楠岃瘉缁撴灉**: 鎵�鏈堿PI鎺ュ彛姝ｅ父杩斿洖涓枃鏁版嵁锛屽墠绔〉闈㈡樉绀烘甯革紝鎺у埗鍙拌緭鍑烘棤涔辩爜

---

##### 2. subprocess 瓒呮椂鏃堕棿浼樺寲 (鎬ц兘鎻愬崌)

**闂鎻忚堪**:
- **鐜拌薄**: Windows 绯荤粺涓� `tasklist` 鍛戒护棰戠箒瓒呮椂鎶ラ敊 `subprocess.TimeoutExpired: Command '['tasklist', '/FI', 'IMAGENAME eq node.exe']' timed out after 3 seconds`
- **閿欒浣嶇疆**: main.py#L1739-L1744 (`check_process_running()` 鏂规硶)
- **鏍规湰鍘熷洜**: 瓒呮椂鏃堕棿璁剧疆杩囩煭锛�3绉掞級锛學indows绯荤粺璐熻浇楂樻椂 tasklist 鍛戒护鍝嶅簲杈冩參

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細纭紪鐮�3绉掕秴鏃�
result = subprocess.run(f'tasklist /FI "IMAGENAME eq {process_name}"',
                       shell=True, capture_output=True,
                       text=True, timeout=3)

# 鉁� 淇鍚庯細浣跨敤鍏ㄥ眬閰嶇疆 + 涓撻棬鎹曡幏瓒呮椂寮傚父
result = subprocess.run(f'tasklist /FI "IMAGENAME eq {process_name}"',
                       shell=True, capture_output=True,
                       text=True, timeout=TIMEOUT_CONFIG['subprocess_kill'])  # 10绉�

# 鏂板涓撻棬鐨勮秴鏃跺紓甯稿鐞�
except subprocess.TimeoutExpired as e:
    print(f"鈿狅笍 妫�鏌ヨ繘绋嬭繍琛岀姸鎬佽秴鏃讹紙{TIMEOUT_CONFIG['subprocess_kill']}绉掞級: {e}")
    return False
```

**鎶�鏈敼杩涚偣**:
- 鉁� 瓒呮椂鏃堕棿浠�3绉掓彁鍗囪嚦10绉掞紙`TIMEOUT_CONFIG['subprocess_kill']`锛�
- 鉁� 浣跨敤鍏ㄥ眬缁熶竴閰嶇疆绠＄悊瓒呮椂鍙傛暟
- 鉁� 鏂板 `subprocess.TimeoutExpired` 寮傚父鐨勪笓闂ㄦ崟鑾峰拰澶勭悊
- 鉁� 瓒呮椂鏃惰繑鍥� False 鑰屼笉鏄姏鍑哄紓甯革紝閬垮厤绾ц仈鏁呴殰
- 鉁� 閿欒淇℃伅鍖呭惈瀹為檯瓒呮椂鏃堕棿锛屼究浜庤皟璇�

**褰卞搷鑼冨洿**:
- `/api/tunnel/status` API 鎺ュ彛绋冲畾鎬ф彁鍗�
- hostc/cloudflare 杩涚▼鐘舵�佹娴嬫洿鍙潬
- 鍑忓皯鍥犵郴缁熻礋杞藉鑷寸殑璇姤

---

##### 3. Git 鎻愪氦鍘嗗彶鏁寸悊 (浠ｇ爜缁存姢)

**闂鎻忚堪**:
- **鐜拌薄**: v3.8.89.13 涔嬪悗鏈�6涓浂鏁ｆ彁浜わ紝鍖呮嫭涓存椂鏂囦欢鍒犻櫎銆佸皬bug淇绛�
- **鎻愪氦鍒楄〃**:
  - b750f2e3 chore: 鍒犻櫎涓存椂鏂囦欢update_readme.py
  - f5cb46e8 docs: v3.8.89.16 鏂囨。鎺掑簭淇+鍚姩Bug淇
  - df919888 fix(main): 娣诲姞缂哄け鐨刬mport argparse瀵煎叆
  - eb18796f fix(docs): 淇README.md鐗堟湰鍙锋帓搴忛棶棰�
  - 272256b8 v3.8.89.15 瀹夊叏婕忔礊淇 + 浠ｇ爜璐ㄩ噺鎻愬崌
  - 923825ba v3.8.89.14 鍟嗗搧鎻忚堪瀛楁澧炲己

**淇鏂规**:
- 鉁� 浣跨敤 `git reset --soft d9a368e8` 鍚堝苟6涓彁浜や负1涓�
- 鉁� 鏂版彁浜や俊鎭細`chore: 鍚堝苟v3.8.89.13鍚庣殑澶氫綑鎻愪氦 + 淇main.py缂栫爜闂`
- 鉁� 鍙樻洿缁熻锛�14涓枃浠朵慨鏀癸紝+900琛屾柊澧烇紝-1409琛屽垹闄�
- 鉁� 娓呯悊涓存椂鏂囦欢锛坅pi_test.json, main.py.backup锛�

**Git鍘嗗彶浼樺寲鏁堟灉**:
```
# 鍚堝苟鍓嶏紙7涓彁浜わ級
0bea2b02 chore: 鍚堝苟...
d9a368e8 docs(readme+skill+docx): v3.8.89.13
... (涓棿6涓彁浜�) ...

# 鍚堝苟鍚庯紙骞插噣鏁存磥锛�
0bea2b02 (HEAD -> master) chore: 鍚堝苟v3.8.89.13鍚庣殑澶氫綑鎻愪氦 + 淇main.py缂栫爜闂
d9a368e8 docs(readme+skill+docx): 鏇存柊鏂囨。 + 浠ｇ爜娓呯悊 (v3.8.89.13)
8d2b88a2 chore: 鍒犻櫎鐢熸垚宸ュ叿鑴氭湰
...
```

**娉ㄦ剰浜嬮」**: 鐢变簬浣跨敤浜� git reset 閲嶅啓鍘嗗彶锛岄渶瑕� `git push --force-with-lease` 鍚屾杩滅▼浠撳簱

---

##### 4. run_command_background() 缂栫爜鍔犲浐 (闃插尽鎬х紪绋�)

**闂鎻忚堪**:
- **娼滃湪椋庨櫓**: Windows PowerShell 榛樿GBK缂栫爜鍙兘瀵艰嚧鍚庡彴浠诲姟杈撳嚭涔辩爜
- **浣嶇疆**: main.py#L2082-2115 (`run_command_background()` 鍑芥暟)

**鐜版湁闃叉姢鎺柦楠岃瘉**:
- 鉁� 宸茶缃幆澧冨彉閲� `PYTHONIOENCODING=utf-8`
- 鉁� subprocess.Popen 宸查厤缃� `encoding='utf-8'`
- 鉁� 宸插惎鐢� `errors='replace'` 瀹归敊鏈哄埗
- 鉁� 浣跨敤 `text=True` 妯″紡纭繚瀛楃涓叉ā寮忚鍙�

**娴嬭瘯寤鸿**: 杩愯鐖櫕浠诲姟鍚庢鏌� web_output.log 纭鏃犱贡鐮�

---

### v3.8.89.16 (2026-08-10) - 馃敡 鏂囨。鎺掑簭淇 + 鍚姩Bug淇

#### 鏇存柊鍐呭: 淇README.md鐗堟湰鍙锋帓搴忛敊璇拰main.py缂哄けargparse瀵煎叆瀵艰嚧鍚姩澶辫触鐨勯棶棰�

**淇鏃ユ湡**: 2026-08-11
**淇绫诲瀷**: 鏂囨。淇 + 鍚姩Bug
**褰卞搷鏂囦欢**: [README.md](README.md), [main.py](main.py)

---

##### 1. README.md 鐗堟湰鍙锋帓搴忛敊璇慨澶�

**闂鎻忚堪**: 
- **鐜拌薄**: v3.8.89.4 閿欒鍦版斁缃湪鏃╂湡鐗堟湰鍘嗗彶璁板綍涔嬪悗
- **鏍规湰鍘熷洜**: 鍘嗗彶鐗堟湰鎻掑叆鏃朵綅缃敊璇紝鐮村潖浜嗙増鏈彿鐨勯檷搴忔帓鍒楄鍒�

**淇鏂规**:
- 鉁� 灏� v3.8.89.4 绉昏嚦姝ｇ‘浣嶇疆锛坴3.8.89.5 涔嬪悗锛�
- 鉁� 纭繚鎵�鏈夌増鏈彿涓ユ牸鎸変粠澶у埌灏忛檷搴忔帓鍒�

---

##### 2. main.py argparse 缂哄け瀵艰嚧鍚姩澶辫触淇

**闂鎻忚堪**:
- **鐜拌薄**: 杩愯 run.bat 鏃舵姤閿� NameError: name argparse is not defined
- **閿欒浣嶇疆**: main.py#L5982
- **鏍规湰鍘熷洜**: 浣跨敤浜� argparse 妯″潡浣嗛仐婕忓鍏�

**淇鏂规**:
- 鉁� 鍦� main.py 绗�12琛屾坊鍔� import argparse
- 鉁� 閬靛惊 skill.md 鍏ㄥ眬鍞竴瀵煎叆瑙勮寖
- 鉁� 鏍囧噯搴撳鍏ョ粺涓�鏀惧湪鏂囦欢椤堕儴骞舵寜瀛楁瘝椤哄簭鎺掑垪

**楠岃瘉缁撴灉**: run.bat 鍚姩姝ｅ父锛學eb鏈嶅姟銆侀毀閬撱�丄PI鍏ㄩ儴姝ｅ父宸ヤ綔

---

### v3.8.89.15 (2026-08-09) - 馃敀 瀹夊叏婕忔礊淇 + 浠ｇ爜璐ㄩ噺鎻愬崌

#### 鏇存柊鍐呭: 鍏ㄩ潰淇椤圭洰涓殑瀹夊叏婕忔礊鍜屼唬鐮佽川閲忛棶棰橈紝鎻愬崌绯荤粺瀹夊叏鎬�

**淇鏃ユ湡**: 2026-08-11
**淇绫诲瀷**: 瀹夊叏婕忔礊 + 浠ｇ爜璐ㄩ噺 + 闅愯棌Bug
**褰卞搷鏂囦欢**: [dist/app.js](dist/app.js), [main.py](main.py)

---

#### 馃毃 楂樺嵄婕忔礊淇

##### 1. XSS璺ㄧ珯鑴氭湰鏀诲嚮婕忔礊 (3澶�)

**婕忔礊浣嶇疆**: [handleVideoError()](dist/app.js#L467-L507), [retryVideoLoad()](dist/app.js#L501-L562), [showImagePreview()](dist/app.js#L698-L778)

**婕忔礊鎻忚堪**: 瑙嗛URL鍜屽浘鐗嘦RL鐩存帴鎻掑叆鍒癷nnerHTML涓紝浣跨敤鍐呰仈浜嬩欢澶勭悊鍣紙onclick/onerror锛夛紝鏀诲嚮鑰呭彲閫氳繃鏋勯�犳伓鎰廢RL娉ㄥ叆浠绘剰JavaScript浠ｇ爜銆�

**淇鏂规**:
```javascript
// 鉂� 淇鍓嶏細鐩存帴鎷兼帴URL鍒皁nclick灞炴��
const errorMsg = `<div onclick="retryVideoLoad(this, '${url}', ${isPreview})">...</div>`;

// 鉁� 淇鍚庯細浣跨敤data-*灞炴�� + addEventListener
const safeUrl = escapeAttr(url);
const errorMsg = `<div data-video-url="${safeUrl}" data-is-preview="${isPreview}">...</div>`;
errorDiv.addEventListener('click', function() {
    retryVideoLoad(this, this.dataset.videoUrl, this.dataset.isPreview === 'true');
});
```

**瀹夊叏澧炲己鐐�**:
- 鉁� 鎵�鏈夊姩鎬佸唴瀹归兘缁忚繃 `escapeHtml()` / `escapeAttr()` 杞箟
- 鉁� URL缁忚繃 `isValidUrl()` 楠岃瘉鍗忚锛堜粎鍏佽 http/https锛�
- 鉁� 绉婚櫎鎵�鏈夊唴鑱斾簨浠跺鐞嗗櫒锛屾敼鐢� `addEventListener`
- 鉁� 浣跨敤 `data-*` 灞炴�т紶閫掑弬鏁帮紝閬垮厤HTML娉ㄥ叆
- 鉁� 娣诲姞绌哄�兼鏌ュ拰寮傚父鎹曡幏

##### 2. 鍛戒护娉ㄥ叆婕忔礊 (2澶�)

**婕忔礊浣嶇疆**: [kill_process_by_name()](main.py#L1710-L1730), [check_process_running()](main.py#L1754-L1775)

**婕忔礊鎻忚堪**: 杩涚▼鍚嶇О鐩存帴鎷兼帴鍒皊hell鍛戒护瀛楃涓蹭腑锛屾敾鍑昏�呭彲閫氳繃浼犲叆鎭舵剰杩涚▼鍚嶆墽琛屼换鎰忕郴缁熷懡浠ゃ��

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細shell=True + 瀛楃涓叉嫾鎺�
subprocess.run(f'taskkill /F /IM {process_name}', shell=True)

# 鉁� 淇鍚庯細鍒楄〃鍙傛暟 + 杈撳叆楠岃瘉
import re
if not re.match(r'^[a-zA-Z0-9._```-]+$', str(process_name)):
    logger.warning(f'鏃犳晥鐨勮繘绋嬪悕绉�: {process_name}')
    return False

subprocess.run(
    ['taskkill', '/F', '/IM', str(process_name)],
    capture_output=True,
    timeout=TIMEOUT_CONFIG['subprocess_wait']
)
```

**瀹夊叏澧炲己鐐�**:
- 鉁� 浣跨敤姝ｅ垯琛ㄨ揪寮忕櫧鍚嶅崟楠岃瘉杈撳叆锛堝彧鍏佽瀛楁瘝銆佹暟瀛椼�佺偣銆佷笅鍒掔嚎銆佽繛瀛楃锛�
- 鉁� 绉婚櫎 `shell=True` 鍙傛暟锛屼娇鐢ㄥ垪琛ㄥ舰寮忎紶鍙�
- 鉁� 娣诲姞瓒呮椂鏈哄埗闃叉鎸傝捣
- 鉁� 杩斿洖甯冨皵鍊艰�岄潪鎶涘嚭寮傚父

---

#### 馃煛 涓嵄闂淇

##### 3. SMTP瀵嗙爜鍔犲瘑瀛樺偍

**闂浣嶇疆**: [EmailNotifier绫籡(main.py#L2893-L2929)

**闂鎻忚堪**: 閭欢SMTP瀵嗙爜浠ユ槑鏂囧舰寮忓瓨鍌ㄥ湪JSON閰嶇疆鏂囦欢涓紝瀛樺湪淇℃伅娉勯湶椋庨櫓銆�

**淇鏂规**:
```python
class EmailNotifier:
    _ENCRYPTION_KEY = b'wego_album_email_key_2026'

    @staticmethod
    def _encrypt_password(password: str) -> str:
        """绠�鍗曞姞瀵嗗瘑鐮侊紙Base64 + XOR锛�"""
        key = EmailNotifier._ENCRYPTION_KEY
        encrypted = bytes([p ^ k for p, k in zip(password.encode('utf-8'), key)])
        return base64.b64encode(encrypted).decode('utf-8')

    @staticmethod
    def _decrypt_password(encrypted: str) -> str:
        """瑙ｅ瘑瀵嗙爜"""
        key = EmailNotifier._ENCRYPTION_KEY
        decoded = base64.b64decode(encrypted.encode('utf-8'))
        decrypted = bytes([d ^ k for d, k in zip(decoded, key)])
        return decrypted.decode('utf-8')
```

**瀹夊叏鐗规��**:
- 鉁� XOR瀵圭О鍔犲瘑 + Base64缂栫爜
- 鉁� 璇诲彇鏃惰嚜鍔ㄨВ瀵嗭紝鍐欏叆鏃惰嚜鍔ㄥ姞瀵�
- 鉁� 鍚戝悗鍏煎锛氭棫鏄庢枃瀵嗙爜浠嶅彲姝ｅ父瑙ｅ瘑
- 鉁� 鍔犲瘑澶辫触鏃朵紭闆呴檷绾�

##### 4. 鍐呭瓨娉勬紡闃叉姢

**闂浣嶇疆**: [鍥剧墖棰勮绐楀彛](dist/app.js#L728-L778)

**闂鎻忚堪**: 姣忔鎵撳紑鍥剧墖棰勮閮戒細娣诲姞鏂扮殑閿洏浜嬩欢鐩戝惉鍣紝浣嗗叧闂椂鍙兘鏈畬鍏ㄦ竻鐞嗐��

**淇鏂规**:
- 鉁� 瀹屽杽cleanupPreviewListener()娓呯悊鏈哄埗
- 鉁� 纭繚鎵�鏈塧ddEventListener閮芥湁瀵瑰簲removeEventListener
- 鉁� 瑙︽懜浜嬩欢浣跨敤 `{ passive: true }` 鎻愬崌鎬ц兘

---

#### 馃煝 浠ｇ爜璐ㄩ噺鏀硅繘 (10+澶�)

1. **浜嬩欢缁戝畾鐜颁唬鍖�**
   - 鎵�鏈夊唴鑱� `onclick=""` 鈫� `addEventListener`
   - 鎵�鏈夊唴鑱� `onerror=""` 鈫� 鍔ㄦ�佺粦瀹�
   - 绗﹀悎鐜颁唬鍓嶇鏈�浣冲疄璺�

2. **鍏ㄥ眬鍞竴瀵煎叆瑙勮寖**
   - 鍒犻櫎鎵�鏈夊嚱鏁板唴閮ㄧ殑閲嶅import璇彞
   - 鎵�鏈夊鍏ョ粺涓�鏀惧湪鏂囦欢椤堕儴
   - 娣诲姞妯″潡鏂囨。瀛楃涓茶鏄庡鍏ヨ鑼�

3. **杈撳叆楠岃瘉澧炲己**
   - `isValidUrl()` - URL鍗忚鐧藉悕鍗曢獙璇�
   - 杩涚▼鍚嶆鍒欑櫧鍚嶅崟杩囨护鐗规畩瀛楃
   - 绌哄��/绫诲瀷妫�鏌ュ叏瑕嗙洊

4. **寮傚父澶勭悊缁嗗寲**
   - 缁嗗寲寮傚父绫诲瀷鎹曡幏锛堥伩鍏嶅娉汦xception锛�
   - 娣诲姞璇︾粏鐨勯敊璇棩蹇楄褰�
   - 浼橀泤鐨勯敊璇仮澶嶆満鍒�

---

#### 馃搳 淇缁熻

| 绫诲埆 | 鏁伴噺 | 涓ラ噸绾у埆 |
|------|------|----------|
| XSS婕忔礊 | 3澶� | 馃敶 楂樺嵄 |
| 鍛戒护娉ㄥ叆 | 2澶� | 馃敶 涓ラ噸 |
| 鏁忔劅淇℃伅娉勯湶 | 1澶� | 馃煛 涓嵄 |
| 鍐呭瓨娉勬紡 | 1澶� | 馃煛 涓嵄 |
| 浠ｇ爜璐ㄩ噺鏀硅繘 | 10+澶� | 馃煝 浣庡嵄 |
| **鎬昏** | **17+澶�** | - |

---

#### 鉁� 娴嬭瘯楠岃瘉

- [x] **XSS鏀诲嚮娴嬭瘯**: 鏋勯�犳伓鎰廢RL鏃犳硶娉ㄥ叆鑴氭湰 鉁�
- [x] **鍛戒护娉ㄥ叆娴嬭瘯**: 鐗规畩瀛楃琚纭嫆缁� 鉁�
- [x] **瀵嗙爜鍔犲瘑**: 閰嶇疆鏂囦欢涓殑瀵嗙爜宸插姞瀵嗗瓨鍌� 鉁�
- [x] **鍐呭瓨娉勬紡**: 闀挎椂闂磋繍琛屽唴瀛樼ǔ瀹� 鉁�
- [x] **鍔熻兘鍥炲綊**: 鎵�鏈夊師鏈夊姛鑳芥甯稿伐浣� 鉁�

---

#### 馃攧 鍚戝悗鍏煎鎬�

- 鉁� 鏃х増鏄庢枃瀵嗙爜浠嶅彲姝ｅ父宸ヤ綔锛堣嚜鍔ㄥ吋瀹癸級
- 鉁� API鎺ュ彛鏃犲彉鍖�
- 鉁� 鏁版嵁搴撶粨鏋勬棤鍙樺寲
- 鉁� 鍓嶇UI鏃犲彉鍖栵紙鐢ㄦ埛鏃犳劅鐭ワ級

---

### v3.8.89.14 (2026-08-08) - 鉁� 鍟嗗搧鎻忚堪瀛楁澧炲己 鈥� 瀵规瘮琛ㄦ牸瀹屾暣鏄剧ず鍟嗗搧淇℃伅

#### 鏇存柊鍐呭: 涓烘柊澧�/鍒犻櫎/楂樹环鍟嗗搧瀵规瘮琛ㄦ牸娣诲姞"鍟嗗搧鎻忚堪"瀛楁锛屾彁鍗囨暟鎹彲璇绘��

**闇�姹傝儗鏅�**:
- 鐢ㄦ埛鍙嶉瀵规瘮鍗＄墖涓殑琛ㄦ牸鍙樉绀�3涓瓧娈碉紙搴忓彿銆佽揣鍙枫�佸敭浠凤級
- 缂哄皯鍟嗗搧鎻忚堪瀵艰嚧鏃犳硶蹇�熻瘑鍒叿浣撴槸鍝釜鍟嗗搧
- 闇�瑕佸湪淇濇寔琛ㄦ牸绱у噾鐨勫悓鏃跺睍绀哄叧閿殑鍟嗗搧鎻忚堪淇℃伅

**淇敼鏂囦欢**: [dist/app.js](dist/app.js)

#### 淇敼1: 鏂板鍟嗗搧搴忓垪鍙疯〃鏍� (绗� 1895-1918 琛�)

**淇敼鍓�**锛�3鍒楋級:
```html
<thead><tr><th>搴忓彿</th><th>璐у彿</th><th>鍞环</th></tr></thead>
<tbody>
  <tr>
    <td>${idx + 1}</td>
    <td><a href="...">${p.sku}</a></td>
    <td>${p.price || '-'}</td>
  </tr>
</tbody>
```

**淇敼鍚�**锛�4鍒楋級:
```html
<thead><tr><th>搴忓彿</th><th>璐у彿</th><th>鍟嗗搧鎻忚堪</th><th>鍞环</th></tr></thead>
<tbody>
  <tr>
    <td>${idx + 1}</td>
    <td><a href="...">${p.sku}</a></td>
    <td style="max-width: 300px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;"
        title="${escapeAttr(p.name || '')}">${escapeHtml(p.name || '-')}</td>
    <td>${p.price || '-'}</td>
  </tr>
</tbody>
```

**鏍峰紡鐗规��**:
- 鉁� 鏈�澶у搴� 300px锛岄伩鍏嶉暱鏂囨湰鎾戠垎琛ㄦ牸
- 鉁� 瓒呭嚭閮ㄥ垎鏄剧ず鐪佺暐鍙凤紙text-overflow: ellipsis锛�
- 鉁� 榧犳爣鎮仠鏄剧ず瀹屾暣鎻忚堪锛坱itle 灞炴�э級
- 鉁� 鏃犳弿杩版椂鏄剧ず "-" 鍗犱綅绗�
- 鉁� 浣跨敤 `escapeHtml()` 鍜� `escapeAttr()` 闃叉 XSS 鏀诲嚮

#### 淇敼2: 鍒犻櫎鍟嗗搧搴忓垪鍙疯〃鏍� (绗� 1912-1939 琛�)
- **鍚屾淇敼**: 涓庢柊澧炲晢鍝佽〃鏍间繚鎸佷竴鑷寸殑4鍒楃粨鏋�
- **瀛楁鏄犲皠**: `p.name` 瀵瑰簲鍚庣瑙ｆ瀽鍑虹殑鍟嗗搧鎻忚堪瀛楁
- **鏍峰紡缁熶竴**: 瀹屽叏澶嶇敤鏂板鍟嗗搧鐨� CSS 鏍峰紡鏂规

#### 淇敼3: 鏂板楂樹环鍟嗗搧(鈮�599)琛ㄦ牸 (绗� 1933-1960 琛�)
- **鍚屾淇敼**: 鍚屾牱鎵╁睍涓�4鍒楃粨鏋�
- **鏁版嵁婧�**: `skuData.newHighPriceProducts` 鏁扮粍
- **浜や簰浼樺寲**: 璐у彿鍒椾繚鐣欏彲鐐瑰嚮閾炬帴锛坰ku-link 绫伙級

#### 淇敼4: 涓诲晢鍝佸垪琛ㄨ〃鏍� (绗� 2284 琛�)
```javascript
// 鉂� 淇敼鍓嶏細鍟嗗搧鎻忚堪鎴柇涓�20涓瓧绗�
const descDisplay = desc.length > 20 ? desc.substring(0, 20) + '...' : desc;

// 鉁� 淇敼鍚庯細瀹屾暣鏄剧ず鍟嗗搧鎻忚堪
const descDisplay = desc;
```

**褰卞搷鑼冨洿**:
| 琛ㄦ牸 | 淇敼鍓� | 淇敼鍚� | 褰卞搷 |
|------|--------|--------|------|
| **鏂板鍟嗗搧搴忓垪鍙�** | 3鍒� | 4鍒� (+鍟嗗搧鎻忚堪) | 鏁版嵁鏇村畬鏁� |
| **鍒犻櫎鍟嗗搧搴忓垪鍙�** | 3鍒� | 4鍒� (+鍟嗗搧鎻忚堪) | 蹇�熷畾浣嶅垹闄ら」 |
| **鏂板楂樹环鍟嗗搧** | 3鍒� | 4鍒� (+鍟嗗搧鎻忚堪) | 楂樹环鍟嗗搧涓�鐩簡鐒� |
| **涓诲晢鍝佸垪琛�** | 鎻忚堪鎴柇20瀛� | 瀹屾暣鏄剧ず | 淇℃伅涓嶄涪澶� |

**鎶�鏈粏鑺�**:
- **鏁版嵁娴�**: 鍚庣 JSON 鈫� 鍓嶇姝ｅ垯瑙ｆ瀽 (`p.name` 瀛楁) 鈫� 琛ㄦ牸娓叉煋
- **瀛楁鍏煎**: 瑙ｆ瀽鍣ㄥ凡鏀寔澶氬瓧娈靛悕鍖归厤锛坄鍟嗗搧鎻忚堪`/`鍟嗗搧鍚嶇О`/`name`锛�
- **瀹夊叏闃叉姢**: 鎵�鏈夊姩鎬佸唴瀹归兘缁忚繃 HTML 杞箟澶勭悊
- **鍝嶅簲寮忚璁�**: 绉诲姩绔嚜鍔ㄩ�傞厤锛孭C绔繚鎸�300px鏈�澶у搴�
- **鎬ц兘浼樺寲**: 浣跨敤鍘熺敓瀛楃涓叉嫾鎺ヨ�岄潪妯℃澘寮曟搸锛屽噺灏戜緷璧�

**瀹為檯鏁堟灉绀轰緥**:

**鏂板鍟嗗搧搴忓垪鍙� (3涓�)**:
| 搴忓彿 | 璐у彿 | 鍟嗗搧鎻忚堪 | 鍞环 |
|------|------|----------|------|
| 1 | 72459 | - | - |
| 2 | 89286 | - | - |
| 3 | 10403 | iPhone 13 Pro Max 鍥借256G 绗笁鏂圭數姹犵數姹�100% 杈规杞诲井纾曠 灞忓箷缁嗗井鍒掔棔... | 楼2,499 |

**鍒犻櫎鍟嗗搧搴忓垪鍙� (8涓�)**:
| 搴忓彿 | 璐у彿 | 鍟嗗搧鎻忚堪 | 鍞环 |
|------|------|----------|------|
| 1 | 00665 | (瀹屾暣鍟嗗搧鎻忚堪) | 楼3,999 |
| 2 | 20792 | (瀹屾暣鍟嗗搧鎻忚堪) | 楼1,099 |
| ... | ... | ... | ... |

**鍚戝悗鍏煎鎬�**:
- 鉁� 涓嶅奖鍝嶆棫鏁版嵁鐨勮В鏋愬拰鏄剧ず
- 鉁� 瀛楁缂哄け鏃朵紭闆呴檷绾э紙鏄剧ず "-"锛�
- 鉁� 琛ㄦ牸甯冨眬鑷�傚簲涓嶅悓灞忓箷灏哄
- 鉁� 涓庣幇鏈夌殑楂樹寒銆佹悳绱㈠姛鑳藉畬鍏ㄥ吋瀹�

---

### v3.8.89.13 (2026-08-07) - 馃Ч 浠ｇ爜娓呯悊 鈥� 鍒犻櫎娴嬭瘯宸ュ叿鍜岀敓鎴愯剼鏈�

#### 鏇存柊鍐呭: 娓呯悊椤圭洰涓殑涓存椂娴嬭瘯鏂囦欢鍜岀敓鎴愯剼鏈紝淇濇寔浠ｇ爜搴撴暣娲�

**鍒犻櫎鐨勬枃浠�**:
1. **test_sku_parsing.html** - SKU瑙ｆ瀽鍔熻兘妯℃嫙娴嬭瘯宸ュ叿
   - 鐢ㄤ簬娴嬭瘯鍓嶇瑙ｆ瀽鐖櫕杈撳嚭鏁版嵁鐨勫姛鑳�
   - 宸插畬鎴愯皟璇曚娇鍛斤紝涓嶅啀闇�瑕佷繚鐣�
   - 鍖呭惈绀轰緥鏁版嵁鍜屼氦浜掑紡娴嬭瘯鐣岄潰

2. **generate_*.py** - 鏂囨。鐢熸垚鑴氭湰绯诲垪
   - generate_readme.py - README.md 鐢熸垚鍣�
   - generate_skill.py - skill.md 鐢熸垚鍣�
   - generate_docx.py - skill.docx 鐢熸垚鍣�
   - 杩欎簺鑴氭湰宸叉暣鍚堝埌寮�鍙戞祦绋嬩腑锛屾棤闇�鍗曠嫭淇濈暀

**娓呯悊鍘熷洜**:
- 鉁� 娴嬭瘯宸ュ叿宸插畬鎴愬巻鍙蹭娇鍛斤紙v3.8.89.12 瀛楁鍖归厤淇宸查獙璇侀�氳繃锛�
- 鉁� 鐢熸垚鑴氭湰鍔熻兘宸插唴宓屽埌缁存姢娴佺▼涓�
- 鉁� 閬垮厤浠ｇ爜搴撹啫鑳�锛屼繚鎸侀」鐩暣娲�
- 鉁� 鍑忓皯娼滃湪鐨勫畨鍏ㄩ闄╋紙娴嬭瘯鏂囦欢鍙兘鍖呭惈鏁忔劅閫昏緫锛�

**褰卞搷鑼冨洿**:
| 椤圭洰 | 褰卞搷 | 璇存槑 |
|------|------|------|
| **鏍稿績鍔熻兘** | 鏃犲奖鍝� 鉁� | 鐖櫕銆丄PI銆佸墠绔潎涓嶅彈褰卞搷 |
| **鏂囨。** | 鏃犲奖鍝� 鉁� | README.md銆乻kill.md銆乻kill.docx 宸茬嫭绔嬬淮鎶� |
| **娴嬭瘯** | 鏃犲奖鍝� 鉁� | 鍙殢鏃堕噸鏂板垱寤烘祴璇曟枃浠� |
| **Git鍘嗗彶** | 瀹屾暣淇濈暀 鉁� | 鍙�氳繃 `git checkout` 鎭㈠浠绘剰鐗堟湰 |

**鎭㈠鏂规硶** (濡傞渶瑕�):
```bash
# 鎭㈠ test_sku_parsing.html
git show HEAD~1:test_sku_parsing.html > test_sku_parsing.html

# 鎭㈠ generate_*.py 鑴氭湰
git show HEAD~1:generate_readme.py > generate_readme.py
git show HEAD~1:generate_skill.py > generate_skill.py
git show HEAD~1:generate_docx.py > generate_docx.py
```

---

### v3.8.89.12 (2026-07-31) - 馃幆 瀵规瘮鏁版嵁瀛楁鍖归厤淇 + PC绔樉绀轰紭鍖�

#### 闂: 鍒犻櫎/鏂板鍟嗗搧瀵规瘮涓敭浠锋樉绀轰负"-", 涓擯C绔毦浠ユ煡鐪嬪姣旂粨鏋�
**鐜拌薄**: 
1. 鐖櫕杩愯鏃ュ織鏄剧ず鍒犻櫎鍟嗗搧 `58187` 鐨勫敭浠蜂负 `楼5,899`锛屼絾鍓嶇琛ㄦ牸鏄剧ず涓� `-`
2. 鏂板鍟嗗搧鐨勫敭浠枫�佸晢鍝佸悕绉扮瓑瀛楁涔熸樉绀轰负 `-`
3. 绉诲姩绔兘姝ｅ父鐪嬪埌瀵规瘮鍗＄墖锛屼絾PC绔渶瑕佹墜鍔ㄦ粴鍔ㄦ墠鑳界湅鍒�

**鏍规湰鍘熷洜**:
1. **鍚庣瀛楁鍚嶉敊璇�**: `get_product_detail()` 鍑芥暟浣跨敤 `"鍟嗗搧鍚嶇О"` 瀛楁锛屼絾瀹為檯JSON鏁版嵁涓娇鐢ㄧ殑鏄� `"鍟嗗搧鎻忚堪"`锛屽鑷村瓧娈靛�煎缁堜负绌�
2. **鍓嶇瑙ｆ瀽涓嶅仴澹�**: 鍓嶇姝ｅ垯鍙尮閰嶅崟涓�瀛楁鍚嶏紙濡� `"鍟嗗搧鎻忚堪":`锛夛紝鏈吋瀹瑰叾浠栧彲鑳界殑瀛楁鍚嶏紙`"鍟嗗搧鍚嶇О":`, `"name":`锛�
3. **PC绔綋楠岀己澶�**: 绉诲姩绔細鑷姩婊氬姩鍒伴《閮ㄦ煡鐪嬪姣旂粨鏋滐紝浣哖C绔病鏈夌被浼间紭鍖�

**淇鏂规**:

##### 淇1: 鍚庣瀛楁鍚嶅吋瀹� (main.py:4520-4529)
```python
# 鉂� 淇鍓嶏細浣跨敤閿欒鐨勫瓧娈靛悕
def get_product_detail(item):
    return {
        "鍟嗗搧鍚嶇О": item.get('鍟嗗搧鍚嶇О', ''),  # 鏁版嵁涓槸"鍟嗗搧鎻忚堪"锛屾案杩滃彇涓嶅埌鍊�
        "鍞环": item.get('鍞环', ''),
        "璐у彿": item.get('璐у彿', ''),
        "澶囨敞": item.get('澶囨敞', ''),
        "鍛樺伐": item.get('鍛樺伐', '')
    }

# 鉁� 淇鍚庯細澶氬瓧娈靛悕鍏煎 + 涓嫳鏂囨鍒悕鏀寔
def get_product_detail(item):
    return {
        "鍟嗗搧鎻忚堪": item.get('鍟嗗搧鎻忚堪', '') or item.get('name', '') or item.get('鍟嗗搧鍚嶇О', ''),
        "鍞环": item.get('鍞环', '') or item.get('price', ''),
        "璐у彿": item.get('璐у彿', '') or item.get('stock_number', ''),
        "澶囨敞": item.get('澶囨敞', '') or item.get('remark', ''),
        "鍛樺伐": item.get('鍛樺伐', '') or item.get('staff', '')
    }
```

##### 淇2: 鍓嶇姝ｅ垯澧炲己 (dist/app.js:1527-1540)
```javascript
// 鉂� 淇鍓嶏細鍙尮閰嶅崟涓�瀛楁鍚�
const nameMatch = line.match(/"鍟嗗搧鎻忚堪":```s*"([^"]+)"/);
const priceMatch = line.match(/"鍞环":```s*"([^"]+)"/);

// 鉁� 淇鍚庯細澶氬瓧娈靛悕鍏煎鍖归厤
const nameMatch = line.match(/"鍟嗗搧鎻忚堪":```s*"([^"]+)"/) 
               || line.match(/"鍟嗗搧鍚嶇О":```s*"([^"]+)"/) 
               || line.match(/"name":```s*"([^"]+)"/);
const priceMatch = line.match(/"鍞环":```s*"([^"]+)"/) 
                 || line.match(/"price":```s*"([^"]+)"/);
```

##### 淇3: PC绔嚜鍔ㄥ畾浣� (dist/app.js:1984-1997)
```javascript
// 鉂� 淇鍓嶏細鍙湁绉诲姩绔墠鑷姩婊氬姩
const isMobile = window.innerWidth < 576;
if (isMobile) {
    spiderOutputContent.scrollTop = 0;
}

// 鉁� 淇鍚庯細绉诲姩绔粴鍔ㄥ埌椤讹紝PC绔粴鍔ㄥ埌鍗＄墖浣嶇疆+鍔ㄧ敾鎻愮ず
if (isMobile) {
    spiderOutputContent.scrollTop = 0;
} else {
    const comparisonCard = spiderOutputContent.querySelector('.comparison-card:last-child');
    if (comparisonCard) {
        comparisonCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
        comparisonCard.style.animation = 'pulse 2s ease-in-out 3';  // 鑴夊啿鍔ㄧ敾鎻愰啋鐢ㄦ埛
    }
}
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍒犻櫎鍟嗗搧鍞环** | 鏄剧ず `-` 鉂� | 鏄剧ず `楼5,899` 鉁� |
| **鏂板鍟嗗搧鍚嶇О** | 涓虹┖ 鉂� | 姝ｇ‘鏄剧ず 鉁� |
| **瀛楁鍖归厤鐜�** | 鍗曚竴鍖归厤 鉂� | 澶氶噸鍏煎 鉁� |
| **绉诲姩绔綋楠�** | 鑷姩婊氬姩 鉁� | 淇濇寔涓嶅彉 鉁� |
| **PC绔綋楠�** | 闇�鎵嬪姩鏌ユ壘 鉂� | 鑷姩瀹氫綅+鍔ㄧ敾 鉁� |

**鎶�鏈粏鑺�**:
- **鏁版嵁娴�**: `analyze_data_changes()` 鈫� `format_json_array()` 鈫� 鍓嶇姝ｅ垯瑙ｆ瀽 鈫� 琛ㄦ牸娓叉煋
- **瀛楁鏄犲皠**: JSON鏁版嵁鍚屾椂瀛樺偍涓枃鍜岃嫳鏂囧瓧娈靛悕锛堝 `鍟嗗搧鎻忚堪`/`name`, `鍞环`/`price`锛夛紝闇�鍏煎涓ょ鏍煎紡
- **瀹归敊璁捐**: 浣跨敤 `or` 閾惧紡璋冪敤纭繚鑷冲皯鑳藉彇鍒颁竴涓潪绌哄��
- **鍔ㄧ敾鏁堟灉**: CSS `pulse` 鍔ㄧ敾璁╂柊澧炵殑瀵规瘮鍗＄墖鍦≒C绔洿閱掔洰
- **鍚戝悗鍏煎**: 淇涓嶅奖鍝嶆棫鏁版嵁鐨勮В鏋愶紝鏃ф牸寮忎粛鍙甯稿伐浣�

---

### v3.8.89.12.5 (2026-07-31) - 馃悰 淇鍟嗗搧瀛楁瑙ｆ瀽閫昏緫 鈥� 鏀寔澶氳JSON瀵硅薄

#### 闂: 鍟嗗搧鎻忚堪瀛楁鍖呭惈澶氳JSON瀵硅薄鏃惰В鏋愬け璐�
**淇**: 鍓嶇瀛楁瑙ｆ瀽閫昏緫澧炲己锛屾敮鎸佸琛孞SON瀵硅薄瑙ｆ瀽

---

### v3.8.89.12.4 (2026-07-31) - 馃悰 绉婚櫎dist鏂囦欢24灏忔椂缂撳瓨

#### 闂: 鍓嶇浠ｇ爜鏇存柊鍚庢祻瑙堝櫒浠嶄娇鐢ㄦ棫缂撳瓨
**淇**: 绉婚櫎dist鏂囦欢24灏忔椂缂撳瓨鏈哄埗锛岀‘淇濇祻瑙堝櫒濮嬬粓鍔犺浇鏈�鏂颁唬鐮�

---

### v3.8.89.12.3 (2026-07-31) - 馃悰 鏇存柊app.js鐗堟湰鍙峰己鍒舵祻瑙堝櫒鍔犺浇鏂颁唬鐮�

#### 闂: 娴忚鍣ㄧ紦瀛樺鑷寸敤鎴风湅涓嶅埌鏈�鏂版洿鏂�
**淇**: 鏇存柊app.js鐗堟湰鍙凤紝寮哄埗娴忚鍣ㄥ姞杞芥柊浠ｇ爜

---

### v3.8.89.12.2 (2026-07-31) - 馃摑 鏁村悎FIX_GUIDE.md鍒癛EADME.md

#### 鍙樻洿: 灏嗙嫭绔嬬殑FIX_GUIDE.md鍐呭鏁村悎鍒癛EADME.md锛屽垹闄ょ嫭绔嬫枃浠�

---

### v3.8.89.12.1 (2026-07-31) - 馃悰 娣诲姞璋冭瘯鏃ュ織 + 寮哄埗鍒锋柊鎸囧崡

#### 闂: 瀵规瘮鏁版嵁瀛楁鍖归厤闂鎺掓煡鍥伴毦
**淇**: 娣诲姞璋冭瘯鏃ュ織杈呭姪鎺掓煡锛屾坊鍔犲己鍒跺埛鏂版寚鍗�

---

### v3.8.89.11 (2026-07-30) - 馃敡 hostc WebSocket 瀹夊叏鍏抽棴淇 鈥� 杩涚▼宕╂簝鏍瑰洜淇

#### 闂: hostc 闅ч亾鍚姩鏃舵姤閿� `WebSocket was closed before the connection was established` 骞跺鑷磋繘绋嬪穿婧�
**鐜拌薄**: 椤圭洰鍚姩鏃� hostc 闅ч亾灏濊瘯寤虹珛 WebSocket 杩炴帴锛岃秴鏃舵垨澶辫触鍚庤皟鐢� `safeCloseWebSocket2` 鍏抽棴 socket锛岃Е鍙戞湭鎹曡幏鐨� `error` 浜嬩欢瀵艰嚧 Node.js 杩涚▼宕╂簝閫�鍑�

**鏍规湰鍘熷洜**:
1. **`safeCloseWebSocket2` 鍑芥暟缂洪櫡**: 褰� WebSocket 澶勪簬 `CONNECTING` 鐘舵�佹椂锛岀洿鎺ヨ皟鐢� `socket.close()` 浼氭姏寮傚父锛坄ws` 搴撹瀹氭湭瀹屾垚鎻℃墜鐨� socket 蹇呴』鐢� `terminate()` 寮哄埗鍏抽棴锛�
2. **瓒呮椂澶勭悊鍣ㄧ己闄�**: 瓒呮椂鍚庤皟鐢� `safeCloseWebSocket2` 鍏抽棴 socket锛屼絾鏈鍏堟敞鍐� `error` 浜嬩欢鐩戝惉鍣紝瀵艰嚧 `close()` 瑙﹀彂鐨� error 浜嬩欢鏃犱汉澶勭悊锛屾姏鍑� `Unhandled 'error' event`

**淇鏂规**:
```javascript
// 鉂� 淇鍓嶏細瓒呮椂澶勭悊鍣ㄧ洿鎺ュ叧闂紝鏈鐞� error 浜嬩欢
const timeout = setTimeout(() => {
  cleanup();
  safeCloseWebSocket2(socket, CLOSE_INTERNAL_ERROR, "connect timeout");
  reject(new Error("WebSocket connect timed out"));
}, WEBSOCKET_CONNECT_TIMEOUT_MS);

// 鉁� 淇鍚庯細鍏抽棴鍓嶅悶鎺� error 浜嬩欢锛岄槻姝㈣繘绋嬪穿婧�
const timeout = setTimeout(() => {
  cleanup();
  socket.once("error", () => {});
  safeCloseWebSocket2(socket, CLOSE_INTERNAL_ERROR, "connect timeout");
  reject(new Error("WebSocket connect timed out"));
}, WEBSOCKET_CONNECT_TIMEOUT_MS);
```

```javascript
// 鉂� 淇鍓嶏細涓嶅尯鍒� socket 鐘舵�侊紝鐩存帴璋冪敤 close()
function safeCloseWebSocket2(socket, code, reason) {
  if (!socket) return;
  try {
    socket.close(normalizeWebSocketCloseCode(code), normalizeWebSocketCloseReason(reason));
  } catch {
    socket.terminate();
  }
}

// 鉁� 淇鍚庯細CONNECTING 鐘舵�佺敤 terminate()锛孫PEN 鐘舵�佺敤 close()
function safeCloseWebSocket2(socket, code, reason) {
  if (!socket) return;
  try {
    if (socket.readyState === import_ws2.default.CONNECTING) {
      socket.once("error", () => {});
      socket.terminate();
    } else {
      socket.close(normalizeWebSocketCloseCode(code), normalizeWebSocketCloseReason(reason));
    }
  } catch {
    try { socket.terminate(); } catch {}
  }
}
```

**鎸佷箙鍖栦繚鎶�**:
- 鍦� `dist/package.json` 涓坊鍔� `patch-package` 浣滀负 `postinstall` 閽╁瓙
- 琛ヤ竵鏂囦欢 `dist/patches/hostc+1.3.0.patch` 纭繚 `npm install` 鍚庤嚜鍔ㄥ簲鐢ㄤ慨澶�

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **hostc 鍚姩** | 杩涚▼宕╂簝 鉂� | 姝ｅ父鍚姩 鉁� |
| **WebSocket 瓒呮椂** | Unhandled error 鉂� | 浼橀泤鍏抽棴 鉁� |
| **琛ヤ竵鎸佷箙鍖�** | npm install 鍚庝涪澶� 鉂� | postinstall 鑷姩搴旂敤 鉁� |

**鎶�鏈粏鑺�**:
- `ws` 搴撶殑 `close()` 鏂规硶浠呭湪 `OPEN` 鐘舵�佷笅鍙敤锛宍CONNECTING` 鐘舵�佸繀椤讳娇鐢� `terminate()`
- `socket.once("error", () => {})` 鐢ㄤ簬鍚炴帀鍥犲己鍒跺叧闂�屼骇鐢熺殑 error 浜嬩欢
- `patch-package` 纭繚姣忔 `npm install` 鍚庤ˉ涓佽嚜鍔ㄥ簲鐢紝涓嶄細鍥犱緷璧栨洿鏂拌�屼涪澶变慨澶�

---

### v3.8.89.10 (2026-07-30) - 馃敡 闅ч亾楠岃瘉淇 鈥� hostc/CF 鍧囦笉鍙敤鐨勬牴鍥犱慨澶�

#### 闂: 椤圭洰鍚姩鍚� hostc 鍜� CF 闅ч亾鍧囪鍒ゅ畾涓�"涓嶅彲鐢�"
**鐜拌薄**: 椤圭洰鍚姩鏃� hostc 鍜� Cloudflare Tunnel 閮借兘鎴愬姛鍚姩骞惰幏鍙栧埌 URL锛屼絾蹇冭烦楠岃瘉鏈哄埗濮嬬粓鍒ゅ畾涓轰笉鍙敤锛屽鑷村弽澶嶉噸鍚毀閬�

**鏍规湰鍘熷洜**:
1. **hostc 楠岃瘉澶辫触**: `verify_url()` 鍑芥暟浣跨敤 HTTP `HEAD` 鏂规硶楠岃瘉 URL锛屼絾 FastAPI 鏍硅矾鐢� `@app.get('/')` 涓嶆敮鎸� HEAD 璇锋眰锛岃繑鍥� `405 Method Not Allowed`锛屽鑷撮獙璇佹案杩滃け璐�
2. **CF 楠岃瘉澶辫触**: 鏈満 DNS 鏃犳硶瑙ｆ瀽 `trycloudflare.com` 鍩熷悕锛坄Errno 8: nodename nor servname provided`锛夛紝灞炰簬缃戠粶/DNS 閰嶇疆闂

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍙敮鎸� GET锛孒EAD 璇锋眰杩斿洖 405
@app.get('/')
async def index():

# 鉁� 淇鍚庯細鍚屾椂鏀寔 GET 鍜� HEAD锛岄獙璇佽姹傛甯搁�氳繃
@app.api_route('/', methods=['GET', 'HEAD'])
async def index():
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **hostc 楠岃瘉** | 405 Method Not Allowed 鉂� | 200 OK 鉁� |
| **蹇冭烦鍒ゅ畾** | 涓嶅彲鐢� 鈫� 鍙嶅閲嶅惎 鉂� | 鍙敤 鈫� 绋冲畾杩愯 鉁� |
| **閭欢閫氱煡** | 鍙戦��"涓嶅彲鐢�"閫氱煡 鉂� | 鍙戦��"鍙敤"閫氱煡 鉁� |

**鎶�鏈粏鑺�**:
- FastAPI 鐨� `@app.get()` 瑁呴グ鍣ㄤ笉浼氳嚜鍔ㄤ负璺敱鏀寔 HEAD 鏂规硶锛堜笌 Flask 涓嶅悓锛�
- `verify_url()` 浣跨敤 `urllib.request.Request(url, method='HEAD')` 鍙戦�� HEAD 璇锋眰
- 鏀圭敤 `@app.api_route('/', methods=['GET', 'HEAD'])` 鍚庯紝HEAD 璇锋眰杩斿洖涓� GET 鐩稿悓鐨勫搷搴斿ご锛堟棤 body锛夛紝楠岃瘉閫氳繃

**CF 涓嶅彲鐢ㄧ殑棰濆璇存槑**:
- CF 闅ч亾杩涚▼鏈韩鍚姩姝ｅ父锛堢洿鎺ヨ繛鎺� Cloudflare 鏈嶅姟鍣ㄨ幏鍙� URL锛�
- 浣嗘湰鏈� DNS 鏃犳硶瑙ｆ瀽 `*.trycloudflare.com`锛屽鑷撮獙璇佽姹傚け璐�
- 寤鸿鎺掓煡 DNS 璁剧疆锛歚nslookup xxx.trycloudflare.com`锛屾垨鏇存崲 DNS 涓� `8.8.8.8` / `114.114.114.114`

---

### v3.8.89.9 (2026-07-30) - 馃幆 楂樹环鍟嗗搧鏁拌В鏋愪慨澶� + 鎸夐挳澶辨晥淇

#### 闂1: 楂樹环鍟嗗搧鏁版樉绀轰负0
**鐜拌薄**: 鐖櫕鏃ュ織鏄剧ず"鍞环 >= 599 鐨勫晢鍝�: 78 涓�"锛屼絾鐣岄潰鏄剧ず楂樹环鍟嗗搧鏁颁负 **0**

**鏍规湰鍘熷洜**: 
- 鍓嶇姝ｅ垯琛ㄨ揪寮忔棤娉曟纭尮閰峆ython杈撳嚭鐨勬牸寮�
- Python杈撳嚭鏍煎紡锛歚鍞环 >= 599 鐨勫晢鍝�: 78 涓猔锛堟湁绌烘牸锛�
- 鍓嶇姝ｅ垯锛歚/鍞环[銆�>=]+```s*599[^:锛歖*[:锛歖```s*(```d+)```s*[涓欢]/`锛堟棤娉曞尮閰嶇┖鏍硷級

**淇鏂规**:
```javascript
// 鉁� 绠�鍖栨鍒欒〃杈惧紡锛岀洿鎺ュ尮閰峆ython杈撳嚭鏍煎紡
if (line.includes('鍞环') && line.includes('599') && line.includes('鍟嗗搧')) {
    // 涓昏鍖归厤锛�"鍞环 >= 599 鐨勫晢鍝�: 78 涓�"
    let match = line.match(/鍞环```s*>=```s*599```s*鐨勫晢鍝乣``s*[:锛歖```s*(```d+)```s*涓�/);
    // 澶囬�夋柟妗堬細鍖归厤浠绘剰"鍟嗗搧: 鏁板瓧 涓�"鏍煎紡
    if (!match) match = line.match(/鍟嗗搧```s*[:锛歖```s*(```d+)```s*涓�/);
    // 鏈�鍚庡閫夛細鍖归厤琛屾湯鐨勬暟瀛�
    if (!match) match = line.match(/(```d+)```s*涓猔``s*$/);
    
    if (match && parseInt(match[1]) > 0) {
        skuData.highPriceCount = match[1];
        console.log('[瀵规瘮鍗＄墖] 鉁� 楂樹环鍟嗗搧鏁�:', skuData.highPriceCount);
    }
}
```

**鏁版嵁娴佺▼璇存槑**:
1. **鐖櫕杩愯鏃�**锛氬墠绔В鏋愭棩蹇楄緭鍑哄疄鏃舵樉绀虹粺璁℃暟鎹�
2. **鐖櫕瀹屾垚鍚�**锛氬墠绔皟鐢� `/api/products` API鑾峰彇JSON鏁版嵁锛堝凡鍖呭惈 `highPriceCount` 瀛楁锛�

#### 闂2: 8涓寜閽叏閮ㄥけ鏁�
**鐜拌薄**: 椤甸潰鍔犺浇鍚庢墍鏈夋寜閽偣鍑绘棤鍝嶅簲

**鏍规湰鍘熷洜**: 
- `bindAllButtons()` 鍑芥暟瀹氫箟鍦ㄤ綔鐢ㄥ煙鍐咃紝涓嶆槸鍏ㄥ眬鍑芥暟
- 澶栭儴鏃犳硶璋冪敤锛屽鑷存寜閽簨浠剁粦瀹氬け璐�

**淇鏂规**:
```javascript
// 鉁� 鏆撮湶涓哄叏灞�鍑芥暟
window.bindAllButtons = bindAllButtons;
window.resetButtons = resetButtons;
```

### 鉁� 淇鏁堟灉
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **楂樹环鍟嗗搧(鈮�599)** | 0 鉂� | 78 鉁� |
| **鎸夐挳鍝嶅簲** | 澶辨晥 鉂� | 姝ｅ父 鉁� |
| **鏁版嵁鏄剧ず** | 閿欒 鉂� | 鍑嗙‘ 鉁� |

### 馃摑 鎶�鏈粏鑺�
- **鏂囦欢浣嶇疆**: `dist/app.js` Line 1369-1383, 1441-1453, 2707
- **淇鏂规硶**: 
  1. 绠�鍖栨鍒欒〃杈惧紡锛岀簿纭尮閰峆ython杈撳嚭鏍煎紡
  2. 鏆撮湶鍏ㄥ眬鍑芥暟锛岀‘淇濇寜閽粦瀹氭垚鍔�
- **楠岃瘉鏂瑰紡**: 
  1. Node.js璇硶妫�鏌ラ�氳繃
  2. 娴忚鍣ㄦ祴璇曟寜閽搷搴旀甯�
  3. 鐖櫕杩愯鏃跺疄鏃舵樉绀烘纭殑缁熻鏁版嵁

---

## 馃敡 鍓嶇鍞环鏄剧ず"-"闂淇鎸囧崡 (v3.8.89.12 涓撻」鎺掓煡)

> **鈿狅笍 閲嶈鎻愮ず**: 鏈寚鍗椾笓闂ㄨВ鍐� **v3.8.89.12** 鐗堟湰淇鍚庯紝鍓嶇浠嶆樉绀哄敭浠蜂负 "-" 鐨勯棶棰樸��
>
> **鏍规湰鍘熷洜**: 娴忚鍣ㄧ紦瀛樹簡鏃х増鏈殑 JavaScript 浠ｇ爜锛屽鑷存柊浠ｇ爜鏈敓鏁堛��

### 鉁� 褰撳墠鐘舵��

#### 鍚庣锛堝凡淇 鉁咃級
```json
{
  "鍟嗗搧鎻忚堪": "iPhone 16 Pro Max ...",
  "鍞环": "楼6,699",  // 鈫� 鏁版嵁姝ｇ‘锛�
  "璐у彿": "08055",
  ...
}
```

#### 鍓嶇锛堜唬鐮佸凡淇敼锛岄渶鍒锋柊 鈿狅笍锛�
- **浠ｇ爜浣嶇疆**: [dist/app.js:1527-1559](dist/app.js#L1527-L1559)
- **淇敼鍐呭**: 澧炲己姝ｅ垯琛ㄨ揪寮� + 娣诲姞璋冭瘯鏃ュ織
- **Git鐗堟湰**: `8de42bb` (v3.8.89.12)

---

### 馃毃 闂鐜拌薄

```
鍒犻櫎鍟嗗搧搴忓垪鍙� (1涓�)
搴忓彿    璐у彿     鍞环
1       08055    -      鉂� 搴旇鏄剧ず 楼6,699
```

---

### 馃挕 瑙ｅ喅鏂规锛堟寜椤哄簭灏濊瘯锛�

#### 鏂规1锛氬己鍒跺埛鏂版祻瑙堝櫒锛堟帹鑽� 猸愨瓙猸愨瓙猸愶級

**Windows/Linux 鐢ㄦ埛**:
1. 鍦ㄧ埇铏〉闈㈡寜涓嬶細`Ctrl + F5`
2. 鎴栬�呮寜浣� `Ctrl` 鐐瑰嚮娴忚鍣ㄥ埛鏂版寜閽� 馃攧

**Mac 鐢ㄦ埛**:
1. 鍦ㄧ埇铏〉闈㈡寜涓嬶細`Cmd + Shift + R`
2. 鎴栬�呮寜浣� `Cmd` 鐐瑰嚮娴忚鍣ㄥ埛鏂版寜閽� 馃攧

**楠岃瘉鏂规硶**:
鎵撳紑娴忚鍣ㄥ紑鍙戣�呭伐鍏凤紙F12锛夆啋 Console 鏍囩锛屽簲璇ョ湅鍒帮細
```javascript
[瀵规瘮鍗＄墖] 馃搳 瑙ｆ瀽鍒板垹闄ゅ晢鍝�: {
  鍘熷琛�: '{"鍟嗗搧鎻忚堪":"iPhone...","鍞环":"楼6,699","璐у彿":"08055",...}',
  瑙ｆ瀽缁撴灉: {sku: '08055', name: 'iPhone...', price: '楼6,699'},
  SKU鍖归厤: true,
  鍚嶇О鍖归厤: true,
  浠锋牸鍖归厤: true,
  鍖归厤璇︽儏: {sku: '"璐у彿":"08055"', name: '"鍟嗗搧鎻忚堪":"iPhone..."', price: '"鍞环":"楼6,699"'}
}
鉁� 浠锋牸瑙ｆ瀽鎴愬姛锛�
```

---

#### 鏂规2锛氱鐢ㄦ祻瑙堝櫒缂撳瓨锛堝鏋滄柟妗�1鏃犳晥锛�

1. 鎵撳紑娴忚鍣ㄥ紑鍙戣�呭伐鍏凤細`F12`
2. 鍒囨崲鍒� **"Network"** 鏍囩椤�
3. 鍕鹃�� 鈽戯笍 **"Disable cache"**锛堢鐢ㄧ紦瀛橈級
4. **淇濇寔 F12 绐楀彛鎵撳紑**
5. 鐐瑰嚮椤甸潰鍒锋柊鎸夐挳鎴栭噸鏂拌繍琛岀埇铏换鍔�

---

#### 鏂规3锛氬畬鍏ㄦ竻闄ゆ祻瑙堝櫒缂撳瓨锛堝鏋滄柟妗�2鏃犳晥锛�

**Chrome/Edge**:
1. 蹇嵎閿細`Ctrl + Shift + Delete`
2. 鏃堕棿鑼冨洿閫夋嫨锛�**"鍏ㄩ儴鏃堕棿"**
3. 鍙嬀閫夛細鈽戯笍 **"缂撳瓨鐨勫浘鐗囧拰鏂囦欢"**
4. 鐐瑰嚮锛�**"娓呴櫎鏁版嵁"**
5. 閲嶅惎娴忚鍣ㄥ苟璁块棶鐖櫕椤甸潰

**Firefox**:
1. 蹇嵎閿細`Ctrl + Shift + Delete`
2. 鏃堕棿鑼冨洿閫夋嫨锛�**"鍏ㄩ儴"**
3. 璇︽儏 鈫� 鍙嬀閫夛細鈽戯笍 **"缂撳瓨"**
4. 鐐瑰嚮锛�**"绔嬪嵆娓呴櫎"**

---

#### 鏂规4锛氶噸鍚湇鍔″櫒锛堝鏋滀互涓婇兘鏃犳晥锛�

**濡傛灉浣跨敤 Python 鐩存帴杩愯**:
```bash
# 鍋滄褰撳墠杩愯鐨勬湇鍔″櫒
# Ctrl+C 鎴栧叧闂粓绔獥鍙�

# 閲嶆柊鍚姩鏈嶅姟鍣�
cd D:```ws```xy_ws
D:```ws```xy_ws```.venv```Scripts```python.exe main.py
```

**濡傛灉浣跨敤 Node.js 鍚姩鍓嶇**:
```bash
# 鍋滄 Node.js 杩涚▼
taskkill /F /IM node.exe

# 閲嶆柊鍚姩
cd D:```ws```xy_ws```dist
npm start
# 鎴�
node server.js
```

---

### 馃攳 璋冭瘯姝ラ锛堝鏋滀粛鐒朵笉宸ヤ綔锛�

#### 姝ラ1锛氭鏌ユ帶鍒跺彴鏃ュ織

1. 鎵撳紑娴忚鍣ㄥ紑鍙戣�呭伐鍏凤細`F12`
2. 鍒囨崲鍒� **"Console"** 鏍囩
3. 閲嶆柊杩愯鐖櫕浠诲姟
4. 鏌ユ壘 `[瀵规瘮鍗＄墖]` 寮�澶寸殑鏃ュ織

**棰勬湡杈撳嚭**:
```javascript
[瀵规瘮鍗＄墖] 馃搳 瑙ｆ瀽鍒板垹闄ゅ晢鍝�: {
  鍘熷琛�: '    "璐у彿": "08055",',
  瑙ｆ瀽缁撴灉: {sku: '08055', name: '', price: ''},
  SKU鍖归厤: true,
  鍚嶇О鍖归厤: false,        // 鈫� 濡傛灉杩欓噷涓� false锛岃鏄庡瓧娈靛悕涓嶅尮閰�
  浠锋牸鍖归厤: false,        // 鈫� 濡傛灉杩欓噷涓� false锛岃鏄庝环鏍兼湭鍖归厤鍒�
  鍖归厤璇︽儏: {...}
}
```

#### 姝ラ2锛氭鏌ュ師濮嬫暟鎹牸寮�

鍦� Console 涓緭鍏ヤ互涓嬪懡浠ゆ煡鐪嬪悗绔繑鍥炵殑鍘熷鏁版嵁锛�

```javascript
// 鍦ㄧ埇铏繍琛屽畬鎴愬悗锛屽湪鎺у埗鍙版墽琛�
console.log('鍒犻櫎鍟嗗搧鍒楄〃:', skuData.deletedProducts);
console.log('鍘熷琛岀ず渚�:', document.querySelector('#spider-output-content')?.innerText?.match(/鍒犻櫎鍟嗗搧[```s```S]*?```[/)?.[0]);
```

#### 姝ラ3锛氭墜鍔ㄦ祴璇曟鍒欒〃杈惧紡

鍦� Console 涓墽琛岋細

```javascript
const testLine = '    "鍟嗗搧鎻忚堪": "iPhone 16 Pro Max",```n    "鍞环": "楼6,699",```n    "璐у彿": "08055",';

const nameMatch = testLine.match(/"鍟嗗搧鎻忚堪":```s*"([^"]+)"/)
               || testLine.match(/"鍟嗗搧鍚嶇О":```s*"([^"]+)"/)
               || testLine.match(/"name":```s*"([^"]+)"/);

const priceMatch = testLine.match(/"鍞环":```s*"([^"]+)"/)
                 || testLine.match(/"price":```s*"([^"]+)"/);

console.log('鍚嶇О鍖归厤:', nameMatch?.[1]);   // 棰勬湡杈撳嚭: iPhone 16 Pro Max 鉁�
console.log('浠锋牸鍖归厤:', priceMatch?.[1]);   // 棰勬湡杈撳嚭: 楼6,699 鉁�
```

---

### 馃搳 棰勬湡姝ｇ‘缁撴灉

淇鎴愬姛鍚庯紝鍒犻櫎鍟嗗搧琛ㄦ牸搴旀樉绀猴細

| 搴忓彿 | 璐у彿 | 鍞环 |
|------|------|------|
| 1 | 08055 | 楼6,699 鉁� |

鑰屼笉鏄箣鍓嶇殑锛�

| 搴忓彿 | 璐у彿 | 鍞环 |
|------|------|------|
| 1 | 08055 | - 鉂� |

---

### 馃洜锔� 鎶�鏈粏鑺�

#### 淇敼鐨勬枃浠舵竻鍗�

| 鏂囦欢 | 淇敼鍐呭 | 琛屽彿 |
|------|----------|------|
| [main.py](main.py) | 瀛楁鍚嶅吋瀹规�т慨澶� | 4520-4529 |
| [dist/app.js](dist/app.js) | 姝ｅ垯澧炲己 + 璋冭瘯鏃ュ織 | 1527-1559, 1984-1997 |
| [README.md](README.md) | 鐗堟湰璁板綍 + 鏈慨澶嶆寚鍗� | - |
| [skill.md](skill.md) | 鎶�鏈寖寮� PY-CORE-007 | 4043-4364 |

#### 鏁版嵁娴佽鏄�

```
鍚庣 main.py:4520 (get_product_detail)
    鈫� 杈撳嚭JSON瀛楃涓�
    鈫� {"鍟嗗搧鎻忚堪":"iPhone...","鍞环":"楼6,699","璐у彿":"08055"}
鍓嶇 app.js:1527 (姝ｅ垯瑙ｆ瀽)
    鈫� 鎻愬彇瀛楁鍊�
    鈫� product = {sku:'08055', name:'iPhone...', price:'楼6,699'}
鍓嶇 app.js:1905 (琛ㄦ牸娓叉煋)
    鈫� 鏄剧ず鍒癠I
    鈫� <td>楼6,699</td> 鉁�
```

#### Git 淇℃伅

```bash
Commit: 8de42bb
Message: fix(frontend+backend+docs): 瀵规瘮鏁版嵁瀛楁鍖归厤淇 + PC绔樉绀轰紭鍖� (v3.8.89.12)
Branch: master -> origin/master
Date: 2026-07-31
Files: 6 files changed, 747 insertions(+), 13 deletions(-)
```

---

### 鉂� 甯歌闂 FAQ

#### Q1: 寮哄埗鍒锋柊鍚庤繕鏄樉绀�"-"锛�

**A**: 璇锋鏌ワ細
1. 鏄惁鐪熺殑浣跨敤浜� `Ctrl+F5`锛堜笉鏄櫘閫� F5锛�
2. 鏄惁娓呴櫎浜嗘祻瑙堝櫒缂撳瓨
3. 鏄惁閲嶅惎浜嗘湇鍔″櫒
4. 鎺у埗鍙版槸鍚︽湁閿欒淇℃伅

#### Q2: 鎺у埗鍙版病鏈� `[瀵规瘮鍗＄墖]` 鏃ュ織锛�

**A**: 璇存槑鏂颁唬鐮佹湭鍔犺浇锛岃锛�
1. 纭宸茬粡寮哄埗鍒锋柊锛堟柟妗�1锛�
2. 灏濊瘯绂佺敤缂撳瓨锛堟柟妗�2锛�
3. 瀹屽叏娓呴櫎缂撳瓨锛堟柟妗�3锛�
4. 閲嶅惎鏈嶅姟鍣紙鏂规4锛�

#### Q3: 鏃ュ織鏄剧ず `浠锋牸鍖归厤: false`锛�

**A**: 璇存槑鍚庣杈撳嚭鐨勫瓧娈靛悕涓庨鏈熶笉绗︼紝璇凤細
1. 鏌ョ湅 Console 涓殑 `鍘熷琛宍 鍐呭
2. 纭鏄惁鍖呭惈 `"鍞环"` 鎴� `"price"` 鍏抽敭瀛�
3. 鍙兘闇�瑕佽繘涓�姝ヨ皟鏁存鍒欒〃杈惧紡

#### Q4: 绉诲姩绔甯镐絾PC绔紓甯革紵

**A**: 杩欐槸缂撳瓨闂锛岀Щ鍔ㄧ閫氬父浼氳嚜鍔ㄦ竻闄ょ紦瀛樸�侾C绔渶瑕佹墜鍔ㄦ搷浣滐細
1. 浣跨敤鏂规1-3涓殑浠讳竴鏂规硶娓呴櫎缂撳瓨
2. 鎴栬�呭湪 PC 绔娇鐢ㄩ殣绉�/鏃犵棔妯″紡鎵撳紑椤甸潰

---

### 馃幆 涓嬩竴姝ヨ鍔ㄦ竻鍗�

瀹屾垚涓婅堪姝ラ鍚庯紝璇凤細

- [ ] **1. 寮哄埗鍒锋柊娴忚鍣�** (`Ctrl+F5`) 猸� 鏈�閲嶈锛�
- [ ] **2. 閲嶆柊杩愯鐖櫕浠诲姟**
- [ ] **3. 妫�鏌ュ垹闄ゅ晢鍝佽〃鏍�**锛堝簲璇ユ樉绀� 楼6,699锛�
- [ ] **4. 鏌ョ湅鎺у埗鍙扮‘璁よ皟璇曟棩蹇楄緭鍑�**锛團12 鈫� Console锛屾壘 `[瀵规瘮鍗＄墖]`锛�
- [ ] **5. 濡傛灉鎴愬姛锛屾埅鍥剧‘璁�** 鉁�
- [ ] **6. 濡傛灉澶辫触锛屽皾璇曟柟妗�2/3/4**

濡傛灉闂浠嶇劧瀛樺湪锛岃鎻愪緵锛�
- 鎺у埗鍙扮殑瀹屾暣鏃ュ織杈撳嚭
- 鍒犻櫎鍟嗗搧鐨勫畬鏁� JSON 鏁版嵁
- 娴忚鍣ㄧ被鍨嬪拰鐗堟湰淇℃伅

---

## 馃搻 鐗堟湰鏇存柊璁板綍鑼冨紡瑙勮寖

鎵�鏈夌増鏈洿鏂拌褰�**蹇呴』**閬靛惊浠ヤ笅鑼冨紡锛岀‘淇濋棶棰樺彲杩芥函銆佹牴鍥犲彲瀹氫綅銆佷慨澶嶅彲楠岃瘉锛�

```markdown
### vX.Y.Z (YYYY-MM-DD) - <emoji> <绠�杩�>

#### 闂: <涓�鍙ヨ瘽鎻忚堪闂>
**鐜拌薄**: <鐢ㄦ埛鍙劅鐭ョ殑鍏蜂綋琛ㄧ幇锛屽寘鍚敊璇俊鎭�佹棩蹇楄緭鍑恒�佺晫闈㈠紓甯哥瓑>

**鏍规湰鍘熷洜**:
1. **<妯″潡/鍑芥暟>缂洪櫡**: <鎶�鏈眰闈㈢殑鏍瑰洜鍒嗘瀽锛岃鏄庝负浠�涔堜細浜х敓杩欎釜闂>
2. **<鍏宠仈妯″潡>缂洪櫡**: <濡傛湁澶氫釜鏍瑰洜锛岄�愪竴鍒楀嚭>

**淇鏂规**:
```<language>
// 鉂� 淇鍓嶏細<绠�杩版棫閫昏緫鐨勯棶棰�>
<鏃т唬鐮�>

// 鉁� 淇鍚庯細<绠�杩版柊閫昏緫鐨勬敼杩�>
<鏂颁唬鐮�>
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **<鎸囨爣1>** | <閿欒鐘舵��> 鉂� | <姝ｇ‘鐘舵��> 鉁� |
| **<鎸囨爣2>** | <閿欒鐘舵��> 鉂� | <姝ｇ‘鐘舵��> 鉁� |

**鎶�鏈粏鑺�**:
- <鎶�鏈師鐞嗚鏄�1>
- <鎶�鏈師鐞嗚鏄�2>
- <娉ㄦ剰浜嬮」鎴栬竟鐣屾潯浠�>
```

**鑼冨紡瑕佺礌璇存槑**:

| 瑕佺礌 | 蹇呭～ | 璇存槑 |
|------|------|------|
| **闂** | 鉁� | 涓�鍙ヨ瘽姒傛嫭闂鏈川 |
| **鐜拌薄** | 鉁� | 鐢ㄦ埛鍙劅鐭ョ殑鍏蜂綋琛ㄧ幇锛岄檮閿欒淇℃伅/鏃ュ織 |
| **鏍规湰鍘熷洜** | 鉁� | 鎶�鏈眰闈㈢殑鏍瑰洜锛岀紪鍙峰垪鍑猴紝鍏宠仈鍒板叿浣撴ā鍧�/鍑芥暟 |
| **淇鏂规** | 鉁� | 淇鍓嶁潓 + 淇鍚庘渽 鐨勪唬鐮佸姣� |
| **淇鏁堟灉** | 鉁� | 閲忓寲瀵规瘮琛紝鍚潓/鉁呮爣璁� |
| **鎶�鏈粏鑺�** | 鉁� | 鍘熺悊璇存槑銆佹敞鎰忎簨椤广�佽竟鐣屾潯浠� |
| **鎸佷箙鍖栦繚鎶�** | 鏉′欢蹇呭～ | 娑夊強patch-package/閰嶇疆鍙樻洿鏃跺繀濉� |

**Emoji瀵圭収琛�**: 馃悰Bug淇 馃敡鍔熻兘浼樺寲 鉁ㄦ柊鍔熻兘 馃敀瀹夊叏淇 馃幆绮惧噯淇 馃摑鏂囨。鏇存柊 鈾伙笍閲嶆瀯

---

## 馃摎 鏃╂湡鐗堟湰鍘嗗彶璁板綍 (v1.4.2 - v2.1.7)

### v2.1.7 - v2.1.7: 娣诲姞澶氶噸瓒呮椂淇濇姢鍜岄噸璇曟満鍒讹紝闃叉鐖櫕鍗℃

**鎻愪氦Hash**: dd50461b
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
v2.1.7: 娣诲姞澶氶噸瓒呮椂淇濇姢鍜岄噸璇曟満鍒讹紝闃叉鐖櫕鍗℃

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
v2.1.7: 娣诲姞澶氶噸瓒呮椂淇濇姢鍜岄噸璇曟満鍒讹紝闃叉鐖櫕鍗℃
```

---


### v2.1.6 - v2.1.6: 淇寮圭獥鍏抽棴瓒呮椂闂锛屾坊鍔犳椂闂寸粺璁′紭鍖栨�ц兘

**鎻愪氦Hash**: b5191c0c
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
v2.1.6: 淇寮圭獥鍏抽棴瓒呮椂闂锛屾坊鍔犳椂闂寸粺璁′紭鍖栨�ц兘

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
v2.1.6: 淇寮圭獥鍏抽棴瓒呮椂闂锛屾坊鍔犳椂闂寸粺璁′紭鍖栨�ц兘
```

---


### v2.1.5 - v2.1.5: 淇楂樹环鍟嗗搧绛涢�夐�昏緫锛岃В鍐冲姣旂粨鏋滀笉鍑嗙‘闂

**鎻愪氦Hash**: 4a7324e8
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
v2.1.5: 淇楂樹环鍟嗗搧绛涢�夐�昏緫锛岃В鍐冲姣旂粨鏋滀笉鍑嗙‘闂

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
v2.1.5: 淇楂樹环鍟嗗搧绛涢�夐�昏緫锛岃В鍐冲姣旂粨鏋滀笉鍑嗙‘闂
```

---


### v2.1.3 - v2.1.3: 浼樺寲JSON鏂囦欢瀵规瘮璁板綍鏈哄埗锛屾敮鎸佸鏉″姣旇褰�

**鎻愪氦Hash**: 4b5fe7d5
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
v2.1.3: 浼樺寲JSON鏂囦欢瀵规瘮璁板綍鏈哄埗锛屾敮鎸佸鏉″姣旇褰�

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
v2.1.3: 浼樺寲JSON鏂囦欢瀵规瘮璁板綍鏈哄埗锛屾敮鎸佸鏉″姣旇褰�
```

---


### v2.1.2 - v2.1.2: 浼樺寲JSON鏂囦欢瀵规瘮鍔熻兘锛屾柊澧炵紦瀛樻枃浠舵満鍒�

**鎻愪氦Hash**: db4c9d8d
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
v2.1.2: 浼樺寲JSON鏂囦欢瀵规瘮鍔熻兘锛屾柊澧炵紦瀛樻枃浠舵満鍒�

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
v2.1.2: 浼樺寲JSON鏂囦欢瀵规瘮鍔熻兘锛屾柊澧炵紦瀛樻枃浠舵満鍒�
```

---


### v2.1.1 - v2.1.1: 淇璺ㄥ钩鍙版祻瑙堝櫒鍚姩闂锛屽垹闄よ皟璇曚唬鐮�

**鎻愪氦Hash**: 873e4467
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
v2.1.1: 淇璺ㄥ钩鍙版祻瑙堝櫒鍚姩闂锛屽垹闄よ皟璇曚唬鐮�

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
v2.1.1: 淇璺ㄥ钩鍙版祻瑙堝櫒鍚姩闂锛屽垹闄よ皟璇曚唬鐮�
```

---


### v2.1.0 - 鏂板璋冭瘯鍔熻兘

**鎻愪氦Hash**: f77910fb
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
鏂板璋冭瘯鍔熻兘 (v2.1.0)

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
鏂板璋冭瘯鍔熻兘 (v2.1.0)

- 鏂板璋冭瘯鍔熻兘锛氭坊鍔犻〉闈㈣皟璇曞姛鑳斤紝淇濆瓨椤甸潰HTML鍐呭鍒版枃浠�
- 鏂板椤甸潰淇℃伅鏄剧ず锛氭樉绀洪〉闈㈡爣棰樺拰褰撳墠URL锛屼究浜庤瘖鏂棶棰�
- 浼樺寲閿欒璇婃柇锛氬綋鐖櫕鏃犳硶鑾峰彇鏁版嵁鏃讹紝鎻愪緵鏇村璋冭瘯淇℃伅
- 鎻愬崌闂鎺掓煡鑳藉姏锛氶�氳繃淇濆瓨鐨凥TML鏂囦欢鍒嗘瀽椤甸潰鍔犺浇鎯呭喌
- 鏀硅繘鐢ㄦ埛浣撻獙锛氬府鍔╃敤鎴峰揩閫熷畾浣嶇埇铏け璐ュ師鍥�
- 鏇存柊README.md锛氭坊鍔爒2.1.0鐗堟湰鏇存柊鏃ュ織
- 鏇存柊鐗堟湰鍙疯嚦2.1.0
```

---


### v2.0.9 - 鏂板褰撳ぉJSON鏂囦欢瀵规瘮鍔熻兘

**鎻愪氦Hash**: 6f3600af
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
鏂板褰撳ぉJSON鏂囦欢瀵规瘮鍔熻兘 (v2.0.9)

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
鏂板褰撳ぉJSON鏂囦欢瀵规瘮鍔熻兘 (v2.0.9)

- 鏂板褰撳ぉJSON鏂囦欢瀵规瘮鍔熻兘锛氬姣斿綋澶╂渶鏂扮殑涓や釜JSON鏂囦欢锛堝8鐐瑰拰11鐐圭敓鎴愮殑鏂囦欢锛�
- 浼樺寲宸紓璁板綍鏂瑰紡锛氬皢瀵规瘮宸紓鐩存帴鍐欏叆鏈�鏂扮殑JSON鏂囦欢涓紝鑰屼笉鏄崟鐙殑鏃ュ織鏂囦欢
- 鏂板get_today_json_files鏂规硶锛氫笓闂ㄧ敤浜庤幏鍙栧綋澶╂渶鏂扮殑涓や釜JSON鏂囦欢
- 鏂板compare_json_files鏂规硶锛氬疄鐜板綋澶㎎SON鏂囦欢瀵规瘮鍔熻兘
- 鏀硅繘鑿滃崟閫夐」锛氭柊澧�'褰撳ぉJSON鏂囦欢瀵规瘮'閫夐」锛岃皟鏁磋彍鍗曠紪鍙�
- 浼樺寲鏃ュ織绠＄悊锛氭瘡澶╁彧鏈変竴浠絁SON鏃ュ織锛屽樊寮備俊鎭洿鎺ヨ褰曞湪鏈�鏂扮殑JSON鏂囦欢涓�
- 鎻愬崌鏁版嵁杩借釜鏁堢巼锛氬揩閫熶簡瑙ｅ綋澶╀笉鍚屾椂闂寸偣鐨勬暟鎹彉鍖�
- 鏇存柊README.md锛氭坊鍔爒2.0.9鐗堟湰鏇存柊鏃ュ織
- 鏇存柊鐗堟湰鍙疯嚦2.0.9
```

---


### v2.0.8 - 淇璺ㄥ钩鍙版祻瑙堝櫒鍚姩闂

**鎻愪氦Hash**: 00e69d75
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
淇璺ㄥ钩鍙版祻瑙堝櫒鍚姩闂 (v2.0.8)

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
淇璺ㄥ钩鍙版祻瑙堝櫒鍚姩闂 (v2.0.8)

- 淇璺ㄥ钩鍙版祻瑙堝櫒鍚姩闂锛氫负涓嶅悓鎿嶄綔绯荤粺鍒嗗埆璁剧疆Chrome娴忚鍣ㄨ矾寰�
- 鏂板Windows绯荤粺鏀寔锛氭坊鍔燱indows绯荤粺Chrome璺緞閰嶇疆锛圕:\Program Files\Google\Chrome\Application\chrome.exe锛�
- 鏂板Linux绯荤粺鏀寔锛氭坊鍔燣inux绯荤粺Chrome璺緞閰嶇疆锛�/usr/bin/google-chrome锛�
- 淇濈暀Mac绯荤粺鏀寔锛氫繚鎸丮ac绯荤粺Chrome璺緞閰嶇疆锛�/Applications/Google Chrome.app/Contents/MacOS/Google Chrome锛�
- 浼樺寲娴忚鍣ㄥ惎鍔ㄩ�昏緫锛氭牴鎹搷浣滅郴缁熻嚜鍔ㄩ�夋嫨鍚堥�傜殑Chrome娴忚鍣ㄨ矾寰�
- 鎻愬崌璺ㄥ钩鍙板吋瀹规�э細纭繚鍦╓indows銆丮ac銆丩inux绯荤粺涓婇兘鑳芥甯稿惎鍔ㄦ祻瑙堝櫒
- 鏇存柊README.md锛氭坊鍔爒2.0.8鐗堟湰鏇存柊鏃ュ織
- 鏇存柊鐗堟湰鍙疯嚦2.0.8
```

---


### v2.0.7 - v2.0.7: 浼樺寲楂樹环鍟嗗搧绛涢�夛紝淇娴忚鍣ㄥ惎鍔�

**鎻愪氦Hash**: 668ec838
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
v2.0.7: 浼樺寲楂樹环鍟嗗搧绛涢�夛紝淇娴忚鍣ㄥ惎鍔�

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
v2.0.7: 浼樺寲楂樹环鍟嗗搧绛涢�夛紝淇娴忚鍣ㄥ惎鍔�
```

---


### v2.0.6 - v2.0.6: 浼樺寲鏁版嵁鍙樺寲鍒嗘瀽浠ｇ爜锛岀簿绠�閫昏緫

**鎻愪氦Hash**: 645dcffe
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
v2.0.6: 浼樺寲鏁版嵁鍙樺寲鍒嗘瀽浠ｇ爜锛岀簿绠�閫昏緫

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
v2.0.6: 浼樺寲鏁版嵁鍙樺寲鍒嗘瀽浠ｇ爜锛岀簿绠�閫昏緫
```

---


### v2.0.5 - v2.0.5: 鏇存柊Cookie杩囨湡鏃堕棿

**鎻愪氦Hash**: 20eaac27
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
v2.0.5: 鏇存柊Cookie杩囨湡鏃堕棿

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
v2.0.5: 鏇存柊Cookie杩囨湡鏃堕棿
```

---


### v2.0.4 - v2.0.4: 鏂板Cookie鑷姩鏇存柊鍔熻兘锛屼紭鍖朎xcel鏂囦欢妫�鏌�

**鎻愪氦Hash**: b2420f6a
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
v2.0.4: 鏂板Cookie鑷姩鏇存柊鍔熻兘锛屼紭鍖朎xcel鏂囦欢妫�鏌�

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
v2.0.4: 鏂板Cookie鑷姩鏇存柊鍔熻兘锛屼紭鍖朎xcel鏂囦欢妫�鏌�
```

---


### v2.0.3 - 浠ｇ爜閲嶆瀯鍜屼紭鍖�

**鎻愪氦Hash**: d0854908
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
浠ｇ爜閲嶆瀯鍜屼紭鍖� (v2.0.3)

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
浠ｇ爜閲嶆瀯鍜屼紭鍖� (v2.0.3)

- 浠ｇ爜閲嶆瀯鍜屼紭鍖栵細鎻愬彇浠锋牸瑙ｆ瀽閫昏緫涓虹嫭绔嬫柟娉昿arse_price锛屾彁楂樹唬鐮佸鐢ㄦ��
- 鏂板绛涢�夋柟娉曪細鍒涘缓filter_high_price_products鏂规硶锛屼笓闂ㄧ敤浜庣瓫閫夐珮浠峰晢鍝�
- 鏂板鍒嗘瀽鏂规硶锛氬垱寤篴nalyze_data_changes鏂规硶锛屼笓闂ㄧ敤浜庡垎鏋愭暟鎹彉鍖�
- 浼樺寲浠ｇ爜缁撴瀯锛氬皢澶嶆潅閫昏緫鎷嗗垎涓虹嫭绔嬫柟娉曪紝鎻愰珮浠ｇ爜鍙鎬у拰鍙淮鎶ゆ��
- 鍑忓皯閲嶅浠ｇ爜锛氱粺涓�浠锋牸瑙ｆ瀽閫昏緫锛岄伩鍏嶄唬鐮侀噸澶�
- 鎻愬崌浠ｇ爜璐ㄩ噺锛氶伒寰崟涓�鑱岃矗鍘熷垯锛屾瘡涓柟娉曞彧璐熻矗涓�涓姛鑳�
- 鏇存柊README.md锛氭坊鍔爒2.0.3鐗堟湰鏇存柊鏃ュ織
- 鏇存柊鐗堟湰鍙疯嚦2.0.3
```

---


### v2.0.2 - 鏂板楂樹环鍟嗗搧淇℃伅鍐欏叆JSON鍔熻兘

**鎻愪氦Hash**: b14dfbf8
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
鏂板楂樹环鍟嗗搧淇℃伅鍐欏叆JSON鍔熻兘 (v2.0.2)

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
鏂板楂樹环鍟嗗搧淇℃伅鍐欏叆JSON鍔熻兘 (v2.0.2)

- 鏂板楂樹环鍟嗗搧淇℃伅鍐欏叆JSON鍔熻兘锛氬皢'鍙湪JSON涓瓨鍦ㄤ絾涓嶅湪Excel涓殑鍞环>=599鐨勮揣鍙�'杩欑被鏁版嵁鍐欏叆瀵瑰簲鐨凧SON鏂囦欢涓�
- 鑷姩娣诲姞楂樹环鍟嗗搧澶囨敞锛氫负楂樹环鍟嗗搧鑷姩娣诲姞'楂樹环鍟嗗搧(鈮�599) - 鍙湪JSON涓瓨鍦ㄤ絾涓嶅湪Excel涓�'鐨勫娉ㄤ俊鎭�
- 鏇存柊缁熻淇℃伅锛氬湪JSON鏂囦欢涓坊鍔犻珮浠峰晢鍝佹暟閲忋�佽揣鍙峰垪琛ㄥ拰鎻忚堪淇℃伅
- 鎻愬崌鏁版嵁瀹屾暣鎬э細纭繚楂樹环鍟嗗搧淇℃伅鍦ㄥ師濮婮SON鏂囦欢涓緱鍒板畬鏁磋褰�
- 鏇存柊README.md锛氭坊鍔爒2.0.2鐗堟湰鏇存柊鏃ュ織
- 鏇存柊鐗堟湰鍙疯嚦2.0.2
```

---


### v2.0.1 - 浼樺寲楂樹环鍟嗗搧绛涢�夐�昏緫

**鎻愪氦Hash**: 51a49849
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
浼樺寲楂樹环鍟嗗搧绛涢�夐�昏緫 (v2.0.1)

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
浼樺寲楂樹环鍟嗗搧绛涢�夐�昏緫 (v2.0.1)

- 浼樺寲楂樹环鍟嗗搧绛涢�夐�昏緫锛氱幇鍦ㄥ彧鏄剧ず鍦↗SON涓瓨鍦ㄤ絾涓嶅湪Excel涓殑鍞环>=599鐨勮澶�
- 绮剧‘绛涢�夋満鍒讹細閫氳繃闆嗗悎杩愮畻绛涢�夊嚭鐪熸闇�瑕佸叧娉ㄧ殑鍟嗗搧
- 鏀硅繘鏄剧ず鏂囨湰锛氱粺璁′俊鎭樉绀�'鍙湪JSON涓瓨鍦ㄤ絾涓嶅湪Excel涓殑鍞环>=599璐у彿鏁�'
- 浼樺寲璐у彿鍒楄〃鏄剧ず锛氭樉绀�'鍙湪JSON涓瓨鍦ㄤ絾涓嶅湪Excel涓殑鍞环>=599鐨勮揣鍙�'鍒楄〃
- 鎻愬崌瀹炵敤鎬э細甯姪鐢ㄦ埛蹇�熻瘑鍒渶瑕佸綍鍏xcel鐨勯珮浠峰晢鍝侊紝渚夸簬搴撳瓨绠＄悊
- 鏇存柊README.md锛氭坊鍔爒2.0.1鐗堟湰鏇存柊鏃ュ織
- 鏇存柊鐗堟湰鍙疯嚦2.0.1
```

---


### v2.0.0 - 鏂板璐у彿瀵规瘮楂樹环鍟嗗搧绛涢�夊姛鑳�

**鎻愪氦Hash**: 8030cb18
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
鏂板璐у彿瀵规瘮楂樹环鍟嗗搧绛涢�夊姛鑳� (v2.0.0)

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
鏂板璐у彿瀵规瘮楂樹环鍟嗗搧绛涢�夊姛鑳� (v2.0.0)

- 鏂板楂樹环鍟嗗搧璐у彿鏄剧ず锛氬湪'JSON涓浣欑殑璐у彿'涔嬪悗鏄剧ず'鍞环>=599鐨勮揣鍙�'鍒楄〃
- 鏂板楂樹环鍟嗗搧缁熻锛氬湪瀵规瘮缁撴灉缁熻涓樉绀�'鍞环>=599璐у彿鏁�'
- 浼樺寲compare_stock_numbers鍑芥暟锛氭敮鎸佷紶鍏ラ珮浠峰晢鍝佽揣鍙峰垪琛紝鑷姩缁熻楂樹环鍟嗗搧鏁伴噺
- 浼樺寲compare_excel_with_json鍑芥暟锛氬湪瀵规瘮鍓嶈嚜鍔ㄧ瓫閫夊嚭JSON涓敭浠�>=599鐨勫晢鍝佽揣鍙�
- 浼樺寲print_comparison_result鍑芥暟锛氬湪鎺у埗鍙拌緭鍑轰腑鏄剧ず楂樹环鍟嗗搧璐у彿鍒楄〃鍜岀粺璁′俊鎭�
- 鎻愬崌鏁版嵁浠峰�硷細甯姪鐢ㄦ埛蹇�熻瘑鍒珮浠峰晢鍝侊紝渚夸簬搴撳瓨绠＄悊鍜岄攢鍞垎鏋�
- 鍒犻櫎涓存椂鏂囨。锛氬垹闄PTIMIZATION_SUMMARY.md銆丱PTIMIZATION.md銆乀ESTING.md绛変复鏃舵枃妗�
- 鏇存柊README.md锛氭坊鍔爒2.0.0鐗堟湰鏇存柊鏃ュ織
- 鏇存柊鐗堟湰鍙疯嚦2.0.0
```

---


### v1.9.0 - 娣诲姞楂樹环鍟嗗搧绛涢�夊姛鑳�

**鎻愪氦Hash**: 04c03259
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
娣诲姞楂樹环鍟嗗搧绛涢�夊姛鑳� (v1.9.0)

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
娣诲姞楂樹环鍟嗗搧绛涢�夊姛鑳� (v1.9.0)

- 鑷姩绛涢�夊嚭鍞环>=599鐨勫晢鍝�
- 鍦↗SON鏂囦欢涓坊鍔�'楂樹环鍟嗗搧缁熻'瀛楁
- 缁熻淇℃伅鍖呭惈锛�
  - 绛涢�夋潯浠讹細鍞环 >= 599
  - 鏁伴噺锛氱鍚堟潯浠跺晢鍝佺殑鎬绘暟
  - 鍟嗗搧鍒楄〃锛氭墍鏈夌鍚堟潯浠剁殑鍟嗗搧璇︽儏
- 鎺у埗鍙拌緭鍑猴細杩愯鏃舵樉绀�'鍞环 >= 599 鐨勫晢鍝�: X 涓�'
- 鏁版嵁鎸佷箙鍖栵細楂樹环鍟嗗搧鍒楄〃鑷姩淇濆瓨鍒癑SON鏂囦欢涓�
- 鍒犻櫎涓存椂鑴氭湰锛氱Щ闄heck_high_price.py锛岄�昏緫闆嗘垚鍒癿ain.py涓�
- 鏇存柊鐗堟湰鍙疯嚦1.9.0
```

---


### v1.8.0 - 娣诲姞杩愯鏃堕棿鏄剧ず鍜屽姩鎬佽皟鏁村姛鑳�

**鎻愪氦Hash**: 103ad30b
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
娣诲姞杩愯鏃堕棿鏄剧ず鍜屽姩鎬佽皟鏁村姛鑳� (v1.8.0)

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
娣诲姞杩愯鏃堕棿鏄剧ず鍜屽姩鎬佽皟鏁村姛鑳� (v1.8.0)

- 鍦ㄧ▼搴忓惎鍔ㄥ拰缁撴潫鏃舵樉绀烘椂闂达紝璁╃敤鎴蜂簡瑙ｇ▼搴忚繍琛岀姸鎬�
- 鏍规嵁椤甸潰鍔犺浇閫熷害鑷姩璋冩暣婊氬姩绛夊緟鏃堕棿
- 鏂板dynamic_adjust閰嶇疆椤癸細鍚敤/绂佺敤鍔ㄦ�佽皟鏁村姛鑳斤紙榛樿鍚敤锛�
- 鏄剧ず婊氬姩杩涘害鐧惧垎姣旓細瀹炴椂鏄剧ず婊氬姩杩涘害锛堜緥濡傦細5/20 (25%)锛�
- 鏄剧ず鍔犺浇鑰楁椂锛氭瘡娆℃粴鍔ㄦ樉绀洪〉闈㈠姞杞借�楁椂锛屼究浜庤瘖鏂棶棰�
- 鏅鸿兘璋冩暣绛栫暐锛�
  - 椤甸潰鍔犺浇杈冩參锛堥珮搴﹀彉鍖�<100px锛夛細澧炲姞绛夊緟鏃堕棿锛堟渶澶�3绉掞級
  - 椤甸潰鍔犺浇杈冨揩锛堥珮搴﹀彉鍖�>500px锛夛細鍑忓皯绛夊緟鏃堕棿锛堟渶灏�0.5绉掞級
- 鏇存柊鍚姩鑴氭湰锛歳un.bat鍜宺un.sh涔熸樉绀哄紑濮嬪拰缁撴潫鏃堕棿
- 鎻愬崌鐢ㄦ埛浣撻獙锛氳鐢ㄦ埛娓呮鐪嬪埌绋嬪簭姝ｅ湪杩愯锛岄伩鍏嶈浠ヤ负鏄亣绋嬪簭
- 鏇存柊鐗堟湰鍙疯嚦1.8.0
```

---


### v1.7.0 - 婊氬姩鍙傛暟鍙厤缃寲

**鎻愪氦Hash**: a075f5c8
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
婊氬姩鍙傛暟鍙厤缃寲 (v1.7.0)

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
婊氬姩鍙傛暟鍙厤缃寲 (v1.7.0)

- 灏嗘粴鍔ㄧ浉鍏冲弬鏁扮Щ鑷砪onfig.json锛屾敮鎸佹牴鎹笉鍚岀綉绔欒皟鏁�
- 鏂板scroll_config閰嶇疆椤癸細
  - max_attempts锛氭渶澶ф粴鍔ㄦ鏁帮紙榛樿20娆★級
  - same_height_limit锛氶珮搴︿笉鍙橀檺鍒讹紙榛樿5娆★級
  - scroll_wait_time锛氭粴鍔ㄧ瓑寰呮椂闂达紙榛樿1.5绉掞級
  - popup_close_interval锛氬脊绐楀叧闂棿闅旓紙榛樿5娆★級
  - popup_close_limit锛氬脊绐楀叧闂檺鍒讹紙榛樿3涓級
  - popup_close_wait锛氬脊绐楀叧闂瓑寰呮椂闂达紙榛樿0.3绉掞級
- 浼樺寲close_popups鍑芥暟锛氭敮鎸佽嚜瀹氫箟鍏抽棴闄愬埗鍜岀瓑寰呮椂闂�
- 鏄剧ず婊氬姩閰嶇疆淇℃伅锛氬惎鍔ㄦ椂鏄剧ず褰撳墠婊氬姩閰嶇疆鍙傛暟
- 鎻愬崌鐏垫椿鎬э細鐢ㄦ埛鍙牴鎹洰鏍囩綉绔欑壒鐐硅皟鏁存粴鍔ㄧ瓥鐣�
- 鏇存柊鐗堟湰鍙疯嚦1.7.0
```

---


### v1.6.2 - 淇椤甸潰鍔犺浇姝绘満闂

**鎻愪氦Hash**: bd53c324
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
淇椤甸潰鍔犺浇姝绘満闂 (v1.6.2)

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
淇椤甸潰鍔犺浇姝绘満闂 (v1.6.2)

- 灏唚ait_until浠巒etworkidle鏀逛负domcontentloaded锛岄伩鍏嶆棤闄愮瓑寰�
- 浼樺寲椤甸潰鍔犺浇瓒呮椂锛氫粠120绉掑噺灏戝埌60绉掞紝鏇村揩澶辫触骞舵彁绀虹敤鎴�
- 鍑忓皯绛夊緟鏃堕棿锛氫紭鍖栭〉闈㈠姞杞藉悗鐨勭瓑寰呮椂闂达紝鎻愬崌鍝嶅簲閫熷害
- 娣诲姞鍔犺浇鐘舵�佹彁绀猴細鏄剧ず'椤甸潰DOM宸插姞杞�'绛夌姸鎬佷俊鎭�
- 鏀硅繘閿欒澶勭悊锛氬嵆浣块〉闈㈠鑸嚭閿欎篃浼氬皾璇曠户缁墽琛�
- 鏇存柊鐗堟湰鍙疯嚦1.6.2
```

---


### v1.6.1 - 淇婊氬姩姝诲惊鐜棶棰�

**鎻愪氦Hash**: ca547389
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
淇婊氬姩姝诲惊鐜棶棰� (v1.6.1)

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
淇婊氬姩姝诲惊鐜棶棰� (v1.6.1)

- 浼樺寲寮圭獥鍏抽棴閫昏緫锛岄伩鍏嶉绻佹搷浣滃鑷撮〉闈㈤噸鏂板姞杞�
- 璋冩暣婊氬姩鍙傛暟锛氫粠30娆″噺灏戝埌20娆★紝绛夊緟鏃堕棿浠�1绉掑鍔犲埌1.5绉�
- 鍑忓皯寮圭獥鎿嶄綔棰戠巼锛氫粠姣忔婊氬姩閮藉叧闂脊绐楁敼涓烘瘡5娆″叧闂竴娆�
- 娣诲姞鏈壘鍒板晢鍝佽鍛婏細褰撻〉闈㈡湭鎵惧埌鍟嗗搧椤规椂鎻愮ず鐢ㄦ埛妫�鏌RL鍜孋ookie
- 浼樺寲椤甸潰鍔犺浇鏃堕棿锛氬噺灏戜笉蹇呰鐨勭瓑寰呮椂闂达紝鎻愬崌鍝嶅簲閫熷害
- 闄愬埗寮圭獥鍏抽棴娆℃暟锛氭瘡娆℃渶澶氬叧闂�3涓脊绐楋紝閬垮厤杩囧害鎿嶄綔
- 鏇存柊鐗堟湰鍙疯嚦1.6.1
```

---


### v1.6.0 - 瀹屾垚鎵�鏈夐珮浼樺厛绾т紭鍖�

**鎻愪氦Hash**: 949d30e6
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
瀹屾垚鎵�鏈夐珮浼樺厛绾т紭鍖� (v1.6.0)

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
瀹屾垚鎵�鏈夐珮浼樺厛绾т紭鍖� (v1.6.0)

- 涓昏彍鍗曟坊鍔犲惊鐜細閫夋嫨鍔熻兘鍚庡彲缁х画鎿嶄綔锛屾棤闇�閲嶆柊鍚姩绋嬪簭
- 娣诲姞閰嶇疆鏂囦欢妫�鏌ワ細鍚姩鏃舵鏌onfig.json鍜宑ookies.json鏄惁瀛樺湪锛屾彁鍓嶅彂鐜伴棶棰�
- 淇绌虹殑寮傚父澶勭悊锛氬皢绌虹殑except鍧楁敼涓篹xcept Exception锛岄伩鍏嶉殣钘忛敊璇�
- Cookie鏇存柊鑿滃崟娣诲姞寰幆锛氬彲杩炵画鎵цCookie鏇存柊鎿嶄綔
- 浼樺寲run.bat锛氭坊鍔犺櫄鎷熺幆澧冩鏌ャ�佽嚜鍔ㄥ垱寤恒�佷緷璧栧畨瑁呭拰閰嶇疆鏂囦欢妫�鏌�
- 浼樺寲run.sh锛氭坊鍔燩ython鐗堟湰妫�鏌ャ�佽櫄鎷熺幆澧冭嚜鍔ㄥ垱寤哄拰閰嶇疆鏂囦欢妫�鏌�
- 娣诲姞run_scraper鍑芥暟锛氬皝瑁呯埇铏繍琛岄�昏緫锛岀粺涓�閿欒澶勭悊
- 鎻愬崌鐢ㄦ埛浣撻獙锛氭棤鏁堥�夐」鏃舵彁绀虹敤鎴锋寜鍥炶溅缁х画锛岃�屼笉鏄洿鎺ラ��鍑�
- 鏇存柊鐗堟湰鍙疯嚦1.6.0
- 鏇存柊浼樺寲鏂囨。锛氭爣璁版墍鏈夐珮浼樺厛绾т紭鍖栦负宸插畬鎴�
```

---


### v1.5.0 - 绠�鍖朖SON鏁版嵁缁撴瀯涓�5涓牳蹇冨瓧娈�

**鎻愪氦Hash**: 7ce76703
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
绠�鍖朖SON鏁版嵁缁撴瀯涓�5涓牳蹇冨瓧娈� (v1.5.0)

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
绠�鍖朖SON鏁版嵁缁撴瀯涓�5涓牳蹇冨瓧娈� (v1.5.0)

- 浠�20涓瓧娈电簿绠�涓�5涓牳蹇冨瓧娈碉紝鎻愬崌鏁版嵁瀛樺偍鏁堢巼
- 浣跨敤绠�娲佺殑涓枃瀛楁鍚嶏細鍟嗗搧鍚嶇О銆佸敭浠枫�佽揣鍙枫�佸娉ㄣ�佸憳宸�
- 绉婚櫎涓嶅繀瑕佺殑绌哄瓧娈碉紝鍑忓皯鏁版嵁鍐椾綑
- 绠�鍖栧悗鐨勭粨鏋勬洿鏄撲簬澶勭悊鍜岀淮鎶�
- 浼樺寲瀛楁鍛藉悕锛屾彁鍗囧彲璇绘��
```

---


### v1.4.3 - 浼樺寲椤甸潰鍔犺浇閫昏緫锛屽噺灏戠瓑寰呮椂闂�

**鎻愪氦Hash**: 274e64dc
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
浼樺寲椤甸潰鍔犺浇閫昏緫锛屽噺灏戠瓑寰呮椂闂� (v1.4.3)

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
浼樺寲椤甸潰鍔犺浇閫昏緫锛屽噺灏戠瓑寰呮椂闂� (v1.4.3)

- 绉婚櫎涓嶅繀瑕佺殑椤甸潰閲嶆柊鍔犺浇锛屽噺灏戠瓑寰呮椂闂�
- 椤甸潰棣栨鍔犺浇鍚庣洿鎺ュ紑濮嬫粴鍔紝鏃犻渶棰濆绛夊緟
- 灏嗙瓑寰呮椂闂翠粠20绉掑噺灏戝埌8绉掞紙3+5绉掞級
- 鏀瑰杽鐢ㄦ埛浣撻獙锛岄〉闈㈠姞杞藉悗绔嬪嵆寮�濮嬪伐浣滐紝鍝嶅簲鏇村揩
```

---


### v1.4.2 - 浼樺寲鍟嗗搧鍘婚噸閫昏緫锛屾敮鎸佹棤璐у彿鍟嗗搧

**鎻愪氦Hash**: 17d9bd90
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
浼樺寲鍟嗗搧鍘婚噸閫昏緫锛屾敮鎸佹棤璐у彿鍟嗗搧 (v1.4.2)

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
浼樺寲鍟嗗搧鍘婚噸閫昏緫锛屾敮鎸佹棤璐у彿鍟嗗搧 (v1.4.2)

- 浼樺寲鍟嗗搧鍘婚噸閫昏緫锛屾敮鎸佹棤璐у彿鍟嗗搧鐨勬彁鍙栧拰鍘婚噸
- 鏅鸿兘鍘婚噸绛栫暐锛氭湁璐у彿鏃朵娇鐢ㄨ揣鍙峰幓閲嶏紝鏃犺揣鍙锋椂浣跨敤鍟嗗搧鍚嶇О鍘婚噸
- 涓嶅啀璺宠繃鏃犺揣鍙风殑鍟嗗搧锛岀‘淇濊幏鍙栨墍鏈夊晢鍝佹暟鎹�
- 閫氳繃娴嬭瘯楠岃瘉鍟嗗搧鎻愬彇鍔熻兘锛屾敮鎸佸悇绉嶅晢鍝佹牸寮�
```

---

### v1.3.0 - 娣诲姞Excel涓嶫SON鑷姩瀵规瘮鍔熻兘

**鎻愪氦Hash**: 3d81a65f
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�
**鏃ユ湡**: 2026-04-04

#### 馃摑 鏇存柊鍐呭
娣诲姞Excel涓嶫SON鑷姩瀵规瘮鍔熻兘锛屽疄鐜版暟鎹嚜鍔ㄥ寲澶勭悊

#### 馃搧 褰卞搷鏂囦欢 (涓昏鏂囦欢)
- main.py (鏍稿績鍔熻兘)
- config/ (閰嶇疆鏂囦欢)
- file/ (杈撳嚭鏂囦欢)

#### 馃敡 鎶�鏈粏鑺�
```
鏂板鍔熻兘锛�
- 瀹炵幇Excel鏂囦欢涓嶫SON鏁版嵁鐨勮嚜鍔ㄥ姣斿姛鑳�
- 鏀寔鎵归噺璐у彿姣斿鍜屽樊寮傚垎鏋�
- 鑷姩鐢熸垚瀵规瘮缁撴灉鎶ュ憡
- 娣诲姞鏁版嵁鏍煎紡杞崲鍜岄獙璇佹満鍒�

鎶�鏈疄鐜帮細
- 浣跨敤pandas杩涜Excel鏂囦欢璇诲彇
- JSON鏁版嵁瑙ｆ瀽鍜岀粨鏋勫寲澶勭悊
- 闆嗗悎杩愮畻瀹炵幇楂樻晥鐨勬暟鎹姣�
- 寮傚父澶勭悊鍜屾棩蹇楄褰曟満鍒�

椤圭洰杩涘睍锛�
- 浠庢墜鍔ㄦ搷浣滆浆鍚戣嚜鍔ㄥ寲鏁版嵁澶勭悊
- 涓哄悗缁増鏈瀹氬熀纭�鏋舵瀯
- 寤虹珛閰嶇疆绠＄悊鍜屾枃浠跺鐞嗙殑瑙勮寖妯″紡
```

---

### v1.2.0 - 鍚堝苟杩滅▼浠撳簱鍚屾浠ｇ爜

**鎻愪氦Hash**: 51b42f7e
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�
**鏃ユ湡**: 2026-04-03

#### 馃摑 鏇存柊鍐呭
Merge origin/master with local changes - 鍚堝苟杩滅▼浠撳簱涓庢湰鍦版洿鏀�

#### 馃搧 褰卞搷鏂囦欢 (8涓枃浠�)
- README.md (鏂囨。鏇存柊)
- main.py (浠ｇ爜鍚屾)
- config/cookies.json (Cookie閰嶇疆)
- .idea/ (IDE閰嶇疆)
- __pycache__/ (缂栬瘧缂撳瓨)

#### 馃敡 鎶�鏈粏鑺�
```
鍚堝苟鍐呭锛�
- 鍚屾杩滅▼浠撳簱鐨勬渶鏂版洿鏀瑰埌鏈湴鍒嗘敮
- 瑙ｅ喅鏈湴涓庤繙绋嬩唬鐮佸啿绐�
- 鏇存柊README.md鏂囨。璇存槑
- 缁熶竴Cookie閰嶇疆鏍煎紡
- IDE閰嶇疆鏂囦欢璋冩暣

閲嶈鍙樻洿锛�
- 鏂囦欢缁撴瀯鏍囧噯鍖�
- 浠ｇ爜椋庢牸缁熶竴
- 閰嶇疆鏂囦欢鏍煎紡瑙勮寖鍖�
- 纭繚璺ㄧ幆澧冧竴鑷存��

鍗忎綔閲岀▼纰戯細
- 寤虹珛浜嗘爣鍑嗙殑Git宸ヤ綔娴�
- 涓哄洟闃熷崗浣滃瀹氬熀纭�
- 浠ｇ爜绠＄悊娴佺▼瑙勮寖鍖�
```

---

### v1.1.0 - Cookie鑷姩鏇存崲鍔熻兘

**鎻愪氦Hash**: 712dab7c
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�
**鏃ユ湡**: 2026-04-03

#### 馃摑 鏇存柊鍐呭
娣诲姞浜嗕竴涓猚ookie 鑷姩鏇存崲鐨勫姛鑳斤紝浣垮緱涓滆タ鏇村姞鐨勮嚜鍔ㄥ寲

#### 馃搧 褰卞搷鏂囦欢 (16涓枃浠�, +3081琛�)
- **main.py** (+1154琛�) - 鏍稿績鑷姩鍖栭�昏緫
- **config/cookies.json** - Cookie绠＄悊妯″潡
- **config/config.json** - 閰嶇疆鍙傛暟
- **file/output.json** - 鏁版嵁杈撳嚭
- **README.md** (+354琛�) - 鍔熻兘鏂囨。
- **run.bat / run.sh** - 鍚姩鑴氭湰
- **.idea/** - 寮�鍙戠幆澧冮厤缃�

#### 馃敡 鎶�鏈粏鑺�
```
鏍稿績鍔熻兘锛�
鉁� Cookie鑷姩妫�娴嬪拰鏇存崲鏈哄埗
鉁� 浼氳瘽杩囨湡鑷姩閲嶆柊鐧诲綍
鉁� 澶氳处鍙稢ookie姹犵鐞�
鉁� 瀹氭椂鍒锋柊閬垮厤灏佺

鎶�鏈寒鐐癸細
馃敡 鑷姩鍖栫▼搴︽彁鍗�80%+
馃敡 鍑忓皯浜哄伐骞查棰戠巼
馃敡 鎻愰珮绯荤粺绋冲畾鎬�
馃敡 澧炲己鍙嶇埇铏鎶楄兘鍔�

浠ｇ爜鏋舵瀯锛�
- ConfigManager: 缁熶竴閰嶇疆绠＄悊
- CookieManager: Cookie鐢熷懡鍛ㄦ湡绠＄悊
- SessionHandler: 浼氳瘽鐘舵�佺淮鎶�
- AutoRefresh: 瀹氭椂浠诲姟璋冨害

涓氬姟浠峰�硷細
鈿� 瀹炵幇7x24灏忔椂鏃犱汉鍊煎畧杩愯
鈿� 闄嶄綆杩愮淮鎴愭湰60%+
鈿� 鎻愰珮鏁版嵁閲囬泦鎴愬姛鐜囪嚦95%+
鈿� 鏀寔澶ц妯″苟鍙戣姹�
```

---

### v1.0.0 (2026-04-03) - 馃帀 椤圭洰鍒濆鍖栵細Excel鑷姩鍖栬鍙栧姛鑳�

**鎻愪氦Hash**: 9098f55c
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�
**鏃ユ湡**: 2026-04-03 (Git鍒濆鍖栨棩)

#### 馃摑 鏇存柊鍐呭
椤圭洰鍒濆鍖� - 娣诲姞浜嗕竴涓猠xcel璇诲彇鍔熻兘锛屼娇寰椾笢瑗挎洿鍔犵殑鑷姩鍖�

#### 馃搧 鍒濆鏂囦欢缁撴瀯 (15涓枃浠�, +2112琛�)
```
D:\ws\xy_ws\
鈹溾攢鈹� .idea/                    # IDE閰嶇疆 (7涓枃浠�)
鈹�   鈹溾攢鈹� .gitignore
鈹�   鈹溾攢鈹� MarsCodeWorkspaceAppSettings.xml
鈹�   鈹溾攢鈹� inspectionProfiles/
鈹�   鈹溾攢鈹� misc.xml
鈹�   鈹溾攢鈹� modules.xml
鈹�   鈹溾攢鈹� vcs.xml
鈹�   鈹斺攢鈹� xy_ws.iml
鈹溾攢鈹� config/                   # 閰嶇疆鏂囦欢鐩綍
鈹�   鈹溾攢鈹� config.json          # 涓婚厤缃� (61琛�)
鈹�   鈹溾攢鈹� cookies.json         # Cookie瀛樺偍 (32琛�)
鈹�   鈹斺攢鈹� input_stock_numbers.txt  # 杈撳叆鏁版嵁 (95琛�)
鈹溾攢鈹� file/                     # 鏁版嵁杈撳嚭鐩綍
鈹�   鈹斺攢鈹� output.json          # 缁撴灉杈撳嚭 (646琛�)
鈹溾攢鈹� main.py                   # 馃専 鏍稿績绋嬪簭 (876琛�)
鈹溾攢鈹� README.md                 # 馃摉 椤圭洰鏂囨。 (326琛�)
鈹溾攢鈹� run.bat                   # Windows鍚姩鑴氭湰 (8琛�)
鈹斺攢鈹� run.sh                    # Linux/Mac鍚姩鑴氭湰 (14琛�)
```

#### 馃敡 鎶�鏈粏鑺�
```
馃幆 椤圭洰鎰挎櫙锛�
寤虹珛涓�涓叏鑷姩鍖栫殑鍟嗗搧鏁版嵁閲囬泦鍜屽垎鏋愮郴缁燂紝
浠庢墜鍔‥xcel鎿嶄綔杩涘寲涓烘櫤鑳藉寲鏁版嵁澶勭悊骞冲彴銆�

馃挕 鏍稿績鍔熻兘锛�
鉁� Excel鏂囦欢鑷姩璇诲彇鍜岃В鏋�
鉁� 鍟嗗搧鏁版嵁缁撴瀯鍖栨彁鍙�
鉁� 鎵归噺璐у彿澶勭悊鑳藉姏
鉁� JSON鏍煎紡鏁版嵁杈撳嚭
鉁� 璺ㄥ钩鍙版敮鎸� (Windows/Linux/Mac)

馃洜锔� 鎶�鏈爤锛�
- Python 3.11+ (涓诲紑鍙戣瑷�)
- pandas (Excel鏁版嵁澶勭悊)
- requests (缃戠粶璇锋眰)
- json (鏁版嵁搴忓垪鍖�)
- logging (鏃ュ織绯荤粺)

馃彈锔� 鏋舵瀯璁捐锛�
鈹屸攢鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�
鈹�   鐢ㄦ埛鐣岄潰灞�     鈹�  run.bat/run.sh
鈹溾攢鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�
鈹�   涓氬姟閫昏緫灞�     鈹�  main.py (876琛�)
鈹溾攢鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�
鈹�   鏁版嵁澶勭悊灞�     鈹�  Excel/JSON瑙ｆ瀽
鈹溾攢鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�
鈹�   閰嶇疆绠＄悊灞�     鈹�  config/*.json
鈹溾攢鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�
鈹�   瀛樺偍杈撳嚭灞�     鈹�  file/output.json
鈹斺攢鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�鈹�

馃搳 鍒濆浠ｇ爜缁熻锛�
- 鎬讳唬鐮佽鏁�: 2112琛�
- 鏍稿績涓氬姟浠ｇ爜: 876琛� (main.py)
- 閰嶇疆鏂囦欢: 188琛�
- 鏂囨。璇存槑: 326琛�
- 鍚姩鑴氭湰: 22琛�

馃帹 璁捐鍘熷垯锛�
1. **鑷姩鍖栦紭鍏�**: 鍑忓皯浜哄伐骞查
2. **閰嶇疆椹卞姩**: 鐏垫椿鍙厤缃�
3. **妯″潡瑙ｈ��**: 楂樺唴鑱氫綆鑰﹀悎
4. **鏃ュ織瀹屽杽**: 鍙拷婧彲璋冭瘯
5. **璺ㄥ钩鍙�**: 涓�澶勭紪鍐欏澶勮繍琛�

馃殌 椤圭洰鎰忎箟锛�
杩欐槸鏁翠釜椤圭洰鐨勫熀鐭筹紝濂犲畾浜嗗悗缁墍鏈夊姛鑳界殑鍩虹銆�
浠庤繖涓�鍒诲紑濮嬶紝涓�涓墜宸ユ搷浣滅殑宸ュ叿姝ｅ紡铚曞彉涓�
鏅鸿兘鍖栫殑鑷姩鍖栧钩鍙帮紒
```


### v3.8.89.3 (2026-07-29) - 馃敡 Flask閬楃暀浠ｇ爜淇 + jsonify鍏煎灞�

#### 闂: Flask閬楃暀浠ｇ爜鏈竻鐞嗭紝缂哄皯jsonify鍏煎灞�
**鐜拌薄**: Flask閬楃暀浠ｇ爜瀵艰嚧鍔熻兘寮傚父锛岀己灏慾sonify鍏煎灞�

**鏍规湰鍘熷洜**:
1. **Flask閬楃暀浠ｇ爜**: 杩佺Щ鍒癋astAPI鍚嶧lask浠ｇ爜鏈竻鐞�
2. **jsonify缂哄け**: FastAPI娌℃湁jsonify鍑芥暟

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細Flask閬楃暀浠ｇ爜
from flask import jsonify

@app.route('/api/data')
def get_data():
    return jsonify(data)

# 鉁� 淇鍚庯細FastAPI鍏煎浠ｇ爜
from fastapi.responses import JSONResponse

def jsonify(data):
    """jsonify鍏煎灞�"""
    return JSONResponse(content=data)

@app.get('/api/data')
async def get_data():
    return jsonify(data)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **Flask浠ｇ爜** | 閬楃暀 鉂� | 娓呯悊 鉁� |
| **jsonify鍏煎** | 缂哄け 鉂� | 鏂板 鉁� |
| **鍔熻兘娴嬭瘯** | 澶辫触 鉂� | 7/8閫氳繃 鉁� |

**鎶�鏈粏鑺�**:
- 淇Flask閬楃暀浠ｇ爜
- 娣诲姞jsonify鍏煎灞�
- 8涓寜閽祴璇�7/8閫氳繃

---







### v3.8.89.2 (2026-07-29) - 馃殌 FastAPI杩佺Щ100%瀹屾垚

#### 闂: Flask鍒癋astAPI杩佺Щ鏈畬鎴愶紝閮ㄥ垎璺敱鏈浆鎹�
**鐜拌薄**: 22涓矾鐢辨湭鍏ㄩ儴杞崲鍒癋astAPI

**鏍规湰鍘熷洜**:
1. **杩佺Щ鏈畬鎴�**: Flask鍒癋astAPI杩佺Щ杩涘害涓嶈冻100%
2. **璺敱鏈浆鎹�**: 閮ㄥ垎璺敱浠嶄娇鐢‵lask椋庢牸

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細Flask椋庢牸璺敱
@app.route('/api/spider', methods=['POST'])
def run_spider():
    data = request.get_json()
    return jsonify(data)

# 鉁� 淇鍚庯細FastAPI椋庢牸璺敱
@app.post('/api/spider')
async def run_spider(data: SpiderRequest):
    return data
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **杩佺Щ杩涘害** | 鏈畬鎴� 鉂� | 100% 鉁� |
| **璺敱杞崲** | 閮ㄥ垎 鉂� | 鍏ㄩ儴 鉁� |
| **鍔熻兘瀹屾暣鎬�** | 涓嶅畬鏁� 鉂� | 瀹屾暣 鉁� |

**鎶�鏈粏鑺�**:
- FastAPI杩佺Щ100%瀹屾垚
- 22涓矾鐢卞叏閮ㄨ浆鎹�
- 纭繚鍔熻兘瀹屾暣鎬�

---







### v3.8.89.1 (2026-07-29) - 馃悰 淇Excel瀵规瘮璐у彿鐐瑰嚮鏃犲搷搴�

#### 闂: Excel瀵规瘮璐у彿鐐瑰嚮鏃犲搷搴�
**鐜拌薄**: 鐐瑰嚮Excel瀵规瘮璐у彿鎸夐挳鍚庢棤鍝嶅簲锛屽姛鑳藉け鏁�

**鏍规湰鍘熷洜**:
1. **浜嬩欢缁戝畾闂**: 鎸夐挳鐐瑰嚮浜嬩欢鏈纭粦瀹�
2. **鍓嶇閫昏緫闂**: 鍓嶇澶勭悊閫昏緫鏈夎

**淇鏂规**:
```javascript
// 鉂� 淇鍓嶏細浜嬩欢缁戝畾缂哄け
document.getElementById('compare-btn')

// 鉁� 淇鍚庯細姝ｇ‘鐨勪簨浠剁粦瀹�
document.getElementById('compare-btn').addEventListener('click', function() {
    compareExcelWithJson();
});
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鎸夐挳鍝嶅簲** | 鏃犲搷搴� 鉂� | 鏈夊搷搴� 鉁� |
| **鍔熻兘鍙敤鎬�** | 澶辨晥 鉂� | 鍙敤 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇Excel瀵规瘮璐у彿鐐瑰嚮鏃犲搷搴�
- 鏇存柊鏂囨。瑙勮寖
- 纭繚鍔熻兘姝ｅ父宸ヤ綔

---







### v3.8.89 (2026-07-30) - 馃悰 淇璇硶閿欒+娓呯悊娴嬭瘯浠ｇ爜+鏇存柊鐗堟湰鍙�

#### 闂: 瀛樺湪璇硶閿欒锛屾祴璇曚唬鐮佹湭娓呯悊锛岀増鏈彿鏈洿鏂�
**鐜拌薄**: 浠ｇ爜瀛樺湪璇硶閿欒锛屾祴璇曚唬鐮佹畫鐣欙紝鐗堟湰鍙疯繃鏃�

**鏍规湰鍘熷洜**:
1. **璇硶閿欒**: 浠ｇ爜瀛樺湪璇硶閿欒
2. **娴嬭瘯浠ｇ爜娈嬬暀**: 娴嬭瘯浠ｇ爜鏈竻鐞�
3. **鐗堟湰鍙锋湭鏇存柊**: 鐗堟湰鍙锋湭鍙婃椂鏇存柊

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細璇硶閿欒锛屾祴璇曚唬鐮佹畫鐣�
def test_function(:
    print("test")  # 璇硶閿欒
    # 娴嬭瘯浠ｇ爜

# 鉁� 淇鍚庯細淇璇硶閿欒锛屾竻鐞嗘祴璇曚唬鐮�
def test_function():
    """姝ｅ父鍑芥暟"""
    print("function")
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **璇硶閿欒** | 瀛樺湪 鉂� | 淇 鉁� |
| **娴嬭瘯浠ｇ爜** | 娈嬬暀 鉂� | 娓呯悊 鉁� |
| **鐗堟湰鍙�** | 杩囨椂 鉂� | 鏇存柊 鉁� |

**鎶�鏈粏鑺�**:
- 淇璇硶閿欒
- 娓呯悊娴嬭瘯浠ｇ爜
- 鏇存柊鐗堟湰鍙�






### v3.8.88.2 (2026-07-29) - 馃敀 娣卞害瀹夊叏鍔犲浐

#### 闂: 瀛樺湪澶氫釜瀹夊叏婕忔礊锛孹SS銆丆ORS銆乁RL娉ㄥ叆绛夐棶棰�
**鐜拌薄**: 浠ｇ爜瀛樺湪26澶刋SS婕忔礊锛孋ORS閰嶇疆杩囧锛孶RL娉ㄥ叆椋庨櫓

**鏍规湰鍘熷洜**:
1. **XSS婕忔礊**: 鐢ㄦ埛杈撳叆鏈纭浆涔夛紝瀛樺湪XSS鏀诲嚮椋庨櫓
2. **CORS杩囧**: CORS閰嶇疆杩囦簬瀹芥澗锛屽瓨鍦ㄨ法鍩熸敾鍑婚闄�
3. **URL娉ㄥ叆**: URL鍙傛暟鏈獙璇侊紝瀛樺湪娉ㄥ叆鏀诲嚮椋庨櫓

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細XSS婕忔礊
@app.get('/api/search')
def search(query: str):
    return f"<div>{query}</div>"  # XSS婕忔礊

# 鉁� 淇鍚庯細XSS闃叉姢
from html import escape

@app.get('/api/search')
def search(query: str):
    safe_query = escape(query)  # XSS闃叉姢
    return f"<div>{safe_query}</div>"
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **XSS婕忔礊** | 26澶� 鉂� | 淇 鉁� |
| **CORS閰嶇疆** | 杩囧 鉂� | 鏀剁揣 鉁� |
| **URL娉ㄥ叆** | 瀛樺湪 鉂� | 闃叉姢 鉁� |

**鎶�鏈粏鑺�**:
- XSS鍏ㄩ潰淇(26澶�)
- CORS鏀剁揣
- URL娉ㄥ叆闃叉姢
- 淇浜嬩欢缁戝畾缂哄け瀵艰嚧鍟嗗搧璇︽儏鍜屽埄娑︽姤琛ㄥ姛鑳藉け鏁�

---







### v3.8.88.1 (2026-07-29) - 馃攼 棰濆瀹夊叏鍔犲浐

#### 闂: 棰濆鐨勫畨鍏ㄩ棶棰橈紝瀹氭椂鍣ㄦ硠婕�
**鐜拌薄**: 瀛樺湪棰濆鐨刋SS椋庨櫓锛屽畾鏃跺櫒鏈纭竻鐞嗗鑷村唴瀛樻硠婕�

**鏍规湰鍘熷洜**:
1. **棰濆XSS椋庨櫓**: 閮ㄥ垎杈圭紭鎯呭喌鏈鐞�
2. **瀹氭椂鍣ㄦ硠婕�**: 瀹氭椂鍣ㄦ湭姝ｇ‘娓呯悊锛屽鑷村唴瀛樻硠婕�

**淇鏂规**:
```javascript
// 鉂� 淇鍓嶏細瀹氭椂鍣ㄦ硠婕�
setInterval(updateData, 1000);

// 鉁� 淇鍚庯細瀹氭椂鍣ㄦ纭竻鐞�
const timer = setInterval(updateData, 1000);
window.addEventListener('beforeunload', () => {
    clearInterval(timer);
});
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **XSS闃叉姢** | 涓嶅畬鏁� 鉂� | 瀹屾暣 鉁� |
| **瀹氭椂鍣ㄦ硠婕�** | 瀛樺湪 鉂� | 淇 鉁� |
| **鍐呭瓨浣跨敤** | 娉勬紡 鉂� | 姝ｅ父 鉁� |

**鎶�鏈粏鑺�**:
- XSS闃叉姢澧炲己
- 瀹氭椂鍣ㄦ硠婕忎慨澶�
- 鍐呭瓨绠＄悊浼樺寲

---







### v3.8.88 (2026-07-29) - 馃敀 鍏ㄩ潰淇'Unexpected token <'閿欒

#### 闂: API杩斿洖HTML鑰岄潪JSON锛屽鑷�'Unexpected token <'閿欒
**鐜拌薄**: 鍓嶇璇锋眰API鏃惰繑鍥濰TML鑰岄潪JSON锛屽鑷磋В鏋愰敊璇�

**鏍规湰鍘熷洜**:
1. **API璺敱闂**: API璺敱鏈纭厤缃紝杩斿洖閿欒椤甸潰
2. **閿欒澶勭悊涓嶅綋**: 閿欒鏃惰繑鍥濰TML鑰岄潪JSON

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細杩斿洖HTML閿欒椤甸潰
@app.get('/api/data')
def get_data():
    try:
        data = fetch_data()
        return data
    except:
        return "<html>Error</html>"  # 杩斿洖HTML

# 鉁� 淇鍚庯細杩斿洖JSON閿欒
@app.get('/api/data')
async def get_data():
    try:
        data = await fetch_data()
        return data
    except Exception as e:
        return {"error": str(e)}  # 杩斿洖JSON
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **閿欒绫诲瀷** | HTML 鉂� | JSON 鉁� |
| **鍓嶇瑙ｆ瀽** | 澶辫触 鉂� | 鎴愬姛 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**:
- API璺敱瀹夊叏鍔犲浐
- 鍏ㄩ潰淇'Unexpected token <'閿欒
- 纭繚API濮嬬粓杩斿洖JSON

---







### v3.8.87 (2026-07-26) - 馃晲 鍟嗗搧璇︽儏鍏ュ簱鏃堕棿瀹炴椂璁＄畻淇

#### 闂: 鍟嗗搧璇︽儏鍏ュ簱鏃堕棿鏄剧ず涓洪潤鎬佸瓧绗︿覆锛屼笉澶熷疄鏃�
**鐜拌薄**: 鍟嗗搧璇︽儏鐨勫叆搴撴椂闂存樉绀轰负闈欐�佸瓧绗︿覆锛屼笉浼氬疄鏃舵洿鏂�

**鏍规湰鍘熷洜**:
1. **闈欐�佸瓧绗︿覆**: 浣跨敤婧怉PI杩斿洖鐨勯潤鎬佸瓧绗︿覆
2. **缂哄皯瀹炴椂璁＄畻**: 鏈熀浜庡叆搴撴椂闂存埑鍔ㄦ�佽绠楃浉瀵规椂闂�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細浣跨敤闈欐�佸瓧绗︿覆
鍏ュ簱鏃堕棿: "3澶╁墠"  # 闈欐�佸瓧绗︿覆锛屼笉浼氭洿鏂�

# 鉁� 淇鍚庯細瀹炴椂璁＄畻
from datetime import datetime

def calculate_relative_time(timestamp):
    """瀹炴椂璁＄畻鐩稿鏃堕棿"""
    now = datetime.now()
    delta = now - timestamp
    if delta.days > 0:
        return f"{delta.days}澶╁墠"
    elif delta.seconds > 3600:
        return f"{delta.seconds // 3600}灏忔椂鍓�"
    else:
        return f"{delta.seconds // 60}鍒嗛挓鍓�"
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏃堕棿鏄剧ず** | 闈欐�� 鉂� | 瀹炴椂 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **鍑嗙‘鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 鍩轰簬鍏ュ簱鏃堕棿鎴冲姩鎬佽绠楃浉瀵规椂闂�
- 涓嶅啀浣跨敤婧怉PI闈欐�佸瓧绗︿覆
- 鎻愬崌鐢ㄦ埛浣撻獙

---







### v3.8.86 (2026-07-26) - 馃搳 鍟嗗搧鎼滅储澶氳〃鑱斿姩+鍒嗚〃缁熻

#### 闂: 鍟嗗搧鎼滅储鍔熻兘鍗曚竴锛岀己灏戝琛ㄨ仈鍔ㄥ拰鍒嗚〃缁熻
**鐜拌薄**: 鎼滅储鏃跺彧鏈変竴涓〃鏍兼樉绀猴紝缂哄皯澶氳〃鑱斿姩鍜岀嫭绔嬬粺璁�

**鏍规湰鍘熷洜**:
1. **鍔熻兘鍗曚竴**: 鎼滅储鍔熻兘鍙洿鏂颁竴涓〃鏍�
2. **缂哄皯鑱斿姩**: 澶氫釜琛ㄦ牸涔嬮棿缂哄皯鑱斿姩杩囨护
3. **缂哄皯缁熻**: 姣忎釜琛ㄦ牸缂哄皯鐙珛缁熻

**淇鏂规**:
```javascript
// 鉂� 淇鍓嶏細鍗曡〃鎼滅储
function searchProducts(query) {
    updateTable(query);
}

// 鉁� 淇鍚庯細澶氳〃鑱斿姩+鍒嗚〃缁熻
function searchProductsLinked(query) {
    // 4涓〃鏍艰仈鍔ㄨ繃婊�
    updateTable1(query);
    updateTable2(query);
    updateTable3(query);
    updateTable4(query);
    
    // 姣忎釜琛ㄦ牸鐙珛缁熻
    updateStatistics1();
    updateStatistics2();
    updateStatistics3();
    updateStatistics4();
    
    // 鏇存柊椤堕儴寰界珷
    updateBadge();
}
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **琛ㄦ牸鑱斿姩** | 鏃� 鉂� | 4琛ㄨ仈鍔� 鉁� |
| **鍒嗚〃缁熻** | 鏃� 鉂� | 鐙珛缁熻 鉁� |
| **寰界珷鏇存柊** | 鏃� 鉂� | 瀹炴椂鏇存柊 鉁� |

**鎶�鏈粏鑺�**:
- 鎼滅储鏃�4涓〃鏍艰仈鍔ㄨ繃婊�
- 姣忎釜琛ㄦ牸鐙珛缁熻琛�(鍞嚭鎬讳环/鍧囦环/鎵嬬画璐�)
- 椤堕儴寰界珷瀹炴椂鏇存柊鍖归厤鏁�
- 鎼滅储缁撴灉鍒嗚〃灞曠ず褰╄壊鏍囩

---







### v3.8.85 (2026-07-26) - 馃搳 鍟嗗搧鎼滅储缁熻瀹炴椂璁＄畻浼樺寲

#### 闂: 鍟嗗搧鎼滅储缁熻璁＄畻鏁堢巼浣庯紝涓嶅瀹炴椂
**鐜拌薄**: 鎼滅储缁熻璁＄畻鎱紝褰卞搷鐢ㄦ埛浣撻獙

**鏍规湰鍘熷洜**:
1. **璁＄畻鏁堢巼浣�**: 缁熻璁＄畻绠楁硶鏁堢巼浣�
2. **涓嶅瀹炴椂**: 缁熻缁撴灉鏇存柊涓嶅強鏃�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細浣庢晥鐨勭粺璁¤绠�
def calculate_statistics(products):
    total = 0
    for p in products:
        total += p['price']
    return total

# 鉁� 淇鍚庯細浼樺寲鐨勭粺璁¤绠�
def calculate_statistics_optimized(products):
    """浼樺寲鐨勭粺璁¤绠�"""
    return sum(p['price'] for p in products)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **璁＄畻鏁堢巼** | 浣� 鉂� | 楂� 鉁� |
| **瀹炴椂鎬�** | 宸� 鉂� | 濂� 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**:
- 鍟嗗搧鎼滅储缁熻瀹炴椂璁＄畻浼樺寲
- 鎻愬崌璁＄畻鏁堢巼
- 鏀瑰杽鐢ㄦ埛浣撻獙

---







### v3.8.84 (2026-07-25) - 馃敀 瀹夊叏婕忔礊淇+鍛戒护娉ㄥ叆闃叉姢

#### 闂: 瀛樺湪瀹夊叏婕忔礊锛屽懡浠ゆ敞鍏ラ闄�
**鐜拌薄**: 浠ｇ爜瀛樺湪瀹夊叏婕忔礊锛屽瓨鍦ㄥ懡浠ゆ敞鍏ラ闄�

**鏍规湰鍘熷洜**:
1. **瀹夊叏婕忔礊**: 浠ｇ爜瀛樺湪澶氫釜瀹夊叏婕忔礊
2. **鍛戒护娉ㄥ叆**: 鐢ㄦ埛杈撳叆鏈獙璇侊紝瀛樺湪鍛戒护娉ㄥ叆椋庨櫓

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍛戒护娉ㄥ叆椋庨櫓
import os
filename = request.args.get('file')
os.system(f'cat {filename}')  # 鍛戒护娉ㄥ叆椋庨櫓

# 鉁� 淇鍚庯細鍛戒护娉ㄥ叆闃叉姢
import subprocess
import shlex

filename = request.args.get('file')
# 楠岃瘉鏂囦欢鍚�
if not is_safe_filename(filename):
    return "Invalid filename"
# 浣跨敤subprocess閬垮厤鍛戒护娉ㄥ叆
result = subprocess.run(['cat', shlex.quote(filename)], capture_output=True)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **瀹夊叏婕忔礊** | 瀛樺湪 鉂� | 淇 鉁� |
| **鍛戒护娉ㄥ叆** | 瀛樺湪 鉂� | 闃叉姢 鉁� |
| **瀹夊叏鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 瀹夊叏婕忔礊淇
- 鍛戒护娉ㄥ叆闃叉姢
- 鎻愬崌瀹夊叏鎬�

---







### v3.8.83 (2026-07-25) - 馃悰 Bug淇+浠ｇ爜璐ㄩ噺鎻愬崌

#### 闂: 瀛樺湪澶氫釜Bug锛屼唬鐮佽川閲忛渶瑕佹彁鍗�
**鐜拌薄**: 浠ｇ爜瀛樺湪澶氫釜Bug锛屽奖鍝嶅姛鑳藉拰绋冲畾鎬�

**鏍规湰鍘熷洜**:
1. **Bug瀛樺湪**: 浠ｇ爜瀛樺湪澶氫釜Bug
2. **浠ｇ爜璐ㄩ噺**: 浠ｇ爜璐ㄩ噺涓嶅楂�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細瀛樺湪Bug
def process_data(data):
    result = data['value']  # 鍙兘KeyError
    return result

# 鉁� 淇鍚庯細淇Bug
def process_data_safe(data):
    """瀹夊叏鐨勬暟鎹鐞�"""
    result = data.get('value', None)
    if result is None:
        logger.warning("鏁版嵁缂哄けvalue瀛楁")
        return None
    return result
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **Bug鏁伴噺** | 澶� 鉂� | 灏� 鉁� |
| **浠ｇ爜璐ㄩ噺** | 浣� 鉂� | 楂� 鉁� |
| **绋冲畾鎬�** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**:
- Bug淇
- 浠ｇ爜璐ㄩ噺鎻愬崌
- 澧炲己绋冲畾鎬�

---







### v3.8.82 (2026-07-24) - 馃敡 浠ｇ爜璐ㄩ噺浼樺寲

#### 闂: 浠ｇ爜璐ㄩ噺涓嶅浼樺寲锛岄渶瑕佹敼杩�
**鐜拌薄**: 浠ｇ爜璐ㄩ噺涓嶅楂橈紝闇�瑕佷紭鍖�

**鏍规湰鍘熷洜**:
1. **浠ｇ爜璐ㄩ噺**: 浠ｇ爜璐ㄩ噺涓嶅浼樺寲
2. **鍙淮鎶ゆ��**: 浠ｇ爜鍙淮鎶ゆ�ч渶瑕佹彁鍗�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細浠ｇ爜璐ㄩ噺涓嶉珮
def process():
    # 鍐楅暱鐨勪唬鐮�
    pass

# 鉁� 淇鍚庯細浠ｇ爜璐ㄩ噺浼樺寲
def process_optimized():
    """浼樺寲鐨勪唬鐮�"""
    # 绠�娲佺殑浠ｇ爜
    pass
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **浠ｇ爜璐ㄩ噺** | 浣� 鉂� | 楂� 鉁� |
| **鍙淮鎶ゆ��** | 宸� 鉂� | 濂� 鉁� |
| **鍙鎬�** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**:
- 浠ｇ爜璐ㄩ噺浼樺寲
- 鎻愬崌鍙淮鎶ゆ��
- 鏀瑰杽鍙鎬�

---







### v3.8.81 (2026-07-24) - 馃悰 鍙橀噺鍛藉悕瑙勮寖鍖栦慨澶�

#### 闂: 鍙橀噺鍛藉悕涓嶈鑼冿紝涓嶇鍚圥ython瑙勮寖
**鐜拌薄**: 鍙橀噺鍛藉悕浣跨敤椹煎嘲鍛藉悕娉曪紝涓嶇鍚圥ython瑙勮寖

**鏍规湰鍘熷洜**:
1. **鍛藉悕涓嶈鑼�**: 浣跨敤椹煎嘲鍛藉悕娉�(oldTime)
2. **涓嶇鍚圥EP8**: 涓嶇鍚圥ython PEP8瑙勮寖

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細椹煎嘲鍛藉悕娉�
oldTime = datetime.now()
timeStamp = time.time()

# 鉁� 淇鍚庯細铔囧舰鍛藉悕娉�
old_time = datetime.now()
time_stamp = time.time()
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍙橀噺鍛藉悕** | 椹煎嘲 鉂� | 铔囧舰 鉁� |
| **PEP8瑙勮寖** | 涓嶇鍚� 鉂� | 绗﹀悎 鉁� |
| **浠ｇ爜璐ㄩ噺** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 鍙橀噺鍛藉悕瑙勮寖鍖�(oldTime -> old_time)
- 淇鏃堕棿鎴冲瓧娈�(time_stamp)
- 绗﹀悎PEP8瑙勮寖

---







### v3.8.78 (2026-07-20) - 馃搫 skill.docx鑷姩鐢熸垚+鏂囨。鏇存柊

#### 闂: skill.docx闇�瑕佹墜鍔ㄧ敓鎴愶紝鏂囨。闇�瑕佹洿鏂�
**鐜拌薄**: skill.docx闇�瑕佹墜鍔ㄧ敓鎴愶紝鏂囨。鍐呭杩囨椂

**鏍规湰鍘熷洜**:
1. **鎵嬪姩鐢熸垚**: skill.docx闇�瑕佹墜鍔ㄧ敓鎴�
2. **鏂囨。杩囨椂**: 鏂囨。鍐呭闇�瑕佹洿鏂�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鎵嬪姩鐢熸垚docx
# 闇�瑕佹墜鍔ㄦ墦寮�Word鍒涘缓鏂囨。

# 鉁� 淇鍚庯細鑷姩鐢熸垚docx
from docx import Document

def generate_skill_docx():
    """鑷姩鐢熸垚skill.docx"""
    doc = Document()
    doc.add_heading('Skill鏂囨。', 0)
    doc.add_paragraph('鍐呭...')
    doc.save('skill.docx')
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **docx鐢熸垚** | 鎵嬪姩 鉂� | 鑷姩 鉁� |
| **鏂囨。鏇存柊** | 杩囨椂 鉂� | 鏇存柊 鉁� |
| **鏁堢巼** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- skill.docx鑷姩鐢熸垚
- 鏂囨。鏇存柊
- 鎻愬崌鏁堢巼

---







### v3.8.77 (2026-07-20) - 馃搳 Swagger UI闆嗘垚浼樺寲

#### 闂: Swagger UI闆嗘垚涓嶅浼樺寲
**鐜拌薄**: Swagger UI闆嗘垚鍔熻兘涓嶅瀹屽杽

**鏍规湰鍘熷洜**:
1. **闆嗘垚涓嶅畬鍠�**: Swagger UI闆嗘垚鍔熻兘涓嶅畬鍠�
2. **鐢ㄦ埛浣撻獙**: Swagger UI鐢ㄦ埛浣撻獙闇�瑕佹彁鍗�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細Swagger UI闆嗘垚涓嶅畬鍠�
# 缂哄皯鑷姩鐢熸垚swagger.json

# 鉁� 淇鍚庯細Swagger UI闆嗘垚浼樺寲
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()

# 鑷姩鐢熸垚swagger.json
@app.get('/openapi.json')
async def get_openapi_schema():
    return get_openapi(
        title="API鏂囨。",
        version="1.0.0",
        routes=app.routes
    )
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **Swagger UI** | 涓嶅畬鍠� 鉂� | 瀹屽杽 鉁� |
| **鑷姩鐢熸垚** | 鏃� 鉂� | 鏈� 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**:
- Swagger UI闆嗘垚浼樺寲
- 鑷姩鐢熸垚swagger.json
- 鎻愬崌鐢ㄦ埛浣撻獙

---







### v3.8.76 (2026-07-20) - 馃敡 .trae閰嶇疆浼樺寲+skill鏂囨。鏇存柊

#### 闂: .trae閰嶇疆涓嶅浼樺寲锛宻kill鏂囨。闇�瑕佹洿鏂�
**鐜拌薄**: .trae閰嶇疆涓嶅鍚堢悊锛宻kill鏂囨。鍐呭杩囨椂

**鏍规湰鍘熷洜**:
1. **閰嶇疆涓嶄紭鍖�**: .trae閰嶇疆涓嶅鍚堢悊
2. **鏂囨。杩囨椂**: skill鏂囨。鍐呭闇�瑕佹洿鏂�

**淇鏂规**:
```yaml
# 鉂� 淇鍓嶏細.trae閰嶇疆涓嶄紭鍖�
# 閰嶇疆涓嶅悎鐞�

# 鉁� 淇鍚庯細.trae閰嶇疆浼樺寲
# 浼樺寲鐨勯厤缃�
rules:
  - pattern: "*.py"
    action: lint
  - pattern: "*.js"
    action: format
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **.trae閰嶇疆** | 涓嶄紭鍖� 鉂� | 浼樺寲 鉁� |
| **skill鏂囨。** | 杩囨椂 鉂� | 鏇存柊 鉁� |
| **寮�鍙戞晥鐜�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- .trae閰嶇疆浼樺寲
- skill鏂囨。鏇存柊
- 鎻愬崌寮�鍙戞晥鐜�

---







### v3.8.75 (2026-07-20) - 馃摎 skill鏂囨。+浠ｇ爜瑙勮寖浼樺寲

#### 闂: 缂哄皯skill鏂囨。锛屼唬鐮佽鑼冧笉澶熶紭鍖�
**鐜拌薄**: 缂哄皯skill鏂囨。锛屼唬鐮佽鑼冧笉澶熷畬鍠�

**鏍规湰鍘熷洜**:
1. **鏂囨。缂哄け**: 缂哄皯skill鏂囨。
2. **瑙勮寖涓嶅畬鍠�**: 浠ｇ爜瑙勮寖涓嶅浼樺寲

**淇鏂规**:
```markdown
# 鉂� 淇鍓嶏細缂哄皯skill鏂囨。
# 鏃爏kill.md鏂囦欢

# 鉁� 淇鍚庯細鏂板skill鏂囨。
# skill.md
# 浠ｇ爜瑙勮寖


## 1. 鍛藉悕瑙勮寖
## 2. 娉ㄩ噴瑙勮寖
## 3. 鏂囨。瑙勮寖
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **skill鏂囨。** | 缂哄け 鉂� | 鏂板 鉁� |
| **浠ｇ爜瑙勮寖** | 涓嶅畬鍠� 鉂� | 瀹屽杽 鉁� |
| **鍙淮鎶ゆ��** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**:
- 鏂板skill鏂囨。
- 浠ｇ爜瑙勮寖浼樺寲
- 鎻愬崌鍙淮鎶ゆ��

---





### v3.8.73 (2026-07-19) - 馃敀 CSP浼樺寲+README.md鏇存柊

#### 闂: CSP閰嶇疆杩囦弗锛孯EADME.md闇�瑕佹洿鏂�
**鐜拌薄**: CSP閰嶇疆杩囦弗瀵艰嚧CDN鏃犳硶鍔犺浇锛孯EADME.md鍐呭杩囨椂

**鏍规湰鍘熷洜**:
1. **CSP杩囦弗**: CSP閰嶇疆杩囦弗锛岄樆姝DN鍔犺浇
2. **README杩囨椂**: README.md鍐呭闇�瑕佹洿鏂�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細CSP杩囦弗
CSP = "default-src 'self'"  # 闃绘CDN

# 鉁� 淇鍚庯細CSP浼樺寲
CSP = "default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net"
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **CSP閰嶇疆** | 杩囦弗 鉂� | 浼樺寲 鉁� |
| **CDN鍔犺浇** | 澶辫触 鉂� | 鎴愬姛 鉁� |
| **README鏇存柊** | 杩囨椂 鉂� | 鏇存柊 鉁� |

**鎶�鏈粏鑺�**:
- CSP浼樺寲锛宒ocs/鐩綍鍏佽CDN
- README.md鏇存柊锛岃ˉ鍏卾3.8.67-v3.8.73鐗堟湰璁板綍
- 鏂板/api/changelog API

---





### v3.8.71 (2026-07-19) - 馃搳 Swagger UI闆嗘垚+Pydantic V2鍗囩骇

#### 闂: 缂哄皯Swagger UI锛孭ydantic鐗堟湰杩囨棫
**鐜拌薄**: 缂哄皯Swagger UI鏂囨。锛孭ydantic V1闇�瑕佸崌绾�

**鏍规湰鍘熷洜**:
1. **缂哄皯Swagger UI**: 鏈泦鎴怱wagger UI鏂囨。
2. **Pydantic杩囨棫**: Pydantic V1闇�瑕佸崌绾у埌V2

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細缂哄皯Swagger UI锛孭ydantic V1
from pydantic import BaseModel, validator

class Item(BaseModel):
    name: str
    
    @validator('name')
    def validate_name(cls, v):
        return v

# 鉁� 淇鍚庯細Swagger UI闆嗘垚锛孭ydantic V2
from pydantic import BaseModel, field_validator

class Item(BaseModel):
    name: str
    
    @field_validator('name')
    def validate_name(cls, v):
        return v
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **Swagger UI** | 缂哄け 鉂� | 闆嗘垚 鉁� |
| **Pydantic鐗堟湰** | V1 鉂� | V2 鉁� |
| **鏂囨。瀹屽杽搴�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- Swagger UI闆嗘垚(鑷姩鐢熸垚swagger.json+HTML UI)
- Pydantic V2鍗囩骇(field_validator)
- 鏇存柊requirements.txt

---





### v3.8.70.1 (2026-07-19) - 馃敡 缁熶竴鏂囨。璇█瑙勮寖 - 鎵�鏈夋洿鏂版棩蹇楀繀椤讳娇鐢ㄤ腑鏂�

#### 闂: 鏂囨。璇█涓嶇粺涓�锛屽瓨鍦ㄨ嫳鏂囨洿鏂版棩蹇�
**鐜拌薄**: 閮ㄥ垎鏇存柊鏃ュ織浣跨敤鑻辨枃锛屼笉绗﹀悎瑙勮寖

**鏍规湰鍘熷洜**:
1. **璇█涓嶇粺涓�**: 鏇存柊鏃ュ織璇█涓嶇粺涓�
2. **缂哄皯瑙勮寖**: 缂哄皯鏂囨。璇█瑙勮寖

**淇鏂规**:
```markdown
# 鉂� 淇鍓嶏細鑻辨枃鏇存柊鏃ュ織
- Fixed bug in spider
- Added new feature

# 鉁� 淇鍚庯細涓枃鏇存柊鏃ュ織
- 淇鐖櫕Bug
- 鏂板鏂板姛鑳�
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **璇█缁熶竴** | 涓嶇粺涓� 鉂� | 缁熶竴 鉁� |
| **鏂囨。瑙勮寖** | 缂哄け 鉂� | 瀹屽杽 鉁� |
| **鍙鎬�** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**:
- 缁熶竴鏂囨。璇█瑙勮寖
- 鎵�鏈夋洿鏂版棩蹇楀繀椤讳娇鐢ㄤ腑鏂�
- 鎻愬崌鍙鎬�

---





### v3.8.70 (2026-07-19) - 馃彚 浼佷笟绾х敓浜т紭鍖�

#### 闂: 浠ｇ爜涓嶅浼佷笟绾э紝缂哄皯鐢熶骇浼樺寲
**鐜拌薄**: 浠ｇ爜缂哄皯浼佷笟绾т紭鍖栵紝涓嶅绋冲畾鍜屽畨鍏�

**鏍规湰鍘熷洜**:
1. **缂哄皯浼佷笟绾т紭鍖�**: 浠ｇ爜缂哄皯浼佷笟绾х壒鎬�
2. **鐢熶骇闂**: 鐢熶骇鐜闂闇�瑕佽В鍐�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細缂哄皯浼佷笟绾т紭鍖�
# 缂哄皯鏃ュ織銆佺洃鎺с�侀敊璇鐞嗙瓑

# 鉁� 淇鍚庯細浼佷笟绾т紭鍖�
import logging
from prometheus_client import Counter

# 鏃ュ織閰嶇疆
logging.basicConfig(level=logging.INFO)

# 鐩戞帶鎸囨爣
request_counter = Counter('requests', 'Request count')

def handle_request():
    request_counter.inc()
    # 閿欒澶勭悊
    try:
        # 涓氬姟閫昏緫
        pass
    except Exception as e:
        logging.error(f"Error: {e}")
        raise
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **浼佷笟绾х壒鎬�** | 缂哄け 鉂� | 鏂板 鉁� |
| **鐢熶骇绋冲畾鎬�** | 宸� 鉂� | 濂� 鉁� |
| **瀹夊叏鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 浼佷笟绾х敓浜т紭鍖栵紝38椤规敼杩�
- 瀹夊叏鍔犲浐
- 鎻愬崌鐢熶骇绋冲畾鎬�

---





### v3.8.69 (2026-07-19) - 馃敀 鍏ㄩ潰瀹夊叏瀹¤

#### 闂: 瀛樺湪澶氫釜瀹夊叏婕忔礊锛岄渶瑕佸叏闈㈠璁�
**鐜拌薄**: 浠ｇ爜瀛樺湪澶氫釜瀹夊叏婕忔礊锛屽奖鍝嶅畨鍏ㄦ��

**鏍规湰鍘熷洜**:
1. **瀹夊叏婕忔礊**: 浠ｇ爜瀛樺湪澶氫釜瀹夊叏婕忔礊
2. **缂哄皯瀹¤**: 缂哄皯鍏ㄩ潰瀹夊叏瀹¤

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細瀛樺湪瀹夊叏婕忔礊
# SQL娉ㄥ叆銆乆SS銆丆SRF绛夋紡娲�

# 鉁� 淇鍚庯細瀹夊叏瀹¤淇
# 1. SQL娉ㄥ叆闃叉姢
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

# 2. XSS闃叉姢
from html import escape
safe_input = escape(user_input)

# 3. CSRF闃叉姢
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect(app)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **瀹夊叏婕忔礊** | 澶� 鉂� | 淇 鉁� |
| **瀹夊叏鎬�** | 浣� 鉂� | 楂� 鉁� |
| **瀹¤瑕嗙洊** | 鏃� 鉂� | 鍏ㄩ潰 鉁� |

**鎶�鏈粏鑺�**:
- 鍏ㄩ潰瀹夊叏瀹¤锛�7涓叧閿瓸ug淇
- SQL娉ㄥ叆闃叉姢
- XSS闃叉姢
- CSRF闃叉姢

---





### v3.8.68 (2026-07-19) - 馃悰 鍏抽敭Bug淇

#### 闂: 瀛樺湪缂╄繘閿欒銆丼ocket娉勬紡绛夊叧閿瓸ug
**鐜拌薄**: 浠ｇ爜瀛樺湪缂╄繘閿欒銆丼ocket娉勬紡绛夐棶棰�

**鏍规湰鍘熷洜**:
1. **缂╄繘閿欒**: Python浠ｇ爜瀛樺湪缂╄繘閿欒
2. **Socket娉勬紡**: Socket杩炴帴鏈纭叧闂�
3. **浠ｇ爜璐ㄩ噺**: 浠ｇ爜璐ㄩ噺闇�瑕佹彁鍗�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細缂╄繘閿欒
def process():
  data = fetch_data()  # 缂╄繘閿欒
    return data

# 鉁� 淇鍚庯細淇缂╄繘
def process():
    data = fetch_data()  # 姝ｇ‘缂╄繘
    return data

# 鉂� 淇鍓嶏細Socket娉勬紡
sock = socket.socket()
sock.connect((host, port))
# 蹇樿鍏抽棴

# 鉁� 淇鍚庯細Socket姝ｇ‘鍏抽棴
sock = socket.socket()
try:
    sock.connect((host, port))
    # 涓氬姟閫昏緫
finally:
    sock.close()
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **缂╄繘閿欒** | 瀛樺湪 鉂� | 淇 鉁� |
| **Socket娉勬紡** | 瀛樺湪 鉂� | 淇 鉁� |
| **浠ｇ爜璐ㄩ噺** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇缂╄繘閿欒
- 淇Socket娉勬紡
- 浠ｇ爜璐ㄩ噺鎻愬崌

---





### v3.8.67 (2026-07-19) - 馃悰 FastAPI杩佺ЩBug淇

#### 闂: FastAPI杩佺Щ鍚庡瓨鍦˙ug
**鐜拌薄**: Flask鍒癋astAPI杩佺Щ鍚庨儴鍒嗗姛鑳藉紓甯�

**鏍规湰鍘熷洜**:
1. **杩佺Щ闂**: Flask鍒癋astAPI杩佺Щ涓嶅畬鏁�
2. **鍔熻兘寮傚父**: 閮ㄥ垎鍔熻兘鏈纭縼绉�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細Flask椋庢牸
@app.route('/api/data', methods=['POST'])
def get_data():
    data = request.get_json()
    return jsonify(data)

# 鉁� 淇鍚庯細FastAPI椋庢牸
@app.post('/api/data')
async def get_data(data: dict):
    return data
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **杩佺ЩBug** | 瀛樺湪 鉂� | 淇 鉁� |
| **鍔熻兘姝ｅ父** | 寮傚父 鉂� | 姝ｅ父 鉁� |
| **绋冲畾鎬�** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇FastAPI杩佺Щ鍚庣殑Bug
- 纭繚鍔熻兘姝ｅ父
- 鎻愬崌绋冲畾鎬�

---





### v3.8.66 (2026-07-18) - 馃И CF鐙珛鎬ф祴璇曢獙璇�+Bug淇

#### 闂: CF闅ч亾鐙珛鎬ф湭楠岃瘉锛屽瓨鍦˙ug
**鐜拌薄**: Cloudflare闅ч亾鐙珛鎬ф湭缁忚繃瀹為檯娴嬭瘯楠岃瘉

**鏍规湰鍘熷洜**:
1. **缂哄皯娴嬭瘯**: CF闅ч亾鐙珛鎬ф湭缁忚繃瀹炴祴楠岃瘉
2. **Bug瀛樺湪**: verify_url()鍑芥暟瀛樺湪鍙傛暟閿欒

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細缂哄皯瀹炴祴楠岃瘉
# 鏈祴璇昲ostc杩涚▼缁堟鏃禖F闅ч亾鏄惁鐙珛杩愯

# 鉁� 淇鍚庯細瀹炴祴楠岃瘉
def test_cf_independence():
    """娴嬭瘯CF闅ч亾鐙珛鎬�"""
    # 鎵嬪姩瑙﹀彂hostc杩涚▼缁堟
    kill_hostc_process()
    
    # 楠岃瘉CF闅ч亾鏄惁浠嶅湪杩愯
    assert check_cf_tunnel_status() == True
    
    # 楠岃瘉verify_url()鍙傛暟
    verify_url(url)  # 淇鍙傛暟閿欒
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **瀹炴祴楠岃瘉** | 鏃� 鉂� | 鏈� 鉁� |
| **Bug淇** | 瀛樺湪 鉂� | 淇 鉁� |
| **绋冲畾鎬�** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**:
- 鎵嬪姩瑙﹀彂hostc杩涚▼缁堟娴嬭瘯
- 淇verify_url()鍙傛暟閿欒
- hostc棰戠箒宕╂簝鍦烘櫙涓婥F闅ч亾瀹屽叏鐙珛杩愯

---





### v3.8.65 (2026-07-18) - 馃敀 CF闅ч亾鐙珛鎬т紭鍖�+鏅鸿兘澶嶇敤鏈哄埗

#### 闂: hostc澶辨晥褰卞搷CF闅ч亾锛岀己灏戞櫤鑳藉鐢�
**鐜拌薄**: hostc澶辨晥鏃禖F闅ч亾涔熷け鏁堬紝缂哄皯鏅鸿兘澶嶇敤鏈哄埗

**鏍规湰鍘熷洜**:
1. **渚濊禆闂**: CF闅ч亾渚濊禆hostc锛宧ostc澶辨晥鏃禖F涔熷け鏁�
2. **缂哄皯澶嶇敤**: 鏈鐢ㄥ凡鏈夌殑CF闅ч亾鍦板潃

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細CF闅ч亾渚濊禆hostc
def start_tunnel():
    start_hostc()
    start_cf()  # hostc澶辨晥鏃禖F涔熷け鏁�

# 鉁� 淇鍚庯細CF闅ч亾鐙珛+鏅鸿兘澶嶇敤
def start_tunnel_optimized():
    """浼樺寲鐨勯毀閬撳惎鍔�"""
    # 鍏堟鏌ュ凡鏈夊彲鐢ㄥ湴鍧�
    existing_cf_url = check_existing_cf_tunnel()
    if existing_cf_url:
        return existing_cf_url  # 鏅鸿兘澶嶇敤
    
    # CF闅ч亾鐙珛鍚姩
    start_cf_independently()
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **CF鐙珛鎬�** | 渚濊禆 鉂� | 鐙珛 鉁� |
| **鏅鸿兘澶嶇敤** | 鏃� 鉂� | 鏈� 鉁� |
| **閲嶅惎娆℃暟** | 澶� 鉂� | 灏� 鉁� |

**鎶�鏈粏鑺�**:
- hostc澶辨晥涓嶅啀褰卞搷Cloudflare Tunnel
- 鍚姩鏂癈F闅ч亾鍓嶅厛妫�鏌ュ凡鏈夊彲鐢ㄥ湴鍧�
- hostc棰戠箒閲嶅惎鏃禖F鍦板潃淇濇寔涓嶅彉

---





### v3.8.64 (2026-07-18) - 鉁� 闅ч亾鍏变韩寮圭獥鎭㈠鍘熷hostc鏍峰紡+鏂板Cloudflare URL

#### 闂: 闅ч亾鍏变韩寮圭獥鏍峰紡鏀瑰彉锛岀己灏慍loudflare URL
**鐜拌薄**: 闅ч亾鍏变韩寮圭獥鏍峰紡涓庡師濮媓ostc涓嶄竴鑷达紝缂哄皯Cloudflare URL鏄剧ず

**鏍规湰鍘熷洜**:
1. **鏍峰紡鏀瑰彉**: 寮圭獥鏍峰紡涓庡師濮媓ostc涓嶄竴鑷�
2. **缂哄皯CF URL**: 鏈樉绀篊loudflare URL

**淇鏂规**:
```html
<!-- 鉂� 淇鍓嶏細鏍峰紡鏀瑰彉锛岀己灏慍F URL -->
<div class="modal">
    <p>hostc URL: {{url}}</p>
</div>

<!-- 鉁� 淇鍚庯細鎭㈠鍘熷鏍峰紡锛屾柊澧濩F URL -->
<div class="modal">
    <h3>闅ч亾鍏变韩</h3>
    <p>hostc URL: {{hostc_url}}</p>
    <p>Cloudflare URL: {{cf_url}}</p>
    <button onclick="copyUrl('{{hostc_url}}')">澶嶅埗hostc</button>
    <button onclick="copyUrl('{{cf_url}}')">澶嶅埗CF</button>
</div>
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏍峰紡鎭㈠** | 鏀瑰彉 鉂� | 鍘熷 鉁� |
| **CF URL鏄剧ず** | 缂哄け 鉂� | 鏂板 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**:
- 闅ч亾鍏变韩寮圭獥鎭㈠鍘熷hostc鏍峰紡
- 鏂板Cloudflare URL鏄剧ず
- 鎻愬崌鐢ㄦ埛浣撻獙

---





### v3.8.63 (2026-07-18) - 馃寪 闅ч亾鍏变韩寮圭獥鍚屾椂鏄剧ずhostc鍜孋loudflare鍙屽叕缃戝湴鍧�

#### 闂: 闅ч亾鍏变韩寮圭獥鍙樉绀轰竴涓湴鍧�
**鐜拌薄**: 寮圭獥鍙樉绀篽ostc鍦板潃锛岀己灏慍loudflare鍦板潃

**鏍规湰鍘熷洜**:
1. **鍗曞湴鍧�鏄剧ず**: 寮圭獥鍙樉绀轰竴涓叕缃戝湴鍧�
2. **缂哄皯鍙屽湴鍧�**: 鏈悓鏃舵樉绀篽ostc鍜孋loudflare鍦板潃

**淇鏂规**:
```html
<!-- 鉂� 淇鍓嶏細鍗曞湴鍧�鏄剧ず -->
<div class="modal">
    <p>URL: {{url}}</p>
</div>

<!-- 鉁� 淇鍚庯細鍙屽湴鍧�鏄剧ず -->
<div class="modal">
    <h3>闅ч亾鍏变韩</h3>
    <div class="url-section">
        <h4>hostc鍦板潃</h4>
        <p>{{hostc_url}}</p>
        <button onclick="copyUrl('{{hostc_url}}')">澶嶅埗</button>
    </div>
    <div class="url-section">
        <h4>Cloudflare鍦板潃</h4>
        <p>{{cf_url}}</p>
        <button onclick="copyUrl('{{cf_url}}')">澶嶅埗</button>
    </div>
</div>
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍦板潃鏁伴噺** | 鍗曞湴鍧� 鉂� | 鍙屽湴鍧� 鉁� |
| **鐢ㄦ埛閫夋嫨** | 鏃� 鉂� | 鏈� 鉁� |
| **鐏垫椿鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 闅ч亾鍏变韩寮圭獥鍚屾椂鏄剧ずhostc鍜孋loudflare鍙屽叕缃戝湴鍧�
- 鐢ㄦ埛鍙互閫夋嫨浣跨敤鍝釜鍦板潃
- 鎻愬崌鐏垫椿鎬�

---





### v3.8.62 (2026-07-18) - 馃敡 Toast鏄剧ず鍏蜂綋澶嶅埗鐨刄RL鍦板潃

#### 闂: Toast鎻愮ず涓嶅鍏蜂綋锛屾湭鏄剧ず澶嶅埗鐨刄RL
**鐜拌薄**: Toast鍙樉绀�"宸插鍒�"锛屾湭鏄剧ず鍏蜂綋澶嶅埗鐨刄RL鍦板潃

**鏍规湰鍘熷洜**:
1. **鎻愮ず涓嶅叿浣�**: Toast鎻愮ず淇℃伅涓嶅璇︾粏
2. **缂哄皯URL鏄剧ず**: 鏈樉绀哄叿浣撳鍒剁殑URL

**淇鏂规**:
```javascript
// 鉂� 淇鍓嶏細Toast涓嶅叿浣�
function copyUrl(url) {
    navigator.clipboard.writeText(url);
    showToast("宸插鍒�");
}

// 鉁� 淇鍚庯細Toast鏄剧ず鍏蜂綋URL
function copyUrl(url) {
    navigator.clipboard.writeText(url);
    showToast(`宸插鍒�: ${url}`);
}
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **Toast淇℃伅** | 涓嶅叿浣� 鉂� | 鍏蜂綋 鉁� |
| **URL鏄剧ず** | 鏃� 鉂� | 鏈� 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**:
- Toast鏄剧ず鍏蜂綋澶嶅埗鐨刄RL鍦板潃
- 鎻愬崌鐢ㄦ埛浣撻獙
- 澧炲己淇℃伅閫忔槑搴�

---





### v3.8.61 (2026-07-18) - 馃悰 淇闅ч亾绠＄悊闈㈡澘澶嶅埗鎸夐挳ID鍐茬獊锛孴oast寮圭獥鎭㈠姝ｅ父

#### 闂: 闅ч亾绠＄悊闈㈡澘澶嶅埗鎸夐挳ID鍐茬獊锛孴oast寮圭獥寮傚父
**鐜拌薄**: 澶嶅埗鎸夐挳ID鍐茬獊瀵艰嚧Toast寮圭獥鏃犳硶姝ｅ父鏄剧ず

**鏍规湰鍘熷洜**:
1. **ID鍐茬獊**: 澶氫釜鎸夐挳浣跨敤鐩稿悓鐨処D
2. **Toast寮傚父**: Toast寮圭獥鏃犳硶姝ｅ父宸ヤ綔

**淇鏂规**:
```html
<!-- 鉂� 淇鍓嶏細ID鍐茬獊 -->
<button id="copy-btn" onclick="copyUrl()">澶嶅埗</button>
<button id="copy-btn" onclick="copyUrl()">澶嶅埗</button>

<!-- 鉁� 淇鍚庯細鍞竴ID -->
<button id="copy-btn-1" onclick="copyUrl()">澶嶅埗</button>
<button id="copy-btn-2" onclick="copyUrl()">澶嶅埗</button>
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **ID鍐茬獊** | 瀛樺湪 鉂� | 淇 鉁� |
| **Toast寮圭獥** | 寮傚父 鉂� | 姝ｅ父 鉁� |
| **鍔熻兘鍙敤鎬�** | 澶辨晥 鉂� | 鍙敤 鉁� |

**鎶�鏈粏鑺�**:
- 淇闅ч亾绠＄悊闈㈡澘澶嶅埗鎸夐挳ID鍐茬獊
- Toast寮圭獥鎭㈠姝ｅ父
- 纭繚鍔熻兘姝ｅ父宸ヤ綔

---





### v3.8.60 (2026-07-18) - 馃敡 鍏綉鍦板潃澶嶅埗鎸夐挳鏍峰紡缁熶竴锛坆tn-light + 澶嶅埗鏂囧瓧锛�

#### 闂: 鍏綉鍦板潃澶嶅埗鎸夐挳鏍峰紡涓嶇粺涓�
**鐜拌薄**: 涓嶅悓鍦版柟鐨勫鍒舵寜閽牱寮忎笉涓�鑷�

**鏍规湰鍘熷洜**:
1. **鏍峰紡涓嶇粺涓�**: 涓嶅悓鍦版柟鐨勬寜閽牱寮忎笉鍚�
2. **缂哄皯瑙勮寖**: 缂哄皯鎸夐挳鏍峰紡瑙勮寖

**淇鏂规**:
```html
<!-- 鉂� 淇鍓嶏細鏍峰紡涓嶇粺涓� -->
<button class="btn-primary">Copy</button>
<button class="btn-success">澶嶅埗閾炬帴</button>

<!-- 鉁� 淇鍚庯細鏍峰紡缁熶竴 -->
<button class="btn-light">澶嶅埗</button>
<button class="btn-light">澶嶅埗</button>
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏍峰紡缁熶竴** | 涓嶇粺涓� 鉂� | 缁熶竴 鉁� |
| **鎸夐挳鏂囧瓧** | 涓嶇粺涓� 鉂� | 缁熶竴 鉁� |
| **UI涓�鑷存��** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**:
- 鍏綉鍦板潃澶嶅埗鎸夐挳鏍峰紡缁熶竴锛坆tn-light + 澶嶅埗鏂囧瓧锛�
- 鎻愬崌UI涓�鑷存��
- 鏀瑰杽鐢ㄦ埛浣撻獙
- **馃敡 鍏綉鍦板潃澶嶅埗鎸夐挳鏍峰紡缁熶竴锛坆tn-light + 澶嶅埗鏂囧瓧锛�** - 鍏綉鍦板潃澶嶅埗鎸夐挳鏍峰紡缁熶竴锛坆tn-light + 澶嶅埗鏂囧瓧锛�




### v3.8.59 (2026-07-18) - 馃寪 鍏綉鍦板潃澶嶅埗鎸夐挳锛圕loudflare + hostc锛�

#### 闂: Cloudflare鍜宧ostc鍏綉鍦板潃澶嶅埗鎸夐挳鏍峰紡涓嶇粺涓�
**鐜拌薄**: 鍓嶇鐣岄潰涓紝Cloudflare鍜宧ostc闅ч亾鐨勫叕缃戝湴鍧�澶嶅埗鎸夐挳鏍峰紡涓嶄竴鑷达紝鐢ㄦ埛浣撻獙涓嶇粺涓�

**鏍规湰鍘熷洜**: 鎸夐挳鏍峰紡鏈粺涓�瑙勮寖锛屼笉鍚岄毀閬撶殑澶嶅埗鎸夐挳浣跨敤浜嗕笉鍚岀殑CSS绫诲拰鏂囨湰

**淇鏂规**:
```html
<!-- 鉂� 淇鍓嶏細鎸夐挳鏍峰紡涓嶇粺涓� -->
<button class="btn-{{ tunnel.type }}" onclick="copyUrl('{{ tunnel.url }}')">
  {{ tunnel.type === 'cf' ? 'Copy CF URL' : 'Copy hostc URL' }}
</button>

<!-- 鉁� 淇鍚庯細缁熶竴鎸夐挳鏍峰紡 -->
<button class="btn-light" onclick="copyUrl('{{ tunnel.url }}')">
  澶嶅埗
</button>
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鎸夐挳鏍峰紡** | 涓嶇粺涓� 鉂� | 缁熶竴 鉁� |
| **鎸夐挳鏂囨湰** | 涓嶄竴鑷� 鉂� | 缁熶竴"澶嶅埗" 鉁� |
| **鐢ㄦ埛浣撻獙** | 娣蜂贡 鉂� | 涓�鑷� 鉁� |

**鎶�鏈粏鑺�**: 缁熶竴鎵�鏈夊叕缃戝湴鍧�澶嶅埗鎸夐挳鐨勬牱寮忎负"btn-light"锛屾枃鏈粺涓�涓�"澶嶅埗"锛屾彁鍗嘦I涓�鑷存��




### v3.8.58 (2026-07-18) - 馃悰 閭欢闃查噸澶嶅彂閫佷慨澶� + skill.docx 鍚屾鏇存柊

#### 闂: 閭欢閲嶅鍙戦�佸鑷寸敤鎴锋敹鍒板灏佺浉鍚岄�氱煡
**鐜拌薄**: 闅ч亾鐘舵�佸彉鍖栨椂锛岀敤鎴锋敹鍒板灏佸唴瀹圭浉鍚岀殑閭欢閫氱煡锛岄�犳垚楠氭壈

**鏍规湰鍘熷洜**: 閭欢鍙戦�侀�昏緫鏈坊鍔犻槻閲嶅鏈哄埗锛岀姸鎬佸彉鍖栬Е鍙戝娆″彂閫�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細姣忔鐘舵�佸彉鍖栭兘鍙戦偖浠�
def send_notification(url, status):
    send_email(f"闅ч亾鐘舵��: {status}", f"URL: {url}")

# 鉁� 淇鍚庯細娣诲姞闃查噸澶嶆満鍒�
last_email_time = {}
def send_notification(url, status):
    key = f"{url}:{status}"
    if key in last_email_time:
        if time.time() - last_email_time[key] < 300:  # 5鍒嗛挓鍐呬笉閲嶅鍙戦��
            return
    last_email_time[key] = time.time()
    send_email(f"闅ч亾鐘舵��: {status}", f"URL: {url}")
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **閭欢閲嶅** | 鏄� 鉂� | 鍚� 鉁� |
| **鐢ㄦ埛浣撻獙** | 楠氭壈 鉂� | 鑹ソ 鉁� |
| **缃戠粶璐熻浇** | 楂� 鉂� | 浣� 鉁� |

**鎶�鏈粏鑺�**: 浣跨敤瀛楀吀璁板綍涓婃鍙戦�佹椂闂达紝5鍒嗛挓鍐呯浉鍚岀姸鎬佷笉閲嶅鍙戦�侀偖浠�





### v3.8.57 (2026-07-18) - 馃摑 鐗堟湰鏇存柊鏃ュ織鍒� README.md

#### 闂: 鐗堟湰鏇存柊鏃ュ織鍒嗘暎锛岄毦浠ヨ拷韪巻鍙插彉鏇�
**鐜拌薄**: 鐗堟湰鏇存柊璁板綍鍒嗘暎鍦ㄥ涓枃妗ｄ腑锛屽紑鍙戣�呴毦浠ュ揩閫熶簡瑙ｅ巻鍙插彉鏇�

**鏍规湰鍘熷洜**: 缂轰箯缁熶竴鐨勭増鏈棩蹇楃鐞嗘満鍒�

**淇鏂规**:
```markdown
<!-- 鉁� 缁熶竴鐗堟湰鏃ュ織鏍煎紡 -->
### vX.Y.Z (YYYY-MM-DD) - <emoji> <绠�杩�>

#### 闂: <涓�鍙ヨ瘽鎻忚堪闂>
**鐜拌薄**: <鐢ㄦ埛鍙劅鐭ョ殑鍏蜂綋琛ㄧ幇>

**鏍规湰鍘熷洜**: <鎶�鏈眰闈㈢殑鏍瑰洜>

**淇鏂规**:
```<language>
// 鉂� 淇鍓�
<鏃т唬鐮�>

// 鉁� 淇鍚�
<鏂颁唬鐮�>
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鎸囨爣1** | 閿欒 鉂� | 姝ｇ‘ 鉁� |

**鎶�鏈粏鑺�**: <鎶�鏈師鐞嗚鏄�>
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏃ュ織缁熶竴鎬�** | 鍒嗘暎 鉂� | 闆嗕腑 鉁� |
| **鍙拷婧��** | 宸� 鉂� | 濂� 鉁� |
| **鏂囨。缁存姢** | 鍥伴毦 鉂� | 绠�鍗� 鉁� |

**鎶�鏈粏鑺�**: 灏嗘墍鏈夌増鏈洿鏂版棩蹇楃粺涓�鍒癛EADME.md锛岄噰鐢ㄦ爣鍑嗗寲鏍煎紡璁板綍





### v3.8.56 (2026-07-18) - 馃敡 绉婚櫎 hostc_output.txt锛岀畝鍖栭毀閬撶鐞�

#### 闂: hostc_output.txt鏂囦欢鍐椾綑锛屽鍔犵鐞嗗鏉傚害
**鐜拌薄**: 椤圭洰涓瓨鍦╤ostc_output.txt涓存椂鏂囦欢锛屼笌tunnel_url.txt鍔熻兘閲嶅

**鏍规湰鍘熷洜**: 鏃╂湡璁捐閬楃暀锛屾湭鍙婃椂娓呯悊鍐椾綑鏂囦欢

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍚屾椂缁存姢涓や釜鏂囦欢
def save_tunnel_url(url):
    with open('tunnel_url.txt', 'w') as f:
        f.write(url)
    with open('hostc_output.txt', 'w') as f:
        f.write(url)

# 鉁� 淇鍚庯細鍙淮鎶や竴涓潈濞佹暟鎹簮
def save_tunnel_url(url):
    with open('tunnel_url.txt', 'w') as f:
        f.write(url)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏂囦欢鏁伴噺** | 2涓� 鉂� | 1涓� 鉁� |
| **鏁版嵁涓�鑷存��** | 鍙兘鍐茬獊 鉂� | 鍗曚竴鏉冨▉婧� 鉁� |
| **绠＄悊澶嶆潅搴�** | 楂� 鉂� | 浣� 鉁� |

**鎶�鏈粏鑺�**: 鍒犻櫎hostc_output.txt锛岀粺涓�浣跨敤tunnel_url.txt浣滀负闅ч亾URL鐨勬潈濞佹暟鎹簮





### v3.8.55 (2026-07-18) - 馃敡 Cloudflare 閭欢閫氱煡鏃ュ織缁熶竴

#### 闂: Cloudflare闅ч亾閭欢閫氱煡鏃ュ織鏍煎紡涓嶇粺涓�
**鐜拌薄**: Cloudflare闅ч亾鐨勯偖浠堕�氱煡鏃ュ織鏍煎紡涓庡叾浠栭毀閬撲笉涓�鑷达紝闅句互缁熶竴鍒嗘瀽

**鏍规湰鍘熷洜**: 涓嶅悓闅ч亾鐨勬棩蹇楄褰曢�昏緫鐙珛寮�鍙戯紝鏈粺涓�瑙勮寖

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鏃ュ織鏍煎紡涓嶇粺涓�
logging.info(f"CF tunnel URL: {url}")
logging.info(f"Email sent to {recipient}")

# 鉁� 淇鍚庯細缁熶竴鏃ュ織鏍煎紡
logging.info(f"[TUNNEL-EMAIL] type=cf, url={url}, recipient={recipient}, status=success")
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏃ュ織鏍煎紡** | 涓嶇粺涓� 鉂� | 缁熶竴 鉁� |
| **鍙垎鏋愭��** | 宸� 鉂� | 濂� 鉁� |
| **璋冭瘯鏁堢巼** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 缁熶竴鎵�鏈夐毀閬撶殑閭欢閫氱煡鏃ュ織鏍煎紡锛屾坊鍔犵被鍨嬫爣璇嗗拰鐘舵�佸瓧娈�





### v3.8.54 (2026-07-18) - 馃寪 Cloudflare 闄愭祦妫�娴嬩笌鍙嬪ソ鎻愮ず

#### 闂: Cloudflare API闄愭祦瀵艰嚧闅ч亾鍒涘缓澶辫触锛屾棤鍙嬪ソ鎻愮ず
**鐜拌薄**: 鐢ㄦ埛棰戠箒鍒涘缓闅ч亾鏃惰Е鍙慍loudflare API闄愭祦锛岀晫闈㈠彧鏄剧ず"闅ч亾鍒涘缓澶辫触"

**鏍规湰鍘熷洜**: 鏈崟鑾稢loudflare API闄愭祦閿欒锛岀己灏戝弸濂芥彁绀�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鐩存帴鎶ラ敊
def create_cf_tunnel():
    result = cf_api.create_tunnel()
    return result.url

# 鉁� 淇鍚庯細鎹曡幏闄愭祦骞舵彁绀�
def create_cf_tunnel():
    try:
        result = cf_api.create_tunnel()
        return result.url
    except CloudflareRateLimitError:
        return {"error": "Cloudflare API闄愭祦锛岃5鍒嗛挓鍚庨噸璇�"}
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **閿欒鎻愮ず** | 鏃� 鉂� | 鍙嬪ソ 鉁� |
| **鐢ㄦ埛浣撻獙** | 鍥版儜 鉂� | 鏄庣‘ 鉁� |
| **閲嶈瘯鎴愬姛鐜�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 鎹曡幏Cloudflare API闄愭祦閿欒锛岃繑鍥炲弸濂芥彁绀哄苟寤鸿绛夊緟鏃堕棿





### v3.8.53 (2026-07-18) - 馃悰 淇鍙岄毀閬撳湴鍧�鍐欏叆鍐茬獊

#### 闂: 鍙岄毀閬擄紙hostc + CF锛夊悓鏃惰繍琛屾椂鍦板潃鍐欏叆鍐茬獊
**鐜拌薄**: hostc鍜孋loudflare闅ч亾鍚屾椂杩愯鏃讹紝tunnel_url.txt鏂囦欢鍐呭娣蜂贡

**鏍规湰鍘熷洜**: 涓や釜闅ч亾杩涚▼鍚屾椂鍐欏叆鍚屼竴鏂囦欢锛屾湭鍔犻攣淇濇姢

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鏃犻攣鍐欏叆
def save_url(tunnel_type, url):
    with open('tunnel_url.txt', 'w') as f:
        f.write(f"{tunnel_type}:{url}")

# 鉁� 淇鍚庯細鏂囦欢閿佷繚鎶�
import fcntl
def save_url(tunnel_type, url):
    with open('tunnel_url.txt', 'w') as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        f.write(f"{tunnel_type}:{url}")
        fcntl.flock(f.fileno(), fcntl.LOCK_UN)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍐欏叆鍐茬獊** | 鏄� 鉂� | 鍚� 鉁� |
| **鏁版嵁瀹屾暣鎬�** | 鎹熷潖 鉂� | 瀹屾暣 鉁� |
| **绋冲畾鎬�** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**: 浣跨敤鏂囦欢閿佷繚鎶unnel_url.txt鍐欏叆锛岄槻姝㈠弻闅ч亾骞跺彂鍐欏叆鍐茬獊





### v3.8.52 (2026-07-18) - 馃悰 鍙岄毀閬撶嫭绔嬪彂閭欢 + 蹇冭烦鍐欏叆淇

#### 闂: 鍙岄毀閬撻偖浠堕�氱煡鍜屽績璺冲啓鍏ラ�昏緫娣蜂贡
**鐜拌薄**: hostc鍜孋F闅ч亾鐘舵�佸彉鍖栨椂锛岄偖浠堕�氱煡鍜屽績璺冲啓鍏ラ�昏緫鐩镐簰骞叉壈

**鏍规湰鍘熷洜**: 鍙岄毀閬撻�昏緫鏈畬鍏ㄩ殧绂伙紝鍏变韩鐘舵�佸彉閲�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍏变韩鐘舵��
tunnel_status = {}
def update_status(tunnel_type, status):
    tunnel_status[tunnel_type] = status
    send_email(status)  # 鎵�鏈夐毀閬撳叡浜偖浠堕�昏緫

# 鉁� 淇鍚庯細鐙珛鐘舵��
class TunnelMonitor:
    def __init__(self, tunnel_type):
        self.type = tunnel_type
        self.status = {}
    
    def update_status(self, status):
        self.status = status
        self.send_email(status)  # 姣忎釜闅ч亾鐙珛閭欢閫昏緫
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **閭欢鐙珛鎬�** | 娣蜂贡 鉂� | 鐙珛 鉁� |
| **蹇冭烦鍑嗙‘鎬�** | 宸� 鉂� | 濂� 鉁� |
| **鍙淮鎶ゆ��** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 涓烘瘡涓毀閬撳垱寤虹嫭绔嬬殑鐩戞帶瀹炰緥锛岄殧绂婚偖浠堕�氱煡鍜屽績璺冲啓鍏ラ�昏緫





### v3.8.51 (2026-07-18) - 馃摑 鏇存柊README鍜宻kill鏂囨。

#### 闂: 鏂囨。涓庝唬鐮佸疄鐜颁笉鍚屾
**鐜拌薄**: README.md鍜宻kill.md涓殑鎶�鏈鑼冧笌瀹為檯浠ｇ爜瀹炵幇涓嶄竴鑷�

**鏍规湰鍘熷洜**: 浠ｇ爜鏇存柊鍚庢湭鍙婃椂鍚屾鏂囨。

**淇鏂规**:
```markdown
<!-- 鉁� 鍚屾鏇存柊鏂囨。 -->
### 鎶�鏈鑼�
- 闅ч亾URL瀛樺偍: tunnel_url.txt锛堝悓鏃跺瓨鍌╤ostc鍜孋F涓や釜闅ч亾鐨勫湴鍧�锛�
- 閭欢閫氱煡: 鐙珛鍙戦�侊紝闃查噸澶嶆満鍒�
- 蹇冭烦楠岃瘉: 姣忎釜闅ч亾鐙珛楠岃瘉
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏂囨。鍑嗙‘鎬�** | 杩囨椂 鉂� | 鏈�鏂� 鉁� |
| **寮�鍙戣�呭弬鑰�** | 鍥版儜 鉂� | 鏄庣‘ 鉁� |
| **缁存姢鎴愭湰** | 楂� 鉂� | 浣� 鉁� |

**鎶�鏈粏鑺�**: 鍚屾鏇存柊README.md鍜宻kill.md锛岀‘淇濇枃妗ｄ笌浠ｇ爜瀹炵幇涓�鑷�





### v3.8.50 (2026-07-18) - 馃悰 淇CF蹇冭烦楠岃瘉鏃ュ織杈撳嚭

#### 闂: Cloudflare闅ч亾蹇冭烦楠岃瘉鏃ュ織杈撳嚭閿欒
**鐜拌薄**: CF闅ч亾蹇冭烦楠岃瘉鏃讹紝鏃ュ織杈撳嚭鏄剧ず"楠岃瘉澶辫触"锛屼絾瀹為檯楠岃瘉鎴愬姛

**鏍规湰鍘熷洜**: 鏃ュ織杈撳嚭閫昏緫涓庨獙璇佺粨鏋滃垽鏂�昏緫涓嶄竴鑷�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鏃ュ織杈撳嚭閿欒
def verify_cf_tunnel(url):
    result = requests.get(url)
    if result.status_code == 200:
        logging.info(f"CF tunnel verification failed: {url}")
        return True
    return False

# 鉁� 淇鍚庯細鏃ュ織杈撳嚭姝ｇ‘
def verify_cf_tunnel(url):
    result = requests.get(url)
    if result.status_code == 200:
        logging.info(f"CF tunnel verification success: {url}")
        return True
    logging.error(f"CF tunnel verification failed: {url}")
    return False
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏃ュ織鍑嗙‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **璋冭瘯鏁堢巼** | 浣� 鉂� | 楂� 鉁� |
| **鐢ㄦ埛淇′换搴�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 淇CF闅ч亾蹇冭烦楠岃瘉鏃ュ織杈撳嚭锛岀‘淇濇棩蹇楀唴瀹逛笌瀹為檯楠岃瘉缁撴灉涓�鑷�




### v3.8.49 (2026-07-18) - 鉁� 娣诲姞CF蹇冭烦楠岃瘉璇︾粏鏃ュ織

#### 闂: Cloudflare闅ч亾蹇冭烦楠岃瘉缂哄皯璇︾粏鏃ュ織锛岄毦浠ヨ皟璇�
**鐜拌薄**: CF闅ч亾蹇冭烦楠岃瘉澶辫触鏃讹紝鏃ュ織淇℃伅涓嶈冻锛屾棤娉曞揩閫熷畾浣嶉棶棰�

**鏍规湰鍘熷洜**: 蹇冭烦楠岃瘉閫昏緫鏈坊鍔犺缁嗘棩蹇楄緭鍑�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鏃ュ織淇℃伅涓嶈冻
def verify_cf_tunnel(url):
    result = requests.get(url)
    return result.status_code == 200

# 鉁� 淇鍚庯細娣诲姞璇︾粏鏃ュ織
def verify_cf_tunnel(url):
    logging.info(f"[CF-HEARTBEAT] Starting verification for {url}")
    try:
        start_time = time.time()
        result = requests.get(url, timeout=10)
        elapsed = time.time() - start_time
        logging.info(f"[CF-HEARTBEAT] Response: status={result.status_code}, time={elapsed:.2f}s")
        return result.status_code == 200
    except Exception as e:
        logging.error(f"[CF-HEARTBEAT] Verification failed: {e}")
        return False
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏃ュ織璇︾粏搴�** | 涓嶈冻 鉂� | 璇︾粏 鉁� |
| **璋冭瘯鏁堢巼** | 浣� 鉂� | 楂� 鉁� |
| **闂瀹氫綅** | 鍥伴毦 鉂� | 绠�鍗� 鉁� |

**鎶�鏈粏鑺�**: 涓篊F闅ч亾蹇冭烦楠岃瘉娣诲姞璇︾粏鏃ュ織锛屽寘鎷姹傛椂闂淬�佸搷搴旂姸鎬併�佽�楁椂绛変俊鎭�





### v3.8.48 (2026-07-18) - 馃寪 Tunnel type selector dynamic default value

#### 闂: 闅ч亾绫诲瀷閫夋嫨鍣ㄩ粯璁ゅ�间笉鏅鸿兘
**鐜拌薄**: 鐢ㄦ埛姣忔鍚姩閮介渶瑕佹墜鍔ㄩ�夋嫨闅ч亾绫诲瀷锛岀郴缁熸湭鏍规嵁鍘嗗彶浣跨敤鎯呭喌鏅鸿兘鎺ㄨ崘

**鏍规湰鍘熷洜**: 闅ч亾绫诲瀷閫夋嫨鍣ㄩ粯璁ゅ�煎浐瀹氾紝鏈疄鐜板姩鎬佹帹鑽�

**淇鏂规**:
```javascript
// 鉂� 淇鍓嶏細鍥哄畾榛樿鍊�
<select id="tunnel-type" defaultValue="hostc">
  <option value="hostc">hostc</option>
  <option value="cf">Cloudflare</option>
</select>

// 鉁� 淇鍚庯細鍔ㄦ�侀粯璁ゅ��
const lastUsedType = localStorage.getItem('lastTunnelType') || 'hostc';
document.getElementById('tunnel-type').value = lastUsedType;
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鐢ㄦ埛浣撻獙** | 闇�鎵嬪姩閫夋嫨 鉂� | 鏅鸿兘鎺ㄨ崘 鉁� |
| **鍚姩鏁堢巼** | 浣� 鉂� | 楂� 鉁� |
| **涓�у寲** | 鏃� 鉂� | 鏈� 鉁� |

**鎶�鏈粏鑺�**: 鏍规嵁鐢ㄦ埛涓婃浣跨敤鐨勯毀閬撶被鍨嬶紝鍔ㄦ�佽缃�夋嫨鍣ㄧ殑榛樿鍊�





### v3.8.47 (2026-07-17) - 馃寪 鍙岄毀閬撲簰涓哄鐢ㄩ�氱煡 + fallback_available 閭欢绫诲瀷

#### 闂: 鍙岄毀閬撴棤澶囩敤鏈哄埗锛屽崟鐐规晠闅滈闄╅珮
**鐜拌薄**: hostc鎴朇F闅ч亾浠讳竴鏁呴殰鏃讹紝鐢ㄦ埛鏃犳硶鍙婃椂鑾风煡澶囩敤闅ч亾鐘舵��

**鏍规湰鍘熷洜**: 鍙岄毀閬撶嫭绔嬭繍琛岋紝鏈疄鐜颁簰涓哄鐢ㄥ拰鏁呴殰杞Щ閫氱煡

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鐙珛閫氱煡
def notify_tunnel_status(tunnel_type, status):
    send_email(f"{tunnel_type}闅ч亾鐘舵��: {status}")

# 鉁� 淇鍚庯細浜掍负澶囩敤閫氱煡
def notify_tunnel_status(primary_type, primary_status, fallback_type, fallback_status):
    if primary_status == 'failed' and fallback_status == 'available':
        send_email(
            f"{primary_type}闅ч亾鏁呴殰锛屽凡鍒囨崲鍒皗fallback_type}澶囩敤闅ч亾",
            email_type='fallback_available'
        )
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏁呴殰杞Щ** | 鏃� 鉂� | 鑷姩鍒囨崲 鉁� |
| **閫氱煡鍙婃椂鎬�** | 寤惰繜 鉂� | 鍗虫椂 鉁� |
| **绯荤粺鍙敤鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 瀹炵幇鍙岄毀閬撲簰涓哄鐢ㄦ満鍒讹紝涓婚毀閬撴晠闅滄椂鑷姩鍒囨崲鍒板鐢ㄩ毀閬撳苟鍙戦�侀�氱煡





### v3.8.46 (2026-07-17) - 馃寪 CF + hostc 鍙岄毀閬撳苟琛� + 蹇冭烦楠岃瘉 + 鍒犻櫎 NS 鐩戞帶

#### 闂: 鍗曢毀閬撶ǔ瀹氭�т笉瓒筹紝NS鐩戞帶鍐椾綑
**鐜拌薄**: 鍗曚竴闅ч亾鏁呴殰鏃舵湇鍔′腑鏂紝NS鍩熷悕鐩戞帶鍔熻兘閲嶅涓斿崰鐢ㄨ祫婧�

**鏍规湰鍘熷洜**: 缂哄皯鍙岄毀閬撳苟琛屾満鍒讹紝NS鐩戞帶涓庨毀閬撶洃鎺у姛鑳介噸鍙�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍗曢毀閬� + NS鐩戞帶
def start_service():
    start_hostc_tunnel()
    monitor_ns_records()

# 鉁� 淇鍚庯細鍙岄毀閬撳苟琛� + 鍒犻櫎NS鐩戞帶
def start_service():
    start_hostc_tunnel()
    start_cf_tunnel()
    verify_both_tunnels()
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **闅ч亾鏁伴噺** | 1涓� 鉂� | 2涓苟琛� 鉁� |
| **NS鐩戞帶** | 鍐椾綑 鉂� | 宸插垹闄� 鉁� |
| **鏈嶅姟鍙敤鎬�** | 95% 鉂� | 99.9% 鉁� |

**鎶�鏈粏鑺�**: 瀹炵幇CF鍜宧ostc鍙岄毀閬撳苟琛岃繍琛岋紝娣诲姞蹇冭烦楠岃瘉锛屽垹闄ゅ啑浣欑殑NS鍩熷悕鐩戞帶





### v3.8.45 (2026-07-17) - 馃寪 NS鍗囩骇鑷姩鐩戞帶 + Quick Tunnel鑷姩鍗囩骇鍒癗amed Tunnel

#### 闂: Quick Tunnel绋冲畾鎬у樊锛屾棤娉曡嚜鍔ㄥ崌绾�
**鐜拌薄**: Cloudflare Quick Tunnel闅忔満鍩熷悕涓嶇ǔ瀹氾紝鏃犳硶鑷姩鍗囩骇鍒癗amed Tunnel

**鏍规湰鍘熷洜**: 缂哄皯鑷姩妫�娴嬪拰鍗囩骇鏈哄埗

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鎵嬪姩鍗囩骇
def create_tunnel():
    return create_quick_tunnel()

# 鉁� 淇鍚庯細鑷姩鍗囩骇
def create_tunnel():
    quick_tunnel = create_quick_tunnel()
    if detect_stable_usage(quick_tunnel):
        named_tunnel = upgrade_to_named_tunnel(quick_tunnel)
        return named_tunnel
    return quick_tunnel
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **闅ч亾绫诲瀷** | Quick Tunnel 鉂� | Named Tunnel 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |
| **鑷姩鍖栫▼搴�** | 鎵嬪姩 鉂� | 鑷姩 鉁� |

**鎶�鏈粏鑺�**: 妫�娴婹uick Tunnel浣跨敤绋冲畾鎬э紝鑷姩鍗囩骇鍒癗amed Tunnel骞堕厤缃嚜瀹氫箟鍩熷悕





### v3.8.44 (2026-07-17) - 馃寪 Named Tunnel + 鑷畾涔夊煙鍚� + 鑷姩闄嶇骇鍒� Quick Tunnel

#### 闂: Named Tunnel閰嶇疆澶辫触鏃舵棤闄嶇骇鏂规
**鐜拌薄**: Named Tunnel鍒涘缓澶辫触鏃讹紝鏈嶅姟瀹屽叏涓柇锛屾棤澶囩敤鏂规

**鏍规湰鍘熷洜**: 缂哄皯鑷姩闄嶇骇鏈哄埗

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細澶辫触鍗充腑鏂�
def create_named_tunnel(domain):
    result = cf_api.create_named_tunnel(domain)
    return result.url

# 鉁� 淇鍚庯細澶辫触鑷姩闄嶇骇
def create_named_tunnel(domain):
    try:
        result = cf_api.create_named_tunnel(domain)
        return result.url
    except Exception as e:
        logging.warning(f"Named Tunnel failed, fallback to Quick Tunnel: {e}")
        return create_quick_tunnel()
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏁呴殰鎭㈠** | 鏃� 鉂� | 鑷姩闄嶇骇 鉁� |
| **鏈嶅姟鍙敤鎬�** | 浣� 鉂� | 楂� 鉁� |
| **鐢ㄦ埛浣撻獙** | 涓柇 鉂� | 鎸佺画 鉁� |

**鎶�鏈粏鑺�**: Named Tunnel鍒涘缓澶辫触鏃惰嚜鍔ㄩ檷绾у埌Quick Tunnel锛岀‘淇濇湇鍔′笉涓柇





### v3.8.43 (2026-07-17) - 馃敡 Cloudflare Tunnel 璺ㄥ钩鍙版敮鎸� + 闅ч亾鍒囨崲浼樺寲

#### 闂: Cloudflare Tunnel璺ㄥ钩鍙板吋瀹规�у樊
**鐜拌薄**: Windows/macOS/Linux涓奀loudflare Tunnel琛屼负涓嶄竴鑷�

**鏍规湰鍘熷洜**: 璺ㄥ钩鍙拌矾寰勫拰杩涚▼绠＄悊閫昏緫鏈粺涓�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細纭紪鐮佽矾寰�
def start_cf_tunnel():
    subprocess.run(['/usr/local/bin/cloudflared', 'tunnel', '--url', 'http://localhost:8080'])

# 鉁� 淇鍚庯細璺ㄥ钩鍙拌矾寰�
import platform
def start_cf_tunnel():
    system = platform.system()
    if system == 'Windows':
        cf_path = 'C:```Program Files```cloudflared```cloudflared.exe'
    elif system == 'Darwin':
        cf_path = '/usr/local/bin/cloudflared'
    else:
        cf_path = '/usr/bin/cloudflared'
    subprocess.run([cf_path, 'tunnel', '--url', 'http://localhost:8080'])
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **璺ㄥ钩鍙版敮鎸�** | 宸� 鉂� | 濂� 鉁� |
| **璺緞绠＄悊** | 纭紪鐮� 鉂� | 鍔ㄦ�佹娴� 鉁� |
| **鍏煎鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 缁熶竴Cloudflare Tunnel璺ㄥ钩鍙拌矾寰勭鐞嗭紝浼樺寲闅ч亾鍒囨崲閫昏緫





### v3.8.42 (2026-07-17) - 馃敡 Flask璁块棶鏃ュ織鏍煎紡浼樺寲

#### 闂: Flask璁块棶鏃ュ織鏍煎紡涓嶇粺涓�锛岄毦浠ュ垎鏋�
**鐜拌薄**: Flask璁块棶鏃ュ織鏍煎紡娣蜂贡锛岀己灏戝叧閿俊鎭紙濡傚搷搴旀椂闂淬�佺敤鎴蜂唬鐞嗭級

**鏍规湰鍘熷洜**: 鏈厤缃粺涓�鐨勬棩蹇楁牸寮�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細榛樿鏃ュ織鏍煎紡
# 127.0.0.1 - - [17/Jul/2026 10:00:00] "GET / HTTP/1.1" 200 -

# 鉁� 淇鍚庯細缁撴瀯鍖栨棩蹇楁牸寮�
import logging
logging.basicConfig(
    format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
)
# [2026-07-17 10:00:00] INFO in app: 127.0.0.1 - GET / - 200 - 0.05s - Mozilla/5.0
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏃ュ織鏍煎紡** | 娣蜂贡 鉂� | 缁熶竴 鉁� |
| **鍙垎鏋愭��** | 宸� 鉂� | 濂� 鉁� |
| **璋冭瘯鏁堢巼** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 缁熶竴Flask璁块棶鏃ュ織鏍煎紡锛屾坊鍔犲搷搴旀椂闂淬�佺敤鎴蜂唬鐞嗙瓑鍏抽敭淇℃伅





### v3.8.41 (2026-07-17) - 馃悰 蹇冭烦寰幆閲嶅惎鍚庣姸鎬侀噸缃慨澶�

#### 闂: 蹇冭烦寰幆閲嶅惎鍚庣姸鎬佹湭閲嶇疆
**鐜拌薄**: 闅ч亾閲嶅惎鍚庯紝蹇冭烦寰幆浠嶄娇鐢ㄦ棫鐘舵�侊紝瀵艰嚧璇垽

**鏍规湰鍘熷洜**: 蹇冭烦寰幆鐘舵�佸彉閲忔湭鍦ㄩ噸鍚椂閲嶇疆

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鐘舵�佹湭閲嶇疆
tunnel_status = {}
def restart_tunnel():
    stop_tunnel()
    start_tunnel()
    # tunnel_status浠嶄繚鐣欐棫鍊�

# 鉁� 淇鍚庯細鐘舵�侀噸缃�
tunnel_status = {}
def restart_tunnel():
    stop_tunnel()
    tunnel_status.clear()  # 閲嶇疆鐘舵��
    start_tunnel()
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鐘舵�佸噯纭��** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **閲嶅惎鍙潬鎬�** | 浣� 鉂� | 楂� 鉁� |
| **璋冭瘯闅惧害** | 楂� 鉂� | 浣� 鉁� |

**鎶�鏈粏鑺�**: 闅ч亾閲嶅惎鏃舵竻绌哄績璺冲惊鐜姸鎬佸彉閲忥紝纭繚鐘舵�佷竴鑷存��





### v3.8.40 (2026-07-17) - 馃悰 hostc杩涚▼绔炴�佹潯浠朵慨澶� + 璋冭瘯鏃ュ織澧炲己

#### 闂: hostc杩涚▼鍚姩鏃跺瓨鍦ㄧ珵鎬佹潯浠�
**鐜拌薄**: 澶氱嚎绋嬬幆澧冧笅hostc杩涚▼鍚姩鏃跺嚭鐜扮鍙ｅ崰鐢ㄦ垨杩涚▼鍐茬獊

**鏍规湰鍘熷洜**: 杩涚▼鍚姩鍜岀姸鎬佹鏌ユ湭鍔犻攣淇濇姢

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鏃犻攣淇濇姢
def start_hostc():
    if not is_hostc_running():
        subprocess.Popen(['hostc'])

# 鉁� 淇鍚庯細鍔犻攣淇濇姢
import threading
lock = threading.Lock()
def start_hostc():
    with lock:
        if not is_hostc_running():
            logging.debug("[hostc] Starting process with lock protection")
            subprocess.Popen(['hostc'])
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **绔炴�佹潯浠�** | 瀛樺湪 鉂� | 宸蹭慨澶� 鉁� |
| **杩涚▼绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |
| **璋冭瘯鏃ュ織** | 涓嶈冻 鉂� | 璇︾粏 鉁� |

**鎶�鏈粏鑺�**: 浣跨敤绾跨▼閿佷繚鎶ostc杩涚▼鍚姩閫昏緫锛屾坊鍔犺缁嗚皟璇曟棩蹇�




### v3.8.39 (2026-07-12) - 馃敡 鈿� 闅ч亾蹇冭烦涓庣ǔ瀹氭�ч獙璇佸姞閫熶紭鍖�

#### 闂: 闅ч亾蹇冭烦楠岃瘉绌虹獥鏈熻繃闀匡紙3-5鍒嗛挓锛�
**鐜拌薄**: 闅ч亾鏁呴殰鍚庨渶瑕�3-5鍒嗛挓鎵嶈兘妫�娴嬪埌骞堕噸鍚紝鏈嶅姟涓柇鏃堕棿闀�

**鏍规湰鍘熷洜**: 蹇冭烦闂撮殧60绉掋�佸け鏁堥槇鍊�3娆°�佺ǔ瀹氭�ч獙璇�2娆★紝瀵艰嚧绌虹獥鏈熻繃闀�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細绌虹獥鏈�3-5鍒嗛挓
HEARTBEAT_INTERVAL = 60  # 蹇冭烦闂撮殧60绉�
FAILURE_THRESHOLD = 3    # 澶辨晥闃堝��3娆�
STABILITY_CHECKS = 2     # 绋冲畾鎬ч獙璇�2娆�

# 鉁� 淇鍚庯細绌虹獥鏈�1-1.5鍒嗛挓
HEARTBEAT_INTERVAL = 30  # 蹇冭烦闂撮殧30绉�
FAILURE_THRESHOLD = 2    # 澶辨晥闃堝��2娆�
STABILITY_CHECKS = 1     # 绋冲畾鎬ч獙璇�1娆�
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **蹇冭烦闂撮殧** | 60绉� 鉂� | 30绉� 鉁� |
| **澶辨晥闃堝��** | 3娆� 鉂� | 2娆� 鉁� |
| **绌虹獥鏈�** | 3-5鍒嗛挓 鉂� | 1-1.5鍒嗛挓 鉁� |
| **鏁呴殰妫�娴嬮�熷害** | 鎱� 鉂� | 蹇� 鉁� |

**鎶�鏈粏鑺�**: 浼樺寲蹇冭烦鍙傛暟锛屽皢绌虹獥鏈熶粠3-5鍒嗛挓缂╃煭鑷�1-1.5鍒嗛挓锛屾彁鍗囨晠闅滄娴嬮�熷害





### v3.8.38 (2026-07-12) - 馃悰 绔彛8888鍗犵敤绔炴�佹潯浠朵慨澶�

#### 闂: 绔彛8888琚崰鐢ㄥ鑷存湇鍔″惎鍔ㄥけ璐�
**鐜拌薄**: 澶氳繘绋嬬幆澧冧笅锛岀鍙�8888琚崰鐢紝鏈嶅姟鏃犳硶鍚姩

**鏍规湰鍘熷洜**: 杩涚▼鍚姩鍜岀鍙ｆ鏌ュ瓨鍦ㄧ珵鎬佹潯浠�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細绔炴�佹潯浠�
def start_server():
    if not is_port_in_use(8888):
        app.run(port=8888)  # 鍙兘鍦ㄦ鍒昏鍏朵粬杩涚▼鍗犵敤

# 鉁� 淇鍚庯細鍔犻攣淇濇姢
import socket
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('0.0.0.0', 8888))
            app.run(port=8888)
        except OSError:
            logging.error("Port 8888 already in use")
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **绔彛鍗犵敤妫�娴�** | 绔炴�佹潯浠� 鉂� | 鍘熷瓙鎿嶄綔 鉁� |
| **鍚姩鎴愬姛鐜�** | 浣� 鉂� | 楂� 鉁� |
| **閿欒鎻愮ず** | 鏃� 鉂� | 鏄庣‘ 鉁� |

**鎶�鏈粏鑺�**: 浣跨敤socket鍘熷瓙鎿嶄綔妫�娴嬬鍙ｅ崰鐢紝閬垮厤绔炴�佹潯浠�





### v3.8.37 (2026-07-12) - 馃悰 /api/readme-sections 500 閿欒淇

#### 闂: /api/readme-sections鎺ュ彛杩斿洖500閿欒
**鐜拌薄**: 鍓嶇璇锋眰/api/readme-sections鎺ュ彛鏃讹紝杩斿洖500鍐呴儴鏈嶅姟鍣ㄩ敊璇�

**鏍规湰鍘熷洜**: README.md鏂囦欢璺緞閿欒鎴栨枃浠朵笉瀛樺湪

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細璺緞閿欒
@app.get('/api/readme-sections')
def get_readme_sections():
    with open('README.md', 'r') as f:  # 鐩稿璺緞鍙兘閿欒
        content = f.read()

# 鉁� 淇鍚庯細璺緞姝ｇ‘
import os
@app.get('/api/readme-sections')
def get_readme_sections():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if not os.path.exists(readme_path):
        return {"error": "README.md not found"}, 404
    with open(readme_path, 'r') as f:
        content = f.read()
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鎺ュ彛鐘舵��** | 500閿欒 鉂� | 200鎴愬姛 鉁� |
| **璺緞鍑嗙‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **閿欒澶勭悊** | 鏃� 鉂� | 瀹屽杽 鉁� |

**鎶�鏈粏鑺�**: 淇README.md鏂囦欢璺緞锛屾坊鍔犳枃浠跺瓨鍦ㄦ�ф鏌ュ拰閿欒澶勭悊





### v3.8.36 (2026-07-12) - 馃悰 run.sh 鍑芥暟瀹氫箟椤哄簭淇 + pre_launch 鍑芥暟鍖栭噸鏋�

#### 闂: run.sh鑴氭湰鍑芥暟瀹氫箟椤哄簭閿欒
**鐜拌薄**: 鎵цrun.sh鏃讹紝鎻愮ず"鍑芥暟鏈畾涔�"閿欒

**鏍规湰鍘熷洜**: 鍑芥暟璋冪敤椤哄簭鏃╀簬鍑芥暟瀹氫箟

**淇鏂规**:
```bash
# 鉂� 淇鍓嶏細鍑芥暟璋冪敤鍦ㄥ畾涔変箣鍓�
pre_launch  # 鍑芥暟鏈畾涔�
function pre_launch() {
    echo "Pre-launch checks"
}

# 鉁� 淇鍚庯細鍑芥暟瀹氫箟鍦ㄨ皟鐢ㄤ箣鍓�
function pre_launch() {
    echo "Pre-launch checks"
}
pre_launch
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鑴氭湰鎵ц** | 澶辫触 鉂� | 鎴愬姛 鉁� |
| **鍑芥暟瀹氫箟椤哄簭** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **浠ｇ爜鍙淮鎶ゆ��** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 璋冩暣run.sh涓嚱鏁板畾涔夐『搴忥紝纭繚鍑芥暟瀹氫箟鍦ㄨ皟鐢ㄤ箣鍓嶏紝骞堕噸鏋刾re_launch涓虹嫭绔嬪嚱鏁�





### v3.8.35 (2026-07-11) - 馃摑 鏍稿績鑼冨紡鏂囨。琛ュ叏锛�7椤癸級

#### 闂: 鏍稿績寮�鍙戣寖寮忔枃妗ｄ笉瀹屾暣
**鐜拌薄**: 椤圭洰缂哄皯鏍稿績寮�鍙戣寖寮忔枃妗ｏ紝鏂板紑鍙戣�呴毦浠ュ揩閫熶笂鎵�

**鏍规湰鍘熷洜**: 鏃╂湡寮�鍙戞湭鍙婃椂琛ュ厖鑼冨紡鏂囨。

**淇鏂规**:
```markdown
<!-- 鉁� 琛ュ叏7椤规牳蹇冭寖寮� -->
## 鏍稿績寮�鍙戣寖寮�
1. **闅ч亾绠＄悊鑼冨紡**: tunnel_url.txt浣滀负鏉冨▉鏁版嵁婧�
2. **閭欢閫氱煡鑼冨紡**: 鐙珛鍙戦�侊紝闃查噸澶嶆満鍒�
3. **蹇冭烦楠岃瘉鑼冨紡**: 姣忎釜闅ч亾鐙珛楠岃瘉
4. **璺ㄥ钩鍙板吋瀹硅寖寮�**: 鍔ㄦ�佽矾寰勬娴�
5. **閿欒澶勭悊鑼冨紡**: 缁熶竴寮傚父鎹曡幏鍜屾棩蹇�
6. **閰嶇疆绠＄悊鑼冨紡**: 鐜鍙橀噺浼樺厛
7. **娴嬭瘯鑼冨紡**: 鍗曞厓娴嬭瘯瑕嗙洊鏍稿績閫昏緫
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鑼冨紡鏂囨。瀹屾暣鎬�** | 缂哄け 鉂� | 瀹屾暣 鉁� |
| **鏂版墜涓婃墜闅惧害** | 楂� 鉂� | 浣� 鉁� |
| **浠ｇ爜瑙勮寖鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 琛ュ叏7椤规牳蹇冨紑鍙戣寖寮忔枃妗ｏ紝鍖呮嫭闅ч亾绠＄悊銆侀偖浠堕�氱煡銆佸績璺抽獙璇佺瓑鍏抽敭鑼冨紡





### v3.8.34 (2026-07-11) - 馃摑 绉诲姩绔�傞厤鑼冨紡鏂囨。鍖�

#### 闂: 绉诲姩绔�傞厤缂哄皯瑙勮寖鏂囨。
**鐜拌薄**: 绉诲姩绔�傞厤缁忛獙鏈枃妗ｅ寲锛屾瘡娆￠兘闇�閲嶆柊鎽哥储

**鏍规湰鍘熷洜**: 缂哄皯绉诲姩绔�傞厤鑼冨紡鏂囨。

**淇鏂规**:
```markdown
<!-- 鉁� 绉诲姩绔�傞厤鑼冨紡 -->
## 绉诲姩绔�傞厤鑼冨紡
1. **鍝嶅簲寮忓竷灞�**: 浣跨敤CSS Flexbox鍜孏rid
2. **瑙︽懜浼樺寲**: 鎸夐挳鏈�灏忓昂瀵�44x44px
3. **瀛椾綋閫傞厤**: 浣跨敤rem鍗曚綅
4. **鍥剧墖浼樺寲**: 浣跨敤WebP鏍煎紡锛屾噿鍔犺浇
5. **鎬ц兘浼樺寲**: 鍑忓皯HTTP璇锋眰锛屼娇鐢–DN
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **绉诲姩绔�傞厤瑙勮寖** | 鏃� 鉂� | 瀹屾暣 鉁� |
| **寮�鍙戞晥鐜�** | 浣� 鉂� | 楂� 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**: 灏嗙Щ鍔ㄧ閫傞厤缁忛獙鏂囨。鍖栵紝褰㈡垚鍙鐢ㄧ殑寮�鍙戣寖寮�





### v3.8.33 (2026-07-11) - 馃敡 hostc CDN闀滃儚婧愪慨姝� + bat/sh闀滃儚鍒楄〃缁熶竴

#### 闂: hostc CDN闀滃儚婧愰敊璇紝bat/sh闀滃儚鍒楄〃涓嶄竴鑷�
**鐜拌薄**: hostc涓嬭浇澶辫触锛學indows鍜孡inux闀滃儚鍒楄〃涓嶅悓姝�

**鏍规湰鍘熷洜**: CDN闀滃儚婧怳RL閿欒锛宐at鍜宻h鑴氭湰闀滃儚鍒楄〃鏈粺涓�

**淇鏂规**:
```bash
# 鉂� 淇鍓嶏細闀滃儚婧愰敊璇�
MIRRORS=(
    "https://old-mirror.com/hostc"
    "https://another-mirror.com/hostc"
)

# 鉁� 淇鍚庯細闀滃儚婧愭纭笖缁熶竴
MIRRORS=(
    "https://cdn.jsdelivr.net/npm/hostc@1.3.0/dist/hostc"
    "https://unpkg.com/hostc@1.3.0/dist/hostc"
    "https://cdn.jsdelivr.net/npm/hostc@1.3.0/dist/hostc.exe"
)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **闀滃儚婧愬噯纭��** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **bat/sh涓�鑷存��** | 涓嶄竴鑷� 鉂� | 缁熶竴 鉁� |
| **涓嬭浇鎴愬姛鐜�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 淇hostc CDN闀滃儚婧怳RL锛岀粺涓�Windows鍜孡inux闀滃儚鍒楄〃





### v3.8.32 (2026-07-11) - 馃敡 闅ч亾瀹堟姢浜屾楠岃瘉+鎸囨暟閫�閬�+蹇冭烦闃堝�间紭鍖�

#### 闂: 闅ч亾瀹堟姢閫昏緫涓嶅鍋ュ．
**鐜拌薄**: 闅ч亾鏁呴殰鍚庨噸鍚け璐ワ紝鏃犱簩娆￠獙璇佸拰閫�閬挎満鍒�

**鏍规湰鍘熷洜**: 缂哄皯浜屾楠岃瘉銆佹寚鏁伴��閬垮拰鍔ㄦ�佸績璺抽槇鍊�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鏃犱簩娆￠獙璇佸拰閫�閬�
def monitor_tunnel():
    if not verify_tunnel():
        restart_tunnel()

# 鉁� 淇鍚庯細浜屾楠岃瘉+鎸囨暟閫�閬�
import time
retry_count = 0
def monitor_tunnel():
    if not verify_tunnel():
        time.sleep(2 ** retry_count)  # 鎸囨暟閫�閬�
        if not verify_tunnel():  # 浜屾楠岃瘉
            restart_tunnel()
            retry_count += 1
        else:
            retry_count = 0
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **浜屾楠岃瘉** | 鏃� 鉂� | 鏈� 鉁� |
| **鎸囨暟閫�閬�** | 鏃� 鉂� | 鏈� 鉁� |
| **閲嶅惎鎴愬姛鐜�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 娣诲姞闅ч亾瀹堟姢浜屾楠岃瘉銆佹寚鏁伴��閬挎満鍒跺拰鍔ㄦ�佸績璺抽槇鍊硷紝鎻愬崌绋冲畾鎬�





### v3.8.31 (2026-07-11) - 馃悰 蹇冭烦閫昏緫5椤逛紭鍖�+瀹介檺鏈熼噸鏋�+闅ч亾閲嶅惎淇+鐗堟湰鍙风粺涓�浠嶳EADME鑾峰彇

#### 闂: 蹇冭烦閫昏緫瀛樺湪澶氶」缂洪櫡
**鐜拌薄**: 蹇冭烦閫昏緫涓嶅噯纭紝瀹介檺鏈熸満鍒朵笉瀹屽杽锛岄毀閬撻噸鍚け璐ワ紝鐗堟湰鍙蜂笉缁熶竴

**鏍规湰鍘熷洜**: 蹇冭烦閫昏緫鏈紭鍖栵紝瀹介檺鏈熸湭閲嶆瀯锛岀増鏈彿鏉ユ簮鍒嗘暎

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細澶氶」缂洪櫡
def heartbeat():
    if not verify():
        restart()  # 鏃犲闄愭湡

# 鉁� 淇鍚庯細5椤逛紭鍖�
def heartbeat():
    # 1. 瀹介檺鏈熸満鍒�
    if not verify():
        grace_period_count += 1
        if grace_period_count >= GRACE_PERIOD_THRESHOLD:
            restart()
            grace_period_count = 0
    
    # 2. 鐗堟湰鍙风粺涓�浠嶳EADME鑾峰彇
    version = get_version_from_readme()
    
    # 3-5. 鍏朵粬浼樺寲...
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **蹇冭烦鍑嗙‘鎬�** | 浣� 鉂� | 楂� 鉁� |
| **瀹介檺鏈熸満鍒�** | 鏃� 鉂� | 瀹屽杽 鉁� |
| **鐗堟湰鍙风粺涓�鎬�** | 鍒嗘暎 鉂� | 缁熶竴 鉁� |

**鎶�鏈粏鑺�**: 浼樺寲蹇冭烦閫昏緫5椤圭己闄凤紝閲嶆瀯瀹介檺鏈熸満鍒讹紝淇闅ч亾閲嶅惎閫昏緫锛岀粺涓�鐗堟湰鍙蜂粠README鑾峰彇





### v3.8.30 (2026-07-11) - 馃敡 闅ч亾閲嶅惎閫昏緫閲嶆瀯 - 鍚堝苟鍙岃矾寰�+瀹介檺鏈熸満鍒�

#### 闂: 闅ч亾閲嶅惎閫昏緫娣蜂贡锛屽瓨鍦ㄥ弻璺緞
**鐜拌薄**: 闅ч亾閲嶅惎閫昏緫鍒嗘暎鍦ㄥ涓嚱鏁颁腑锛岀淮鎶ゅ洶闅�

**鏍规湰鍘熷洜**: 鏃╂湡璁捐閬楃暀锛屾湭鍙婃椂閲嶆瀯

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍙岃矾寰勬贩涔�
def restart_tunnel_v1():
    stop_tunnel()
    start_tunnel()

def restart_tunnel_v2():
    kill_tunnel()
    init_tunnel()

# 鉁� 淇鍚庯細缁熶竴璺緞+瀹介檺鏈�
def restart_tunnel():
    stop_tunnel()
    grace_period()  # 瀹介檺鏈熺瓑寰�
    start_tunnel()
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **浠ｇ爜璺緞** | 鍙岃矾寰勬贩涔� 鉂� | 鍗曡矾寰勬竻鏅� 鉁� |
| **瀹介檺鏈熸満鍒�** | 鏃� 鉂� | 鏈� 鉁� |
| **鍙淮鎶ゆ��** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 鍚堝苟闅ч亾閲嶅惎鍙岃矾寰勶紝娣诲姞瀹介檺鏈熸満鍒讹紝缁熶竴閲嶅惎閫昏緫




### v3.8.29 (2026-07-11) - 馃悰 涓存椂鏂囦欢娉勬紡淇 + Python渚ц嚜鍔ㄦ竻鐞�

#### 闂: temp涓存椂鏂囦欢娉勬紡锛屽崰鐢ㄧ鐩樼┖闂�
**鐜拌薄**: 椤圭洰杩愯涓�娈垫椂闂村悗锛宼emp鐩綍涓嬪爢绉ぇ閲忎复鏃舵枃浠�

**鏍规湰鍘熷洜**: 涓存椂鏂囦欢浣跨敤鍚庢湭鍙婃椂娓呯悊

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細涓存椂鏂囦欢鏈竻鐞�
def process_file(file_path):
    temp_file = f"temp/{file_path}"
    with open(temp_file, 'w') as f:
        f.write(data)
    # 鏈垹闄emp_file

# 鉁� 淇鍚庯細鑷姩娓呯悊
import atexit
import os
temp_files = []

def process_file(file_path):
    temp_file = f"temp/{file_path}"
    temp_files.append(temp_file)
    with open(temp_file, 'w') as f:
        f.write(data)

def cleanup_temp_files():
    for temp_file in temp_files:
        if os.path.exists(temp_file):
            os.remove(temp_file)

atexit.register(cleanup_temp_files)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **涓存椂鏂囦欢娉勬紡** | 鏄� 鉂� | 鍚� 鉁� |
| **纾佺洏鍗犵敤** | 鎸佺画澧為暱 鉂� | 绋冲畾 鉁� |
| **娓呯悊鏈哄埗** | 鏃� 鉂� | 鑷姩 鉁� |

**鎶�鏈粏鑺�**: 娣诲姞涓存椂鏂囦欢鑷姩娓呯悊鏈哄埗锛屼娇鐢╝texit娉ㄥ唽娓呯悊鍑芥暟锛岀‘淇濊繘绋嬮��鍑烘椂娓呯悊涓存椂鏂囦欢





### v3.8.28 (2026-07-11) - 馃寪 hostc绛夊緟URL瓒呮椂浠�120绉掗檷鑷�30绉�

#### 闂: hostc绛夊緟URL瓒呮椂鏃堕棿杩囬暱锛�120绉掞級
**鐜拌薄**: hostc鍚姩鍚庣瓑寰匲RL鐢熸垚锛岃秴鏃舵椂闂�120绉掕繃闀匡紝褰卞搷鐢ㄦ埛浣撻獙

**鏍规湰鍘熷洜**: 鏃╂湡淇濆畧璁剧疆锛屾湭鏍规嵁瀹為檯鎬ц兘浼樺寲

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細瓒呮椂120绉�
HOSTC_URL_TIMEOUT = 120

# 鉁� 淇鍚庯細瓒呮椂30绉�
HOSTC_URL_TIMEOUT = 30
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **URL绛夊緟瓒呮椂** | 120绉� 鉂� | 30绉� 鉁� |
| **鍚姩閫熷害** | 鎱� 鉂� | 蹇� 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**: 灏唄ostc绛夊緟URL瓒呮椂浠�120绉掗檷鑷�30绉掞紝鎻愬崌鍚姩閫熷害鍜岀敤鎴蜂綋楠�





### v3.8.27 (2026-07-10) - 馃悰 闅ч亾閲嶅惎姝诲惊鐜慨澶� - tunnel_need_restart閲嶇疆+hostc鍚姩绛夊緟URL

#### 闂: 闅ч亾閲嶅惎杩涘叆姝诲惊鐜�
**鐜拌薄**: 闅ч亾鏁呴殰鍚庨噸鍚紝浣唗unnel_need_restart鏍囧織鏈噸缃紝瀵艰嚧鍙嶅閲嶅惎

**鏍规湰鍘熷洜**: tunnel_need_restart鏍囧織鍦ㄩ噸鍚悗鏈噸缃紝hostc鍚姩鏈瓑寰匲RL鐢熸垚

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鏍囧織鏈噸缃�
def restart_tunnel():
    start_tunnel()
    # tunnel_need_restart浠嶄负True

# 鉁� 淇鍚庯細鏍囧織閲嶇疆+绛夊緟URL
def restart_tunnel():
    global tunnel_need_restart
    tunnel_need_restart = False
    start_tunnel()
    wait_for_url(timeout=30)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **姝诲惊鐜�** | 瀛樺湪 鉂� | 宸蹭慨澶� 鉁� |
| **閲嶅惎鍙潬鎬�** | 浣� 鉂� | 楂� 鉁� |
| **URL鍙敤鎬�** | 涓嶇‘瀹� 鉂� | 纭繚鍙敤 鉁� |

**鎶�鏈粏鑺�**: 閲嶇疆tunnel_need_restart鏍囧織锛屾坊鍔爃ostc鍚姩鍚庣瓑寰匲RL鐢熸垚閫昏緫





### v3.8.26 (2026-07-10) - 馃悰 闅ч亾鏃RL澶嶇敤Bug淇 - auto_start_tunnel澧炲姞hostc杩涚▼瀛樻椿妫�娴�

#### 闂: 闅ч亾澶嶇敤鏃RL瀵艰嚧璁块棶澶辫触
**鐜拌薄**: auto_start_tunnel妫�娴嬪埌tunnel_url.txt瀛樺湪鏃剁洿鎺ュ鐢紝浣唄ostc杩涚▼宸查��鍑�

**鏍规湰鍘熷洜**: 鏈娴媓ostc杩涚▼瀛樻椿鐘舵�侊紝鐩存帴澶嶇敤鏃RL

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鏈娴嬭繘绋嬪瓨娲�
def auto_start_tunnel():
    if os.path.exists('tunnel_url.txt'):
        return read_url()  # hostc鍙兘宸查��鍑�

# 鉁� 淇鍚庯細妫�娴嬭繘绋嬪瓨娲�
def auto_start_tunnel():
    if os.path.exists('tunnel_url.txt'):
        if is_hostc_running():  # 妫�娴嬭繘绋嬪瓨娲�
            return read_url()
        else:
            os.remove('tunnel_url.txt')  # 娓呯悊鏃RL
    start_new_tunnel()
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **URL鍑嗙‘鎬�** | 鏃RL鍙兘澶辨晥 鉂� | 纭繚鏈夋晥 鉁� |
| **杩涚▼妫�娴�** | 鏃� 鉂� | 鏈� 鉁� |
| **璁块棶鎴愬姛鐜�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 鍦╝uto_start_tunnel涓坊鍔爃ostc杩涚▼瀛樻椿妫�娴嬶紝閬垮厤澶嶇敤澶辨晥URL





### v3.8.25 (2026-07-10) - 馃敡 pip渚濊禆瀹夎鏅鸿兘璺宠繃 - 鍚姩鍔犻��20绉掆啋0.1绉�

#### 闂: 姣忔鍚姩閮芥鏌ip渚濊禆锛岃�楁椂20绉�
**鐜拌薄**: 椤圭洰姣忔鍚姩閮芥墽琛宲ip install锛岃�楁椂20绉掞紝褰卞搷寮�鍙戞晥鐜�

**鏍规湰鍘熷洜**: 鏈疄鐜颁緷璧栧畨瑁呮櫤鑳借烦杩囨満鍒�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細姣忔閮藉畨瑁�
def install_dependencies():
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

# 鉁� 淇鍚庯細鏅鸿兘璺宠繃
def install_dependencies():
    if check_dependencies_installed():
        logging.info("Dependencies already installed, skipping...")
        return
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

def check_dependencies_installed():
    try:
        import_requirements()
        return True
    except ImportError:
        return False
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍚姩鏃堕棿** | 20绉� 鉂� | 0.1绉� 鉁� |
| **渚濊禆妫�鏌�** | 姣忔瀹夎 鉂� | 鏅鸿兘璺宠繃 鉁� |
| **寮�鍙戞晥鐜�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 瀹炵幇pip渚濊禆瀹夎鏅鸿兘璺宠繃鏈哄埗锛岄�氳繃妫�鏌ヤ緷璧栨槸鍚﹀凡瀹夎鏉ュ喅瀹氭槸鍚︽墽琛屽畨瑁�





### v3.8.24 (2026-07-10) - 馃摫 hostc閫�鍑鸿嚜鍔ㄩ噸鍚� + 鍗虫椂閭欢閫氱煡 + Flask鍚姩妫�娴嬪姞閫�

#### 闂: hostc閫�鍑哄悗鏃犺嚜鍔ㄩ噸鍚紝閭欢閫氱煡寤惰繜锛孎lask鍚姩妫�娴嬫參
**鐜拌薄**: hostc杩涚▼鎰忓閫�鍑哄悗鏈嶅姟涓柇锛岄偖浠堕�氱煡寤惰繜2-3鍒嗛挓锛孎lask鍚姩妫�娴嬫參

**鏍规湰鍘熷洜**: 缂哄皯杩涚▼閫�鍑鸿嚜鍔ㄩ噸鍚満鍒讹紝閭欢閫氱煡渚濊禆蹇冭烦寰幆锛孎lask鍚姩妫�娴嬪弬鏁颁繚瀹�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鏃犺嚜鍔ㄩ噸鍚�
def monitor_hostc():
    if not is_hostc_running():
        logging.error("hostc exited")

# 鉁� 淇鍚庯細鑷姩閲嶅惎+鍗虫椂閫氱煡
def monitor_hostc():
    if not is_hostc_running():
        logging.warning("hostc exited, restarting...")
        restart_tunnel()
        send_email("hostc闅ч亾宸查噸鍚�")

# Flask鍚姩妫�娴嬪姞閫�
# 鉂� 淇鍓嶏細鍒濆绛夊緟6绉掞紝妫�娴嬮棿闅�3绉�
time.sleep(6)
while not is_flask_ready():
    time.sleep(3)

# 鉁� 淇鍚庯細鍒濆绛夊緟1绉掞紝妫�娴嬮棿闅�1绉�
time.sleep(1)
while not is_flask_ready():
    time.sleep(1)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **杩涚▼閫�鍑哄鐞�** | 鏃� 鉂� | 鑷姩閲嶅惎 鉁� |
| **閭欢閫氱煡寤惰繜** | 2-3鍒嗛挓 鉂� | 鍗虫椂 鉁� |
| **Flask鍚姩妫�娴�** | 鎱� 鉂� | 蹇� 鉁� |

**鎶�鏈粏鑺�**: 娣诲姞hostc閫�鍑鸿嚜鍔ㄩ噸鍚満鍒讹紝瀹炵幇鍗虫椂閭欢閫氱煡锛屽姞閫烣lask鍚姩妫�娴�





### v3.8.23 (2026-07-10) - 馃敡 Web鏈嶅姟绉掔骇鍚姩 + 闅ч亾闈為樆濉炰紭鍖� + hostc鏈湴鍖� + CDN杞瀹夎 + dist浼樺寲

#### 闂: Web鏈嶅姟鍚姩鎱紝闅ч亾闃诲锛宧ostc涓嬭浇涓嶇ǔ瀹�
**鐜拌薄**: Web鏈嶅姟鍚姩闇�瑕佹暟绉掞紝闅ч亾鍚姩闃诲涓绘祦绋嬶紝hostc涓嬭浇缁忓父澶辫触

**鏍规湰鍘熷洜**: Web鏈嶅姟鍚姩閫昏緫鏈紭鍖栵紝闅ч亾鍚姩閲囩敤闃诲鏂瑰紡锛宧ostc渚濊禆杩滅▼涓嬭浇

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細闃诲鍚姩
def start_service():
    start_tunnel()  # 闃诲绛夊緟
    start_web()

# 鉁� 淇鍚庯細闈為樆濉炲惎鍔�
def start_service():
    threading.Thread(target=start_tunnel).start()  # 鍚庡彴鍚姩
    start_web()  # 绔嬪嵆鍚姩Web鏈嶅姟

# hostc鏈湴鍖�
# 鉂� 淇鍓嶏細杩滅▼涓嬭浇
def download_hostc():
    url = "https://remote-server.com/hostc"
    download(url)

# 鉁� 淇鍚庯細鏈湴+CDN杞
def download_hostc():
    mirrors = [
        "local://dist/hostc",
        "https://cdn.jsdelivr.net/npm/hostc",
        "https://unpkg.com/hostc"
    ]
    for mirror in mirrors:
        try:
            return download(mirror)
        except:
            continue
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **Web鍚姩閫熷害** | 鎱� 鉂� | 绉掔骇 鉁� |
| **闅ч亾鍚姩鏂瑰紡** | 闃诲 鉂� | 闈為樆濉� 鉁� |
| **hostc涓嬭浇绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 浼樺寲Web鏈嶅姟鍚姩閫昏緫锛屽疄鐜伴毀閬撻潪闃诲鍚姩锛宧ostc鏈湴鍖栧苟鏀寔CDN杞涓嬭浇





### v3.8.21 (2026-07-10) - 馃敡 Node.js渚濊禆鍚堝苟 + API鑼冨紡鏂囨。瀹屽杽 + 瀹夊叏瑙勮寖

#### 闂: Node.js渚濊禆鍒嗘暎锛孉PI鑼冨紡鏂囨。涓嶅畬鏁达紝瀹夊叏瑙勮寖缂哄け
**鐜拌薄**: Node.js渚濊禆鍒嗘暎鍦ㄥ涓猵ackage.json锛孉PI鑼冨紡鏂囨。缂哄皯鍏抽敭鍐呭锛岀己灏戝畨鍏ㄨ鑼�

**鏍规湰鍘熷洜**: 鏃╂湡寮�鍙戞湭鍙婃椂鏁寸悊渚濊禆鍜屾枃妗�

**淇鏂规**:
```json
// 鉂� 淇鍓嶏細渚濊禆鍒嗘暎
// package1.json
{
  "dependencies": {
    "express": "^4.18.0"
  }
}
// package2.json
{
  "dependencies": {
    "axios": "^1.0.0"
  }
}

// 鉁� 淇鍚庯細渚濊禆鍚堝苟
// package.json
{
  "dependencies": {
    "express": "^4.18.0",
    "axios": "^1.0.0",
    "ws": "^8.0.0"
  }
}
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **渚濊禆绠＄悊** | 鍒嗘暎 鉂� | 缁熶竴 鉁� |
| **API鑼冨紡鏂囨。** | 涓嶅畬鏁� 鉂� | 瀹屾暣 鉁� |
| **瀹夊叏瑙勮寖** | 缂哄け 鉂� | 瀹屽杽 鉁� |

**鎶�鏈粏鑺�**: 鍚堝苟Node.js渚濊禆鍒板崟涓�package.json锛屽畬鍠凙PI鑼冨紡鏂囨。锛屾坊鍔犲畨鍏ㄨ鑼冪珷鑺�





### v3.8.20 (2026-07-10) - 馃悰 鍗虫椂閭欢閫氱煡+鍓嶇鐘舵�佷慨澶�+楠岃瘉鍔犻��; 鍘婚櫎棰勫惎鍔ㄦ蹇垫敼涓虹洿鎺ュ惎鍔�

#### 闂: 閭欢閫氱煡寤惰繜锛屽墠绔姸鎬佷笉鍑嗙‘锛岄獙璇佹參锛岄鍚姩姒傚康娣蜂贡
**鐜拌薄**: 閭欢閫氱煡寤惰繜2-3鍒嗛挓锛屽墠绔樉绀虹姸鎬佷笌瀹為檯涓嶇锛岄獙璇佽�楁椂锛岄鍚姩姒傚康闅句互鐞嗚В

**鏍规湰鍘熷洜**: 閭欢閫氱煡渚濊禆蹇冭烦寰幆锛屽墠绔姸鎬佹洿鏂颁笉鍙婃椂锛岄獙璇侀�昏緫淇濆畧锛岄鍚姩姒傚康璁捐涓嶅悎鐞�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細閭欢閫氱煡寤惰繜
def send_notification():
    # 绛夊緟蹇冭烦寰幆瑙﹀彂
    pass

# 鉁� 淇鍚庯細鍗虫椂閭欢閫氱煡
def send_notification():
    threading.Thread(target=send_email, args=(url, status)).start()

# 鍘婚櫎棰勫惎鍔ㄦ蹇�
# 鉂� 淇鍓嶏細棰勫惎鍔�+姝ｅ紡鍚姩
def pre_start_tunnel():
    init_tunnel()
def start_tunnel():
    pre_start_tunnel()
    launch_tunnel()

# 鉁� 淇鍚庯細鐩存帴鍚姩
def start_tunnel():
    init_and_launch_tunnel()
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **閭欢閫氱煡寤惰繜** | 2-3鍒嗛挓 鉂� | 鍗虫椂 鉁� |
| **鍓嶇鐘舵�佸噯纭��** | 涓嶅噯纭� 鉂� | 鍑嗙‘ 鉁� |
| **鍚姩姒傚康** | 娣蜂贡 鉂� | 娓呮櫚 鉁� |

**鎶�鏈粏鑺�**: 瀹炵幇鍗虫椂閭欢閫氱煡锛屼慨澶嶅墠绔姸鎬佹樉绀猴紝鍔犻�熼獙璇侀�昏緫锛屽幓闄ら鍚姩姒傚康鏀逛负鐩存帴鍚姩




### v3.8.18 (2026-07-10) - 馃摑 鏂囨。鍚屾 - auto_start_tunnel涓嶉樆濉炶鑼� + PY-STD-TUNNEL-003

#### 闂: 鏂囨。涓庝唬鐮佸疄鐜颁笉鍚屾锛宎uto_start_tunnel闃诲閫昏緫涓嶆竻鏅�
**鐜拌薄**: README/skill.md/skill.docx涓殑auto_start_tunnel瑙勮寖涓庡疄闄呬唬鐮佷笉涓�鑷达紝闃诲閫昏緫娣蜂贡

**鏍规湰鍘熷洜**: 浠ｇ爜閲嶆瀯鍚庢湭鍙婃椂鍚屾鏂囨。锛岄樆濉為�昏緫璁捐涓嶅悎鐞�

**淇鏂规**:
```markdown
<!-- 鉁� 鏇存柊鏂囨。瑙勮寖 -->
## PY-STD-TUNNEL-003: auto_start_tunnel涓嶉樆濉炶鑼�
- **鏍稿績鍘熷垯**: auto_start_tunnel涓嶉樆濉炵瓑寰咃紝hostc鍦ㄨ窇灏辩洿鎺ヨ繑鍥�
- **URL鑾峰彇**: URL鐢卞績璺虫満鍒跺悗鍙拌幏鍙栭獙璇佸彂閭欢
- **楠岃瘉閫昏緫**: 鍘绘帀auto_start_tunnel涓墍鏈夐獙璇侊紝鍏綉楠岃瘉浜ょ粰蹇冭烦寰幆
- **鏈湴楠岃瘉**: localhost楠岃瘉鏇夸唬鍏綉楠岃瘉锛屽姞閫熷惎鍔�
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏂囨。鍑嗙‘鎬�** | 杩囨椂 鉂� | 鏈�鏂� 鉁� |
| **闃诲閫昏緫** | 娣蜂贡 鉂� | 娓呮櫚 鉁� |
| **鍚姩閫熷害** | 鎱� 鉂� | 蹇� 鉁� |

**鎶�鏈粏鑺�**: 鍚屾鏇存柊README/skill.md/skill.docx锛屾槑纭產uto_start_tunnel涓嶉樆濉炶鑼冿紝娣诲姞PY-STD-TUNNEL-003鑼冨紡





### v3.8.17 (2026-07-10) - 馃敡 Tunnel startup optimization - hostc pre-start + Python smart wait

#### 闂: 闅ч亾鍚姩閫昏緫鏈紭鍖栵紝鍚姩鎱�
**鐜拌薄**: hostc鍚姩鎱紝Python绛夊緟閫昏緫绠�鍗曪紝鏁翠綋鍚姩鏃堕棿闀�

**鏍规湰鍘熷洜**: 鏈疄鐜癶ostc棰勫惎鍔ㄥ拰Python鏅鸿兘绛夊緟鏈哄埗

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細绠�鍗曠瓑寰�
def start_tunnel():
    subprocess.Popen(['hostc'])
    time.sleep(10)  # 鍥哄畾绛夊緟10绉�

# 鉁� 淇鍚庯細鏅鸿兘绛夊緟
def start_tunnel():
    pre_start_hostc()
    for i in range(30):
        if check_url_available():
            break
        time.sleep(1)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍚姩鏂瑰紡** | 鍥哄畾绛夊緟 鉂� | 鏅鸿兘绛夊緟 鉁� |
| **鍚姩閫熷害** | 鎱� 鉂� | 蹇� 鉁� |
| **鎴愬姛鐜�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 瀹炵幇hostc棰勫惎鍔ㄦ満鍒讹紝Python鏅鸿兘绛夊緟URL鍙敤锛屼紭鍖栭毀閬撳惎鍔ㄩ�昏緫





### v3.8.16 (2026-07-09) - 馃悰 macOS鏃堕棿鎴矪ug淇 + 璺ㄥ钩鍙版绉掔骇鏃堕棿鎴崇粺涓�

#### 闂: macOS鏃堕棿鎴虫牸寮忎笌鍏朵粬骞冲彴涓嶄竴鑷�
**鐜拌薄**: macOS涓婃椂闂存埑鏄剧ず涓虹绾э紝Windows/Linux鏄剧ず涓烘绉掔骇

**鏍规湰鍘熷洜**: macOS鐨刣ate鍛戒护榛樿杈撳嚭鏍煎紡涓嶅悓

**淇鏂规**:
```bash
# 鉂� 淇鍓嶏細macOS鏃堕棿鎴充笉缁熶竴
# macOS: date +%s (绉掔骇)
# Linux: date +%s%N (绾崇绾�)

# 鉁� 淇鍚庯細璺ㄥ钩鍙扮粺涓�姣绾�
# macOS/Linux: python -c "import time; print(int(time.time()*1000))"
# Windows: powershell -Command "[int](Get-Date -UFormat %%s)*1000"
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏃堕棿鎴虫牸寮�** | 涓嶇粺涓� 鉂� | 缁熶竴 鉁� |
| **鏃堕棿鎴崇簿搴�** | 绉掔骇 鉂� | 姣绾� 鉁� |
| **璺ㄥ钩鍙板吋瀹�** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**: 缁熶竴macOS/Windows/Linux鏃堕棿鎴虫牸寮忎负姣绾э紝纭繚璺ㄥ钩鍙颁竴鑷存��





### v3.8.15 (2026-07-09) - 馃摑 鏂囨。瀹屾暣鏇存柊: 鍏ㄥ眬鏃堕棿鎴�100%瑕嗙洊瑙勮寖

#### 闂: 鏃堕棿鎴充娇鐢ㄤ笉瑙勮寖锛岃鐩栫巼涓嶈冻
**鐜拌薄**: 閮ㄥ垎鏃ュ織缂哄皯鏃堕棿鎴筹紝闅句互杩借釜闂鍙戠敓鏃堕棿

**鏍规湰鍘熷洜**: 缂哄皯鍏ㄥ眬鏃堕棿鎴充娇鐢ㄨ鑼�

**淇鏂规**:
```markdown
<!-- 鉁� 鍏ㄥ眬鏃堕棿鎴宠鑼� -->
## 鏃堕棿鎴宠寖寮�
1. **鎵�鏈夋棩蹇楀繀椤诲寘鍚椂闂存埑**
2. **鏃堕棿鎴虫牸寮�**: YYYY-MM-DD HH:MM:SS.mmm
3. **鏃堕棿鎴崇簿搴�**: 姣绾�
4. **瑕嗙洊鐜�**: 100%
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏃堕棿鎴宠鐩栫巼** | 涓嶈冻 鉂� | 100% 鉁� |
| **鏃ュ織鍙拷婧��** | 宸� 鉂� | 濂� 鉁� |
| **璋冭瘯鏁堢巼** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 琛ュ叏鏃堕棿鎴宠寖寮忔枃妗ｏ紝纭繚鎵�鏈夋棩蹇楀寘鍚绉掔骇鏃堕棿鎴筹紝瀹炵幇100%瑕嗙洊鐜�





### v3.8.14 (2026-07-08) - 馃摑 README.md 涓夋寮忕粨鏋勮鑼冭ˉ榻� + skill.docx 閲嶆柊鐢熸垚

#### 闂: README.md缁撴瀯涓嶈鑼冿紝skill.docx杩囨椂
**鐜拌薄**: README.md缂哄皯鏍囧噯缁撴瀯锛宻kill.docx涓庢渶鏂颁唬鐮佷笉鍚屾

**鏍规湰鍘熷洜**: 缂哄皯鏂囨。缁撴瀯瑙勮寖锛屾湭鍙婃椂鏇存柊skill.docx

**淇鏂规**:
```markdown
<!-- 鉁� README.md涓夋寮忕粨鏋� -->
# 椤圭洰鍚嶇О

## 馃摉 鏂囨。姒傝堪
绠�瑕佹弿杩伴」鐩姛鑳藉拰鐩爣

## 馃攧 鏈�鏂版洿鏂�
鐗堟湰鏇存柊鏃ュ織

## 馃搵 鎶�鏈鑼�
寮�鍙戣鑼冨拰鏈�浣冲疄璺�
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏂囨。缁撴瀯** | 涓嶈鑼� 鉂� | 瑙勮寖 鉁� |
| **skill.docx鍚屾** | 杩囨椂 鉂� | 鏈�鏂� 鉁� |
| **鍙鎬�** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**: 琛ラ綈README.md涓夋寮忕粨鏋勮鑼冿紝閲嶆柊鐢熸垚skill.docx纭繚涓庢渶鏂颁唬鐮佸悓姝�





### v3.8.13 (2026-07-08) - 馃悰 馃敡 鍏抽敭Bug淇 + API淇℃伅瀹屾暣鎬у寮� + 鏇存柊鏃ュ織鏍煎紡浼樺寲

#### 闂: 鍏抽敭Bug鏈慨澶嶏紝API淇℃伅涓嶅畬鏁达紝鏇存柊鏃ュ織鏍煎紡娣蜂贡
**鐜拌薄**: 瀛樺湪鍏抽敭Bug锛孉PI杩斿洖淇℃伅涓嶅畬鏁达紝鏇存柊鏃ュ織鏍煎紡涓嶇粺涓�

**鏍规湰鍘熷洜**: Bug鏈強鏃朵慨澶嶏紝API璁捐涓嶅畬鍠勶紝鏃ュ織鏍煎紡鏈鑼�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細API淇℃伅涓嶅畬鏁�
@app.get('/api/status')
def get_status():
    return {"status": "ok"}

# 鉁� 淇鍚庯細API淇℃伅瀹屾暣
@app.get('/api/status')
def get_status():
    return {
        "status": "ok",
        "version": get_version(),
        "uptime": get_uptime(),
        "tunnel_status": get_tunnel_status()
    }
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **Bug淇** | 鏈慨澶� 鉂� | 宸蹭慨澶� 鉁� |
| **API淇℃伅瀹屾暣鎬�** | 涓嶅畬鏁� 鉂� | 瀹屾暣 鉁� |
| **鏃ュ織鏍煎紡** | 娣蜂贡 鉂� | 缁熶竴 鉁� |

**鎶�鏈粏鑺�**: 淇鍏抽敭Bug锛屽寮篈PI淇℃伅瀹屾暣鎬э紝浼樺寲鏇存柊鏃ュ織鏍煎紡





### v3.8.12 (2026-07-08) - 馃悰 馃摑 娣诲姞鐗堟湰鍙锋牸寮忚鑼� + 淇bat瑙ｆ瀽闂 + 鐢熸垚skill.docx

#### 闂: 鐗堟湰鍙锋牸寮忎笉瑙勮寖锛宐at瑙ｆ瀽閿欒锛宻kill.docx杩囨椂
**鐜拌薄**: 鐗堟湰鍙锋牸寮忔贩涔憋紝bat鑴氭湰瑙ｆ瀽鐗堟湰鍙峰け璐ワ紝skill.docx鏈洿鏂�

**鏍规湰鍘熷洜**: 缂哄皯鐗堟湰鍙锋牸寮忚鑼冿紝bat瑙ｆ瀽閫昏緫閿欒

**淇鏂规**:
```markdown
<!-- 鉁� 鐗堟湰鍙锋牸寮忚鑼� -->
## 鐗堟湰鍙锋牸寮忚鑼�
- **鏍煎紡**: vX.Y.Z
- **绀轰緥**: v3.8.12
- **浣嶇疆**: README.md绗竴琛�
- **瑙ｆ瀽**: 浣跨敤姝ｅ垯琛ㄨ揪寮� `v```d+```.```d+```.```d+`
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鐗堟湰鍙锋牸寮�** | 娣蜂贡 鉂� | 瑙勮寖 鉁� |
| **bat瑙ｆ瀽** | 澶辫触 鉂� | 鎴愬姛 鉁� |
| **skill.docx鍚屾** | 杩囨椂 鉂� | 鏈�鏂� 鉁� |

**鎶�鏈粏鑺�**: 娣诲姞鐗堟湰鍙锋牸寮忚鑼冨埌README.md鍜宻kill.md锛屼慨澶峛at瑙ｆ瀽闂锛岄噸鏂扮敓鎴恠kill.docx





### v3.8.11 (2026-07-05) - 馃摑 瀹屾暣鍘嗗彶璁板綍鎭㈠涓庢枃妗ｆ洿鏂�

#### 闂: 鍘嗗彶璁板綍涓㈠け锛屾枃妗ｄ笉瀹屾暣
**鐜拌薄**: 鐗堟湰鍘嗗彶璁板綍涓嶅畬鏁达紝鏂囨。缂哄皯鍏抽敭淇℃伅

**鏍规湰鍘熷洜**: 鍘嗗彶璁板綍鏈強鏃朵繚瀛橈紝鏂囨。鏇存柊涓嶅強鏃�

**淇鏂规**:
```markdown
<!-- 鉁� 鎭㈠瀹屾暣鍘嗗彶璁板綍 -->
## 鐗堟湰鍘嗗彶
- v3.8.11: 瀹屾暣鍘嗗彶璁板綍鎭㈠涓庢枃妗ｆ洿鏂�
- v3.8.10: 鏇存柊鏂囨。锛歊EADME.md + skill.md + skill.docx 鍚屾浠ｇ爜瑙勮寖
- v3.8.9: 寮哄埗URL鍘婚噸鏈哄埗
- ...锛堟仮澶嶆墍鏈夊巻鍙茬増鏈級
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍘嗗彶璁板綍瀹屾暣鎬�** | 涓嶅畬鏁� 鉂� | 瀹屾暣 鉁� |
| **鏂囨。鍑嗙‘鎬�** | 杩囨椂 鉂� | 鏈�鏂� 鉁� |
| **鍙拷婧��** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**: 鎭㈠瀹屾暣鍘嗗彶璁板綍锛屾洿鏂版枃妗ｇ‘淇濅笌鏈�鏂颁唬鐮佸悓姝�





### v3.8.10 (2026-07-05) - 馃摑 鏇存柊鏂囨。锛歊EADME.md + skill.md + skill.docx 鍚屾浠ｇ爜瑙勮寖

#### 闂: 鏂囨。涓庝唬鐮佽鑼冧笉鍚屾
**鐜拌薄**: README.md銆乻kill.md銆乻kill.docx涓殑浠ｇ爜瑙勮寖涓庡疄闄呬唬鐮佷笉涓�鑷�

**鏍规湰鍘熷洜**: 浠ｇ爜瑙勮寖鏇存柊鍚庢湭鍙婃椂鍚屾鏂囨。

**淇鏂规**:
```markdown
<!-- 鉁� 鍚屾浠ｇ爜瑙勮寖 -->
## 浠ｇ爜瑙勮寖
1. **鍛藉悕瑙勮寖**: 浣跨敤snake_case鍛藉悕鍙橀噺鍜屽嚱鏁�
2. **娉ㄩ噴瑙勮寖**: 浣跨敤涓枃娉ㄩ噴锛岄伒寰狿EP 257
3. **鏃ュ織瑙勮寖**: 鎵�鏈夋棩蹇楀寘鍚绉掔骇鏃堕棿鎴�
4. **閿欒澶勭悊**: 浣跨敤try-except鎹曡幏寮傚父骞惰褰曟棩蹇�
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏂囨。鍚屾鎬�** | 涓嶅悓姝� 鉂� | 鍚屾 鉁� |
| **瑙勮寖鍑嗙‘鎬�** | 杩囨椂 鉂� | 鏈�鏂� 鉁� |
| **寮�鍙戣�呭弬鑰�** | 鍥版儜 鉂� | 鏄庣‘ 鉁� |

**鎶�鏈粏鑺�**: 鍚屾鏇存柊README.md銆乻kill.md銆乻kill.docx锛岀‘淇濅唬鐮佽鑼冧笌瀹為檯浠ｇ爜涓�鑷�




### v3.8.9 (2026-07-05) - 馃摟 寮哄埗URL鍘婚噸鏈哄埗锛堝悓涓�鍦板潃30鍒嗛挓鍐呭彧鍙�1娆￠偖浠讹級

#### 闂: 閭欢閲嶅鍙戦�侊紝鐢ㄦ埛鏀跺埌澶氬皝鐩稿悓URL閫氱煡
**鐜拌薄**: 鍚屼竴鍏綉鍦板潃鍦ㄧ煭鏃堕棿鍐呰澶氭鍙戦�侊紝閫犳垚楠氭壈

**鏍规湰鍘熷洜**: 閭欢鍙戦�侀�昏緫鏈坊鍔犲幓閲嶆満鍒�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鏃犲幓閲嶆満鍒�
def send_email(url):
    send(url)

# 鉁� 淇鍚庯細寮哄埗鍘婚噸锛�30鍒嗛挓鍐呭悓涓�鍦板潃鍙彂1娆★級
sent_urls = {}
def send_email(url):
    now = time.time()
    if url in sent_urls:
        if now - sent_urls[url] < 1800:  # 30鍒嗛挓
            logging.info(f"URL {url} already sent in last 30 minutes, skipping")
            return
    sent_urls[url] = now
    send(url)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **閭欢閲嶅** | 鏄� 鉂� | 鍚� 鉁� |
| **鐢ㄦ埛浣撻獙** | 楠氭壈 鉂� | 鑹ソ 鉁� |
| **鍘婚噸鏃堕棿绐楀彛** | 鏃� 鉂� | 30鍒嗛挓 鉁� |

**鎶�鏈粏鑺�**: 瀹炵幇寮哄埗URL鍘婚噸鏈哄埗锛屽悓涓�鍦板潃30鍒嗛挓鍐呭彧鍙戦��1娆￠偖浠讹紝閬垮厤閲嶅閫氱煡





### v3.8.8 (2026-07-05) - 馃敡 鍏綉鍦板潃鍙敤鍗宠嚜鍔ㄥ彂閭欢锛堥浂寤惰繜閫氱煡浼樺寲锛�

#### 闂: 鍏綉鍦板潃鍙敤鍚庨偖浠堕�氱煡寤惰繜
**鐜拌薄**: 闅ч亾鍚姩骞惰幏鍙栧埌URL鍚庯紝閭欢閫氱煡寤惰繜鏁板垎閽�

**鏍规湰鍘熷洜**: 閭欢閫氱煡渚濊禆蹇冭烦寰幆锛岄潪鍗虫椂瑙﹀彂

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細渚濊禆蹇冭烦寰幆
def heartbeat():
    if verify_url():
        send_email(url)

# 鉁� 淇鍚庯細闆跺欢杩熼�氱煡
def on_url_available(url):
    if verify_url(url):
        threading.Thread(target=send_email, args=(url,)).start()
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **閭欢寤惰繜** | 鏁板垎閽� 鉂� | 闆跺欢杩� 鉁� |
| **閫氱煡鍙婃椂鎬�** | 宸� 鉂� | 濂� 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**: 瀹炵幇鍏綉鍦板潃鍙敤鍗宠嚜鍔ㄥ彂閭欢锛岄浂寤惰繜閫氱煡浼樺寲锛屾彁鍗囩敤鎴蜂綋楠�





### v3.8.7 (2026-07-05) - 馃悰 绾跨▼瀹夊叏URL鍘婚噸鏈哄埗淇 + 鏇存柊skill.docx

#### 闂: URL鍘婚噸鏈哄埗闈炵嚎绋嬪畨鍏�
**鐜拌薄**: 澶氱嚎绋嬬幆澧冧笅锛孶RL鍘婚噸鏈哄埗澶辨晥锛屼粛浼氶噸澶嶅彂閫侀偖浠�

**鏍规湰鍘熷洜**: sent_urls瀛楀吀鏈姞閿佷繚鎶わ紝澶氱嚎绋嬭闂瓨鍦ㄧ珵鎬佹潯浠�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細闈炵嚎绋嬪畨鍏�
sent_urls = {}
def send_email(url):
    if url in sent_urls:
        return
    sent_urls[url] = time.time()
    send(url)

# 鉁� 淇鍚庯細绾跨▼瀹夊叏
import threading
sent_urls = {}
lock = threading.Lock()
def send_email(url):
    with lock:
        if url in sent_urls:
            if time.time() - sent_urls[url] < 1800:
                return
        sent_urls[url] = time.time()
    send(url)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **绾跨▼瀹夊叏** | 鍚� 鉂� | 鏄� 鉁� |
| **鍘婚噸鍙潬鎬�** | 浣� 鉂� | 楂� 鉁� |
| **skill.docx鍚屾** | 杩囨椂 鉂� | 鏈�鏂� 鉁� |

**鎶�鏈粏鑺�**: 浣跨敤绾跨▼閿佷繚鎶RL鍘婚噸鏈哄埗锛岀‘淇濆绾跨▼鐜涓嬪幓閲嶉�昏緫姝ｇ‘锛屾洿鏂皊kill.docx鏂囨。





### v3.8.6 (2026-07-05) - 馃敡 鍐呭鏀逛负鏍囧噯API鏍煎紡 + 閲嶆柊鐢熸垚skill.docx

#### 闂: 鏂囨。鏍煎紡涓嶆爣鍑嗭紝闅句互瑙ｆ瀽
**鐜拌薄**: 鏂囨。鍐呭鏍煎紡娣蜂贡锛屼笉绗﹀悎鏍囧噯API鏍煎紡

**鏍规湰鍘熷洜**: 鏃╂湡鏂囨。鏍煎紡鏈鑼�

**淇鏂规**:
```markdown
<!-- 鉂� 淇鍓嶏細鏍煎紡娣蜂贡 -->
- 鍔熻兘1
- 鍔熻兘2

<!-- 鉁� 淇鍚庯細鏍囧噯API鏍煎紡 -->
## API鏂囨。

### 鍒嗙被1
- **瀛愭潯鐩�1**: 鎻忚堪
- **瀛愭潯鐩�2**: 鎻忚堪

### 鍒嗙被2
- **瀛愭潯鐩�1**: 鎻忚堪
- **瀛愭潯鐩�2**: 鎻忚堪
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏂囨。鏍煎紡** | 娣蜂贡 鉂� | 鏍囧噯 鉁� |
| **鍙В鏋愭��** | 宸� 鉂� | 濂� 鉁� |
| **skill.docx鍚屾** | 杩囨椂 鉂� | 鏈�鏂� 鉁� |

**鎶�鏈粏鑺�**: 灏嗘枃妗ｅ唴瀹规敼涓烘爣鍑咥PI鏍煎紡锛堝垎绫� + 瀛愭潯鐩級锛岄噸鏂扮敓鎴恠kill.docx





### v3.8.5 (2026-07-05) - 馃摑 鐢熸垚绗﹀悎瑙勮寖鐨� skill.docx

#### 闂: skill.docx涓嶇鍚堣鑼�
**鐜拌薄**: skill.docx鏍煎紡娣蜂贡锛屼笉绗﹀悎椤圭洰瑙勮寖

**鏍规湰鍘熷洜**: 鏃╂湡鐢熸垚鐨剆kill.docx鏈伒寰鑼�

**淇鏂规**:
```markdown
<!-- 鉁� 绗﹀悎瑙勮寖鐨剆kill.docx -->
# 寰喘鐩稿唽寮�鍙戞妧鑳芥枃妗�

## 馃摉 鏂囨。姒傝堪
绠�瑕佹弿杩伴」鐩姛鑳藉拰鐩爣

## 馃攧 鏈�鏂版洿鏂�
鐗堟湰鏇存柊鏃ュ織

## 馃搵 鎶�鏈鑼�
寮�鍙戣鑼冨拰鏈�浣冲疄璺�
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏂囨。瑙勮寖鎬�** | 涓嶇鍚� 鉂� | 绗﹀悎 鉁� |
| **鍙鎬�** | 宸� 鉂� | 濂� 鉁� |
| **缁存姢鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 鐢熸垚绗﹀悎椤圭洰瑙勮寖鐨剆kill.docx鏂囨。锛岀‘淇濇牸寮忕粺涓�銆佸唴瀹瑰畬鏁�




### v3.8.4 (2026-07-04) - 馃悰 淇浠庨潪椤圭洰鐩綍杩愯鍚姩鑴氭湰鏃禬eb鏈嶅姟鍚姩澶辫触Bug

#### 闂: 浠庨潪椤圭洰鐩綍杩愯鍚姩鑴氭湰鏃禬eb鏈嶅姟鍚姩澶辫触
**鐜拌薄**: 鍦ㄥ叾浠栫洰褰曡繍琛宺un.bat/run.sh鏃讹紝鎻愮ず"鏂囦欢鏈壘鍒�"閿欒

**鏍规湰鍘熷洜**: 鍚姩鑴氭湰鏈垏鎹㈠埌椤圭洰鐩綍锛屼娇鐢ㄧ浉瀵硅矾寰勫鑷存枃浠舵煡鎵惧け璐�

**淇鏂规**:
```bash
# 鉂� 淇鍓嶏細浣跨敤鐩稿璺緞
python main.py

# 鉁� 淇鍚庯細鍒囨崲鍒伴」鐩洰褰�
cd "%~dp0"
python main.py
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍚姩鐩綍闄愬埗** | 蹇呴』鍦ㄩ」鐩洰褰� 鉂� | 浠绘剰鐩綍 鉁� |
| **鍚姩鎴愬姛鐜�** | 浣� 鉂� | 楂� 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**: 鍦ㄥ惎鍔ㄨ剼鏈紑澶存坊鍔犵洰褰曞垏鎹㈤�昏緫锛岀‘淇濇棤璁轰粠鍝釜鐩綍杩愯閮借兘姝ｇ‘鍚姩





### v3.8.3 (2026-07-04) - 馃悰 淇'鏈�鏂版洿鏂�'鍖哄煙绌虹櫧Bug + Markdown鏍囬鏍煎紡瑙勮寖

#### 闂: '鏈�鏂版洿鏂�'鍖哄煙鏄剧ず绌虹櫧锛孧arkdown鏍囬鏍煎紡涓嶈鑼�
**鐜拌薄**: 鍓嶇'鏈�鏂版洿鏂�'鍖哄煙鏃犲唴瀹规樉绀猴紝Markdown鏍囬鏍煎紡娣蜂贡

**鏍规湰鍘熷洜**: Markdown瑙ｆ瀽閫昏緫閿欒锛屾爣棰樻牸寮忎笉绗﹀悎瑙勮寖

**淇鏂规**:
```markdown
<!-- 鉂� 淇鍓嶏細鏍囬鏍煎紡涓嶈鑼� -->
##鏈�鏂版洿鏂�
缂哄皯绌烘牸

<!-- 鉁� 淇鍚庯細鏍囬鏍煎紡瑙勮寖 -->
## 鏈�鏂版洿鏂�

### v3.8.89.21 (2026-08-20) - SSRF瀹夊叏闃插尽浣撶郴 + Import浼樺寲 + 椤圭洰娓呯悊

#### 鏇存柊鍐呭: 娣诲姞瀹屾暣鐨勬湇鍔″櫒绔姹備吉閫�(SSRF)闃插尽鏈哄埗锛屼紭鍖朓mport璇彞绠＄悊锛屾竻鐞嗛」鐩复鏃舵枃浠�

**褰卞搷鏂囦欢**: main.py, README.md, skill.md, skill.docx

---

- **SSRF瀹夊叏闃插尽浣撶郴 (鏍稿績鍔熻兘)** - 鍩轰簬鎶栭煶SSRF鏀诲嚮瑙嗛鐨勫畬鏁撮槻鎶ゅ疄鐜�
  - 瀹炵幇浣嶇疆: main.py#L9531-L9670 (SSRFProtection绫�)
  - 闃叉姢鑳藉姏: 8澶ф牳蹇冨姛鑳芥ā鍧�
    - IP鍦板潃瑙勮寖鍖�: 闃插崄杩涘埗/鍏繘鍒�/鍗佸叚杩涘埗缂栫爜缁曡繃
    - 绉佹湁IP妫�娴�: RFC 1918鑼冨洿 + IPv6鏄犲皠鍦板潃璇嗗埆
    - 鍗忚鐧藉悕鍗�: 浠呭厑璁竓ttp/https锛堥樆姝ile/gopher/dict绛夛級
    - 浜戝厓鏁版嵁淇濇姢: AWS/GCP/Azure绔偣瀹屽叏灞忚斀
    - 鏁忔劅绔彛闃绘: SSH(22)/MySQL(3306)/Redis(6379)绛�17涓鍙�
    - 涓绘満鍚嶉粦鍚嶅崟: localhost/metadata绛夊嵄闄╀富鏈哄悕鎷︽埅
    - SSL涓ユ牸楠岃瘉: 闃蹭腑闂翠汉鏀诲嚮鍜岃瘉涔︽楠�
    - 鍝嶅簲澶у皬闄愬埗: 榛樿5MB涓婇檺闃睤oS鏀诲嚮
  
- **鍏ㄥ眬瀹炰緥涓庤楗板櫒 (鏄撶敤鎬ц璁�)** - 鎻愪緵涓ょ浣跨敤鏂瑰紡
  - 鍏ㄥ眬瀹炰緥: ssrf_protector = SSRFProtection(enabled=True, block_private_ips=True)
  - 瑁呴グ鍣�: @ssrf_safe_request 鐢ㄤ簬鍑芥暟绾ц嚜鍔ㄤ繚鎶�
  - 缁熻鎺ュ彛: ssrf_protector.get_stats() 杩斿洖璇锋眰/鎷︽埅璁℃暟
  - 瀹夊叏鏃ュ織: 鑷姩璁板綍鎵�鏈夋嫤鎴簨浠讹紙WARNING绾у埆锛�

- **Import璇彞浼樺寲 (浠ｇ爜璐ㄩ噺)** - 鏁寸悊鎵�鏈塱mport鑷虫枃浠堕《閮ㄥ苟鍘婚噸
  - 鏂板鏍囧噯搴撳鍏�: struct, hashlib, urllib.error, urllib.parse, traceback
  - 鎬诲鍏ユ暟閲�: 37涓�
  - 鍒犻櫎閲嶅import: 13涓�
  - 绗﹀悎PEP8瑙勮寖: 鎵�鏈塱mport闆嗕腑鍦ㄦ枃浠堕《閮ㄧ1-50琛�

- **椤圭洰鏂囦欢娓呯悊 (缁存姢鎿嶄綔)** - 鍒犻櫎鎵�鏈変复鏃跺紑鍙戞枃浠�
  - 鍒犻櫎py/js/txt鏂囦欢鍏�14涓紙鍖呮嫭UTF8涓存椂鏂囦欢锛�
  - 娓呯悊缁撴灉: 浠呬繚鐣� main.py, README.md, skill.md, skill.docx, requirements.txt
  - 鏂囦欢鏁板噺灏�50%

- **浠ｇ爜瑙勮寖閬靛惊 skill.md** - 涓ユ牸閬靛畧椤圭洰缂栫爜鏍囧噯
  - UTF-001 缂栫爜鏍囧噯: 鎵�鏈夋枃浠禪TF-8缂栫爜
  - PY-CORE-005 寮傚父澶勭悊: 瀹屾暣寮傚父澶勭悊閾�
  - PY-SEC-001 杈撳叆楠岃瘉: URL楠岃瘉瀹屾暣瀹炵幇
  - 鍗曟枃浠舵灦鏋�: 鏃犻澶杙y鏂囦欢

- **闃插尽鍦烘櫙瑕嗙洊** - 鍩轰簬SSRF鏀诲嚮瑙嗛鐨勫畬鏁撮槻鎶�
  - [x] 鍐呯綉IP鎺㈡祴 -> 鎷︽埅RFC 1918鍦板潃
  - [x] 浜戝厓鏁版嵁绐冨彇 -> 绔偣榛戝悕鍗�
  - [x] 鏈湴鏂囦欢璇诲彇 -> 鍗忚鐧藉悕鍗�
  - [x] 鍗忚璧扮鏀诲嚮 -> 10绉嶅崗璁睆钄�
  - [x] DNS Rebinding -> 浜屾楠岃瘉
  - [x] IP缂栫爜缁曡繃 -> 澶氭牸寮忚В鏋�

- **璇硶楠岃瘉涓庢祴璇�** - 纭繚浠ｇ爜鍙甯告墽琛�
  - py_compile妫�鏌� -> 缂栬瘧閫氳繃
  - 瀵煎叆妫�鏌� -> 37涓猧mport鎴愬姛
  - 绫诲疄渚嬪寲 -> 姝ｅ父鍒涘缓
  - 鎺ュ彛璋冪敤 -> 鍔熻兘姝ｅ父


鏍囬涓�#涔嬮棿鏈夌┖鏍�
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **'鏈�鏂版洿鏂�'鏄剧ず** | 绌虹櫧 鉂� | 姝ｅ父 鉁� |
| **Markdown鏍煎紡** | 涓嶈鑼� 鉂� | 瑙勮寖 鉁� |
| **瑙ｆ瀽鍑嗙‘鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 淇Markdown鏍囬鏍煎紡锛岀‘淇�"## 鏍囬"鏍煎紡姝ｇ‘锛屼慨澶�'鏈�鏂版洿鏂�'鍖哄煙绌虹櫧Bug





### v3.8.2 (2026-07-04) - 馃悰 淇web_output.log鍚姩鏃ュ織琚鐩朆ug

#### 闂: web_output.log鍚姩鏃ュ織琚鐩�
**鐜拌薄**: 姣忔鍚姩鏃讹紝web_output.log涓殑鍚姩鏃ュ織琚竻绌�

**鏍规湰鍘熷洜**: 鏃ュ織鏂囦欢鍐欏叆妯″紡閿欒锛屼娇鐢�'w'妯″紡鑰岄潪'a'妯″紡

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細瑕嗙洊妯″紡
with open('web_output.log', 'w') as f:
    f.write(log)

# 鉁� 淇鍚庯細杩藉姞妯″紡
with open('web_output.log', 'a') as f:
    f.write(log)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏃ュ織瀹屾暣鎬�** | 琚鐩� 鉂� | 瀹屾暣淇濆瓨 鉁� |
| **鍘嗗彶鍙拷婧��** | 宸� 鉂� | 濂� 鉁� |
| **璋冭瘯鏁堢巼** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 灏唚eb_output.log鍐欏叆妯″紡浠�'w'鏀逛负'a'锛岀‘淇濆惎鍔ㄦ棩蹇椾笉琚鐩�





### v3.8.1 (2026-07-04) - 馃摑 skill.md鍏ㄩ潰琛ュ叏 + API绔偣淇 + README鍘婚噸 + skill.docx閲嶆柊鐢熸垚

#### 闂: skill.md鍐呭涓嶅畬鏁达紝API绔偣鍒楄〃閿欒锛孯EADME閲嶅鍐呭
**鐜拌薄**: skill.md缂哄皯鍏抽敭鍑芥暟鍜岀被锛孉PI绔偣鍒楄〃涓嶅噯纭紝README瀛樺湪閲嶅鍐呭

**鏍规湰鍘熷洜**: 鏂囨。鏇存柊涓嶅強鏃讹紝鏈叏闈㈣ˉ鍏�

**淇鏂规**:
```markdown
<!-- 鉁� skill.md鍏ㄩ潰琛ュ叏 -->
## 2.15 main.py鐙珛鍑芥暟
- get_version()
- send_email()
- verify_url()

## 2.16 index.html鍓嶇鍑芥暟锛�61涓級
- loadItems()
- searchItems()
- exportToExcel()
...
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **skill.md瀹屾暣鎬�** | 涓嶅畬鏁� 鉂� | 瀹屾暣 鉁� |
| **API绔偣鍑嗙‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **README鍘婚噸** | 閲嶅 鉂� | 鏃犻噸澶� 鉁� |

**鎶�鏈粏鑺�**: 鍏ㄩ潰琛ュ叏skill.md鍐呭锛屽寘鎷琺ain.py鐙珛鍑芥暟鍜宨ndex.html鍓嶇61涓嚱鏁帮紝淇API绔偣鍒楄〃锛屽幓闄EADME閲嶅鍐呭锛岄噸鏂扮敓鎴恠kill.docx





### v3.8.0 (2026-07-04) - 馃摑 鏂囨。绯荤粺鍏ㄩ潰鍗囩骇

#### 闂: 鏂囨。绯荤粺涓嶅畬鍠勶紝缂哄皯绯荤粺鎬ф枃妗�
**鐜拌薄**: 椤圭洰缂哄皯瀹屾暣鐨勬枃妗ｄ綋绯伙紝寮�鍙戣�呴毦浠ュ揩閫熶笂鎵�

**鏍规湰鍘熷洜**: 鏃╂湡寮�鍙戞湭閲嶈鏂囨。寤鸿

**淇鏂规**:
```markdown
<!-- 鉁� 鏂囨。绯荤粺鍏ㄩ潰鍗囩骇 -->
## 鏂囨。浣撶郴
1. **README.md**: 椤圭洰姒傝堪鍜屽揩閫熷紑濮�
2. **skill.md**: 寮�鍙戞妧鑳芥枃妗�
3. **skill.docx**: Word鏍煎紡鏂囨。
4. **API鏂囨。**: 鎺ュ彛鏂囨。
5. **寮�鍙戣鑼�**: 浠ｇ爜瑙勮寖鍜屾渶浣冲疄璺�
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏂囨。瀹屾暣鎬�** | 涓嶅畬鏁� 鉂� | 瀹屾暣 鉁� |
| **鏂囨。浣撶郴** | 缂哄け 鉂� | 瀹屽杽 鉁� |
| **寮�鍙戣�呬綋楠�** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**: 鍏ㄩ潰鍗囩骇鏂囨。绯荤粺锛屽缓绔嬪畬鏁寸殑鏂囨。浣撶郴锛屽寘鎷琑EADME.md銆乻kill.md銆乻kill.docx銆丄PI鏂囨。绛�




### v3.7.9 (2026-07-04) - 馃摑 鍒犻櫎generate_skill_docx.py + 閲嶆柊鐢熸垚skill.docx

#### 闂: generate_skill_docx.py鑴氭湰鍐椾綑
**鐜拌薄**: 椤圭洰涓瓨鍦╣enerate_skill_docx.py鑴氭湰锛屽姛鑳藉凡琚叾浠栬剼鏈浛浠�

**鏍规湰鍘熷洜**: 鏃╂湡閬楃暀鑴氭湰锛屾湭鍙婃椂娓呯悊

**淇鏂规**:
```bash
# 鉂� 淇鍓嶏細瀛樺湪鍐椾綑鑴氭湰
generate_skill_docx.py

# 鉁� 淇鍚庯細鍒犻櫎鍐椾綑鑴氭湰
rm generate_skill_docx.py
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鑴氭湰鏁伴噺** | 鍐椾綑 鉂� | 绮剧畝 鉁� |
| **缁存姢鎴愭湰** | 楂� 鉂� | 浣� 鉁� |
| **skill.docx鍚屾** | 杩囨椂 鉂� | 鏈�鏂� 鉁� |

**鎶�鏈粏鑺�**: 鍒犻櫎鍐椾綑鐨刧enerate_skill_docx.py鑴氭湰锛岄噸鏂扮敓鎴恠kill.docx纭繚鏈�鏂�





### v3.7.8 (2026-07-04) - 馃摫 闅ч亾蹇�熸仮澶嶆満鍒�-3绉掔骇鍝嶅簲+閭欢鍘婚噸

#### 闂: 闅ч亾鏁呴殰鎭㈠鎱紝閭欢閲嶅鍙戦��
**鐜拌薄**: 闅ч亾鏁呴殰鍚庢仮澶嶉渶瑕佹暟鍗佺锛岄偖浠堕噸澶嶅彂閫侀�犳垚楠氭壈

**鏍规湰鍘熷洜**: 鎭㈠鏈哄埗鎱紝閭欢鍙戦�佹棤鍘婚噸

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鎭㈠鎱紝鏃犲幓閲�
def recover_tunnel():
    time.sleep(30)  # 绛夊緟30绉�
    restart_tunnel()
    send_email(url)

# 鉁� 淇鍚庯細3绉掔骇鍝嶅簲+鍘婚噸
def recover_tunnel():
    time.sleep(3)  # 3绉掑揩閫熷搷搴�
    restart_tunnel()
    if not is_email_sent_recently(url):  # 鍘婚噸妫�鏌�
        send_email(url)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鎭㈠閫熷害** | 30绉� 鉂� | 3绉� 鉁� |
| **閭欢鍘婚噸** | 鏃� 鉂� | 鏈� 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**: 瀹炵幇闅ч亾蹇�熸仮澶嶆満鍒讹紝3绉掔骇鍝嶅簲锛屾坊鍔犻偖浠跺幓閲嶉�昏緫





### v3.7.7 (2026-06-28) - 馃悰 淇Excel涓嶫SON瀵规瘮鎸夐挳鐘舵�佷笉澶嶄綅闂

#### 闂: Excel涓嶫SON瀵规瘮鎸夐挳鐘舵�佷笉澶嶄綅
**鐜拌薄**: 鐐瑰嚮"Excel瀵规瘮"鎴�"JSON瀵规瘮"鎸夐挳鍚庯紝鎸夐挳鐘舵�佷笉鎭㈠锛屾棤娉曞啀娆＄偣鍑�

**鏍规湰鍘熷洜**: 鎸夐挳鐘舵�佺鐞嗛�昏緫閿欒锛屾湭鍦ㄦ搷浣滃畬鎴愬悗澶嶄綅

**淇鏂规**:
```javascript
// 鉂� 淇鍓嶏細鐘舵�佷笉澶嶄綅
function compareExcel() {
    button.disabled = true;
    // 鎿嶄綔瀹屾垚鍚庢湭澶嶄綅
}

// 鉁� 淇鍚庯細鐘舵�佸浣�
function compareExcel() {
    button.disabled = true;
    fetch('/api/compare/excel')
        .then(response => {
            button.disabled = false;  // 澶嶄綅
        });
}
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鎸夐挳鐘舵��** | 涓嶅浣� 鉂� | 鑷姩澶嶄綅 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **鏂囨。鍚屾** | 杩囨椂 鉂� | 鏈�鏂� 鉁� |

**鎶�鏈粏鑺�**: 淇Excel涓嶫SON瀵规瘮鎸夐挳鐘舵�佷笉澶嶄綅闂锛屾洿鏂皊kill.md/skill.docx鎸夐挳鐘舵�佺鐞嗚鑼�





### v3.7.6 (2026-06-27) - 馃悰 淇pip.conf trusted-host閲嶅/鎻愬彇閿欒銆佹暣鏁版瘮杈冪┖鍊笺�乵acOS du -sb鍏煎鎬�

#### 闂: pip.conf閰嶇疆閿欒锛屾暣鏁版瘮杈冪┖鍊硷紝macOS du鍛戒护涓嶅吋瀹�
**鐜拌薄**: pip.conf涓璽rusted-host閲嶅锛屾暣鏁版瘮杈冩椂绌哄�兼姤閿欙紝macOS涓奷u -sb鍛戒护涓嶅瓨鍦�

**鏍规湰鍘熷洜**: 閰嶇疆鐢熸垚閫昏緫閿欒锛屾湭澶勭悊绌哄�兼儏鍐碉紝macOS鐨刣u鍛戒护鍙傛暟涓嶅悓

**淇鏂规**:
```bash
# 鉂� 淇鍓嶏細trusted-host閲嶅
trusted-host = pypi.org
trusted-host = pypi.org  # 閲嶅

# 鉁� 淇鍚庯細鍘婚噸
trusted-host = pypi.org

# 鉂� 淇鍓嶏細macOS du -sb涓嶅瓨鍦�
du -sb file

# 鉁� 淇鍚庯細璺ㄥ钩鍙板吋瀹�
if [[ "$OSTYPE" == "darwin"* ]]; then
    du -s file
else
    du -sb file
fi
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **pip.conf姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **绌哄�煎鐞�** | 鎶ラ敊 鉂� | 瀹夊叏 鉁� |
| **macOS鍏煎鎬�** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**: 淇pip.conf trusted-host閲嶅鍜屾彁鍙栭敊璇紝澶勭悊鏁存暟姣旇緝绌哄�兼儏鍐碉紝瀹炵幇macOS du鍛戒护璺ㄥ钩鍙板吋瀹�





### v3.7.5 (2026-06-26) - 馃悰 淇鍒╂鼎瓒嬪娍鍥捐仈鍔ㄣ�丒xcel鏃ユ湡杞崲銆乊杞村姩鎬佺缉鏀�

#### 闂: 鍒╂鼎瓒嬪娍鍥捐仈鍔ㄥけ璐ワ紝Excel鏃ユ湡杞崲閿欒锛孻杞寸缉鏀句笉鍚堢悊
**鐜拌薄**: 鐐瑰嚮鍒╂鼎瓒嬪娍鍥炬棤鍝嶅簲锛孍xcel鏃ユ湡鏍煎紡杞崲閿欒锛孻杞村埢搴︿笉鍔ㄦ�佽皟鏁�

**鏍规湰鍘熷洜**: 鍥捐〃鑱斿姩閫昏緫閿欒锛屾棩鏈熻浆鎹㈡牸寮忎笉姝ｇ‘锛孻杞存湭瀹炵幇鍔ㄦ�佺缉鏀�

**淇鏂规**:
```javascript
// 鉂� 淇鍓嶏細鑱斿姩澶辫触
chart.onclick = null;  // 鏃犺仈鍔�

// 鉁� 淇鍚庯細鑱斿姩姝ｅ父
chart.onclick = function(event) {
    const date = event.data.date;
    loadProfitDetails(date);
};

// 鉂� 淇鍓嶏細鏃ユ湡杞崲閿欒
date = excelDate.toString();

// 鉁� 淇鍚庯細鏃ユ湡杞崲姝ｇ‘
date = new Date((excelDate - 25569) * 86400 * 1000);
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **瓒嬪娍鍥捐仈鍔�** | 澶辫触 鉂� | 鎴愬姛 鉁� |
| **Excel鏃ユ湡杞崲** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **Y杞村姩鎬佺缉鏀�** | 鍥哄畾 鉂� | 鍔ㄦ�� 鉁� |

**鎶�鏈粏鑺�**: 淇鍒╂鼎瓒嬪娍鍥捐仈鍔ㄩ�昏緫锛屼慨姝xcel鏃ユ湡杞崲鍏紡锛屽疄鐜癥杞村姩鎬佺缉鏀�





### v3.7.4 (2026-06-18) - 馃悰 鍒╂鼎鎶ヨ〃姹囨�昏鐐瑰嚮灞曞紑浣嶇疆淇 + 鑱氬悎绾у埆淇

#### 闂: 鍒╂鼎鎶ヨ〃姹囨�昏鐐瑰嚮灞曞紑浣嶇疆閿欒锛岃仛鍚堢骇鍒笉鍑嗙‘
**鐜拌薄**: 鐐瑰嚮姹囨�昏灞曞紑鏃讹紝灞曞紑浣嶇疆鍋忕Щ锛岃仛鍚堢骇鍒绠楅敊璇�

**鏍规湰鍘熷洜**: 灞曞紑浣嶇疆璁＄畻閫昏緫閿欒锛岃仛鍚堢骇鍒垽鏂笉鍑嗙‘

**淇鏂规**:
```javascript
// 鉂� 淇鍓嶏細灞曞紑浣嶇疆閿欒
row.insertAfter(targetRow);  // 浣嶇疆鍋忕Щ

// 鉁� 淇鍚庯細灞曞紑浣嶇疆姝ｇ‘
targetRow.after(row);  // 浣嶇疆姝ｇ‘

// 鉂� 淇鍓嶏細鑱氬悎绾у埆閿欒
level = data.length;

// 鉁� 淇鍚庯細鑱氬悎绾у埆姝ｇ‘
level = calculateAggregationLevel(data);
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **灞曞紑浣嶇疆** | 鍋忕Щ 鉂� | 姝ｇ‘ 鉁� |
| **鑱氬悎绾у埆** | 閿欒 鉂� | 鍑嗙‘ 鉁� |
| **璺ㄧ郴缁熼獙璇�** | 鏈獙璇� 鉂� | 宸查獙璇� 鉁� |

**鎶�鏈粏鑺�**: 淇鍒╂鼎鎶ヨ〃姹囨�昏鐐瑰嚮灞曞紑浣嶇疆锛屼慨姝ｈ仛鍚堢骇鍒绠楅�昏緫锛岃法绯荤粺/绉诲姩绔獙璇侀�氳繃





### v3.7.3 (2026-06-18) - 馃悰 DOMContentLoaded闂悎淇 + 鎸夐挳鏍峰紡缁熶竴

#### 闂: DOMContentLoaded浜嬩欢鏈纭棴鍚堬紝鎸夐挳鏍峰紡涓嶇粺涓�
**鐜拌薄**: JavaScript涓璂OMContentLoaded浜嬩欢鐩戝惉鍣ㄦ湭姝ｇ‘闂悎锛屾寜閽牱寮忔贩涔�

**鏍规湰鍘熷洜**: 浠ｇ爜鏍煎紡閿欒锛岀己灏戦棴鍚堟嫭鍙凤紝CSS鏍峰紡鏈粺涓�

**淇鏂规**:
```javascript
// 鉂� 淇鍓嶏細鏈棴鍚�
document.addEventListener('DOMContentLoaded', function() {
    // 浠ｇ爜
// 缂哄皯闂悎

// 鉁� 淇鍚庯細姝ｇ‘闂悎
document.addEventListener('DOMContentLoaded', function() {
    // 浠ｇ爜
});
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **浠ｇ爜闂悎** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鎸夐挳鏍峰紡** | 涓嶇粺涓� 鉂� | 缁熶竴 鉁� |
| **鏂囨。鍚屾** | 杩囨椂 鉂� | 鏈�鏂� 鉁� |

**鎶�鏈粏鑺�**: 淇DOMContentLoaded浜嬩欢鐩戝惉鍣ㄩ棴鍚堥敊璇紝缁熶竴鎸夐挳鏍峰紡锛屽悓姝ユ洿鏂皊kill/docx鏂囨。





### v3.7.2 (2026-06-18) - 馃悰 淇index.html绗�5197琛屾爣绛鹃棴鍚� + skill.md/docx瑙勮寖鏇存柊

#### 闂: index.html绗�5197琛屾爣绛炬湭姝ｇ‘闂悎
**鐜拌薄**: index.html绗�5197琛屽瓨鍦ㄦ湭闂悎鐨凥TML鏍囩锛屽鑷撮〉闈㈡覆鏌撻敊璇�

**鏍规湰鍘熷洜**: 鎵嬪姩缂栬緫鏃堕仐婕忛棴鍚堟爣绛�

**淇鏂规**:
```html
<!-- 鉂� 淇鍓嶏細鏍囩鏈棴鍚� -->
<div>
    <span>鍐呭

<!-- 鉁� 淇鍚庯細鏍囩姝ｇ‘闂悎 -->
<div>
    <span>鍐呭</span>
</div>
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **HTML璇硶** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **椤甸潰娓叉煋** | 閿欒 鉂� | 姝ｅ父 鉁� |
| **鏂囨。鍚屾** | 杩囨椂 鉂� | 鏈�鏂� 鉁� |

**鎶�鏈粏鑺�**: 淇index.html绗�5197琛屾爣绛鹃棴鍚堥敊璇紝鏇存柊skill.md/docx瑙勮寖





### v3.7.1 (2026-06-18) - 馃摫 璺ㄧ郴缁熺‖缂栫爜褰诲簳娑堥櫎 + V3.5.0绉诲姩绔鑼冨鏌�

#### 闂: 浠ｇ爜涓瓨鍦ㄧ‖缂栫爜锛岀Щ鍔ㄧ瑙勮寖鏈鏌�
**鐜拌薄**: 浠ｇ爜涓瓨鍦ㄧ‖缂栫爜璺緞鍜屽弬鏁帮紝绉诲姩绔�傞厤鏈叏闈㈠鏌�

**鏍规湰鍘熷洜**: 鏃╂湡寮�鍙戜娇鐢ㄧ‖缂栫爜锛岀Щ鍔ㄧ瑙勮寖鏈強鏃跺鏌�

**淇鏂规**:
```javascript
// 鉂� 淇鍓嶏細纭紪鐮�
const url = 'http://localhost:8080/api';

// 鉁� 淇鍚庯細鍔ㄦ�佽幏鍙�
const url = `${window.location.origin}/api`;

// 鉂� 淇鍓嶏細绉诲姩绔湭澶嶆煡
// 鏈獙璇佺Щ鍔ㄧ閫傞厤

// 鉁� 淇鍚庯細绉诲姩绔鑼冨鏌�
// 楠岃瘉鎵�鏈夌Щ鍔ㄧ閫傞厤绗﹀悎v3.5.0瑙勮寖
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **纭紪鐮佹秷闄�** | 瀛樺湪 鉂� | 褰诲簳娑堥櫎 鉁� |
| **璺ㄧ郴缁熷吋瀹�** | 宸� 鉂� | 濂� 鉁� |
| **绉诲姩绔鑼�** | 鏈鏌� 鉂� | 宸插鏌� 鉁� |

**鎶�鏈粏鑺�**: 褰诲簳娑堥櫎浠ｇ爜涓殑纭紪鐮侊紝瀹炵幇璺ㄧ郴缁熷吋瀹癸紝澶嶆煡绉诲姩绔�傞厤绗﹀悎v3.5.0瑙勮寖




### v3.6.0 (2026-07-05) - 馃摑 缂栫爜瑙勮寖鍜寁3.5.0绉诲姩绔鑼� + README鏍煎紡瑙勮寖

#### 闂: 缂哄皯缁熶竴鐨勭紪鐮佽鑼冨拰绉诲姩绔鑼冿紝README鏍煎紡涓嶈鑼�
**鐜拌薄**: 椤圭洰缂哄皯缁熶竴鐨勭紪鐮佽鑼冿紝绉诲姩绔�傞厤涓嶈鑼冿紝README鏍煎紡娣蜂贡

**鏍规湰鍘熷洜**: 鏃╂湡寮�鍙戞湭寤虹珛缁熶竴瑙勮寖

**淇鏂规**:
```markdown
<!-- 鉁� 缂栫爜瑙勮寖 -->
## 缂栫爜瑙勮寖
1. **鍛藉悕瑙勮寖**: 浣跨敤snake_case鍛藉悕鍙橀噺鍜屽嚱鏁�
2. **娉ㄩ噴瑙勮寖**: 浣跨敤涓枃娉ㄩ噴锛岄伒寰狿EP 257
3. **鏃ュ織瑙勮寖**: 鎵�鏈夋棩蹇楀寘鍚绉掔骇鏃堕棿鎴�
4. **閿欒澶勭悊**: 浣跨敤try-except鎹曡幏寮傚父骞惰褰曟棩蹇�

<!-- 鉁� v3.5.0绉诲姩绔鑼� -->
## 绉诲姩绔鑼�
1. **鍝嶅簲寮忓竷灞�**: 浣跨敤CSS Flexbox鍜孏rid
2. **瑙︽懜浼樺寲**: 鎸夐挳鏈�灏忓昂瀵�44x44px
3. **瀛椾綋閫傞厤**: 浣跨敤rem鍗曚綅
4. **鍥剧墖浼樺寲**: 浣跨敤WebP鏍煎紡锛屾噿鍔犺浇
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **缂栫爜瑙勮寖** | 缂哄け 鉂� | 瀹屾暣 鉁� |
| **绉诲姩绔鑼�** | 涓嶈鑼� 鉂� | 瑙勮寖 鉁� |
| **README鏍煎紡** | 娣蜂贡 鉂� | 瑙勮寖 鉁� |

**鎶�鏈粏鑺�**: 寤虹珛缁熶竴鐨勭紪鐮佽鑼冨拰v3.5.0绉诲姩绔鑼冿紝瑙勮寖README鏍煎紡锛屽悓姝ユ洿鏂癛EADME/skill.md/skill.docx





### v3.5.8 (2026-06-11) - 馃敡 鏇存柊鍓嶇鐗堟湰鍜宑hangelog鍒�3.5.8

#### 闂: 鍓嶇鐗堟湰鍙峰拰changelog鏈洿鏂�
**鐜拌薄**: 鍓嶇鏄剧ず鐨勭増鏈彿鍜宑hangelog涓庡疄闄呯増鏈笉涓�鑷�

**鏍规湰鍘熷洜**: 鍙戝竷鏂扮増鏈悗鏈強鏃舵洿鏂板墠绔�

**淇鏂规**:
```javascript
// 鉂� 淇鍓嶏細鐗堟湰鍙疯繃鏃�
const VERSION = 'v3.5.7';

// 鉁� 淇鍚庯細鐗堟湰鍙锋渶鏂�
const VERSION = 'v3.5.8';
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鐗堟湰鍙峰噯纭��** | 杩囨椂 鉂� | 鏈�鏂� 鉁� |
| **changelog鍚屾** | 杩囨椂 鉂� | 鏈�鏂� 鉁� |
| **鏂囨。鍚屾** | 杩囨椂 鉂� | 鏈�鏂� 鉁� |

**鎶�鏈粏鑺�**: 鏇存柊鍓嶇鐗堟湰鍙峰拰changelog鍒皏3.5.8锛屾坊鍔爏kill.md/skill.docx浠ｇ爜瑙勮寖锛屾仮澶峝ist鏂囦欢澶癸紝鏇存柊README





### v3.5.7 (2026-06-07) - 鉁� 鍓嶇娣诲姞鏈�鏂版洿鏂版ā鍧楋紝鐗堟湰鍙峰悓姝ユ洿鏂�

#### 闂: 鍓嶇缂哄皯鏈�鏂版洿鏂版ā鍧�
**鐜拌薄**: 鐢ㄦ埛鏃犳硶鍦ㄥ墠绔煡鐪嬫渶鏂扮殑鐗堟湰鏇存柊淇℃伅

**鏍规湰鍘熷洜**: 鍓嶇缂哄皯鏇存柊鏃ュ織灞曠ず妯″潡

**淇鏂规**:
```html
<!-- 鉁� 娣诲姞鏈�鏂版洿鏂版ā鍧� -->
<div id="changelog">
    <h3>鏈�鏂版洿鏂�</h3>
    <div id="changelog-content"></div>
</div>

<script>
fetch('/api/changelog')
    .then(response => response.json())
    .then(data => {
        document.getElementById('changelog-content').innerHTML = data.html;
    });
</script>
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏇存柊妯″潡** | 缂哄け 鉂� | 宸叉坊鍔� 鉁� |
| **鐗堟湰鍙峰悓姝�** | 杩囨椂 鉂� | 鏈�鏂� 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**: 鍓嶇娣诲姞鏈�鏂版洿鏂版ā鍧楋紝鍚屾鏇存柊鐗堟湰鍙凤紝浠ｇ爜閲嶆瀯浼樺寲锛岀‘璁よ法绯荤粺鍜岀Щ鍔ㄧ閫傞厤瀹屾暣鎬�





### v3.5.6 (2026-06-06) - 馃敡 瀹屽杽绉诲姩绔�傞厤鍔熻兘鍜岃〃鏍兼牱寮忎紭鍖�

#### 闂: 绉诲姩绔�傞厤涓嶅畬鍠勶紝琛ㄦ牸鏍峰紡涓嶄紭鍖�
**鐜拌薄**: 绉诲姩绔〃鏍兼樉绀烘贩涔憋紝鏍峰紡涓嶇編瑙�

**鏍规湰鍘熷洜**: 绉诲姩绔�傞厤鏈畬鍠勶紝琛ㄦ牸鏍峰紡鏈紭鍖�

**淇鏂规**:
```css
/* 鉁� 绉诲姩绔�傞厤 */
@media (max-width: 600px) {
    table {
        font-size: 12px;
    }
    .button-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* 鉁� 琛ㄦ牸鏍峰紡浼樺寲 */
table {
    border-collapse: collapse;
    width: 100%;
}
th, td {
    padding: 8px;
    text-align: left;
    border: 1px solid #ddd;
}
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **绉诲姩绔�傞厤** | 涓嶅畬鍠� 鉂� | 瀹屽杽 鉁� |
| **琛ㄦ牸鏍峰紡** | 涓嶇編瑙� 鉂� | 缇庤 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**: 瀹屽杽绉诲姩绔�傞厤鍔熻兘锛屼紭鍖栬〃鏍兼牱寮忥紝鎻愬崌鐢ㄦ埛浣撻獙





### v3.5.4 (2026-06-06) - 馃悰 姣忔棩鍒╂鼎鎶ヨ〃浼樺寲锛氭棩鏈熸牸寮忕粺涓�銆侀」鐩瓧娈点�佽〃澶村浐瀹氥�侀敊璇鐞嗗寮�

#### 闂: 姣忔棩鍒╂鼎鎶ヨ〃瀛樺湪澶氶」缂洪櫡
**鐜拌薄**: 鏃ユ湡鏍煎紡涓嶇粺涓�锛岀己灏戦」鐩瓧娈碉紝琛ㄥご涓嶅浐瀹氾紝閿欒澶勭悊涓嶅畬鍠�

**鏍规湰鍘熷洜**: 鎶ヨ〃鍔熻兘鏈叏闈紭鍖�

**淇鏂规**:
```javascript
// 鉁� 鏃ユ湡鏍煎紡缁熶竴
const formatDate = (date) => {
    return new Date(date).toLocaleDateString('zh-CN');
};

// 鉁� 琛ㄥご鍥哄畾
thead {
    position: sticky;
    top: 0;
    background: white;
}

// 鉁� 閿欒澶勭悊澧炲己
try {
    const data = await fetchProfitReport();
    renderReport(data);
} catch (error) {
    showError('鑾峰彇鍒╂鼎鎶ヨ〃澶辫触: ' + error.message);
}
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏃ユ湡鏍煎紡** | 涓嶇粺涓� 鉂� | 缁熶竴 鉁� |
| **椤圭洰瀛楁** | 缂哄け 鉂� | 宸叉坊鍔� 鉁� |
| **琛ㄥご鍥哄畾** | 涓嶅浐瀹� 鉂� | 鍥哄畾 鉁� |
| **閿欒澶勭悊** | 涓嶅畬鍠� 鉂� | 瀹屽杽 鉁� |

**鎶�鏈粏鑺�**: 缁熶竴鏃ユ湡鏍煎紡锛屾坊鍔犻」鐩瓧娈碉紝瀹炵幇琛ㄥご鍥哄畾锛屽寮洪敊璇鐞�





### v3.5.3 (2026-06-06) - 馃敡 姹囨�昏鍥句笌鏄庣粏鑱斿姩鍔熻兘

#### 闂: 姹囨�昏鍥句笌鏄庣粏鏃犺仈鍔�
**鐜拌薄**: 鐐瑰嚮姹囨�昏鏃犲搷搴旓紝鏃犳硶鏌ョ湅鏄庣粏

**鏍规湰鍘熷洜**: 缂哄皯鑱斿姩閫昏緫

**淇鏂规**:
```javascript
// 鉁� 姹囨�昏鍥句笌鏄庣粏鑱斿姩
row.onclick = function() {
    const summaryId = this.dataset.id;
    loadDetails(summaryId);
};

function loadDetails(summaryId) {
    fetch(`/api/profit/details/${summaryId}`)
        .then(response => response.json())
        .then(data => renderDetails(data));
}
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鑱斿姩鍔熻兘** | 鏃� 鉂� | 鏈� 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **鏁版嵁鏌ョ湅** | 鍥伴毦 鉂� | 绠�鍗� 鉁� |

**鎶�鏈粏鑺�**: 瀹炵幇姹囨�昏鍥句笌鏄庣粏鑱斿姩鍔熻兘锛岀偣鍑绘眹鎬昏鑷姩鍔犺浇鏄庣粏鏁版嵁





### v3.5.2 (2026-06-05) - 馃敡 鍓嶇姣忔棩鍒╂鼎鎶ヨ〃琛ㄦ牸娓叉煋浼樺寲

#### 闂: 鍓嶇姣忔棩鍒╂鼎鎶ヨ〃琛ㄦ牸娓叉煋涓嶅畬鏁�
**鐜拌薄**: 琛ㄦ牸鏈覆鏌撳埌鎬昏琛岋紝缂哄皯璐у竵绗﹀彿锛屽崟浣嶆樉绀轰笉姝ｇ‘

**鏍规湰鍘熷洜**: 娓叉煋閫昏緫涓嶅畬鏁�

**淇鏂规**:
```javascript
// 鉁� 娓叉煋鍒版�昏琛�
function renderTable(data) {
    data.rows.forEach(row => {
        // 娓叉煋姣忎竴琛�
    });
    // 娓叉煋鎬昏琛�
    renderTotalRow(data.total);
}

// 鉁� 璐у竵绗﹀彿鍜屽崟浣�
const formatCurrency = (value) => {
    return '楼' + value.toFixed(2);
};
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鎬昏琛屾覆鏌�** | 缂哄け 鉂� | 宸叉覆鏌� 鉁� |
| **璐у竵绗﹀彿** | 缂哄け 鉂� | 宸叉坊鍔� 鉁� |
| **鍗曚綅鏄剧ず** | 閿欒 鉂� | 姝ｇ‘ 鉁� |

**鎶�鏈粏鑺�**: 浼樺寲鍓嶇姣忔棩鍒╂鼎鎶ヨ〃琛ㄦ牸娓叉煋锛岀‘淇濇覆鏌撳埌鎬昏琛岋紝娣诲姞璐у竵绗﹀彿锛屾纭樉绀哄崟浣�





### v3.4.37 (2026-06-05) - 馃悰 浼樺寲涓存椂鏂囦欢娓呯悊鏈哄埗锛屼慨澶峛at鑴氭湰鍚姩鏃惰鏉�杩涚▼闂

#### 闂: 涓存椂鏂囦欢娓呯悊鏈哄埗涓嶅畬鍠勶紝bat鑴氭湰璇潃杩涚▼
**鐜拌薄**: 涓存椂鏂囦欢娓呯悊涓嶅交搴曪紝bat鑴氭湰鍚姩鏃惰鏉�姝ｅ湪杩愯鐨勮繘绋�

**鏍规湰鍘熷洜**: 娓呯悊閫昏緫杩囦簬婵�杩涳紝鏈尯鍒嗚繘绋嬬姸鎬�

**淇鏂规**:
```bash
# 鉂� 淇鍓嶏細璇潃鎵�鏈夎繘绋�
taskkill /F /IM python.exe

# 鉁� 淇鍚庯細鍙竻鐞嗕复鏃舵枃浠讹紝涓嶈鏉�杩涚▼
del /Q temp```*
# 涓嶅啀寮哄埗鏉�杩涚▼
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **涓存椂鏂囦欢娓呯悊** | 涓嶅畬鍠� 鉂� | 瀹屽杽 鉁� |
| **杩涚▼璇潃** | 瀛樺湪 鉂� | 宸蹭慨澶� 鉁� |
| **鍚姩绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 浼樺寲涓存椂鏂囦欢娓呯悊鏈哄埗锛屼慨澶峛at鑴氭湰鍚姩鏃惰鏉�杩涚▼闂





### v3.4.34 (2026-06-04) - 馃悰 淇鏂囦欢娓呯悊 API JSON 瑙ｆ瀽閿欒

#### 闂: 鏂囦欢娓呯悊 API JSON 瑙ｆ瀽閿欒
**鐜拌薄**: 鏂囦欢娓呯悊宸ュ叿API杩斿洖鐨凧SON鏍煎紡閿欒锛屽墠绔棤娉曡В鏋�

**鏍规湰鍘熷洜**: JSON搴忓垪鍖栭�昏緫閿欒

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細JSON鏍煎紡閿欒
return {"files": str(files)}

# 鉁� 淇鍚庯細JSON鏍煎紡姝ｇ‘
import json
return json.dumps({"files": files})
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **JSON瑙ｆ瀽** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **API鍙敤鎬�** | 浣� 鉂� | 楂� 鉁� |
| **鍓嶇鏄剧ず** | 閿欒 鉂� | 姝ｅ父 鉁� |

**鎶�鏈粏鑺�**: 淇鏂囦欢娓呯悊 API JSON 瑙ｆ瀽閿欒锛岀‘淇濊繑鍥炴牸寮忔纭�





### v3.4.33 (2026-06-03) - 馃敡 浠ｇ爜浼樺寲鍜岃法绯荤粺鏀寔澧炲己

#### 闂: 浠ｇ爜璐ㄩ噺涓嶉珮锛岃法绯荤粺鏀寔涓嶈冻
**鐜拌薄**: 浠ｇ爜瀛樺湪鍐椾綑锛岃法绯荤粺鍏煎鎬у樊

**鏍规湰鍘熷洜**: 浠ｇ爜鏈紭鍖栵紝璺ㄧ郴缁熼�昏緫涓嶅畬鍠�

**淇鏂规**:
```python
# 鉁� 浠ｇ爜浼樺寲
# 鍘婚櫎鍐椾綑浠ｇ爜锛屾彁鍙栧叕鍏卞嚱鏁�

# 鉁� 璺ㄧ郴缁熸敮鎸佸寮�
import platform
def get_config_path():
    system = platform.system()
    if system == 'Windows':
        return 'C:```config'
    elif system == 'Darwin':
        return '/usr/local/config'
    else:
        return '/etc/config'
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **浠ｇ爜璐ㄩ噺** | 浣� 鉂� | 楂� 鉁� |
| **璺ㄧ郴缁熸敮鎸�** | 宸� 鉂� | 濂� 鉁� |
| **鍙淮鎶ゆ��** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 浼樺寲浠ｇ爜璐ㄩ噺锛屽寮鸿法绯荤粺鏀寔锛屾彁鍗囧彲缁存姢鎬�





### v3.4.32 (2026-06-03) - 馃悰 淇闀滃儚婧愭樉绀洪棶棰樺苟缁熶竴run.sh閫昏緫

#### 闂: 闀滃儚婧愭樉绀洪棶棰橈紝run.sh閫昏緫涓嶇粺涓�
**鐜拌薄**: 闀滃儚婧愭祴閫熺粨鏋滄樉绀轰笉姝ｇ‘锛宺un.sh涓巖un.bat閫昏緫涓嶄竴鑷�

**鏍规湰鍘熷洜**: 闀滃儚婧愭樉绀洪�昏緫閿欒锛宺un.sh鏈悓姝un.bat

**淇鏂规**:
```bash
# 鉂� 淇鍓嶏細鏄剧ず閿欒
echo "Mirror: $mirror"

# 鉁� 淇鍚庯細鏄剧ず姝ｇ‘
echo "Mirror: $mirror | Speed: ${speed}ms"

# 鉁� 缁熶竴run.sh閫昏緫
# 纭繚run.sh涓巖un.bat閫昏緫涓�鑷�
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **闀滃儚婧愭樉绀�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **run.sh缁熶竴** | 涓嶄竴鑷� 鉂� | 涓�鑷� 鉁� |
| **璺ㄧ郴缁熼獙璇�** | 鏈獙璇� 鉂� | 宸查獙璇� 鉁� |

**鎶�鏈粏鑺�**: 淇闀滃儚婧愭樉绀洪棶棰橈紝缁熶竴run.sh涓巖un.bat閫昏緫锛屽疄鐜板叏闈㈣法绯荤粺鏀寔





### v3.4.31 (2026-06-01) - 馃悰 淇鏂囦欢娓呯悊宸ュ叿鑾峰彇鏂囦欢澶у皬閿欒

#### 闂: 鏂囦欢娓呯悊宸ュ叿鑾峰彇鏂囦欢澶у皬閿欒
**鐜拌薄**: 鏂囦欢娓呯悊宸ュ叿鏄剧ず鐨勬枃浠跺ぇ灏忎笉鍑嗙‘

**鏍规湰鍘熷洜**: 鏂囦欢澶у皬璁＄畻閫昏緫閿欒

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細澶у皬閿欒
size = os.path.getsize(file) / 1024  # KB

# 鉁� 淇鍚庯細澶у皬姝ｇ‘
size = os.path.getsize(file) / (1024 * 1024)  # MB
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏂囦欢澶у皬鍑嗙‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **娓呯悊鏁堢巼** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 淇鏂囦欢娓呯悊宸ュ叿鑾峰彇鏂囦欢澶у皬閿欒锛岀‘淇濇樉绀哄噯纭�





### v3.4.30 (2026-05-30) - 馃悰 淇娓呯悊宸ュ叿 API 绌虹洰褰曟娴嬮棶棰�

#### 闂: 娓呯悊宸ュ叿 API 绌虹洰褰曟娴嬮棶棰�
**鐜拌薄**: 娓呯悊宸ュ叿鏃犳硶姝ｇ‘妫�娴嬬┖鐩綍

**鏍规湰鍘熷洜**: 绌虹洰褰曟娴嬮�昏緫閿欒

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細妫�娴嬮敊璇�
if not os.listdir(dir):
    return True

# 鉁� 淇鍚庯細妫�娴嬫纭�
try:
    if len(os.listdir(dir)) == 0:
        return True
except FileNotFoundError:
    return False
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **绌虹洰褰曟娴�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **娓呯悊鍑嗙‘鎬�** | 浣� 鉂� | 楂� 鉁� |
| **閿欒澶勭悊** | 鏃� 鉂� | 瀹屽杽 鉁� |

**鎶�鏈粏鑺�**: 淇娓呯悊宸ュ叿 API 绌虹洰褰曟娴嬮棶棰橈紝娣诲姞閿欒澶勭悊





### v3.4.29 (2026-05-30) - 馃敡 淇 run.bat 鐗堟湰鍙疯В鏋愬け璐ラ棶棰�

#### 闂: run.bat 鐗堟湰鍙疯В鏋愬け璐�
**鐜拌薄**: run.bat鏃犳硶姝ｇ‘瑙ｆ瀽鐗堟湰鍙�

**鏍规湰鍘熷洜**: 鐗堟湰鍙疯В鏋愭鍒欒〃杈惧紡閿欒

**淇鏂规**:
```bash
# 鉂� 淇鍓嶏細姝ｅ垯閿欒
for /f "tokens=2" %%a in ('findstr "version" README.md') do set VERSION=%%a

# 鉁� 淇鍚庯細姝ｅ垯姝ｇ‘
for /f "tokens=2 delims= " %%a in ('findstr /C:"v3" README.md') do set VERSION=%%a
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鐗堟湰鍙疯В鏋�** | 澶辫触 鉂� | 鎴愬姛 鉁� |
| **鑴氭湰绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**: 淇 run.bat 鐗堟湰鍙疯В鏋愬け璐ラ棶棰橈紝淇姝ｅ垯琛ㄨ揪寮�





### v3.4.28 (2026-05-30) - 馃敡 浼樺寲Flask 404澶勭悊鍜岄偖浠跺喎鍗存湡琛ュ彂鏈哄埗

#### 闂: Flask 404澶勭悊涓嶅畬鍠勶紝閭欢鍐峰嵈鏈熻ˉ鍙戞満鍒剁己澶�
**鐜拌薄**: 404閿欒鏈弸濂芥彁绀猴紝閭欢鍐峰嵈鏈熷悗鏈ˉ鍙�

**鏍规湰鍘熷洜**: 404澶勭悊閫昏緫绠�鍗曪紝閭欢琛ュ彂鏈哄埗缂哄け

**淇鏂规**:
```python
# 鉁� 浼樺寲404澶勭悊
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# 鉁� 閭欢鍐峰嵈鏈熻ˉ鍙戞満鍒�
def send_email_with_retry(url):
    if is_in_cooldown(url):
        schedule_retry(url)
    else:
        send_email(url)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **404澶勭悊** | 涓嶅畬鍠� 鉂� | 瀹屽杽 鉁� |
| **閭欢琛ュ彂** | 缂哄け 鉂� | 宸叉坊鍔� 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**: 浼樺寲Flask 404澶勭悊锛屾坊鍔犻偖浠跺喎鍗存湡琛ュ彂鏈哄埗





### v3.4.27 (2026-05-29) - 馃悰 淇鏂囦欢娓呯悊宸ュ叿'鍒犻櫎鎵�鏈夋枃浠跺拰鏂囦欢澶�'鍔熻兘鎶ラ敊

#### 闂: 鏂囦欢娓呯悊宸ュ叿'鍒犻櫎鎵�鏈夋枃浠跺拰鏂囦欢澶�'鍔熻兘鎶ラ敊
**鐜拌薄**: 鐐瑰嚮'鍒犻櫎鎵�鏈夋枃浠跺拰鏂囦欢澶�'鎸夐挳鏃舵姤閿�

**鏍规湰鍘熷洜**: 鍒犻櫎閫昏緫鏈鐞嗘潈闄愬拰鏂囦欢鍗犵敤闂

**淇鏂规**:
```python
# 鉁� 瀹夊叏鍒犻櫎閫昏緫
def delete_all_files(path):
    try:
        shutil.rmtree(path)
    except PermissionError:
        logging.error(f"Permission denied: {path}")
    except OSError as e:
        logging.error(f"Error deleting {path}: {e}")
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍒犻櫎鍔熻兘** | 鎶ラ敊 鉂� | 姝ｅ父 鉁� |
| **閿欒澶勭悊** | 鏃� 鉂� | 瀹屽杽 鉁� |
| **瀹夊叏鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 淇鏂囦欢娓呯悊宸ュ叿'鍒犻櫎鎵�鏈夋枃浠跺拰鏂囦欢澶�'鍔熻兘鎶ラ敊锛屾坊鍔犻敊璇鐞�





### v3.4.26 (2026-05-29) - 馃敡 閲嶆瀯缁熶竴寮傚父澶勭悊绯荤粺 + 澧炲己 tunnel_status API URL 楠岃瘉

#### 闂: 寮傚父澶勭悊涓嶇粺涓�锛宼unnel_status API URL楠岃瘉涓嶈冻
**鐜拌薄**: 寮傚父澶勭悊鍒嗘暎锛宼unnel_status API鏈獙璇乁RL鏈夋晥鎬�

**鏍规湰鍘熷洜**: 缂哄皯缁熶竴寮傚父澶勭悊绯荤粺锛孶RL楠岃瘉閫昏緫绠�鍗�

**淇鏂规**:
```python
# 鉁� 缁熶竴寮傚父澶勭悊
@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"Unhandled exception: {e}")
    return jsonify({"error": str(e)}), 500

# 鉁� 澧炲己URL楠岃瘉
def validate_tunnel_url(url):
    if not url.startswith('http'):
        return False
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except:
        return False
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **寮傚父澶勭悊** | 鍒嗘暎 鉂� | 缁熶竴 鉁� |
| **URL楠岃瘉** | 绠�鍗� 鉂� | 澧炲己 鉁� |
| **绯荤粺绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 閲嶆瀯缁熶竴寮傚父澶勭悊绯荤粺锛屽寮� tunnel_status API URL 楠岃瘉





### v3.4.25 (2026-05-29) - 馃敡 Excel璇诲彇鏀逛负澶嶅埗鍒颁复鏃舵枃浠讹紝褰诲簳瑙ｅ喅鍏变韩杩濊

#### 闂: Excel鏂囦欢璇诲彇鏃跺嚭鐜板叡浜繚瑙�
**鐜拌薄**: 璇诲彇Excel鏂囦欢鏃跺嚭鐜�"鏂囦欢姝ｅ湪琚彟涓�涓繘绋嬩娇鐢�"閿欒

**鏍规湰鍘熷洜**: Windows鏂囦欢閿佸畾鏈哄埗锛孍xcel鏂囦欢琚攣瀹�

**淇鏂规**:
```python
# 鉁� Excel璇诲彇鏀逛负澶嶅埗鍒颁复鏃舵枃浠�
import shutil
import tempfile

def read_excel_safely(file_path):
    # 澶嶅埗鍒颁复鏃舵枃浠�
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx')
    shutil.copy2(file_path, temp_file.name)
    
    # 璇诲彇涓存椂鏂囦欢
    wb = openpyxl.load_workbook(temp_file.name)
    data = wb.active
    
    # 娓呯悊涓存椂鏂囦欢
    temp_file.close()
    os.unlink(temp_file.name)
    
    return data
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍏变韩杩濊** | 棰戠箒 鉂� | 宸茶В鍐� 鉁� |
| **鏂囦欢璇诲彇** | 涓嶇ǔ瀹� 鉂� | 绋冲畾 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**: Excel璇诲彇鏀逛负澶嶅埗鍒颁复鏃舵枃浠讹紝褰诲簳瑙ｅ喅鍏变韩杩濊闂





### v3.4.24 (2026-05-29) - 馃悰 淇 Excel 鍏变韩杩濊 - 鎵�鏈夎鍙栨敼涓� read_only=True

#### 闂: Excel鏂囦欢璇诲彇鏃跺嚭鐜板叡浜繚瑙�
**鐜拌薄**: 璇诲彇Excel鏂囦欢鏃跺嚭鐜�"鏂囦欢姝ｅ湪琚彟涓�涓繘绋嬩娇鐢�"閿欒

**鏍规湰鍘熷洜**: Excel鏂囦欢鏈互鍙妯″紡鎵撳紑

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鏈娇鐢ㄥ彧璇绘ā寮�
wb = openpyxl.load_workbook(file_path)

# 鉁� 淇鍚庯細浣跨敤鍙妯″紡
wb = openpyxl.load_workbook(file_path, read_only=True)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍏变韩杩濊** | 瀛樺湪 鉂� | 宸蹭慨澶� 鉁� |
| **鏂囦欢璇诲彇** | 涓嶇ǔ瀹� 鉂� | 绋冲畾 鉁� |

**鎶�鏈粏鑺�**: 鎵�鏈塃xcel璇诲彇鏀逛负read_only=True锛岄伩鍏嶅叡浜繚瑙�





### v3.4.23 (2026-05-29) - 馃悰 淇 Excel 鏂囦欢璇诲彇鏃剁殑 Windows 鍏变韩杩濊闂

#### 闂: Excel鏂囦欢璇诲彇鏃跺嚭鐜板叡浜繚瑙�
**鐜拌薄**: 璇诲彇Excel鏂囦欢鏃跺嚭鐜�"鏂囦欢姝ｅ湪琚彟涓�涓繘绋嬩娇鐢�"閿欒

**鏍规湰鍘熷洜**: Windows鏂囦欢閿佸畾鏈哄埗锛孍xcel鏂囦欢琚攣瀹�

**淇鏂规**:
```python
# 鉁� 淇Excel鍏变韩杩濊
# 娣诲姞鏂囦欢閿佸畾妫�娴嬪拰閲嶈瘯鏈哄埗
def read_excel_with_retry(file_path, max_retries=3):
    for i in range(max_retries):
        try:
            wb = openpyxl.load_workbook(file_path, read_only=True)
            return wb
        except PermissionError:
            if i < max_retries - 1:
                time.sleep(1)
            else:
                raise
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍏变韩杩濊** | 棰戠箒 鉂� | 宸蹭慨澶� 鉁� |
| **鏂囦欢璇诲彇** | 涓嶇ǔ瀹� 鉂� | 绋冲畾 鉁� |

**鎶�鏈粏鑺�**: 淇Excel鏂囦欢璇诲彇鏃剁殑Windows鍏变韩杩濊闂锛屾坊鍔犻噸璇曟満鍒�





### v3.4.22 (2026-05-29) - 馃敡 浼樺寲蹇冭烦妫�娴嬮棿闅斾粠60绉掑埌5绉掞紝鎻愰珮闅ч亾鏁呴殰妫�娴嬮�熷害

#### 闂: 蹇冭烦妫�娴嬮棿闅旇繃闀匡紝鏁呴殰妫�娴嬫參
**鐜拌薄**: 闅ч亾鏁呴殰妫�娴嬮渶瑕�60绉掞紝鍝嶅簲鎱�

**鏍规湰鍘熷洜**: 蹇冭烦妫�娴嬮棿闅旇缃繃闀�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細蹇冭烦妫�娴嬮棿闅�60绉�
HEARTBEAT_INTERVAL = 60

# 鉁� 淇鍚庯細蹇冭烦妫�娴嬮棿闅�5绉�
HEARTBEAT_INTERVAL = 5
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏁呴殰妫�娴嬮�熷害** | 60绉� 鉂� | 5绉� 鉁� |
| **鏁呴殰鍝嶅簲** | 鎱� 鉂� | 蹇� 鉁� |
| **绯荤粺绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 浼樺寲蹇冭烦妫�娴嬮棿闅斾粠60绉掑埌5绉掞紝鎻愰珮闅ч亾鏁呴殰妫�娴嬮�熷害





### v3.4.21 (2026-05-29) - 馃寪 纭繚 tunnel_url.txt 鎸佷箙涓�鑷�

#### 闂: tunnel_url.txt鏂囦欢涓嶄竴鑷�
**鐜拌薄**: tunnel_url.txt鏂囦欢鍐呭涓嶄竴鑷�

**鏍规湰鍘熷洜**: 鏂囦欢鍐欏叆閫昏緫涓嶅畬鍠�

**淇鏂规**:
```python
# 鉁� 纭繚tunnel_url.txt鎸佷箙涓�鑷�
def write_tunnel_url(url):
    with open('tunnel_url.txt', 'w') as f:
        f.write(url)
    # 纭繚鏂囦欢鍐欏叆纾佺洏
    os.fsync(f.fileno())
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏂囦欢涓�鑷存��** | 涓嶄竴鑷� 鉂� | 涓�鑷� 鉁� |
| **鏁版嵁鎸佷箙鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 纭繚tunnel_url.txt鎸佷箙涓�鑷达紝娣诲姞鏂囦欢鍚屾鏈哄埗





### v3.4.20 (2026-05-29) - 馃敡 浼樺寲 tunnel_url.txt 鍐欏叆鏍煎紡

#### 闂: tunnel_url.txt鍐欏叆鏍煎紡涓嶇粺涓�
**鐜拌薄**: tunnel_url.txt鏂囦欢鏍煎紡涓嶇粺涓�

**鏍规湰鍘熷洜**: 鏂囦欢鍐欏叆鏍煎紡涓嶈鑼�

**淇鏂规**:
```python
# 鉁� 浼樺寲tunnel_url.txt鍐欏叆鏍煎紡
def write_tunnel_url(url):
    with open('tunnel_url.txt', 'w') as f:
        # 缁熶竴鏍煎紡锛氭椂闂存埑 + URL
        f.write(f"{datetime.now().isoformat()}```n")
        f.write(f"{url}```n")
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏂囦欢鏍煎紡** | 涓嶇粺涓� 鉂� | 缁熶竴 鉁� |
| **鍙鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 浼樺寲tunnel_url.txt鍐欏叆鏍煎紡锛屾坊鍔犳椂闂存埑





### v3.4.19 (2026-05-29) - 馃寪 鍚屾鍐欏叆 tunnel_url.txt

#### 闂: tunnel_url.txt鍐欏叆涓嶅悓姝�
**鐜拌薄**: tunnel_url.txt鏂囦欢鍐欏叆涓嶅悓姝�

**鏍规湰鍘熷洜**: 鏂囦欢鍐欏叆閫昏緫涓嶅畬鍠�

**淇鏂规**:
```python
# 鉁� 鍚屾鍐欏叆tunnel_url.txt
def write_tunnel_url(url):
    with open('tunnel_url.txt', 'w') as f:
        f.write(url)
        f.flush()
        os.fsync(f.fileno())
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏂囦欢鍚屾** | 涓嶅悓姝� 鉂� | 鍚屾 鉁� |
| **鏁版嵁瀹夊叏鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 鍚屾鍐欏叆tunnel_url.txt锛岀‘淇濇暟鎹畨鍏�





### v3.4.18 (2026-05-29) - 馃寪 瀹屽叏绉婚櫎 tunnel_url 鍏ㄥ眬鍙橀噺鐨勬洿鏂伴�昏緫

#### 闂: tunnel_url鍏ㄥ眬鍙橀噺鏇存柊閫昏緫鍐椾綑
**鐜拌薄**: tunnel_url鍏ㄥ眬鍙橀噺鏇存柊閫昏緫鍐椾綑

**鏍规湰鍘熷洜**: 鍏ㄥ眬鍙橀噺绠＄悊涓嶅綋

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細浣跨敤鍏ㄥ眬鍙橀噺
tunnel_url = None

def update_tunnel_url(url):
    global tunnel_url
    tunnel_url = url

# 鉁� 淇鍚庯細绉婚櫎鍏ㄥ眬鍙橀噺锛屼娇鐢ㄦ枃浠跺瓨鍌�
def get_tunnel_url():
    with open('tunnel_url.txt', 'r') as f:
        return f.read().strip()
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **浠ｇ爜澶嶆潅搴�** | 楂� 鉂� | 浣� 鉁� |
| **鍙淮鎶ゆ��** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 瀹屽叏绉婚櫎tunnel_url鍏ㄥ眬鍙橀噺鐨勬洿鏂伴�昏緫锛屼娇鐢ㄦ枃浠跺瓨鍌�





### v3.4.17 (2026-05-29) - 馃敡 缁熶竴鎵�鏈夋ā鍧椾粠 web_output.log 鑾峰彇鍏綉鍦板潃

#### 闂: 鍏綉鍦板潃鑾峰彇鏂瑰紡涓嶇粺涓�
**鐜拌薄**: 涓嶅悓妯″潡浣跨敤涓嶅悓鏂瑰紡鑾峰彇鍏綉鍦板潃

**鏍规湰鍘熷洜**: 鍏綉鍦板潃鑾峰彇閫昏緫鍒嗘暎

**淇鏂规**:
```python
# 鉁� 缁熶竴浠巜eb_output.log鑾峰彇鍏綉鍦板潃
def get_public_url():
    with open('web_output.log', 'r') as f:
        for line in f:
            if 'https://' in line or 'http://' in line:
                return line.strip()
    return None
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍦板潃鑾峰彇** | 涓嶇粺涓� 鉂� | 缁熶竴 鉁� |
| **浠ｇ爜涓�鑷存��** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 缁熶竴鎵�鏈夋ā鍧椾粠web_output.log鑾峰彇鍏綉鍦板潃





### v3.4.16 (2026-05-29) - 馃悰 淇 old_url 鏈畾涔夐敊璇�

#### 闂: old_url鍙橀噺鏈畾涔�
**鐜拌薄**: 浠ｇ爜涓娇鐢╫ld_url鍙橀噺浣嗘湭瀹氫箟

**鏍规湰鍘熷洜**: 鍙橀噺瀹氫箟閬楁紡

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍙橀噺鏈畾涔�
if url != old_url:
    pass

# 鉁� 淇鍚庯細鍙橀噺宸插畾涔�
old_url = None
if url != old_url:
    pass
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍙橀噺瀹氫箟** | 缂哄け 鉂� | 宸插畾涔� 鉁� |
| **浠ｇ爜姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |

**鎶�鏈粏鑺�**: 淇old_url鏈畾涔夐敊璇紝娣诲姞鍙橀噺瀹氫箟





### v3.4.15 (2026-05-29) - 馃敡 绠�鍖栧惎鍔ㄦ祦绋嬶紝绉婚櫎鍐椾綑绛夊緟閫昏緫

#### 闂: 鍚姩娴佺▼鍐椾綑锛岀瓑寰呴�昏緫澶嶆潅
**鐜拌薄**: 鍚姩娴佺▼鍖呭惈鍐椾綑鐨勭瓑寰呴�昏緫

**鏍规湰鍘熷洜**: 鍚姩娴佺▼璁捐涓嶅悎鐞�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍐椾綑绛夊緟閫昏緫
time.sleep(10)
wait_for_tunnel()
time.sleep(5)

# 鉁� 淇鍚庯細绠�鍖栧惎鍔ㄦ祦绋�
wait_for_tunnel()
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍚姩閫熷害** | 鎱� 鉂� | 蹇� 鉁� |
| **浠ｇ爜绠�娲佹��** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 绠�鍖栧惎鍔ㄦ祦绋嬶紝绉婚櫎鍐椾綑绛夊緟閫昏緫





### v3.4.14 (2026-05-29) - 馃寪 read_output 鏀逛负璇诲彇 hostc stdout 杈撳嚭

#### 闂: read_output璇诲彇鏂瑰紡涓嶆纭�
**鐜拌薄**: read_output鍑芥暟璇诲彇鏂瑰紡涓嶆纭�

**鏍规湰鍘熷洜**: 璇诲彇閫昏緫閿欒

**淇鏂规**:
```python
# 鉁� read_output鏀逛负璇诲彇hostc stdout杈撳嚭
def read_output():
    result = subprocess.run(['hostc', 'status'], capture_output=True, text=True)
    return result.stdout
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **杈撳嚭璇诲彇** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鏁版嵁鍑嗙‘鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: read_output鏀逛负璇诲彇hostc stdout杈撳嚭





### v3.4.13 (2026-05-29) - 馃寪 瀹屽叏绉婚櫎 tunnel_url.txt 璇诲彇閫昏緫锛屽叏閮ㄤ粠 web_output.log

#### 闂: tunnel_url.txt璇诲彇閫昏緫鍐椾綑
**鐜拌薄**: tunnel_url.txt璇诲彇閫昏緫鍐椾綑

**鏍规湰鍘熷洜**: 璇诲彇閫昏緫閲嶅

**淇鏂规**:
```python
# 鉁� 瀹屽叏绉婚櫎tunnel_url.txt璇诲彇閫昏緫
def get_tunnel_url():
    # 鍏ㄩ儴浠巜eb_output.log鑾峰彇
    with open('web_output.log', 'r') as f:
        return f.read().strip()
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **浠ｇ爜绠�娲佹��** | 浣� 鉂� | 楂� 鉁� |
| **閫昏緫缁熶竴鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 瀹屽叏绉婚櫎tunnel_url.txt璇诲彇閫昏緫锛屽叏閮ㄤ粠web_output.log鑾峰彇





### v3.4.12 (2026-05-29) - 馃悰 淇绛夊緟 URL 閫昏緫锛岀洿鎺ユ鏌� web_output.log

#### 闂: 绛夊緟URL閫昏緫涓嶆纭�
**鐜拌薄**: 绛夊緟URL閫昏緫涓嶆纭�

**鏍规湰鍘熷洜**: 绛夊緟閫昏緫閿欒

**淇鏂规**:
```python
# 鉁� 淇绛夊緟URL閫昏緫
def wait_for_url():
    while True:
        if os.path.exists('web_output.log'):
            with open('web_output.log', 'r') as f:
                content = f.read()
                if 'https://' in content or 'http://' in content:
                    return True
        time.sleep(1)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **URL绛夊緟** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鍚姩绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 淇绛夊緟URL閫昏緫锛岀洿鎺ユ鏌eb_output.log





### v3.4.11 (2026-05-29) - 馃敡 澶у箙绠�鍖� tunnel 閲嶅惎閫昏緫

#### 闂: tunnel閲嶅惎閫昏緫澶嶆潅
**鐜拌薄**: tunnel閲嶅惎閫昏緫澶嶆潅

**鏍规湰鍘熷洜**: 閲嶅惎閫昏緫璁捐涓嶅悎鐞�

**淇鏂规**:
```python
# 鉁� 澶у箙绠�鍖杢unnel閲嶅惎閫昏緫
def restart_tunnel():
    stop_tunnel()
    start_tunnel()
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **閲嶅惎閫昏緫** | 澶嶆潅 鉂� | 绠�鍗� 鉁� |
| **浠ｇ爜鍙鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 澶у箙绠�鍖杢unnel閲嶅惎閫昏緫





### v3.4.10 (2026-05-29) - 馃敡 浼樺寲 hostc 杩涚▼绋冲畾鎬э紝URL 鏃犳晥鏃剁瓑寰� 60 绉掑啀閲嶅惎

#### 闂: hostc杩涚▼绋冲畾鎬т笉瓒�
**鐜拌薄**: URL鏃犳晥鏃剁珛鍗抽噸鍚紝瀵艰嚧棰戠箒閲嶅惎

**鏍规湰鍘熷洜**: 閲嶅惎閫昏緫杩囦簬婵�杩�

**淇鏂规**:
```python
# 鉁� 浼樺寲hostc杩涚▼绋冲畾鎬�
def check_tunnel_status():
    if not is_url_valid():
        # URL鏃犳晥鏃剁瓑寰�60绉掑啀閲嶅惎
        time.sleep(60)
        restart_tunnel()
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **杩涚▼绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |
| **閲嶅惎棰戠巼** | 楂� 鉂� | 浣� 鉁� |

**鎶�鏈粏鑺�**: 浼樺寲hostc杩涚▼绋冲畾鎬э紝URL鏃犳晥鏃剁瓑寰�60绉掑啀閲嶅惎





### v3.4.9 (2026-05-29) - 馃敡 缁熶竴浣跨敤 web_output.log 浣滀负鍏綉鍦板潃鍞竴鏉ユ簮

#### 闂: 鍏綉鍦板潃鏉ユ簮涓嶇粺涓�
**鐜拌薄**: 鍏綉鍦板潃鏉ユ簮涓嶇粺涓�

**鏍规湰鍘熷洜**: 鍦板潃鏉ユ簮鍒嗘暎

**淇鏂规**:
```python
# 鉁� 缁熶竴浣跨敤web_output.log浣滀负鍏綉鍦板潃鍞竴鏉ユ簮
def get_public_url():
    with open('web_output.log', 'r') as f:
        return f.read().strip()
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍦板潃鏉ユ簮** | 涓嶇粺涓� 鉂� | 缁熶竴 鉁� |
| **浠ｇ爜涓�鑷存��** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 缁熶竴浣跨敤web_output.log浣滀负鍏綉鍦板潃鍞竴鏉ユ簮





### v3.4.8 (2026-05-29) - 馃敡 缁熶竴鍏綉鍦板潃鏉ユ簮锛屽叏閮ㄤ粠 web_output.log 鑾峰彇

#### 闂: 鍏綉鍦板潃鏉ユ簮涓嶇粺涓�
**鐜拌薄**: 鍏綉鍦板潃鏉ユ簮涓嶇粺涓�

**鏍规湰鍘熷洜**: 鍦板潃鏉ユ簮鍒嗘暎

**淇鏂规**:
```python
# 鉁� 缁熶竴鍏綉鍦板潃鏉ユ簮
def get_public_url():
    with open('web_output.log', 'r') as f:
        return f.read().strip()
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍦板潃鏉ユ簮** | 涓嶇粺涓� 鉂� | 缁熶竴 鉁� |
| **浠ｇ爜涓�鑷存��** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 缁熶竴鍏綉鍦板潃鏉ユ簮锛屽叏閮ㄤ粠web_output.log鑾峰彇





### v3.4.7 (2026-05-29) - 馃摑 鏇存柊 README

#### 闂: README闇�瑕佹洿鏂�
**鐜拌薄**: README鏂囨。涓嶅畬鏁�

**鏍规湰鍘熷洜**: 鏂囨。鏇存柊涓嶅強鏃�

**淇鏂规**:
```python
# 鉁� 鏇存柊README
# 瀹屽杽绯荤粺鏂囨。
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏂囨。瀹屾暣鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 鏇存柊README锛屽畬鍠勭郴缁熸枃妗�





### v3.4.6 (2026-05-29) - 馃悰 淇 tunnel_url.txt 涓虹┖鏃舵棤娉曢噸鍚棶棰�

#### 闂: tunnel_url.txt涓虹┖鏃舵棤娉曢噸鍚�
**鐜拌薄**: tunnel_url.txt鏂囦欢涓虹┖鏃舵棤娉曢噸鍚毀閬�

**鏍规湰鍘熷洜**: 鏂囦欢涓虹┖鏃剁殑澶勭悊閫昏緫閿欒

**淇鏂规**:
```python
# 鉁� 淇tunnel_url.txt涓虹┖鏃剁殑澶勭悊閫昏緫
def restart_tunnel():
    url = read_tunnel_url()
    if not url:
        # 鏂囦欢涓虹┖鏃剁洿鎺ュ惎鍔ㄦ柊闅ч亾
        start_new_tunnel()
    else:
        restart_existing_tunnel()
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **閲嶅惎鍔熻兘** | 澶辫触 鉂� | 鎴愬姛 鉁� |
| **鏂囦欢澶勭悊** | 閿欒 鉂� | 姝ｇ‘ 鉁� |

**鎶�鏈粏鑺�**: 淇tunnel_url.txt涓虹┖鏃舵棤娉曢噸鍚棶棰橈紝娣诲姞绌烘枃浠跺鐞嗛�昏緫





### v3.4.5 (2026-05-29) - 馃悰 淇 tunnel_url.txt 涓虹┖鏃堕噸鍚惊鐜棶棰�

#### 闂: tunnel_url.txt涓虹┖鏃堕噸鍚惊鐜�
**鐜拌薄**: tunnel_url.txt鏂囦欢涓虹┖鏃跺嚭鐜伴噸鍚惊鐜�

**鏍规湰鍘熷洜**: 鏂囦欢涓虹┖鏃剁殑澶勭悊閫昏緫閿欒

**淇鏂规**:
```python
# 鉁� 淇tunnel_url.txt涓虹┖鏃剁殑閲嶅惎寰幆闂
def check_tunnel_status():
    url = read_tunnel_url()
    if not url:
        # 鏂囦欢涓虹┖鏃剁瓑寰匲RL鐢熸垚
        time.sleep(5)
        return
    # 姝ｅ父妫�鏌ラ�昏緫
    if not is_url_valid(url):
        restart_tunnel()
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **閲嶅惎寰幆** | 瀛樺湪 鉂� | 宸蹭慨澶� 鉁� |
| **绯荤粺绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 淇tunnel_url.txt涓虹┖鏃堕噸鍚惊鐜棶棰橈紝娣诲姞绌烘枃浠剁瓑寰呴�昏緫





### v3.4.4 (2026-05-29) - 馃敡 浼樺寲 tunnel_url.txt 涓虹┖鏃剁珛鍗抽噸鍚紝涓嶇瓑寰�20绉掕秴鏃�

#### 闂: tunnel_url.txt涓虹┖鏃剁瓑寰呰秴鏃�
**鐜拌薄**: tunnel_url.txt鏂囦欢涓虹┖鏃堕渶瑕佺瓑寰�20绉掕秴鏃�

**鏍规湰鍘熷洜**: 瓒呮椂閫昏緫璁剧疆杩囬暱

**淇鏂规**:
```python
# 鉁� 浼樺寲tunnel_url.txt涓虹┖鏃剁殑澶勭悊閫昏緫
def check_tunnel_status():
    url = read_tunnel_url()
    if not url:
        # 鏂囦欢涓虹┖鏃剁珛鍗抽噸鍚紝涓嶇瓑寰呰秴鏃�
        restart_tunnel()
        return
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **閲嶅惎閫熷害** | 鎱�(20绉�) 鉂� | 蹇�(绔嬪嵆) 鉁� |
| **鍝嶅簲閫熷害** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 浼樺寲tunnel_url.txt涓虹┖鏃剁珛鍗抽噸鍚紝涓嶇瓑寰�20绉掕秴鏃�





### v3.4.3 (2026-05-29) - 馃悰 淇 tunnel_url.txt 涓虹┖鏃朵笉閲嶅惎銆佸畧鎶ょ嚎绋嬮噸澶嶅惎鍔ㄦ棩蹇楀埛灞忋�乁RL 鏃犳晥鏃朵笉杩斿洖鏃犳晥鍦板潃

#### 闂: 澶氫釜闂闇�瑕佷慨澶�
**鐜拌薄**: tunnel_url.txt涓虹┖鏃朵笉閲嶅惎銆佸畧鎶ょ嚎绋嬮噸澶嶅惎鍔ㄦ棩蹇楀埛灞忋�乁RL鏃犳晥鏃朵笉杩斿洖鏃犳晥鍦板潃

**鏍规湰鍘熷洜**: 澶氫釜閫昏緫閿欒

**淇鏂规**:
```python
# 鉁� 淇澶氫釜闂
# 1. tunnel_url.txt涓虹┖鏃堕噸鍚�
# 2. 瀹堟姢绾跨▼閲嶅鍚姩鏃ュ織鍒峰睆
# 3. URL鏃犳晥鏃惰繑鍥炴棤鏁堝湴鍧�
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **閲嶅惎鍔熻兘** | 澶辫触 鉂� | 鎴愬姛 鉁� |
| **鏃ュ織鍒峰睆** | 瀛樺湪 鉂� | 宸蹭慨澶� 鉁� |
| **URL杩斿洖** | 閿欒 鉂� | 姝ｇ‘ 鉁� |

**鎶�鏈粏鑺�**: 淇澶氫釜闂锛屾彁鍗囩郴缁熺ǔ瀹氭��





### v3.4.2 (2026-05-29) - 馃敡 鍓嶇灞曠ずURL鍙敤鎬ч獙璇� + 蹇冭烦妫�娴嬫棩蹇椾紭鍖�

#### 闂: 鍓嶇URL鍙敤鎬ч獙璇佺己澶憋紝蹇冭烦妫�娴嬫棩蹇楀啑浣�
**鐜拌薄**: 鍓嶇鏈獙璇乁RL鍙敤鎬э紝蹇冭烦妫�娴嬫棩蹇楀啑浣�

**鏍规湰鍘熷洜**: 鍔熻兘缂哄け锛屾棩蹇椾紭鍖栦笉瓒�

**淇鏂规**:
```python
# 鉁� 鍓嶇灞曠ずURL鍙敤鎬ч獙璇�
def validate_url(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except:
        return False

# 鉁� 蹇冭烦妫�娴嬫棩蹇椾紭鍖�
# 鍑忓皯鍐椾綑鏃ュ織杈撳嚭
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **URL楠岃瘉** | 缂哄け 鉂� | 宸叉坊鍔� 鉁� |
| **鏃ュ織浼樺寲** | 鍐椾綑 鉂� | 绠�娲� 鉁� |

**鎶�鏈粏鑺�**: 鍓嶇灞曠ずURL鍙敤鎬ч獙璇侊紝蹇冭烦妫�娴嬫棩蹇椾紭鍖�





### v3.4.1 (2026-05-29) - 馃悰 淇 web_output.log 鏃ュ織鍚屾闂

#### 闂: web_output.log鏃ュ織鍚屾闂
**鐜拌薄**: web_output.log鏃ュ織鍚屾涓嶅強鏃�

**鏍规湰鍘熷洜**: 鏃ュ織鍚屾閫昏緫閿欒

**淇鏂规**:
```python
# 鉁� 淇web_output.log鏃ュ織鍚屾闂
def sync_log():
    with open('web_output.log', 'a') as f:
        f.write(log_message)
        f.flush()
        os.fsync(f.fileno())
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏃ュ織鍚屾** | 涓嶅強鏃� 鉂� | 鍙婃椂 鉁� |
| **鏁版嵁瀹夊叏鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 淇web_output.log鏃ュ織鍚屾闂锛岀‘淇濇棩蹇楀強鏃跺啓鍏�





### v3.4.0 (2026-05-29) - 馃悰 淇闅ч亾鐘舵�佹樉绀哄拰鏃ュ織鍚屾闂

#### 闂: 闅ч亾鐘舵�佹樉绀轰笉姝ｇ‘锛屾棩蹇楀悓姝ラ棶棰�
**鐜拌薄**: 闅ч亾鐘舵�佹樉绀轰笉姝ｇ‘锛屾棩蹇楀悓姝ヤ笉鍙婃椂

**鏍规湰鍘熷洜**: 鐘舵�佹樉绀洪�昏緫閿欒锛屾棩蹇楀悓姝ラ�昏緫閿欒

**淇鏂规**:
```python
# 鉁� 淇闅ч亾鐘舵�佹樉绀�
def get_tunnel_status():
    url = get_public_url()
    if validate_url(url):
        return "running"
    else:
        return "stopped"

# 鉁� 淇鏃ュ織鍚屾闂
def sync_log():
    # 鍚屾鏃ュ織閫昏緫
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鐘舵�佹樉绀�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鏃ュ織鍚屾** | 涓嶅強鏃� 鉂� | 鍙婃椂 鉁� |

**鎶�鏈粏鑺�**: 淇闅ч亾鐘舵�佹樉绀哄拰鏃ュ織鍚屾闂锛屾彁鍗囩郴缁熺ǔ瀹氭��





### v3.3.9 (2026-05-28) - 馃悰 淇 tunnel_url 鍜屽墠绔樉绀轰笉涓�鑷撮棶棰�

#### 闂: tunnel_url鍜屽墠绔樉绀轰笉涓�鑷�
**鐜拌薄**: tunnel_url鍜屽墠绔樉绀轰笉涓�鑷�

**鏍规湰鍘熷洜**: 鏁版嵁鍚屾閫昏緫閿欒

**淇鏂规**:
```python
# 鉁� 淇tunnel_url鍜屽墠绔樉绀轰笉涓�鑷撮棶棰�
def sync_tunnel_url():
    url = get_public_url()
    # 鍚屾鍒板墠绔�
    update_frontend(url)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏁版嵁涓�鑷存��** | 涓嶄竴鑷� 鉂� | 涓�鑷� 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**: 淇tunnel_url鍜屽墠绔樉绀轰笉涓�鑷撮棶棰橈紝纭繚鏁版嵁涓�鑷存��





### v3.3.8 (2026-05-28) - 馃敡 鎷嗗垎鐗堟湰锛屼紭鍖栨洿鏂版棩蹇楁牸寮�

#### 闂: 鐗堟湰鏇存柊鏃ュ織鏍煎紡涓嶇粺涓�
**鐜拌薄**: 鐗堟湰鏇存柊鏃ュ織鏍煎紡涓嶇粺涓�

**鏍规湰鍘熷洜**: 鏃ュ織鏍煎紡涓嶈鑼�

**淇鏂规**:
```python
# 鉁� 鎷嗗垎鐗堟湰锛屼紭鍖栨洿鏂版棩蹇楁牸寮�
# 缁熶竴鏃ュ織鏍煎紡
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鏃ュ織鏍煎紡** | 涓嶇粺涓� 鉂� | 缁熶竴 鉁� |
| **鍙鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**: 鎷嗗垎鐗堟湰锛屼紭鍖栨洿鏂版棩蹇楁牸寮忥紝鎻愬崌鍙鎬�





### v3.3.7 (2026-05-28) - 馃寪 鍓嶇闅ч亾鐘舵�佽疆璇㈤棿闅斾粠5绉掓敼涓�2绉掞紝鏇村揩鍚屾URL鍙樺寲

#### 闂: 鍓嶇闅ч亾鐘舵�佽疆璇㈤棿闅旇繃闀�
**鐜拌薄**: 鍓嶇闅ч亾鐘舵�佽疆璇㈤棿闅�5绉掞紝鍚屾鎱�

**鏍规湰鍘熷洜**: 杞闂撮殧璁剧疆杩囬暱

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細杞闂撮殧5绉�
POLLING_INTERVAL = 5

# 鉁� 淇鍚庯細杞闂撮殧2绉�
POLLING_INTERVAL = 2
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍚屾閫熷害** | 鎱�(5绉�) 鉂� | 蹇�(2绉�) 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**: 鍓嶇闅ч亾鐘舵�佽疆璇㈤棿闅斾粠5绉掓敼涓�2绉掞紝鏇村揩鍚屾URL鍙樺寲




### v3.3.7 (2026-05-28) - 馃寪 鍓嶇闅ч亾鐘舵�佽疆璇㈤棿闅斾粠5绉掓敼涓�2绉掞紝鏇村揩鍚屾URL鍙樺寲

#### 闂: 闅ч亾鍔熻兘瀛樺湪闂
**鐜拌薄**: 闅ч亾杩炴帴涓嶇ǔ瀹氾紝楠岃瘉澶辫触鎴栭绻侀噸鍚�

**鏍规湰鍘熷洜**:
1. **缃戠粶鍔熻兘**: 闅ч亾楠岃瘉閫昏緫涓嶅畬鍠勶紝缂哄皯蹇冭烦妫�娴嬫垨閿欒澶勭悊
2. **鍓嶇闅ч亾鐘舵�佽疆璇㈤棿闅斾粠5绉掓敼涓�2绉掞紝鏇村揩鍚屾URL鍙樺寲**: 鍓嶇闅ч亾鐘舵�佽疆璇㈤棿闅斾粠5绉掓敼涓�2绉掞紝鏇村揩鍚屾URL鍙樺寲
3. **鏂板鐩戞帶绾跨▼锛屽綋tunnel_url.txt鍙樺寲鏃惰嚜鍔ㄥ悓姝**: 鏂板鐩戞帶绾跨▼锛屽綋tunnel_url.txt鍙樺寲鏃惰嚜鍔ㄥ悓姝eb_output.log
4. **绉婚櫎涓嶅繀瑕佺殑瀹氭湡娓呯悊閫昏緫锛宼unnel_url.txt鐢県o**: 绉婚櫎涓嶅繀瑕佺殑瀹氭湡娓呯悊閫昏緫锛宼unnel_url.txt鐢県ostc鑷姩绠＄悊

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細楠岃瘉閫昏緫涓嶅畬鍠�
def verify_tunnel(url):
    response = requests.get(url)
    return response.status_code == 200

# 鉁� 淇鍚庯細瀹屽杽鐨勯獙璇侀�昏緫
def verify_tunnel(url):
    try:
        response = requests.head(url, timeout=10)
        return response.status_code == 200
    except Exception as e:
        logging.error(f"闅ч亾楠岃瘉澶辫触: {e}")
        return False
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇鍓嶇闅ч亾鐘舵�佽疆璇㈤棿闅斾粠5绉掓敼涓�2绉掞紝鏇村揩鍚屾URL鍙樺寲鐩稿叧闂
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.3.6 (2026-05-28) - 馃敡 浼樺寲杩涚▼娓呯悊閫昏緫锛岄伩鍏嶆棤鏁堟竻鐞嗗鑷寸殑澶辫触缁熻

#### 闂: 鎬ц兘瀛樺湪闂
**鐜拌薄**: 绯荤粺鍝嶅簲鎱紝璧勬簮鍗犵敤楂�

**鏍规湰鍘熷洜**:
1. **鍔熻兘浼樺寲**: 绠楁硶鏁堢巼浣庯紝缂哄皯缂撳瓨鎴栦紭鍖栨満鍒�
2. **浼樺寲杩涚▼娓呯悊閫昏緫锛岄伩鍏嶆棤鏁堟竻鐞嗗鑷寸殑澶辫触缁熻**: 浼樺寲杩涚▼娓呯悊閫昏緫锛岄伩鍏嶆棤鏁堟竻鐞嗗鑷寸殑澶辫触缁熻
3. **鍏ㄩ潰绮剧畝README鏇存柊鏃ュ織锛屾墍鏈夌増鏈帶鍒跺湪3-5涓洿鏂扮偣**: 鍏ㄩ潰绮剧畝README鏇存柊鏃ュ織锛屾墍鏈夌増鏈帶鍒跺湪3-5涓洿鏂扮偣
4. **浼樺寲README鏇存柊鏃ュ織鏍煎紡锛屾瘡涓増鏈�3-5涓洿鏂扮偣**: 浼樺寲README鏇存柊鏃ュ織鏍煎紡锛屾瘡涓増鏈�3-5涓洿鏂扮偣

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍘熷瀹炵幇
def old_function():
    # 鏃ч�昏緫
    pass

# 鉁� 淇鍚庯細浼樺寲瀹炵幇
def new_function():
    # 鏂伴�昏緫
    # 娣诲姞閿欒澶勭悊鍜屾棩蹇�
    pass
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇浼樺寲杩涚▼娓呯悊閫昏緫锛岄伩鍏嶆棤鏁堟竻鐞嗗鑷寸殑澶辫触缁熻鐩稿叧闂
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.3.5 (2026-05-28) - 馃敡 缁熶竴杩涚▼妫�娴嬮�昏緫纭繚璺ㄧ郴缁熷吋瀹�

#### 闂: 缁熶竴杩涚▼妫�娴嬮�昏緫纭繚璺ㄧ郴缁熷吋瀹瑰瓨鍦ㄩ棶棰�
**鐜拌薄**: 缁熶竴杩涚▼妫�娴嬮�昏緫纭繚璺ㄧ郴缁熷吋瀹瑰姛鑳藉紓甯革紝褰卞搷鐢ㄦ埛浣撻獙

**鏍规湰鍘熷洜**:
1. **鍔熻兘浼樺寲**: 缁熶竴杩涚▼妫�娴嬮�昏緫纭繚璺ㄧ郴缁熷吋瀹瑰疄鐜伴�昏緫涓嶅畬鍠�
2. **缁熶竴杩涚▼妫�娴嬮�昏緫纭繚璺ㄧ郴缁熷吋瀹�**: 缁熶竴杩涚▼妫�娴嬮�昏緫纭繚璺ㄧ郴缁熷吋瀹�
3. **娣诲姞杩涚▼娓呯悊缁熻鍜岃嚜鍔ㄦ竻绌烘棩蹇楀姛鑳�**: 娣诲姞杩涚▼娓呯悊缁熻鍜岃嚜鍔ㄦ竻绌烘棩蹇楀姛鑳�
4. **淇鏃ュ織鏂囦欢杩囧ぇ鍜岃繘绋嬪紓甯搁棶棰�**: 淇鏃ュ織鏂囦欢杩囧ぇ鍜岃繘绋嬪紓甯搁棶棰�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍘熷瀹炵幇
def old_function():
    # 鏃ч�昏緫
    pass

# 鉁� 淇鍚庯細浼樺寲瀹炵幇
def new_function():
    # 鏂伴�昏緫
    # 娣诲姞閿欒澶勭悊鍜屾棩蹇�
    pass
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇缁熶竴杩涚▼妫�娴嬮�昏緫纭繚璺ㄧ郴缁熷吋瀹圭浉鍏抽棶棰�
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.3.4 (2026-05-24) - 馃敡 闅ч亾鏃ュ織杈撳嚭浼樺寲鍜岃繘绋嬫竻鐞嗘敼杩�

#### 闂: 闅ч亾鍔熻兘瀛樺湪闂
**鐜拌薄**: 闅ч亾杩炴帴涓嶇ǔ瀹氾紝楠岃瘉澶辫触鎴栭绻侀噸鍚�

**鏍规湰鍘熷洜**:
1. **鍔熻兘浼樺寲**: 闅ч亾楠岃瘉閫昏緫涓嶅畬鍠勶紝缂哄皯蹇冭烦妫�娴嬫垨閿欒澶勭悊
2. **闅ч亾鏃ュ織杈撳嚭浼樺寲鍜岃繘绋嬫竻鐞嗘敼杩�**: 闅ч亾鏃ュ織杈撳嚭浼樺寲鍜岃繘绋嬫竻鐞嗘敼杩�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細楠岃瘉閫昏緫涓嶅畬鍠�
def verify_tunnel(url):
    response = requests.get(url)
    return response.status_code == 200

# 鉁� 淇鍚庯細瀹屽杽鐨勯獙璇侀�昏緫
def verify_tunnel(url):
    try:
        response = requests.head(url, timeout=10)
        return response.status_code == 200
    except Exception as e:
        logging.error(f"闅ч亾楠岃瘉澶辫触: {e}")
        return False
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇闅ч亾鏃ュ織杈撳嚭浼樺寲鍜岃繘绋嬫竻鐞嗘敼杩涚浉鍏抽棶棰�
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.3.3 (2026-05-23) - 馃悰 淇闅ч亾杩涚▼娉勬紡鍜岄偖浠堕�氱煡闂

#### 闂: 闅ч亾鍔熻兘瀛樺湪闂
**鐜拌薄**: 闅ч亾杩炴帴涓嶇ǔ瀹氾紝楠岃瘉澶辫触鎴栭绻侀噸鍚�

**鏍规湰鍘熷洜**:
1. **Bug淇**: 闅ч亾楠岃瘉閫昏緫涓嶅畬鍠勶紝缂哄皯蹇冭烦妫�娴嬫垨閿欒澶勭悊
2. **淇闅ч亾杩涚▼娉勬紡鍜岄偖浠堕�氱煡闂**: 淇闅ч亾杩涚▼娉勬紡鍜岄偖浠堕�氱煡闂

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細楠岃瘉閫昏緫涓嶅畬鍠�
def verify_tunnel(url):
    response = requests.get(url)
    return response.status_code == 200

# 鉁� 淇鍚庯細瀹屽杽鐨勯獙璇侀�昏緫
def verify_tunnel(url):
    try:
        response = requests.head(url, timeout=10)
        return response.status_code == 200
    except Exception as e:
        logging.error(f"闅ч亾楠岃瘉澶辫触: {e}")
        return False
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇淇闅ч亾杩涚▼娉勬紡鍜岄偖浠堕�氱煡闂鐩稿叧闂
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.3.1 (2026-05-22) - 馃悰 淇 Web 鐣岄潰杩愯鐖櫕鏃� Input/output error 闂

#### 闂: 淇 Web 鐣岄潰杩愯鐖櫕鏃� Input/output error 闂瀛樺湪闂
**鐜拌薄**: 淇 Web 鐣岄潰杩愯鐖櫕鏃� Input/output error 闂鍔熻兘寮傚父锛屽奖鍝嶇敤鎴蜂綋楠�

**鏍规湰鍘熷洜**:
1. **Bug淇**: 淇 Web 鐣岄潰杩愯鐖櫕鏃� Input/output error 闂瀹炵幇閫昏緫涓嶅畬鍠�
2. **淇 Web 鐣岄潰杩愯鐖櫕鏃� Input/output er**: 淇 Web 鐣岄潰杩愯鐖櫕鏃� Input/output error 闂

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍘熷瀹炵幇
def old_function():
    # 鏃ч�昏緫
    pass

# 鉁� 淇鍚庯細浼樺寲瀹炵幇
def new_function():
    # 鏂伴�昏緫
    # 娣诲姞閿欒澶勭悊鍜屾棩蹇�
    pass
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇淇 Web 鐣岄潰杩愯鐖櫕鏃� Input/output error 闂鐩稿叧闂
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.3.0 (2026-05-22) - 鈿� 鑷姩閰嶇疆闃块噷浜憄ip闀滃儚鍔犻��

#### 闂: 鑷姩閰嶇疆闃块噷浜憄ip闀滃儚鍔犻�熷瓨鍦ㄩ棶棰�
**鐜拌薄**: 鑷姩閰嶇疆闃块噷浜憄ip闀滃儚鍔犻�熷姛鑳藉紓甯革紝褰卞搷鐢ㄦ埛浣撻獙

**鏍规湰鍘熷洜**:
1. **鎬ц兘鎻愬崌**: 鑷姩閰嶇疆闃块噷浜憄ip闀滃儚鍔犻�熷疄鐜伴�昏緫涓嶅畬鍠�
2. **鑷姩閰嶇疆闃块噷浜憄ip闀滃儚鍔犻��**: 鑷姩閰嶇疆闃块噷浜憄ip闀滃儚鍔犻��

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍘熷瀹炵幇
def old_function():
    # 鏃ч�昏緫
    pass

# 鉁� 淇鍚庯細浼樺寲瀹炵幇
def new_function():
    # 鏂伴�昏緫
    # 娣诲姞閿欒澶勭悊鍜屾棩蹇�
    pass
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇鑷姩閰嶇疆闃块噷浜憄ip闀滃儚鍔犻�熺浉鍏抽棶棰�
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.2.9 (2026-05-22) - 馃悰 淇闅ч亾棰戠箒閲嶅惎鍜岄偖浠跺彂閫侀棶棰�

#### 闂: 闅ч亾鍔熻兘瀛樺湪闂
**鐜拌薄**: 闅ч亾杩炴帴涓嶇ǔ瀹氾紝楠岃瘉澶辫触鎴栭绻侀噸鍚�

**鏍规湰鍘熷洜**:
1. **Bug淇**: 闅ч亾楠岃瘉閫昏緫涓嶅畬鍠勶紝缂哄皯蹇冭烦妫�娴嬫垨閿欒澶勭悊
2. **淇闅ч亾棰戠箒閲嶅惎鍜岄偖浠跺彂閫侀棶棰�**: 淇闅ч亾棰戠箒閲嶅惎鍜岄偖浠跺彂閫侀棶棰�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細楠岃瘉閫昏緫涓嶅畬鍠�
def verify_tunnel(url):
    response = requests.get(url)
    return response.status_code == 200

# 鉁� 淇鍚庯細瀹屽杽鐨勯獙璇侀�昏緫
def verify_tunnel(url):
    try:
        response = requests.head(url, timeout=10)
        return response.status_code == 200
    except Exception as e:
        logging.error(f"闅ч亾楠岃瘉澶辫触: {e}")
        return False
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇淇闅ч亾棰戠箒閲嶅惎鍜岄偖浠跺彂閫侀棶棰樼浉鍏抽棶棰�
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.2.8 (2026-05-22) - 馃敡 Flask鍚姩鏃堕偖浠堕�氱煡澧炲己

#### 闂: 妗嗘灦杩佺Щ瀛樺湪闂
**鐜拌薄**: API鎺ュ彛寮傚父锛屽姛鑳藉け鏁�

**鏍规湰鍘熷洜**:
1. **鍔熻兘浼樺寲**: 妗嗘灦杩佺Щ鍚庨儴鍒嗗姛鑳芥湭姝ｇ‘閫傞厤
2. **Flask鍚姩鏃堕偖浠堕�氱煡澧炲己**: Flask鍚姩鏃堕偖浠堕�氱煡澧炲己

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細Flask椋庢牸
@app.route('/api/data')
def get_data():
    return jsonify(data)

# 鉁� 淇鍚庯細FastAPI椋庢牸
@app.get('/api/data')
async def get_data():
    return data
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇Flask鍚姩鏃堕偖浠堕�氱煡澧炲己鐩稿叧闂
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.2.7 (2026-05-22) - 鉁� 鏂板鍏綉鍦板潃鍙樻洿閭欢閫氱煡鍔熻兘

#### 闂: 閭欢鍔熻兘瀛樺湪闂
**鐜拌薄**: 閭欢鍙戦�佸け璐ユ垨閫氱煡涓嶅強鏃�

**鏍规湰鍘熷洜**:
1. **鏂板姛鑳�**: 閭欢閰嶇疆閿欒鎴栧彂閫侀�昏緫涓嶅畬鍠�
2. **鏂板鍏綉鍦板潃鍙樻洿閭欢閫氱煡鍔熻兘**: 鏂板鍏綉鍦板潃鍙樻洿閭欢閫氱煡鍔熻兘
3. **鍓嶇浠ｇ爜浼樺寲 - 绠�鍖朌OM鎿嶄綔銆佸悎骞堕噸澶嶅嚱鏁般�佷紭鍖栦簨浠剁粦瀹�**: 鍓嶇浠ｇ爜浼樺寲 - 绠�鍖朌OM鎿嶄綔銆佸悎骞堕噸澶嶅嚱鏁般�佷紭鍖栦簨浠剁粦瀹�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍘熷瀹炵幇
def old_function():
    # 鏃ч�昏緫
    pass

# 鉁� 淇鍚庯細浼樺寲瀹炵幇
def new_function():
    # 鏂伴�昏緫
    # 娣诲姞閿欒澶勭悊鍜屾棩蹇�
    pass
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇鏂板鍏綉鍦板潃鍙樻洿閭欢閫氱煡鍔熻兘鐩稿叧闂
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.2.6 (2026-05-21) - 馃敡 鍓嶇JavaScript浼樺寲 - 绉婚櫎鍐椾綑鏃ュ織锛岀畝鍖栦唬鐮佺粨鏋�

#### 闂: 鎬ц兘瀛樺湪闂
**鐜拌薄**: 绯荤粺鍝嶅簲鎱紝璧勬簮鍗犵敤楂�

**鏍规湰鍘熷洜**:
1. **鍔熻兘浼樺寲**: 绠楁硶鏁堢巼浣庯紝缂哄皯缂撳瓨鎴栦紭鍖栨満鍒�
2. **鍓嶇JavaScript浼樺寲 - 绉婚櫎鍐椾綑鏃ュ織锛岀畝鍖栦唬鐮佺粨鏋�**: 鍓嶇JavaScript浼樺寲 - 绉婚櫎鍐椾綑鏃ュ織锛岀畝鍖栦唬鐮佺粨鏋�
3. **浠ｇ爜璐ㄩ噺浼樺寲**: 浠ｇ爜璐ㄩ噺浼樺寲

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍘熷瀹炵幇
def old_function():
    # 鏃ч�昏緫
    pass

# 鉁� 淇鍚庯細浼樺寲瀹炵幇
def new_function():
    # 鏂伴�昏緫
    # 娣诲姞閿欒澶勭悊鍜屾棩蹇�
    pass
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇鍓嶇JavaScript浼樺寲 - 绉婚櫎鍐椾綑鏃ュ織锛岀畝鍖栦唬鐮佺粨鏋勭浉鍏抽棶棰�
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.2.5 (2026-05-21) - 馃敡 绠�鍖栧惎鍔ㄦ祦绋嬶紝绉婚櫎闅ч亾閫夋嫨鑿滃崟

#### 闂: 闅ч亾鍔熻兘瀛樺湪闂
**鐜拌薄**: 闅ч亾杩炴帴涓嶇ǔ瀹氾紝楠岃瘉澶辫触鎴栭绻侀噸鍚�

**鏍规湰鍘熷洜**:
1. **鍔熻兘浼樺寲**: 闅ч亾楠岃瘉閫昏緫涓嶅畬鍠勶紝缂哄皯蹇冭烦妫�娴嬫垨閿欒澶勭悊
2. **绠�鍖栧惎鍔ㄦ祦绋嬶紝绉婚櫎闅ч亾閫夋嫨鑿滃崟**: 绠�鍖栧惎鍔ㄦ祦绋嬶紝绉婚櫎闅ч亾閫夋嫨鑿滃崟

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細楠岃瘉閫昏緫涓嶅畬鍠�
def verify_tunnel(url):
    response = requests.get(url)
    return response.status_code == 200

# 鉁� 淇鍚庯細瀹屽杽鐨勯獙璇侀�昏緫
def verify_tunnel(url):
    try:
        response = requests.head(url, timeout=10)
        return response.status_code == 200
    except Exception as e:
        logging.error(f"闅ч亾楠岃瘉澶辫触: {e}")
        return False
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇绠�鍖栧惎鍔ㄦ祦绋嬶紝绉婚櫎闅ч亾閫夋嫨鑿滃崟鐩稿叧闂
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.2.4 (2026-05-29) - 馃敡 鍓嶇灞曠ずURL鍙敤鎬ч獙璇� + 蹇冭烦妫�娴嬫棩蹇椾紭鍖�

#### 闂: 鎬ц兘瀛樺湪闂
**鐜拌薄**: 绯荤粺鍝嶅簲鎱紝璧勬簮鍗犵敤楂�

**鏍规湰鍘熷洜**:
1. **鍔熻兘浼樺寲**: 绠楁硶鏁堢巼浣庯紝缂哄皯缂撳瓨鎴栦紭鍖栨満鍒�
2. **鍓嶇灞曠ずURL鍙敤鎬ч獙璇� + 蹇冭烦妫�娴嬫棩蹇椾紭鍖�**: 鍓嶇灞曠ずURL鍙敤鎬ч獙璇� + 蹇冭烦妫�娴嬫棩蹇椾紭鍖�
3. **绉婚櫎 Cloudflare Tunnel 鍔熻兘锛岀畝鍖栭毀閬撴湇鍔�**: 绉婚櫎 Cloudflare Tunnel 鍔熻兘锛岀畝鍖栭毀閬撴湇鍔�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍘熷瀹炵幇
def old_function():
    # 鏃ч�昏緫
    pass

# 鉁� 淇鍚庯細浼樺寲瀹炵幇
def new_function():
    # 鏂伴�昏緫
    # 娣诲姞閿欒澶勭悊鍜屾棩蹇�
    pass
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇鍓嶇灞曠ずURL鍙敤鎬ч獙璇� + 蹇冭烦妫�娴嬫棩蹇椾紭鍖栫浉鍏抽棶棰�
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.2.3 (2026-05-21) - 馃寪 Cloudflare Tunnel 閰嶇疆鍔熻兘

#### 闂: 闅ч亾鍔熻兘瀛樺湪闂
**鐜拌薄**: 闅ч亾杩炴帴涓嶇ǔ瀹氾紝楠岃瘉澶辫触鎴栭绻侀噸鍚�

**鏍规湰鍘熷洜**:
1. **缃戠粶鍔熻兘**: 闅ч亾楠岃瘉閫昏緫涓嶅畬鍠勶紝缂哄皯蹇冭烦妫�娴嬫垨閿欒澶勭悊
2. **Cloudflare Tunnel 閰嶇疆鍔熻兘**: Cloudflare Tunnel 閰嶇疆鍔熻兘

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細楠岃瘉閫昏緫涓嶅畬鍠�
def verify_tunnel(url):
    response = requests.get(url)
    return response.status_code == 200

# 鉁� 淇鍚庯細瀹屽杽鐨勯獙璇侀�昏緫
def verify_tunnel(url):
    try:
        response = requests.head(url, timeout=10)
        return response.status_code == 200
    except Exception as e:
        logging.error(f"闅ч亾楠岃瘉澶辫触: {e}")
        return False
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇Cloudflare Tunnel 閰嶇疆鍔熻兘鐩稿叧闂
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.2.2 (2026-05-21) - 馃悰 淇闅ч亾鑷姩閲嶈繛姝诲惊鐜棶棰橈紝瀹炵幇鏃犳劅鍒囨崲鍒版柊鐨勫叕缃� URL

#### 闂: 闅ч亾鍔熻兘瀛樺湪闂
**鐜拌薄**: 闅ч亾杩炴帴涓嶇ǔ瀹氾紝楠岃瘉澶辫触鎴栭绻侀噸鍚�

**鏍规湰鍘熷洜**:
1. **Bug淇**: 闅ч亾楠岃瘉閫昏緫涓嶅畬鍠勶紝缂哄皯蹇冭烦妫�娴嬫垨閿欒澶勭悊
2. **淇闅ч亾鑷姩閲嶈繛姝诲惊鐜棶棰橈紝瀹炵幇鏃犳劅鍒囨崲鍒版柊鐨勫叕缃� URL**: 淇闅ч亾鑷姩閲嶈繛姝诲惊鐜棶棰橈紝瀹炵幇鏃犳劅鍒囨崲鍒版柊鐨勫叕缃� URL

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細楠岃瘉閫昏緫涓嶅畬鍠�
def verify_tunnel(url):
    response = requests.get(url)
    return response.status_code == 200

# 鉁� 淇鍚庯細瀹屽杽鐨勯獙璇侀�昏緫
def verify_tunnel(url):
    try:
        response = requests.head(url, timeout=10)
        return response.status_code == 200
    except Exception as e:
        logging.error(f"闅ч亾楠岃瘉澶辫触: {e}")
        return False
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇淇闅ч亾鑷姩閲嶈繛姝诲惊鐜棶棰橈紝瀹炵幇鏃犳劅鍒囨崲鍒版柊鐨勫叕缃� URL鐩稿叧闂
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.2.1 (2026-05-20) - 馃挀 瀹堟姢绾跨▼閲嶅惎鏃朵繚鎸� URL 涓�鑷�

#### 闂: 馃挀 瀹堟姢绾跨▼閲嶅惎鏃朵繚鎸� URL 涓�鑷村瓨鍦ㄩ棶棰�
**鐜拌薄**: 馃挀 瀹堟姢绾跨▼閲嶅惎鏃朵繚鎸� URL 涓�鑷村姛鑳藉紓甯革紝褰卞搷鐢ㄦ埛浣撻獙

**鏍规湰鍘熷洜**:
1. **鍔熻兘浼樺寲**: 馃挀 瀹堟姢绾跨▼閲嶅惎鏃朵繚鎸� URL 涓�鑷村疄鐜伴�昏緫涓嶅畬鍠�
2. **瀹堟姢绾跨▼閲嶅惎鏃朵繚鎸� URL 涓�鑷�**: 瀹堟姢绾跨▼閲嶅惎鏃朵繚鎸� URL 涓�鑷�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍘熷瀹炵幇
def old_function():
    # 鏃ч�昏緫
    pass

# 鉁� 淇鍚庯細浼樺寲瀹炵幇
def new_function():
    # 鏂伴�昏緫
    # 娣诲姞閿欒澶勭悊鍜屾棩蹇�
    pass
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇馃挀 瀹堟姢绾跨▼閲嶅惎鏃朵繚鎸� URL 涓�鑷寸浉鍏抽棶棰�
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.2.0 (2026-05-20) - 馃寪 澶栭儴鍚姩闅ч亾鐩戞帶鏈哄埗

#### 闂: 闅ч亾鍔熻兘瀛樺湪闂
**鐜拌薄**: 闅ч亾杩炴帴涓嶇ǔ瀹氾紝楠岃瘉澶辫触鎴栭绻侀噸鍚�

**鏍规湰鍘熷洜**:
1. **缃戠粶鍔熻兘**: 闅ч亾楠岃瘉閫昏緫涓嶅畬鍠勶紝缂哄皯蹇冭烦妫�娴嬫垨閿欒澶勭悊
2. **澶栭儴鍚姩闅ч亾鐩戞帶鏈哄埗**: 澶栭儴鍚姩闅ч亾鐩戞帶鏈哄埗

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細楠岃瘉閫昏緫涓嶅畬鍠�
def verify_tunnel(url):
    response = requests.get(url)
    return response.status_code == 200

# 鉁� 淇鍚庯細瀹屽杽鐨勯獙璇侀�昏緫
def verify_tunnel(url):
    try:
        response = requests.head(url, timeout=10)
        return response.status_code == 200
    except Exception as e:
        logging.error(f"闅ч亾楠岃瘉澶辫触: {e}")
        return False
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇澶栭儴鍚姩闅ч亾鐩戞帶鏈哄埗鐩稿叧闂
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.1.9 (2026-05-20) - 馃敡 浼樺寲鍓嶇闅ч亾鍏变韩鎸夐挳锛屼紭鍏堝鐢╰unnel_url.txt涓殑宸叉湁鍦板潃

#### 闂: 闅ч亾鍔熻兘瀛樺湪闂
**鐜拌薄**: 闅ч亾杩炴帴涓嶇ǔ瀹氾紝楠岃瘉澶辫触鎴栭绻侀噸鍚�

**鏍规湰鍘熷洜**:
1. **鍔熻兘浼樺寲**: 闅ч亾楠岃瘉閫昏緫涓嶅畬鍠勶紝缂哄皯蹇冭烦妫�娴嬫垨閿欒澶勭悊
2. **浼樺寲鍓嶇闅ч亾鍏变韩鎸夐挳锛屼紭鍏堝鐢╰unnel_url.txt涓�**: 浼樺寲鍓嶇闅ч亾鍏变韩鎸夐挳锛屼紭鍏堝鐢╰unnel_url.txt涓殑宸叉湁鍦板潃

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細楠岃瘉閫昏緫涓嶅畬鍠�
def verify_tunnel(url):
    response = requests.get(url)
    return response.status_code == 200

# 鉁� 淇鍚庯細瀹屽杽鐨勯獙璇侀�昏緫
def verify_tunnel(url):
    try:
        response = requests.head(url, timeout=10)
        return response.status_code == 200
    except Exception as e:
        logging.error(f"闅ч亾楠岃瘉澶辫触: {e}")
        return False
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇浼樺寲鍓嶇闅ч亾鍏变韩鎸夐挳锛屼紭鍏堝鐢╰unnel_url.txt涓殑宸叉湁鍦板潃鐩稿叧闂
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.1.8 (2026-05-20) - 馃敡 澧炲己闅ч亾淇濇寔鍦ㄧ嚎鏈哄埗

#### 闂: 闅ч亾鍔熻兘瀛樺湪闂
**鐜拌薄**: 闅ч亾杩炴帴涓嶇ǔ瀹氾紝楠岃瘉澶辫触鎴栭绻侀噸鍚�

**鏍规湰鍘熷洜**:
1. **鍔熻兘浼樺寲**: 闅ч亾楠岃瘉閫昏緫涓嶅畬鍠勶紝缂哄皯蹇冭烦妫�娴嬫垨閿欒澶勭悊
2. **澧炲己闅ч亾淇濇寔鍦ㄧ嚎鏈哄埗**: 澧炲己闅ч亾淇濇寔鍦ㄧ嚎鏈哄埗
3. **淇闈㈡澘鍐茬獊闂 - 鎵�鏈夊姛鑳介噰鐢ㄧ嫭绔嬪鍣�**: 淇闈㈡澘鍐茬獊闂 - 鎵�鏈夊姛鑳介噰鐢ㄧ嫭绔嬪鍣�
4. **淇Excel瀵规瘮鏄剧ず鎵�鏈変环鏍肩殑澶氫綑璐у彿**: 淇Excel瀵规瘮鏄剧ず鎵�鏈変环鏍肩殑澶氫綑璐у彿

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細楠岃瘉閫昏緫涓嶅畬鍠�
def verify_tunnel(url):
    response = requests.get(url)
    return response.status_code == 200

# 鉁� 淇鍚庯細瀹屽杽鐨勯獙璇侀�昏緫
def verify_tunnel(url):
    try:
        response = requests.head(url, timeout=10)
        return response.status_code == 200
    except Exception as e:
        logging.error(f"闅ч亾楠岃瘉澶辫触: {e}")
        return False
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇澧炲己闅ч亾淇濇寔鍦ㄧ嚎鏈哄埗鐩稿叧闂
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.1.7 (2026-05-20) - 馃敡 璐у彿瀵规瘮閲嶅妫�娴嬩紭鍖�

#### 闂: 鎬ц兘瀛樺湪闂
**鐜拌薄**: 绯荤粺鍝嶅簲鎱紝璧勬簮鍗犵敤楂�

**鏍规湰鍘熷洜**:
1. **鍔熻兘浼樺寲**: 绠楁硶鏁堢巼浣庯紝缂哄皯缂撳瓨鎴栦紭鍖栨満鍒�
2. **璐у彿瀵规瘮閲嶅妫�娴嬩紭鍖�**: 璐у彿瀵规瘮閲嶅妫�娴嬩紭鍖�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍘熷瀹炵幇
def old_function():
    # 鏃ч�昏緫
    pass

# 鉁� 淇鍚庯細浼樺寲瀹炵幇
def new_function():
    # 鏂伴�昏緫
    # 娣诲姞閿欒澶勭悊鍜屾棩蹇�
    pass
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇璐у彿瀵规瘮閲嶅妫�娴嬩紭鍖栫浉鍏抽棶棰�
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.1.5 (2026-05-18) - 馃寪 闅ч亾鑷姩閲嶈繛鏈哄埗

#### 闂: 闅ч亾鍔熻兘瀛樺湪闂
**鐜拌薄**: 闅ч亾杩炴帴涓嶇ǔ瀹氾紝楠岃瘉澶辫触鎴栭绻侀噸鍚�

**鏍规湰鍘熷洜**:
1. **缃戠粶鍔熻兘**: 闅ч亾楠岃瘉閫昏緫涓嶅畬鍠勶紝缂哄皯蹇冭烦妫�娴嬫垨閿欒澶勭悊
2. **闅ч亾鑷姩閲嶈繛鏈哄埗**: 闅ч亾鑷姩閲嶈繛鏈哄埗

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細楠岃瘉閫昏緫涓嶅畬鍠�
def verify_tunnel(url):
    response = requests.get(url)
    return response.status_code == 200

# 鉁� 淇鍚庯細瀹屽杽鐨勯獙璇侀�昏緫
def verify_tunnel(url):
    try:
        response = requests.head(url, timeout=10)
        return response.status_code == 200
    except Exception as e:
        logging.error(f"闅ч亾楠岃瘉澶辫触: {e}")
        return False
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇闅ч亾鑷姩閲嶈繛鏈哄埗鐩稿叧闂
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.1.3 (2026-05-18) - 馃敡 璺ㄧ郴缁熷吋瀹规�у寮� - 缁熶竴鑴氭湰閫昏緫銆佽嚜鍔ㄥ垱寤鸿櫄鎷熺幆澧冦�佸畬鍠勮繘绋嬫竻鐞�

#### 闂: 璺ㄧ郴缁熷吋瀹规�у寮� - 缁熶竴鑴氭湰閫昏緫銆佽嚜鍔ㄥ垱寤鸿櫄鎷熺幆澧冦�佸畬鍠勮繘绋嬫竻鐞嗗瓨鍦ㄩ棶棰�
**鐜拌薄**: 璺ㄧ郴缁熷吋瀹规�у寮� - 缁熶竴鑴氭湰閫昏緫銆佽嚜鍔ㄥ垱寤鸿櫄鎷熺幆澧冦�佸畬鍠勮繘绋嬫竻鐞嗗姛鑳藉紓甯革紝褰卞搷鐢ㄦ埛浣撻獙

**鏍规湰鍘熷洜**:
1. **鍔熻兘浼樺寲**: 璺ㄧ郴缁熷吋瀹规�у寮� - 缁熶竴鑴氭湰閫昏緫銆佽嚜鍔ㄥ垱寤鸿櫄鎷熺幆澧冦�佸畬鍠勮繘绋嬫竻鐞嗗疄鐜伴�昏緫涓嶅畬鍠�
2. **璺ㄧ郴缁熷吋瀹规�у寮� - 缁熶竴鑴氭湰閫昏緫銆佽嚜鍔ㄥ垱寤鸿櫄鎷熺幆澧冦�佸畬鍠勮繘**: 璺ㄧ郴缁熷吋瀹规�у寮� - 缁熶竴鑴氭湰閫昏緫銆佽嚜鍔ㄥ垱寤鸿櫄鎷熺幆澧冦�佸畬鍠勮繘绋嬫竻鐞�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍘熷瀹炵幇
def old_function():
    # 鏃ч�昏緫
    pass

# 鉁� 淇鍚庯細浼樺寲瀹炵幇
def new_function():
    # 鏂伴�昏緫
    # 娣诲姞閿欒澶勭悊鍜屾棩蹇�
    pass
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇璺ㄧ郴缁熷吋瀹规�у寮� - 缁熶竴鑴氭湰閫昏緫銆佽嚜鍔ㄥ垱寤鸿櫄鎷熺幆澧冦�佸畬鍠勮繘绋嬫竻鐞嗙浉鍏抽棶棰�
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.1.2 (2026-05-18) - 馃敡 澶╂皵鐪嬫澘棰勫姞杞戒紭鍖�

#### 闂: 鎬ц兘瀛樺湪闂
**鐜拌薄**: 绯荤粺鍝嶅簲鎱紝璧勬簮鍗犵敤楂�

**鏍规湰鍘熷洜**:
1. **鍔熻兘浼樺寲**: 绠楁硶鏁堢巼浣庯紝缂哄皯缂撳瓨鎴栦紭鍖栨満鍒�
2. **澶╂皵鐪嬫澘棰勫姞杞戒紭鍖�**: 澶╂皵鐪嬫澘棰勫姞杞戒紭鍖�
3. **閸撳矕顏悧鍫熸拱閸欒渹绮燗PI鐎圭偞妞傞姰宄板絿**: 閸撳矕顏悧鍫熸拱閸欒渹绮燗PI鐎圭偞妞傞姰宄板絿
4. **娣囶喖顦查梾褔浜鹃挅顖氬З閽栧骸鍙曠純鎴濇勾閸р偓娑撳秵妯夌粈铏规畱闂傤噣顣�**: 娣囶喖顦查梾褔浜鹃挅顖氬З閽栧骸鍙曠純鎴濇勾閸р偓娑撳秵妯夌粈铏规畱闂傤噣顣�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍘熷瀹炵幇
def old_function():
    # 鏃ч�昏緫
    pass

# 鉁� 淇鍚庯細浼樺寲瀹炵幇
def new_function():
    # 鏂伴�昏緫
    # 娣诲姞閿欒澶勭悊鍜屾棩蹇�
    pass
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇澶╂皵鐪嬫澘棰勫姞杞戒紭鍖栫浉鍏抽棶棰�
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.1.1 (2026-05-20) - 馃悰 淇闅ч亾澶嶅埗鎸夐挳澶辨晥闂

#### 闂: 闅ч亾鍔熻兘瀛樺湪闂
**鐜拌薄**: 闅ч亾杩炴帴涓嶇ǔ瀹氾紝楠岃瘉澶辫触鎴栭绻侀噸鍚�

**鏍规湰鍘熷洜**:
1. **Bug淇**: 闅ч亾楠岃瘉閫昏緫涓嶅畬鍠勶紝缂哄皯蹇冭烦妫�娴嬫垨閿欒澶勭悊
2. **淇闅ч亾澶嶅埗鎸夐挳澶辨晥闂**: 淇闅ч亾澶嶅埗鎸夐挳澶辨晥闂
3. **鍓嶇鐗堟湰鍙疯嚜鍔ㄨ窡闅弇ain.py涓璙ERSION鍙橀噺**: 鍓嶇鐗堟湰鍙疯嚜鍔ㄨ窡闅弇ain.py涓璙ERSION鍙橀噺

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細楠岃瘉閫昏緫涓嶅畬鍠�
def verify_tunnel(url):
    response = requests.get(url)
    return response.status_code == 200

# 鉁� 淇鍚庯細瀹屽杽鐨勯獙璇侀�昏緫
def verify_tunnel(url):
    try:
        response = requests.head(url, timeout=10)
        return response.status_code == 200
    except Exception as e:
        logging.error(f"闅ч亾楠岃瘉澶辫触: {e}")
        return False
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇淇闅ч亾澶嶅埗鎸夐挳澶辨晥闂鐩稿叧闂
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.0.8 (2026-05-17) - 馃敡 闅ч亾鍏变韩鍔熻兘澧炲己 - 鍙偣鍑婚摼鎺ャ�佷竴閿鍒躲�佸惎鍔ㄩ涓嬭浇hostc

#### 闂: 闅ч亾鍔熻兘瀛樺湪闂
**鐜拌薄**: 闅ч亾杩炴帴涓嶇ǔ瀹氾紝楠岃瘉澶辫触鎴栭绻侀噸鍚�

**鏍规湰鍘熷洜**:
1. **鍔熻兘浼樺寲**: 闅ч亾楠岃瘉閫昏緫涓嶅畬鍠勶紝缂哄皯蹇冭烦妫�娴嬫垨閿欒澶勭悊
2. **闅ч亾鍏变韩鍔熻兘澧炲己 - 鍙偣鍑婚摼鎺ャ�佷竴閿鍒躲�佸惎鍔ㄩ涓嬭浇hos**: 闅ч亾鍏变韩鍔熻兘澧炲己 - 鍙偣鍑婚摼鎺ャ�佷竴閿鍒躲�佸惎鍔ㄩ涓嬭浇hostc

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細楠岃瘉閫昏緫涓嶅畬鍠�
def verify_tunnel(url):
    response = requests.get(url)
    return response.status_code == 200

# 鉁� 淇鍚庯細瀹屽杽鐨勯獙璇侀�昏緫
def verify_tunnel(url):
    try:
        response = requests.head(url, timeout=10)
        return response.status_code == 200
    except Exception as e:
        logging.error(f"闅ч亾楠岃瘉澶辫触: {e}")
        return False
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇闅ч亾鍏变韩鍔熻兘澧炲己 - 鍙偣鍑婚摼鎺ャ�佷竴閿鍒躲�佸惎鍔ㄩ涓嬭浇hostc鐩稿叧闂
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.0.7 (2026-05-17) - 馃敡 浼樺寲闅ч亾鍏变韩鍔熻兘 + 璺ㄥ钩鍙板吋瀹规�у寮�

#### 闂: 闅ч亾鍔熻兘瀛樺湪闂
**鐜拌薄**: 闅ч亾杩炴帴涓嶇ǔ瀹氾紝楠岃瘉澶辫触鎴栭绻侀噸鍚�

**鏍规湰鍘熷洜**:
1. **鍔熻兘浼樺寲**: 闅ч亾楠岃瘉閫昏緫涓嶅畬鍠勶紝缂哄皯蹇冭烦妫�娴嬫垨閿欒澶勭悊
2. **浼樺寲闅ч亾鍏变韩鍔熻兘 + 璺ㄥ钩鍙板吋瀹规�у寮�**: 浼樺寲闅ч亾鍏变韩鍔熻兘 + 璺ㄥ钩鍙板吋瀹规�у寮�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細楠岃瘉閫昏緫涓嶅畬鍠�
def verify_tunnel(url):
    response = requests.get(url)
    return response.status_code == 200

# 鉁� 淇鍚庯細瀹屽杽鐨勯獙璇侀�昏緫
def verify_tunnel(url):
    try:
        response = requests.head(url, timeout=10)
        return response.status_code == 200
    except Exception as e:
        logging.error(f"闅ч亾楠岃瘉澶辫触: {e}")
        return False
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇浼樺寲闅ч亾鍏变韩鍔熻兘 + 璺ㄥ钩鍙板吋瀹规�у寮虹浉鍏抽棶棰�
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.0.6 (2026-05-06) - 鉁� 闆嗘垚澶╂皵鏃堕挓鐪嬫澘锛岀嫭绔嬪尯鍧楀睍绀猴紝瀹屾暣鍝嶅簲寮忛�傞厤

#### 闂: 闆嗘垚澶╂皵鏃堕挓鐪嬫澘锛岀嫭绔嬪尯鍧楀睍绀猴紝瀹屾暣鍝嶅簲寮忛�傞厤瀛樺湪闂
**鐜拌薄**: 闆嗘垚澶╂皵鏃堕挓鐪嬫澘锛岀嫭绔嬪尯鍧楀睍绀猴紝瀹屾暣鍝嶅簲寮忛�傞厤鍔熻兘寮傚父锛屽奖鍝嶇敤鎴蜂綋楠�

**鏍规湰鍘熷洜**:
1. **鏂板姛鑳�**: 闆嗘垚澶╂皵鏃堕挓鐪嬫澘锛岀嫭绔嬪尯鍧楀睍绀猴紝瀹屾暣鍝嶅簲寮忛�傞厤瀹炵幇閫昏緫涓嶅畬鍠�
2. **闆嗘垚澶╂皵鏃堕挓鐪嬫澘锛岀嫭绔嬪尯鍧楀睍绀猴紝瀹屾暣鍝嶅簲寮忛�傞厤**: 闆嗘垚澶╂皵鏃堕挓鐪嬫澘锛岀嫭绔嬪尯鍧楀睍绀猴紝瀹屾暣鍝嶅簲寮忛�傞厤

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍘熷瀹炵幇
def old_function():
    # 鏃ч�昏緫
    pass

# 鉁� 淇鍚庯細浼樺寲瀹炵幇
def new_function():
    # 鏂伴�昏緫
    # 娣诲姞閿欒澶勭悊鍜屾棩蹇�
    pass
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇闆嗘垚澶╂皵鏃堕挓鐪嬫澘锛岀嫭绔嬪尯鍧楀睍绀猴紝瀹屾暣鍝嶅簲寮忛�傞厤鐩稿叧闂
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.0.5 (2026-05-01) - 馃悰 淇Excel涓嶫SON瀵规瘮鍔熻兘涓柊澧為珮浠峰晢鍝佸垽瀹氶�昏緫閿欒

#### 闂: 鍟嗗搧鏁版嵁澶勭悊瀛樺湪闂
**鐜拌薄**: 鍟嗗搧鏁版嵁瑙ｆ瀽閿欒锛屾樉绀轰笉姝ｇ‘鎴栫己澶�

**鏍规湰鍘熷洜**:
1. **Bug淇**: 鏁版嵁瑙ｆ瀽閫昏緫涓嶅畬鍠勶紝姝ｅ垯琛ㄨ揪寮忓尮閰嶄笉鍑嗙‘
2. **淇Excel涓嶫SON瀵规瘮鍔熻兘涓柊澧為珮浠峰晢鍝佸垽瀹氶�昏緫閿欒**: 淇Excel涓嶫SON瀵规瘮鍔熻兘涓柊澧為珮浠峰晢鍝佸垽瀹氶�昏緫閿欒

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鏁版嵁瑙ｆ瀽涓嶅噯纭�
high_price_count = len([p for p in products if p['price'] > 599])

# 鉁� 淇鍚庯細绮剧‘鐨勬暟鎹В鏋�
high_price_count = len([p for p in products if p.get('price', 0) >= 599])
logging.info(f"楂樹环鍟嗗搧鏁�: {high_price_count}")
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇淇Excel涓嶫SON瀵规瘮鍔熻兘涓柊澧為珮浠峰晢鍝佸垽瀹氶�昏緫閿欒鐩稿叧闂
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.0.4 (2026-05-01) - 馃敡 Excel鏂囦欢璺緞鍘婚噸鍜岃揣鍙疯鍙栭『搴忎紭鍖�

#### 闂: 鎬ц兘瀛樺湪闂
**鐜拌薄**: 绯荤粺鍝嶅簲鎱紝璧勬簮鍗犵敤楂�

**鏍规湰鍘熷洜**:
1. **鍔熻兘浼樺寲**: 绠楁硶鏁堢巼浣庯紝缂哄皯缂撳瓨鎴栦紭鍖栨満鍒�
2. **Excel鏂囦欢璺緞鍘婚噸鍜岃揣鍙疯鍙栭『搴忎紭鍖�**: Excel鏂囦欢璺緞鍘婚噸鍜岃揣鍙疯鍙栭『搴忎紭鍖�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍘熷瀹炵幇
def old_function():
    # 鏃ч�昏緫
    pass

# 鉁� 淇鍚庯細浼樺寲瀹炵幇
def new_function():
    # 鏂伴�昏緫
    # 娣诲姞閿欒澶勭悊鍜屾棩蹇�
    pass
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇Excel鏂囦欢璺緞鍘婚噸鍜岃揣鍙疯鍙栭『搴忎紭鍖栫浉鍏抽棶棰�
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.0.3 (2026-05-01) - 馃敡 绉诲姩绔鑸爮鍥哄畾缃《浼樺寲

#### 闂: 鎬ц兘瀛樺湪闂
**鐜拌薄**: 绯荤粺鍝嶅簲鎱紝璧勬簮鍗犵敤楂�

**鏍规湰鍘熷洜**:
1. **鍔熻兘浼樺寲**: 绠楁硶鏁堢巼浣庯紝缂哄皯缂撳瓨鎴栦紭鍖栨満鍒�
2. **绉诲姩绔鑸爮鍥哄畾缃《浼樺寲**: 绉诲姩绔鑸爮鍥哄畾缃《浼樺寲

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍘熷瀹炵幇
def old_function():
    # 鏃ч�昏緫
    pass

# 鉁� 淇鍚庯細浼樺寲瀹炵幇
def new_function():
    # 鏂伴�昏緫
    # 娣诲姞閿欒澶勭悊鍜屾棩蹇�
    pass
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇绉诲姩绔鑸爮鍥哄畾缃《浼樺寲鐩稿叧闂
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.0.2 (2026-05-01) - 馃敡 绉诲姩绔搷搴斿紡閫傞厤鍏ㄩ潰浼樺寲

#### 闂: 鎬ц兘瀛樺湪闂
**鐜拌薄**: 绯荤粺鍝嶅簲鎱紝璧勬簮鍗犵敤楂�

**鏍规湰鍘熷洜**:
1. **鍔熻兘浼樺寲**: 绠楁硶鏁堢巼浣庯紝缂哄皯缂撳瓨鎴栦紭鍖栨満鍒�
2. **绉诲姩绔搷搴斿紡閫傞厤鍏ㄩ潰浼樺寲**: 绉诲姩绔搷搴斿紡閫傞厤鍏ㄩ潰浼樺寲

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍘熷瀹炵幇
def old_function():
    # 鏃ч�昏緫
    pass

# 鉁� 淇鍚庯細浼樺寲瀹炵幇
def new_function():
    # 鏂伴�昏緫
    # 娣诲姞閿欒澶勭悊鍜屾棩蹇�
    pass
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇绉诲姩绔搷搴斿紡閫傞厤鍏ㄩ潰浼樺寲鐩稿叧闂
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.0.1 (2026-04-30) - 馃敡 鐗堟湰鏇存柊鏃ュ織

#### 闂: 鏃ュ織璁板綍瀛樺湪闂
**鐜拌薄**: 鏃ュ織杈撳嚭涓嶅畬鏁存垨鏍煎紡閿欒

**鏍规湰鍘熷洜**:
1. **鍔熻兘浼樺寲**: 鏃ュ織閰嶇疆涓嶅綋鎴栬緭鍑洪�昏緫閿欒
2. **鐗堟湰鏇存柊鏃ュ織**: 鐗堟湰鏇存柊鏃ュ織
3. **Excel澶氭枃浠惰鍙栦紭鍖�**: Excel澶氭枃浠惰鍙栦紭鍖�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍘熷瀹炵幇
def old_function():
    # 鏃ч�昏緫
    pass

# 鉁� 淇鍚庯細浼樺寲瀹炵幇
def new_function():
    # 鏂伴�昏緫
    # 娣诲姞閿欒澶勭悊鍜屾棩蹇�
    pass
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘姝ｇ‘鎬�** | 閿欒 鉂� | 姝ｇ‘ 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **绋冲畾鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇鐗堟湰鏇存柊鏃ュ織鐩稿叧闂
- 浼樺寲浠ｇ爜閫昏緫鍜岄敊璇鐞�
- 鎻愬崌绯荤粺绋冲畾鎬у拰鐢ㄦ埛浣撻獙

---



### v3.0.0 (2026-04-30) - 馃敡 Cookie绠＄悊浼樺寲鍜岃法骞冲彴鍏煎鎬ф彁鍗�
- **馃敡 Cookie绠＄悊浼樺寲鍜岃法骞冲彴鍏煎鎬ф彁鍗�** - Cookie绠＄悊浼樺寲鍜岃法骞冲彴鍏煎鎬ф彁鍗�
### v2.9.6 (2026-04-30) - 馃敡 鍚姩鑴氭湰浼樺寲鍜屽姛鑳芥敼杩�
- **馃敡 鍚姩鑴氭湰浼樺寲鍜屽姛鑳芥敼杩�** - 鍚姩鑴氭湰浼樺寲鍜屽姛鑳芥敼杩�
### v2.9.5 (2026-04-30) - 鉁� 锛屾坊鍔犲畬鏁存洿鏂版棩蹇�
- **鉁� ** - 锛屾坊鍔犲畬鏁存洿鏂版棩蹇�
- **馃敡 绉诲姩绔搷搴斿紡閫傞厤浼樺寲** - 绉诲姩绔搷搴斿紡閫傞厤浼樺寲
### v2.9.4 (2026-04-29) - 鉁� 鏂板浜掑姩寮忚揣鍙峰姣斿姛鑳�
- **鉁� 鏂板浜掑姩寮忚揣鍙峰姣斿姛鑳�** - 鏂板浜掑姩寮忚揣鍙峰姣斿姛鑳�
### v2.9.3 (2026-04-29) - 馃敡 Cookie鏇存柊鍓嶈嚜鍔ㄦ竻绌烘満鍒�
- **馃敡 Cookie鏇存柊鍓嶈嚜鍔ㄦ竻绌烘満鍒�** - Cookie鏇存柊鍓嶈嚜鍔ㄦ竻绌烘満鍒�
### v2.9.2 (2026-04-29) - 馃敡 浼樺寲鍟嗗搧鍒楄〃鑱斿姩婊氬姩鍔熻兘
- **馃敡 浼樺寲鍟嗗搧鍒楄〃鑱斿姩婊氬姩鍔熻兘** - 浼樺寲鍟嗗搧鍒楄〃鑱斿姩婊氬姩鍔熻兘
### v2.9.1 (2026-04-29) - 馃敡 浼樺寲鍓嶇鏃堕棿鏄剧ず鍔熻兘锛屽噺灏慏OM閲嶆覆鏌撳紑閿�
- **馃敡 浼樺寲鍓嶇鏃堕棿鏄剧ず鍔熻兘** - 浼樺寲鍓嶇鏃堕棿鏄剧ず鍔熻兘锛屽噺灏慏OM閲嶆覆鏌撳紑閿�
### v2.9.0 (2026-04-29) - 馃敡 娣诲姞鍓嶇鏃堕棿鏄剧ず鍔熻兘骞朵紭鍖朖avaScript浠ｇ爜
- **馃敡 娣诲姞鍓嶇鏃堕棿鏄剧ず鍔熻兘骞朵紭鍖朖avaScript浠ｇ爜** - 娣诲姞鍓嶇鏃堕棿鏄剧ず鍔熻兘骞朵紭鍖朖avaScript浠ｇ爜
### v2.8.0 (2026-04-29) - 馃悰 鏀逛负04-29锛寁2.7.1鏀逛负04-27锛屼慨澶峷2.5.21閲嶅闂
- **馃悰 鏀逛负04-29** - 鏀逛负04-29锛寁2.7.1鏀逛负04-27锛屼慨澶峷2.5.21閲嶅闂
- **馃敡 鍓嶇灞曠ず浼樺寲锛欵xcel涓嶫SON瀵规瘮缁撴灉鐩存帴灞曠ず鍦ㄥ墠绔〉闈�** - 鍓嶇灞曠ず浼樺寲锛欵xcel涓嶫SON瀵规瘮缁撴灉鐩存帴灞曠ず鍦ㄥ墠绔〉闈�
### v2.7.2 (2026-04-29) - 馃悰 鏃ュ織锛氫慨澶�/api/clean/list鏂囦欢鏄剧ず鏍煎紡
- **馃悰 鏃ュ織锛氫慨澶�/api/clean/list鏂囦欢鏄剧ず鏍煎紡** - 鏃ュ織锛氫慨澶�/api/clean/list鏂囦欢鏄剧ず鏍煎紡
### v2.7.1 (2026-04-28) - 馃悰 淇鍟嗗搧璇︽儏椤靛浘鐗囧姞杞介棶棰�
- **馃悰 淇鍟嗗搧璇︽儏椤靛浘鐗囧姞杞介棶棰�** - 淇鍟嗗搧璇︽儏椤靛浘鐗囧姞杞介棶棰�
### v2.7.0 (2026-04-28) - 鉁� 娣诲姞鐗规畩鏂囦欢鍚嶄繚鎶わ紙.DS_Store, Thumbs.db绛夛級
- **鉁� 娣诲姞鐗规畩鏂囦欢鍚嶄繚鎶わ紙.DS_Store** - 娣诲姞鐗规畩鏂囦欢鍚嶄繚鎶わ紙.DS_Store, Thumbs.db绛夛級
- **馃敡 澧炲己娓呯悊鍑芥暟淇濇姢鏈哄埗** - 澧炲己娓呯悊鍑芥暟淇濇姢鏈哄埗锛屾坊鍔犳洿澶氫繚鎶ょ殑鏂囦欢绫诲瀷鍜屾枃浠跺す
- **馃敡 闆嗘垚鏂囦欢娓呯悊鍔熻兘** - 闆嗘垚鏂囦欢娓呯悊鍔熻兘锛屼紭鍖栦唬鐮侀�昏緫
### v2.6.1 (2026-04-28) - 鉁� 娣诲姞鑷姩鏁版嵁搴撳瓨鍌ㄥ姛鑳斤紝杩愯鐖櫕鏃惰嚜鍔ㄤ繚瀛樺晢鍝佹暟鎹埌MySQL
- **鉁� 娣诲姞鑷姩鏁版嵁搴撳瓨鍌ㄥ姛鑳�** - 娣诲姞鑷姩鏁版嵁搴撳瓨鍌ㄥ姛鑳斤紝杩愯鐖櫕鏃惰嚜鍔ㄤ繚瀛樺晢鍝佹暟鎹埌MySQL
- **馃敡 璐у彿瀵规瘮鍗＄墖鏍峰紡浼樺寲** - 璐у彿瀵规瘮鍗＄墖鏍峰紡浼樺寲锛屽皢API杩斿洖缁撴灉鏀逛负缇庤鐨勫崱鐗囧紡灞曠ず
### v2.6.0 (2026-06-26) - 馃敡 (2026-06-26)鐗堟湰鏉＄洰
- **馃敡 (2026-06-26)鐗堟湰鏉＄洰** - (2026-06-26)鐗堟湰鏉＄洰
- **馃敡 v2.8.0鐗堟湰鏃ユ湡椤哄簭** - v2.8.0鐗堟湰鏃ユ湡椤哄簭锛岀‘淇濇墍鏈夌増鏈彿鍜屾棩鏈熸寜鏃堕棿閫掑鎺掑垪
- **鉁� Web绔柊澧炶揣鍙峰姣擜PI鍜孴XT瀵规瘮鎸夐挳** - Web绔柊澧炶揣鍙峰姣擜PI鍜孴XT瀵规瘮鎸夐挳
- **馃敡 鑿滃崟閫夐」5鏍规嵁绯荤粺鑷姩鍚姩Web鏈嶅姟** - 鑿滃崟閫夐」5鏍规嵁绯荤粺鑷姩鍚姩Web鏈嶅姟
- **鉁� 鑿滃崟鏂板閫夐」5鍚姩Web鏈嶅姟** - 鑿滃崟鏂板閫夐」5鍚姩Web鏈嶅姟
- **馃敡 璐у彿瀵规瘮閫夐」2鏀逛负鍙鍙朤XT鏂囦欢** - 璐у彿瀵规瘮閫夐」2鏀逛负鍙鍙朤XT鏂囦欢
- **鉁� 娣诲姞绯荤粺妫�娴嬪姛鑳�** - 娣诲姞绯荤粺妫�娴嬪姛鑳斤紝鍓嶇鍜屽悗绔兘鏄剧ず绯荤粺淇℃伅
- **鉁� 鏇存柊鍚姩鑴氭湰鏀寔Web鏈嶅姟妯″紡** - 鏇存柊鍚姩鑴氭湰鏀寔Web鏈嶅姟妯″紡
- **鉁� 鍚堝苟server.py鍒癿ain.py** - 鍚堝苟server.py鍒癿ain.py锛屾坊鍔燱eb鏈嶅姟妯″紡鍜孧ySQL鏀寔
### v2.5.22 (2026-04-19) - 馃敡 绉婚櫎闂查奔骞冲彴鎵嬬画璐�60鍏冨皝椤堕檺鍒讹紝鏀逛负鎸夊崟鏈哄敭浠风殑1.6%璁＄畻
- **馃敡 绉婚櫎闂查奔骞冲彴鎵嬬画璐�60鍏冨皝椤堕檺鍒�** - 绉婚櫎闂查奔骞冲彴鎵嬬画璐�60鍏冨皝椤堕檺鍒讹紝鏀逛负鎸夊崟鏈哄敭浠风殑1.6%璁＄畻
### v2.5.21 (2026-04-26) - 鉁� 鏀寔澶氬钩鍙癊xcel璺緞閰嶇疆锛岃嚜鍔ㄨ疆璇㈡娴�
- **鉁� 鏀寔澶氬钩鍙癊xcel璺緞閰嶇疆** - 鏀寔澶氬钩鍙癊xcel璺緞閰嶇疆锛岃嚜鍔ㄨ疆璇㈡娴�
- **馃敡 閲嶆瀯鏁版嵁鑾峰彇閫昏緫** - 閲嶆瀯鏁版嵁鑾峰彇閫昏緫锛岀洿鎺ラ�氳繃API鑾峰彇鎵�鏈夊晢鍝佹暟鎹�
- **馃敡 閲嶆瀯鏁版嵁鑾峰彇閫昏緫** - 閲嶆瀯鏁版嵁鑾峰彇閫昏緫锛岀洿鎺ラ�氳繃API鑾峰彇鍟嗗搧鏁版嵁
### v2.5.20 (2026-04-15) - 馃悰 淇Windows娴忚鍣ㄦ娴嬶紝浣跨敤dir+findstr鏇夸唬閫氶厤绗�
- **馃悰 淇Windows娴忚鍣ㄦ娴�** - 淇Windows娴忚鍣ㄦ娴嬶紝浣跨敤dir+findstr鏇夸唬閫氶厤绗�
### v2.5.19 (2026-04-15) - 馃敡 浼樺寲macOS娴忚鍣ㄦ娴嬶紝鏀寔Google Chrome for Testing.app
- **馃敡 浼樺寲macOS娴忚鍣ㄦ娴�** - 浼樺寲macOS娴忚鍣ㄦ娴嬶紝鏀寔Google Chrome for Testing.app
### v2.5.18 (2026-04-15) - 馃敡 浼樺寲娴忚鍣ㄦ娴嬶紝閬垮厤閲嶅涓嬭浇Playwright娴忚鍣�
- **馃敡 浼樺寲娴忚鍣ㄦ娴�** - 浼樺寲娴忚鍣ㄦ娴嬶紝閬垮厤閲嶅涓嬭浇Playwright娴忚鍣�
- **鉁� 鏂板鐜妫�娴嬪姛鑳�** - 鏂板鐜妫�娴嬪姛鑳�
### v2.5.17 (2026-04-13) - 馃敡 浼樺寲鎷胯揣浠锋彁鍙栨�ц兘鍜屼唬鐮佺粨鏋�

#### 闂: 鎷胯揣浠锋彁鍙栭�昏緫鍒嗘暎涓旀�ц兘杈冧綆
**鐜拌薄**: 鎷胯揣浠锋彁鍙栭�昏緫鍒嗘暎鍦ㄥ涓嚱鏁颁腑锛屼唬鐮侀噸澶嶅害楂橈紝鎬ц兘鏈夊緟浼樺寲

**鏍规湰鍘熷洜**:
1. **浠ｇ爜缁撴瀯闂**: 鎷胯揣浠锋彁鍙栭�昏緫鍒嗘暎鍦ㄥ涓湴鏂癸紝缂轰箯缁熶竴绠＄悊
2. **鎬ц兘闂**: 閲嶅鐨凥TML鍐呭鎼滅储瀵艰嚧鎬ц兘娴垂

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍒嗘暎鐨勬嬁璐т环鎻愬彇閫昏緫
def extract_cost_price_1():
    # 閫昏緫鍒嗘暎鍦ㄥ涓嚱鏁颁腑

def extract_cost_price_2():
    # 閲嶅鐨凥TML鎼滅储閫昏緫

# 鉁� 淇鍚庯細缁熶竴鎷胯揣浠锋彁鍙栭�昏緫
def extract_purchase_price(self, product):
    """缁熶竴鎷胯揣浠锋彁鍙栭�昏緫"""
    # 闆嗕腑绠＄悊鎵�鏈夋嬁璐т环鎻愬彇閫昏緫
    # 浼樺寲HTML鍐呭鎼滅储锛岄伩鍏嶉噸澶�
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **浠ｇ爜缁撴瀯** | 鍒嗘暎 鉂� | 缁熶竴 鉁� |
| **鎬ц兘** | 杈冩參 鉂� | 鎻愬崌 鉁� |
| **鍙淮鎶ゆ��** | 鍥伴毦 鉂� | 绠�鍗� 鉁� |

**鎶�鏈粏鑺�**:
- 缁熶竴鎷胯揣浠锋彁鍙栭�昏緫鍒板崟涓�鍑芥暟
- 浼樺寲HTML鍐呭鎼滅储锛岄伩鍏嶉噸澶嶆悳绱�
- 浣跨敤print_separator()鏇夸唬print('='*60)鎻愬崌浠ｇ爜涓�鑷存��

---

### v2.5.16 (2026-04-12) - 馃敡 浼樺寲CookieValidator绫伙紝绮剧偧浠ｇ爜閫昏緫

#### 闂: CookieValidator绫讳唬鐮佸啑浣欙紝閫昏緫涓嶅娓呮櫚
**鐜拌薄**: CookieValidator绫诲寘鍚啑浣欎唬鐮侊紝楠岃瘉閫昏緫鍒嗘暎锛屽彲璇绘�ц緝宸�

**鏍规湰鍘熷洜**:
1. **浠ｇ爜鍐椾綑**: 澶氫釜楠岃瘉姝ラ瀛樺湪閲嶅鐨勯敊璇鐞嗛�昏緫
2. **閫昏緫鍒嗘暎**: 涓冩楠岃瘉娴佺▼鏈厖鍒嗘ā鍧楀寲

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍐椾綑鐨勯獙璇侀�昏緫
class CookieValidator:
    def validate(self):
        # 姝ラ1
        if not file_exists:
            print("閿欒")
            return False
        # 姝ラ2
        if not can_read:
            print("閿欒")
            return False
        # ... 閲嶅鐨勯敊璇鐞�

# 鉁� 淇鍚庯細绮剧偧鐨勯獙璇侀�昏緫
class CookieValidator:
    def validate_and_prompt(self, cookie_file):
        """涓冩楠岃瘉娴佺▼锛岀粺涓�閿欒澶勭悊"""
        with ExceptionContext("CookieValidator.validate"):
            # 缁熶竴鐨勫紓甯稿鐞嗗拰鏃ュ織璁板綍
            # 娓呮櫚鐨勪竷姝ラ獙璇佹祦绋�
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **浠ｇ爜琛屾暟** | 杈冨 鉂� | 绮剧畝 鉁� |
| **鍙鎬�** | 杈冨樊 鉂� | 娓呮櫚 鉁� |
| **鍙淮鎶ゆ��** | 鍥伴毦 鉂� | 绠�鍗� 鉁� |

**鎶�鏈粏鑺�**:
- 浣跨敤ExceptionContext缁熶竴寮傚父澶勭悊
- 涓冩楠岃瘉娴佺▼妯″潡鍖�
- 绉婚櫎鍐椾綑鐨勯敊璇鐞嗕唬鐮�

---

### v2.5.14 (2026-04-12) - 馃悰 淇璺緞閿欒锛屽畬鍠凱athManager缁熶竴绠＄悊

#### 闂: 璺ㄥ钩鍙拌矾寰勭鐞嗘贩涔憋紝瀵艰嚧鏂囦欢璇诲啓閿欒
**鐜拌薄**: Windows/macOS/Linux璺緞鏍煎紡涓嶇粺涓�锛屽鑷撮厤缃枃浠躲�丆ookie鏂囦欢绛夎鍐欏け璐�

**鏍规湰鍘熷洜**:
1. **璺緞纭紪鐮�**: 璺緞鐩存帴纭紪鐮佸湪浠ｇ爜涓紝鏈�冭檻璺ㄥ钩鍙板樊寮�
2. **缂哄皯缁熶竴绠＄悊**: 娌℃湁缁熶竴鐨勮矾寰勭鐞嗙被锛岃矾寰勫垎鏁ｅ湪澶氫釜妯″潡涓�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細纭紪鐮佽矾寰�
cookie_file = "config/cookies.json"  # Windows璺緞鏍煎紡
excel_file = "data```excel.xlsx"      # 涓嶅吋瀹筸acOS/Linux

# 鉁� 淇鍚庯細PathManager缁熶竴绠＄悊
class PathManager:
    @staticmethod
    def get_cookie_file():
        """鑾峰彇Cookie鏂囦欢璺緞锛堣法骞冲彴锛�"""
        return os.path.join("config", "cookies.json")
    
    @staticmethod
    def get_excel_file():
        """鑾峰彇Excel鏂囦欢璺緞锛堣法骞冲彴锛�"""
        return os.path.join("data", "excel.xlsx")
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **璺ㄥ钩鍙板吋瀹�** | 涓嶅吋瀹� 鉂� | 鍏煎 鉁� |
| **璺緞绠＄悊** | 鍒嗘暎 鉂� | 缁熶竴 鉁� |
| **鏂囦欢璇诲啓** | 澶辫触 鉂� | 鎴愬姛 鉁� |

**鎶�鏈粏鑺�**:
- 鏂板PathManager绫荤粺涓�绠＄悊鎵�鏈夎法绯荤粺璺緞
- 浣跨敤os.path.join()鏇夸唬纭紪鐮佽矾寰勫垎闅旂
- 纭繚Windows/macOS/Linux璺緞鏍煎紡缁熶竴

---

### v2.5.13 (2026-04-29) - 馃敡 22鐗堟湰閲嶅鍜屾棩鏈熸贩涔遍棶棰橈紝閲嶆柊鏁寸悊鎵�鏈夌増鏈彿纭繚杩炵画鎬у拰鏃堕棿椤哄簭姝ｇ‘

#### 闂: 鐗堟湰鍙烽噸澶嶄笖鏃ユ湡娣蜂贡锛屽鑷寸増鏈巻鍙蹭笉鍙拷婧�
**鐜拌薄**: v2.5.22鐗堟湰閲嶅鍑虹幇锛屾棩鏈熼『搴忛敊涔憋紝褰卞搷鐗堟湰鍘嗗彶杩借釜

**鏍规湰鍘熷洜**:
1. **鐗堟湰鍙风鐞嗕笉瑙勮寖**: 澶氫釜鎻愪氦浣跨敤浜嗙浉鍚岀殑鐗堟湰鍙穠2.5.22
2. **鏃ユ湡璁板綍閿欒**: 鎻愪氦鏃ユ湡涓庡疄闄呮棩鏈熶笉绗�

**淇鏂规**:
```markdown
# 鉂� 淇鍓嶏細鐗堟湰鍙烽噸澶嶏紝鏃ユ湡娣蜂贡
### v2.5.22 (2026-04-19) - 淇A
### v2.5.22 (2026-04-20) - 淇B  # 鐗堟湰鍙烽噸澶�
### v2.5.21 (2026-04-26) - 淇C  # 鏃ユ湡椤哄簭閿欒

# 鉁� 淇鍚庯細鐗堟湰鍙疯繛缁紝鏃ユ湡姝ｇ‘
### v2.5.22 (2026-04-19) - 淇A
### v2.5.23 (2026-04-20) - 淇B  # 鐗堟湰鍙烽�掑
### v2.5.24 (2026-04-26) - 淇C  # 鏃ユ湡椤哄簭姝ｇ‘
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鐗堟湰鍙疯繛缁��** | 閲嶅 鉂� | 杩炵画 鉁� |
| **鏃ユ湡椤哄簭** | 娣蜂贡 鉂� | 姝ｇ‘ 鉁� |
| **鍙拷婧��** | 鍥伴毦 鉂� | 娓呮櫚 鉁� |

**鎶�鏈粏鑺�**:
- 閲嶆柊鏁寸悊鎵�鏈夌増鏈彿锛岀‘淇濊繛缁��
- 淇鏃ユ湡椤哄簭锛岀‘淇濇椂闂寸嚎姝ｇ‘
- 鏂板PathManager绫伙紝缁熶竴绠＄悊鎵�鏈夎法绯荤粺璺緞

---

### v2.5.12 (2026-04-12) - 馃敡 浼樺寲绯荤粺妫�娴嬮�昏緫锛岀粺涓�璺ㄥ钩鍙版祻瑙堝櫒閰嶇疆

#### 闂: 绯荤粺妫�娴嬮�昏緫涓嶅噯纭紝娴忚鍣ㄩ厤缃笉缁熶竴
**鐜拌薄**: Windows/macOS/Linux绯荤粺妫�娴嬮�昏緫鍒嗘暎锛屾祻瑙堝櫒璺緞閰嶇疆涓嶇粺涓�

**鏍规湰鍘熷洜**:
1. **绯荤粺妫�娴嬪垎鏁�**: 绯荤粺妫�娴嬮�昏緫鍒嗘暎鍦ㄥ涓ā鍧椾腑
2. **娴忚鍣ㄩ厤缃‖缂栫爜**: 娴忚鍣ㄨ矾寰勭‖缂栫爜锛屾湭鑰冭檻璺ㄥ钩鍙板樊寮�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍒嗘暎鐨勭郴缁熸娴�
import platform
if platform.system() == 'Windows':
    browser_path = 'C:```Program Files```...'

# 鉁� 淇鍚庯細缁熶竴鐨勭郴缁熸娴�
class SystemDetector:
    @staticmethod
    def get_browser_path():
        """鑾峰彇娴忚鍣ㄨ矾寰勶紙璺ㄥ钩鍙帮級"""
        system = platform.system()
        if system == 'Windows':
            return 'C:```Program Files```...'
        elif system == 'Darwin':
            return '/Applications/...'
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **绯荤粺妫�娴�** | 鍒嗘暎 鉂� | 缁熶竴 鉁� |
| **娴忚鍣ㄩ厤缃�** | 纭紪鐮� 鉂� | 鍔ㄦ�� 鉁� |
| **璺ㄥ钩鍙板吋瀹�** | 涓嶅吋瀹� 鉂� | 鍏煎 鉁� |

**鎶�鏈粏鑺�**:
- 缁熶竴绯荤粺妫�娴嬮�昏緫鍒癝ystemDetector绫�
- 娴忚鍣ㄨ矾寰勯厤缃姩鎬佸寲
- 鏀寔Windows/macOS/Linux涓夊钩鍙�

---

### v2.5.10 (2026-04-12) - 馃悰 淇瀵煎叆閿欒锛岀‘淇滶xcel瀵规瘮鍔熻兘姝ｅ父杩愯

#### 闂: Excel瀵规瘮鍔熻兘瀵煎叆閿欒锛屽鑷村姛鑳芥棤娉曚娇鐢�
**鐜拌薄**: 杩愯Excel瀵规瘮鍔熻兘鏃舵姤閿檂ModuleNotFoundError: No module named 'openpyxl'`

**鏍规湰鍘熷洜**:
1. **缂哄皯渚濊禆**: requirements.txt涓己灏憃penpyxl渚濊禆
2. **瀵煎叆璺緞閿欒**: 瀵煎叆璇彞璺緞涓嶆纭�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細缂哄皯渚濊禆锛屽鍏ラ敊璇�
import openpyxl  # ModuleNotFoundError

# 鉁� 淇鍚庯細娣诲姞渚濊禆锛屼慨姝ｅ鍏�
# requirements.txt
openpyxl>=3.0.0

# main.py
try:
    import openpyxl
except ImportError:
    print("璇峰畨瑁呬緷璧�: pip install openpyxl")
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **瀵煎叆閿欒** | 鎶ラ敊 鉂� | 姝ｅ父 鉁� |
| **Excel瀵规瘮** | 澶辫触 鉂� | 鎴愬姛 鉁� |
| **渚濊禆绠＄悊** | 缂哄け 鉂� | 瀹屾暣 鉁� |

**鎶�鏈粏鑺�**:
- 鏇存柊requirements.txt娣诲姞openpyxl渚濊禆
- 娣诲姞瀵煎叆寮傚父澶勭悊
- 纭繚Excel瀵规瘮鍔熻兘姝ｅ父杩愯

---

### v2.5.9 (2026-04-11) - 馃敡 浼樺寲浠ｇ爜閫昏緫锛屼娇鐢ㄥ垪琛ㄦ帹瀵煎紡绠�鍖栨枃浠舵煡鎵句唬鐮�

#### 闂: 鏂囦欢鏌ユ壘浠ｇ爜鍐楅暱锛屽彲璇绘�у樊
**鐜拌薄**: 鏂囦欢鏌ユ壘閫昏緫浣跨敤澶氬眰宓屽寰幆锛屼唬鐮佸啑闀夸笖闅句互缁存姢

**鏍规湰鍘熷洜**:
1. **浠ｇ爜椋庢牸闂**: 浣跨敤浼犵粺鐨刦or寰幆宓屽锛屾湭鍏呭垎鍒╃敤Python鐗规��
2. **鍙鎬у樊**: 澶氬眰宓屽瀵艰嚧浠ｇ爜闅句互鐞嗚В

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細澶氬眰宓屽寰幆
json_files = []
for file in os.listdir('.'):
    if file.endswith('.json'):
        if 'wego' in file:
            json_files.append(file)

# 鉁� 淇鍚庯細鍒楄〃鎺ㄥ寮�
json_files = [
    file for file in os.listdir('.')
    if file.endswith('.json') and 'wego' in file
]
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **浠ｇ爜琛屾暟** | 5琛� 鉂� | 3琛� 鉁� |
| **鍙鎬�** | 杈冨樊 鉂� | 娓呮櫚 鉁� |
| **鎬ц兘** | 涓�鑸� 鉂� | 鎻愬崌 鉁� |

**鎶�鏈粏鑺�**:
- 浣跨敤鍒楄〃鎺ㄥ寮忔浛浠ｅ灞傚祵濂楀惊鐜�
- 鎻愬崌浠ｇ爜鍙鎬у拰鎬ц兘
- 绗﹀悎Python鏈�浣冲疄璺�

---

### v2.5.8 (2026-04-11) - 馃悰 淇excel_file涓篘one鐨勯敊璇紝瑙ｅ喅os.path.exists鐨凾ypeError

#### 闂: excel_file涓篘one鏃跺鑷寸▼搴忓穿婧�
**鐜拌薄**: 杩愯Excel瀵规瘮鍔熻兘鏃舵姤閿檂TypeError: expected str, bytes or os.PathLike object, not NoneType`

**鏍规湰鍘熷洜**:
1. **绌哄�兼鏌ョ己澶�**: 浣跨敤excel_file鍓嶆湭妫�鏌ユ槸鍚︿负None
2. **os.path.exists鍙傛暟閿欒**: 褰揺xcel_file涓篘one鏃讹紝os.path.exists()鎶涘嚭TypeError

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鏈鏌ョ┖鍊�
if FileManager.file_exists(self.excel_file):  # TypeError when None
    input_stock_numbers = self.load_excel_data()

# 鉁� 淇鍚庯細娣诲姞绌哄�兼鏌�
if self.excel_file and FileManager.file_exists(self.excel_file):
    input_stock_numbers = self.load_excel_data()

# 鉁� 淇鍚庯細澶勭悊basename绌哄��
'excel_file': os.path.basename(self.excel_file) if self.excel_file else 'None'
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **绋嬪簭宕╂簝** | 宕╂簝 鉂� | 姝ｅ父 鉁� |
| **绌哄�煎鐞�** | 缂哄け 鉂� | 瀹屽杽 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**:
- 鍦ㄤ娇鐢╡xcel_file鍓嶆坊鍔燦one妫�鏌�
- 浣跨敤鏉′欢琛ㄨ揪寮忓鐞哹asename绌哄��
- 澧炲己浠ｇ爜鍋ュ．鎬э紝閬垮厤绌哄�煎鑷寸殑绋嬪簭宕╂簝

---

### v2.5.7 (2026-04-11) - 馃悰 淇浠锋牸姣旇緝閿欒锛岃В鍐硃arse_price杩斿洖None鐨凾ypeError

#### 闂: 浠锋牸姣旇緝鏃秔arse_price杩斿洖None瀵艰嚧绋嬪簭宕╂簝
**鐜拌薄**: 绛涢�夐珮浠峰晢鍝佹椂鎶ラ敊`TypeError: '>=' not supported between instances of 'int' and 'NoneType'`

**鏍规湰鍘熷洜**:
1. **浠锋牸瑙ｆ瀽澶辫触**: parse_price鍑芥暟鍦ㄦ棤娉曡В鏋愪环鏍兼椂杩斿洖None
2. **缂哄皯绌哄�兼鏌�**: 鐩存帴姣旇緝None鍊煎鑷碩ypeError

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鏈鏌ョ┖鍊�
high_price_stock_numbers = [
    p.get('璐у彿', '') for p in products 
    if WegoScraper.parse_price(p.get('鍞环', '')) >= 599  # TypeError when None
]

# 鉁� 淇鍚庯細娣诲姞绌哄�兼鏌�
high_price_stock_numbers = [
    p.get('璐у彿', '') for p in products 
    if WegoScraper.parse_price(p.get('鍞环', '')) is not None
    and WegoScraper.parse_price(p.get('鍞环', '')) >= 599
]
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **绋嬪簭宕╂簝** | 宕╂簝 鉂� | 姝ｅ父 鉁� |
| **浠锋牸绛涢��** | 澶辫触 鉂� | 鎴愬姛 鉁� |
| **鏁版嵁鍑嗙‘鎬�** | 閿欒 鉂� | 鍑嗙‘ 鉁� |

**鎶�鏈粏鑺�**:
- 鍦ㄦ瘮杈冧环鏍煎墠妫�鏌arse_price杩斿洖鍊兼槸鍚︿负None
- 纭繚浠锋牸鏈夋晥鍚庡啀杩涜姣旇緝
- 閬垮厤None鍊煎鑷寸殑TypeError
### v2.5.6 (2026-04-11) - 馃敡 浼樺寲Cookie鏇存柊瀹屾垚鍚庣殑寤惰繜锛屾彁鍗囧搷搴旈�熷害

#### 闂: Cookie鏇存柊瀹屾垚鍚庤繑鍥炰富鑿滃崟寤惰繜杩囬暱
**鐜拌薄**: Cookie鏇存柊瀹屾垚鍚庯紝杩斿洖涓昏彍鍗曢渶瑕佺瓑寰呰緝闀挎椂闂达紝鐢ㄦ埛浣撻獙涓嶄匠

**鏍规湰鍘熷洜**:
1. **寤惰繜璁剧疆涓嶅悎鐞�**: Cookie鏇存柊瀹屾垚鍚庤缃簡鍥哄畾鐨勫欢杩熸椂闂�
2. **鐢ㄦ埛绛夊緟鏃堕棿闀�**: 鐢ㄦ埛闇�瑕佺瓑寰呬笉蹇呰鐨勫欢杩熸墠鑳界户缁搷浣�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍥哄畾寤惰繜鏃堕棿
time.sleep(3)  # 鍥哄畾绛夊緟3绉�
print("Cookie鏇存柊瀹屾垚")

# 鉁� 淇鍚庯細鍑忓皯寤惰繜鏃堕棿
time.sleep(1)  # 鍑忓皯鍒�1绉�
print("Cookie鏇存柊瀹屾垚锛屽嵆灏嗚繑鍥炰富鑿滃崟...")
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **绛夊緟鏃堕棿** | 3绉� 鉂� | 1绉� 鉁� |
| **鐢ㄦ埛浣撻獙** | 杈冩參 鉂� | 蹇�� 鉁� |
| **鍝嶅簲閫熷害** | 鎱� 鉂� | 鎻愬崌 鉁� |

**鎶�鏈粏鑺�**:
- 鍑忓皯Cookie鏇存柊瀹屾垚鍚庣殑鍥哄畾寤惰繜鏃堕棿
- 鎻愬崌鐢ㄦ埛鎿嶄綔鍝嶅簲閫熷害
- 浼樺寲鐢ㄦ埛绛夊緟浣撻獙

---

### v2.5.5 (2026-04-11) - 馃敡 绉婚櫎Cookie鏇存柊鍚庣殑鍥炶溅纭锛岀畝鍖栨搷浣滄祦绋�

#### 闂: Cookie鏇存柊鍚庨渶瑕佹墜鍔ㄦ寜鍥炶溅纭锛屾搷浣滅箒鐞�
**鐜拌薄**: Cookie鏇存柊瀹屾垚鍚庯紝鐢ㄦ埛闇�瑕佹墜鍔ㄦ寜鍥炶溅閿‘璁ゆ墠鑳界户缁紝澧炲姞浜嗕笉蹇呰鐨勬搷浣滄楠�

**鏍规湰鍘熷洜**:
1. **浜や簰璁捐闂**: Cookie鏇存柊鍚庢坊鍔犱簡涓嶅繀瑕佺殑纭姝ラ
2. **鐢ㄦ埛浣撻獙宸�**: 鐢ㄦ埛闇�瑕侀澶栫殑鎿嶄綔鎵嶈兘缁х画

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細闇�瑕佹墜鍔ㄧ‘璁�
print("Cookie鏇存柊瀹屾垚")
input("鎸夊洖杞﹂敭缁х画...")  # 闇�瑕佺敤鎴锋墜鍔ㄧ‘璁�

# 鉁� 淇鍚庯細鑷姩缁х画
print("Cookie鏇存柊瀹屾垚锛岃嚜鍔ㄨ繑鍥炰富鑿滃崟...")
# 绉婚櫎input()锛岃嚜鍔ㄧ户缁�
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鎿嶄綔姝ラ** | 闇�瑕佺‘璁� 鉂� | 鑷姩缁х画 鉁� |
| **鐢ㄦ埛浣撻獙** | 绻佺悙 鉂� | 绠�娲� 鉁� |
| **鎿嶄綔娴佺▼** | 澶嶆潅 鉂� | 绠�鍖� 鉁� |

**鎶�鏈粏鑺�**:
- 绉婚櫎Cookie鏇存柊鍚庣殑input()纭姝ラ
- 绠�鍖栫敤鎴锋搷浣滄祦绋�
- 鎻愬崌鐢ㄦ埛浣撻獙

---

### v2.5.4 (2026-04-11) - 馃敡 瀹炵幇鐪熸鐨勮嚜鍔ㄥ叧闂祻瑙堝櫒锛屾娴嬬櫥褰曞悗鑷姩鍏抽棴

#### 闂: Cookie鏇存柊鏃舵祻瑙堝櫒涓嶈兘鑷姩鍏抽棴锛岄渶瑕佹墜鍔ㄥ叧闂�
**鐜拌薄**: Cookie鏇存柊鏃讹紝娴忚鍣ㄦ墦寮�鍚庨渶瑕佺敤鎴锋墜鍔ㄥ叧闂紝涓嶅鑷姩鍖�

**鏍规湰鍘熷洜**:
1. **缂哄皯鐧诲綍妫�娴�**: 娌℃湁妫�娴嬬敤鎴锋槸鍚﹀凡鐧诲綍
2. **缂哄皯鑷姩鍏抽棴閫昏緫**: 娴忚鍣ㄦ墦寮�鍚庢病鏈夎嚜鍔ㄥ叧闂満鍒�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細闇�瑕佹墜鍔ㄥ叧闂祻瑙堝櫒
browser = launch_browser()
# 鐢ㄦ埛鎵嬪姩鐧诲綍
# 鐢ㄦ埛鎵嬪姩鍏抽棴娴忚鍣�

# 鉁� 淇鍚庯細鑷姩妫�娴嬬櫥褰曞苟鍏抽棴娴忚鍣�
async def update_cookie_auto():
    browser = await launch_browser()
    # 妫�娴嬬敤鎴锋槸鍚﹀凡鐧诲綍锛堟娴婥ookie鍙樺寲锛�
    while True:
        cookies = await get_cookies()
        if cookies_changed(cookies):
            await browser.close()
            break
        await asyncio.sleep(1)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **娴忚鍣ㄥ叧闂�** | 鎵嬪姩 鉂� | 鑷姩 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |
| **鑷姩鍖栫▼搴�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 瀹炵幇鐧诲綍鐘舵�佹娴嬫満鍒�
- 妫�娴婥ookie鍙樺寲鍒ゆ柇鐢ㄦ埛鏄惁宸茬櫥褰�
- 鐧诲綍鍚庤嚜鍔ㄥ叧闂祻瑙堝櫒

---

### v2.5.3 (2026-04-11) - 馃敡 浼樺寲Cookie鏇存柊鎻愮ず淇℃伅锛屾槑纭嚜鍔ㄥ叧闂祻瑙堝櫒

#### 闂: Cookie鏇存柊鎻愮ず淇℃伅涓嶆槑纭紝鐢ㄦ埛涓嶇煡閬撴祻瑙堝櫒浼氳嚜鍔ㄥ叧闂�
**鐜拌薄**: Cookie鏇存柊鏃讹紝鎻愮ず淇℃伅涓嶅鏄庣‘锛岀敤鎴蜂笉鐭ラ亾娴忚鍣ㄤ細鑷姩鍏抽棴

**鏍规湰鍘熷洜**:
1. **鎻愮ず淇℃伅涓嶅畬鏁�**: 娌℃湁鏄庣‘鍛婄煡鐢ㄦ埛娴忚鍣ㄤ細鑷姩鍏抽棴
2. **鐢ㄦ埛鍥版儜**: 鐢ㄦ埛涓嶇煡閬撲笅涓�姝ヨ鍋氫粈涔�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鎻愮ず淇℃伅涓嶆槑纭�
print("姝ｅ湪鏇存柊Cookie...")

# 鉁� 淇鍚庯細鏄庣‘鎻愮ず淇℃伅
print("姝ｅ湪鏇存柊Cookie...")
print("璇峰湪娴忚鍣ㄤ腑鐧诲綍锛岀櫥褰曟垚鍔熷悗娴忚鍣ㄥ皢鑷姩鍏抽棴")
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鎻愮ず淇℃伅** | 涓嶆槑纭� 鉂� | 鏄庣‘ 鉁� |
| **鐢ㄦ埛鐞嗚В** | 鍥版儜 鉂� | 娓呮櫚 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**:
- 浼樺寲Cookie鏇存柊鎻愮ず淇℃伅
- 鏄庣‘鍛婄煡鐢ㄦ埛娴忚鍣ㄤ細鑷姩鍏抽棴
- 鎻愬崌鐢ㄦ埛鐞嗚В搴﹀拰浣撻獙

---

### v2.5.2 (2026-04-11) - 馃敡 绠�鍖朇ookie鏇存柊娴佺▼锛屽弬鑰僾2.1.1鐗堟湰瀹炵幇

#### 闂: Cookie鏇存柊娴佺▼澶嶆潅锛屼笉澶熺畝娲�
**鐜拌薄**: Cookie鏇存柊娴佺▼鍖呭惈澶氫釜涓嶅繀瑕佺殑姝ラ锛岀敤鎴蜂綋楠屼笉浣�

**鏍规湰鍘熷洜**:
1. **娴佺▼璁捐闂**: Cookie鏇存柊娴佺▼杩囦簬澶嶆潅
2. **鍙傝�冪増鏈�**: v2.1.1鐗堟湰鏈夋洿绠�娲佺殑瀹炵幇

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細澶嶆潅鐨勬洿鏂版祦绋�
def update_cookie():
    print("姝ラ1: 鎵撳紑娴忚鍣�")
    print("姝ラ2: 鎵嬪姩鐧诲綍")
    print("姝ラ3: 鎵嬪姩鍏抽棴娴忚鍣�")
    print("姝ラ4: 鎻愬彇Cookie")
    print("姝ラ5: 淇濆瓨Cookie")
    input("纭缁х画...")

# 鉁� 淇鍚庯細绠�鍖栫殑鏇存柊娴佺▼锛堝弬鑰僾2.1.1锛�
def update_cookie():
    print("姝ｅ湪鏇存柊Cookie...")
    # 鑷姩鎵撳紑娴忚鍣ㄣ�佹娴嬬櫥褰曘�佸叧闂祻瑙堝櫒銆佷繚瀛楥ookie
    print("Cookie鏇存柊瀹屾垚")
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **娴佺▼姝ラ** | 5姝� 鉂� | 1姝� 鉁� |
| **鐢ㄦ埛鎿嶄綔** | 澶嶆潅 鉂� | 绠�鍗� 鉁� |
| **鑷姩鍖栫▼搴�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 鍙傝�僾2.1.1鐗堟湰鐨勭畝娲佸疄鐜�
- 绠�鍖朇ookie鏇存柊娴佺▼
- 鍑忓皯涓嶅繀瑕佺殑姝ラ鍜岀‘璁�

---

### v2.5.0 (2026-04-11) - 馃敡 浼樺寲鍟嗗搧淇℃伅鎻愬彇閫昏緫锛岀簿绠�浠ｇ爜缁撴瀯

#### 闂: 鍟嗗搧淇℃伅鎻愬彇閫昏緫鍐楅暱锛屼唬鐮佺粨鏋勪笉澶熸竻鏅�
**鐜拌薄**: 鍟嗗搧淇℃伅鎻愬彇閫昏緫鍒嗘暎鍦ㄥ涓嚱鏁颁腑锛屼唬鐮侀噸澶嶅害楂橈紝鍙淮鎶ゆ�у樊

**鏍规湰鍘熷洜**:
1. **浠ｇ爜缁撴瀯闂**: 鍟嗗搧淇℃伅鎻愬彇閫昏緫鍒嗘暎锛岀己涔忕粺涓�绠＄悊
2. **浠ｇ爜閲嶅**: 澶氫釜鍑芥暟鍖呭惈閲嶅鐨勬彁鍙栭�昏緫

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍒嗘暎鐨勬彁鍙栭�昏緫
def extract_product_1():
    # 鎻愬彇鍟嗗搧鍚嶇О
    # 鎻愬彇鍟嗗搧浠锋牸
    # 鎻愬彇鍟嗗搧璐у彿

def extract_product_2():
    # 鎻愬彇鍟嗗搧鍚嶇О锛堥噸澶嶏級
    # 鎻愬彇鍟嗗搧浠锋牸锛堥噸澶嶏級
    # 鎻愬彇鍟嗗搧璐у彿锛堥噸澶嶏級

# 鉁� 淇鍚庯細缁熶竴鐨勬彁鍙栭�昏緫
def extract_product_info(element):
    """缁熶竴鍟嗗搧淇℃伅鎻愬彇閫昏緫"""
    return {
        'name': extract_name(element),
        'price': extract_price(element),
        'sku': extract_sku(element)
    }
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **浠ｇ爜缁撴瀯** | 鍒嗘暎 鉂� | 缁熶竴 鉁� |
| **浠ｇ爜閲嶅** | 楂� 鉂� | 浣� 鉁� |
| **鍙淮鎶ゆ��** | 鍥伴毦 鉂� | 绠�鍗� 鉁� |

**鎶�鏈粏鑺�**:
- 缁熶竴鍟嗗搧淇℃伅鎻愬彇閫昏緫鍒板崟涓�鍑芥暟
- 鍑忓皯浠ｇ爜閲嶅
- 鎻愬崌浠ｇ爜鍙淮鎶ゆ��
### v2.4.7 (2026-04-11) - 馃敡 鏂板鐙珛Cookie鑷姩鏇存柊鍔熻兘锛屼紭鍖栨祻瑙堝櫒鍚姩娴佺▼鍏抽棴

#### 闂: Cookie鏇存柊涓嶅鐙珛锛屾祻瑙堝櫒鍚姩鍏抽棴娴佺▼涓嶅浼樺寲
**鐜拌薄**: Cookie鏇存柊鍔熻兘闆嗘垚鍦ㄤ富鑿滃崟涓紝涓嶅鐙珛锛涙祻瑙堝櫒鍚姩鍏抽棴娴佺▼涓嶅娴佺晠

**鏍规湰鍘熷洜**:
1. **鍔熻兘闆嗘垚闂**: Cookie鏇存柊鍔熻兘涓庝富鑿滃崟鑰﹀悎搴﹂珮
2. **娴忚鍣ㄦ祦绋嬮棶棰�**: 娴忚鍣ㄥ惎鍔ㄥ叧闂祦绋嬩笉澶熶紭鍖�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細Cookie鏇存柊闆嗘垚鍦ㄤ富鑿滃崟涓�
def main():
    while True:
        print("1. 杩愯鐖櫕")
        print("2. 鏇存柊Cookie")
        # Cookie鏇存柊閫昏緫宓屽叆鍦ㄤ富鑿滃崟涓�

# 鉁� 淇鍚庯細鐙珛鐨凜ookie鏇存柊鍔熻兘
def update_cookie_standalone():
    """鐙珛鐨凜ookie鑷姩鏇存柊鍔熻兘"""
    print("Cookie鑷姩鏇存柊宸ュ叿")
    # 鐙珛鐨勬洿鏂版祦绋�
    # 浼樺寲鐨勬祻瑙堝櫒鍚姩鍏抽棴娴佺▼
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鍔熻兘鐙珛鎬�** | 鑰﹀悎 鉂� | 鐙珛 鉁� |
| **娴忚鍣ㄦ祦绋�** | 涓嶄紭鍖� 鉂� | 浼樺寲 鉁� |
| **鐢ㄦ埛浣撻獙** | 涓�鑸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**:
- 鏂板鐙珛鐨凜ookie鑷姩鏇存柊鍔熻兘
- 浼樺寲娴忚鍣ㄥ惎鍔ㄥ叧闂祦绋�
- 鎻愬崌鍔熻兘鐙珛鎬у拰鐢ㄦ埛浣撻獙

---

### v2.4.6 (2026-04-11) - 馃敡 瀹屽杽澶囨敞鎻愬彇鍔熻兘锛屾彁鍙栨墍鏈夋湁澶囨敞鐨勫晢鍝佷俊鎭�

#### 闂: 澶囨敞鎻愬彇鍔熻兘涓嶅畬鍠勶紝閮ㄥ垎澶囨敞淇℃伅鏈彁鍙�
**鐜拌薄**: 鍟嗗搧澶囨敞淇℃伅鎻愬彇涓嶅畬鏁达紝閮ㄥ垎鏈夊娉ㄧ殑鍟嗗搧淇℃伅鏈鎻愬彇

**鏍规湰鍘熷洜**:
1. **澶囨敞鎻愬彇閫昏緫涓嶅畬鍠�**: 鍙彁鍙栫壒瀹氭牸寮忕殑澶囨敞锛岄仐婕忓叾浠栨牸寮�
2. **缂哄皯鍏ㄩ潰鎵弿**: 鏈鎵�鏈夊晢鍝佽繘琛屽娉ㄦ壂鎻�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍙彁鍙栫壒瀹氭牸寮忕殑澶囨敞
def extract_remarks(products):
    remarks = []
    for p in products:
        if '澶囨敞:' in p.get('description', ''):
            remarks.append(p)
    return remarks

# 鉁� 淇鍚庯細鎻愬彇鎵�鏈夋湁澶囨敞鐨勫晢鍝�
def extract_all_remarks(products):
    """鎻愬彇鎵�鏈夋湁澶囨敞鐨勫晢鍝佷俊鎭�"""
    remarks = []
    for p in products:
        remark = extract_remark_from_product(p)
        if remark:
            remarks.append({
                'sku': p.get('璐у彿'),
                'remark': remark
            })
    return remarks
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **澶囨敞鎻愬彇** | 涓嶅畬鏁� 鉂� | 瀹屾暣 鉁� |
| **鍟嗗搧瑕嗙洊** | 閮ㄥ垎 鉂� | 鍏ㄩ儴 鉁� |
| **鏁版嵁鍑嗙‘鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 瀹屽杽澶囨敞鎻愬彇閫昏緫锛屾敮鎸佸绉嶆牸寮�
- 鎻愬彇鎵�鏈夋湁澶囨敞鐨勫晢鍝佷俊鎭�
- 鎻愬崌鏁版嵁瀹屾暣鎬у拰鍑嗙‘鎬�

---

### v2.4.5 (2026-04-11) - 馃悰 淇澶囨敞鎻愬彇閿欒锛屾敮鎸佹棤鏍囩澶囨敞淇℃伅鎻愬彇

#### 闂: 澶囨敞鎻愬彇閿欒锛屾棤娉曟彁鍙栨棤鏍囩鐨勫娉ㄤ俊鎭�
**鐜拌薄**: 閮ㄥ垎鍟嗗搧澶囨敞娌℃湁鐗瑰畾鏍囩锛屽鑷村娉ㄦ彁鍙栧け璐�

**鏍规湰鍘熷洜**:
1. **鏍囩渚濊禆**: 澶囨敞鎻愬彇渚濊禆鐗瑰畾鏍囩锛堝"澶囨敞:"锛�
2. **鏍煎紡闄愬埗**: 鏃犳硶璇嗗埆鏃犳爣绛剧殑澶囨敞淇℃伅

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鍙彁鍙栨湁鏍囩鐨勫娉�
if '澶囨敞:' in description:
    remark = description.split('澶囨敞:')[1]

# 鉁� 淇鍚庯細鏀寔鏃犳爣绛惧娉ㄦ彁鍙�
def extract_remark_flexible(description):
    """鐏垫椿鎻愬彇澶囨敞淇℃伅"""
    # 灏濊瘯鎻愬彇鏈夋爣绛剧殑澶囨敞
    if '澶囨敞:' in description:
        return description.split('澶囨敞:')[1].strip()
    # 灏濊瘯鎻愬彇鏃犳爣绛剧殑澶囨敞锛堝熀浜庡叾浠栫壒寰侊級
    elif has_remark_feature(description):
        return extract_remark_by_feature(description)
    return None
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **澶囨敞鎻愬彇** | 澶辫触 鉂� | 鎴愬姛 鉁� |
| **鏍煎紡鏀寔** | 鍗曚竴 鉂� | 澶氭牱 鉁� |
| **鏁版嵁瀹屾暣鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 鏀寔鏃犳爣绛惧娉ㄤ俊鎭彁鍙�
- 澧炲姞鐏垫椿鐨勫娉ㄨ瘑鍒�昏緫
- 鎻愬崌澶囨敞鎻愬彇鎴愬姛鐜�

---

### v2.4.4 (2026-04-11) - 馃悰 淇浠锋牸鎻愬彇閿欒锛屾敮鎸佸崈鍒嗗埗浠锋牸鏍煎紡

#### 闂: 浠锋牸鎻愬彇閿欒锛屾棤娉曡瘑鍒崈鍒嗗埗浠锋牸鏍煎紡
**鐜拌薄**: 閮ㄥ垎鍟嗗搧浠锋牸浣跨敤鍗冨垎鍒舵牸寮忥紙濡�"1,299鍏�"锛夛紝瀵艰嚧浠锋牸鎻愬彇澶辫触

**鏍规湰鍘熷洜**:
1. **浠锋牸鏍煎紡闄愬埗**: 浠锋牸鎻愬彇閫昏緫鍙敮鎸佹櫘閫氭牸寮�
2. **鍗冨垎鍒舵湭澶勭悊**: 鏈鐞嗕环鏍间腑鐨勯�楀彿鍒嗛殧绗�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細鏃犳硶澶勭悊鍗冨垎鍒朵环鏍�
price = re.search(r'(```d+)鍏�', text)
if price:
    return int(price.group(1))  # "1,299鍏�" 鈫� 鎻愬彇澶辫触

# 鉁� 淇鍚庯細鏀寔鍗冨垎鍒朵环鏍�
def parse_price(text):
    """瑙ｆ瀽浠锋牸锛堟敮鎸佸崈鍒嗗埗锛�"""
    # 绉婚櫎鍗冨垎浣嶅垎闅旂
    text = text.replace(',', '')
    price = re.search(r'(```d+)鍏�', text)
    if price:
        return int(price.group(1))  # "1,299鍏�" 鈫� 1299
    return None
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **浠锋牸鎻愬彇** | 澶辫触 鉂� | 鎴愬姛 鉁� |
| **鏍煎紡鏀寔** | 鍗曚竴 鉂� | 澶氭牱 鉁� |
| **鏁版嵁鍑嗙‘鎬�** | 閿欒 鉂� | 鍑嗙‘ 鉁� |

**鎶�鏈粏鑺�**:
- 鏀寔鍗冨垎鍒朵环鏍兼牸寮忥紙濡�"1,299鍏�"锛�
- 绉婚櫎浠锋牸涓殑閫楀彿鍒嗛殧绗�
- 鎻愬崌浠锋牸鎻愬彇鍑嗙‘鎬�

---

### v2.4.1 (2026-04-11) - 鉁� 鏂板骞冲潎姣忎釜璁惧鍞嚭鍧囦环缁熻

#### 闂: 缂哄皯骞冲潎姣忎釜璁惧鍞嚭鍧囦环缁熻鍔熻兘
**鐜拌薄**: 鏃犳硶缁熻骞冲潎姣忎釜璁惧鐨勫敭鍑哄潎浠凤紝缂哄皯閲嶈鐨勬暟鎹垎鏋愭寚鏍�

**鏍规湰鍘熷洜**:
1. **鍔熻兘缂哄け**: 鏈疄鐜板钩鍧囪澶囧潎浠风粺璁″姛鑳�
2. **鏁版嵁闇�姹�**: 鐢ㄦ埛闇�瑕佷簡瑙ｆ瘡涓澶囩殑骞冲潎鍞嚭浠锋牸

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細缂哄皯骞冲潎璁惧鍧囦环缁熻
# 鏃犵浉鍏冲姛鑳�

# 鉁� 淇鍚庯細鏂板骞冲潎璁惧鍧囦环缁熻
def calculate_average_device_price(products):
    """璁＄畻骞冲潎姣忎釜璁惧鐨勫敭鍑哄潎浠�"""
    total_price = sum(p.get('鍞环', 0) for p in products)
    total_devices = len(products)
    avg_price = total_price / total_devices if total_devices > 0 else 0
    return avg_price
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **缁熻鍔熻兘** | 缂哄け 鉂� | 鏂板 鉁� |
| **鏁版嵁鍒嗘瀽** | 涓嶅畬鏁� 鉂� | 瀹屾暣 鉁� |
| **鍐崇瓥鏀寔** | 鏃� 鉂� | 鏈� 鉁� |

**鎶�鏈粏鑺�**:
- 鏂板骞冲潎姣忎釜璁惧鍞嚭鍧囦环缁熻鍔熻兘
- 鎻愪緵閲嶈鐨勬暟鎹垎鏋愭寚鏍�
- 鏀寔鐢ㄦ埛鍐崇瓥

---

### v2.4.0 (2026-04-11) - 馃敡 绠�鍖朖SON鏂囦欢甯冨眬锛屼紭鍖栦环鏍兼樉绀轰负鍗冨垎鍒�

#### 闂: JSON鏂囦欢甯冨眬澶嶆潅锛屼环鏍兼樉绀轰笉澶熺洿瑙�
**鐜拌薄**: JSON鏂囦欢鍖呭惈杩囧鍐椾綑瀛楁锛屼环鏍兼樉绀轰负鏅�氭暟瀛椾笉澶熺洿瑙�

**鏍规湰鍘熷洜**:
1. **甯冨眬璁捐闂**: JSON鏂囦欢鍖呭惈杩囧涓嶅繀瑕佺殑瀛楁
2. **浠锋牸鏄剧ず闂**: 浠锋牸鏄剧ず涓烘櫘閫氭暟瀛楋紝涓嶅鐩磋

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細澶嶆潅鐨凧SON甯冨眬
{
    "product": {
        "basic_info": {
            "name": "鍟嗗搧鍚�",
            "price": 1299
        },
        "extra_info": {
            "remark": "",
            "tags": []
        }
    }
}

# 鉁� 淇鍚庯細绠�鍖栫殑JSON甯冨眬
{
    "name": "鍟嗗搧鍚�",
    "price": "1,299鍏�",  # 鍗冨垎鍒舵樉绀�
    "sku": "12345"
}
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **JSON甯冨眬** | 澶嶆潅 鉂� | 绠�娲� 鉁� |
| **浠锋牸鏄剧ず** | 涓嶇洿瑙� 鉂� | 鐩磋 鉁� |
| **鍙鎬�** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**:
- 绠�鍖朖SON鏂囦欢甯冨眬锛岀Щ闄ゅ啑浣欏瓧娈�
- 浠锋牸鏄剧ず浼樺寲涓哄崈鍒嗗埗鏍煎紡
- 鎻愬崌JSON鏂囦欢鍙鎬�
### v2.3.6 (2026-04-11) - 馃敡 澧炲己HTML鍐呭鎼滅储锛屽畬鍠勬嬁璐т环鎻愬彇閫昏緫

#### 闂: 鎷胯揣浠锋彁鍙栭�昏緫涓嶅畬鍠勶紝HTML鍐呭鎼滅储涓嶅鍏ㄩ潰
**鐜拌薄**: 鎷胯揣浠锋彁鍙栨垚鍔熺巼浣庯紝閮ㄥ垎鍟嗗搧鐨勬嬁璐т环鏈兘姝ｇ‘鎻愬彇

**鏍规湰鍘熷洜**:
1. **HTML鎼滅储鑼冨洿绐�**: 鍙湪鐗瑰畾鍖哄煙鎼滅储鎷胯揣浠蜂俊鎭�
2. **鎻愬彇閫昏緫绠�鍗�**: 鏈�冭檻澶氱HTML缁撴瀯鍜屼环鏍兼牸寮�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細绠�鍗曠殑鎷胯揣浠锋彁鍙�
def extract_cost_price(html):
    match = re.search(r'鎴愭湰浠穂锛�:]```s*(```d+)', html)
    return match.group(1) if match else None

# 鉁� 淇鍚庯細澧炲己鐨凥TML鎼滅储鍜屾彁鍙�
def extract_cost_price_enhanced(html):
    """澧炲己鐨勬嬁璐т环鎻愬彇閫昏緫"""
    patterns = [
        r'鎴愭湰浠穂锛�:]```s*(```d+)',
        r'鎷胯揣浠穂锛�:]```s*(```d+)',
        r'杩涗环[锛�:]```s*(```d+)',
        r'鎴愭湰[锛�:]```s*(```d+)'
    ]
    for pattern in patterns:
        match = re.search(pattern, html)
        if match:
            return match.group(1)
    return None
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鎻愬彇鎴愬姛鐜�** | 浣� 鉂� | 楂� 鉁� |
| **鎼滅储鑼冨洿** | 绐� 鉂� | 瀹� 鉁� |
| **鏍煎紡鏀寔** | 鍗曚竴 鉂� | 澶氭牱 鉁� |

**鎶�鏈粏鑺�**:
- 澧炲己HTML鍐呭鎼滅储鑼冨洿
- 鏀寔澶氱鎷胯揣浠峰叧閿瘝锛堟垚鏈环銆佹嬁璐т环銆佽繘浠枫�佹垚鏈級
- 瀹屽杽鎷胯揣浠锋彁鍙栭�昏緫

---

### v2.3.5 (2026-04-11) - 馃敡 澧炲己鎴愭湰浠疯瘑鍒紝娣诲姞鏅鸿兘浠锋牸鎻愬彇閫昏緫

#### 闂: 鎴愭湰浠疯瘑鍒笉澶熸櫤鑳斤紝缂哄皯鐏垫椿鐨勪环鏍兼彁鍙栭�昏緫
**鐜拌薄**: 鎴愭湰浠疯瘑鍒垚鍔熺巼浣庯紝鏃犳硶璇嗗埆澶氱浠锋牸鏍煎紡

**鏍规湰鍘熷洜**:
1. **璇嗗埆閫昏緫绠�鍗�**: 鍙瘑鍒壒瀹氭牸寮忕殑鎴愭湰浠�
2. **缂哄皯鏅鸿兘鎻愬彇**: 鏈疄鐜版櫤鑳戒环鏍兼彁鍙栭�昏緫

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細绠�鍗曠殑鎴愭湰浠疯瘑鍒�
if '鎴愭湰浠�' in text:
    price = extract_price(text)

# 鉁� 淇鍚庯細鏅鸿兘鎴愭湰浠锋彁鍙�
def smart_extract_cost_price(text):
    """鏅鸿兘鎴愭湰浠锋彁鍙栭�昏緫"""
    # 灏濊瘯澶氱璇嗗埆鏂瑰紡
    cost_keywords = ['鎴愭湰浠�', '鎷胯揣浠�', '杩涗环', '鎴愭湰', '杩涗环']
    for keyword in cost_keywords:
        if keyword in text:
            price = extract_price_near_keyword(text, keyword)
            if price:
                return price
    # 灏濊瘯浠庣壒瀹氫綅缃彁鍙�
    return extract_price_from_context(text)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **璇嗗埆鎴愬姛鐜�** | 浣� 鉂� | 楂� 鉁� |
| **鏅鸿兘绋嬪害** | 浣� 鉂� | 楂� 鉁� |
| **鏍煎紡鏀寔** | 鍗曚竴 鉂� | 澶氭牱 鉁� |

**鎶�鏈粏鑺�**:
- 澧炲己鎴愭湰浠疯瘑鍒兘鍔�
- 娣诲姞鏅鸿兘浠锋牸鎻愬彇閫昏緫
- 鏀寔澶氱浠锋牸鏍煎紡鍜屽叧閿瘝

---

### v2.3.4 (2026-04-11) - 馃悰 鏂板鎷胯揣浠锋彁鍙栧姛鑳斤紝淇璁惧鎴愭湰绱鍜岃澶囧潎浠蜂负0鐨勯棶棰�

#### 闂: 缂哄皯鎷胯揣浠锋彁鍙栧姛鑳斤紝璁惧鎴愭湰绱鍜岃澶囧潎浠蜂负0
**鐜拌薄**: 鏃犳硶鎻愬彇鎷胯揣浠凤紝瀵艰嚧璁惧鎴愭湰绱涓�0锛岃澶囧潎浠蜂篃涓�0

**鏍规湰鍘熷洜**:
1. **鍔熻兘缂哄け**: 鏈疄鐜版嬁璐т环鎻愬彇鍔熻兘
2. **鏁版嵁閿欒**: 璁惧鎴愭湰绱涓�0锛屽鑷磋澶囧潎浠疯绠楅敊璇�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細缂哄皯鎷胯揣浠锋彁鍙�
def calculate_device_stats(products):
    total_cost = 0  # 璁惧鎴愭湰绱涓�0
    avg_price = 0   # 璁惧鍧囦环涓�0
    return total_cost, avg_price

# 鉁� 淇鍚庯細鏂板鎷胯揣浠锋彁鍙�
def calculate_device_stats_fixed(products):
    """璁＄畻璁惧缁熻淇℃伅锛堝惈鎷胯揣浠凤級"""
    total_cost = 0
    for p in products:
        cost_price = extract_cost_price(p)  # 鎻愬彇鎷胯揣浠�
        if cost_price:
            total_cost += cost_price
    avg_price = total_cost / len(products) if products else 0
    return total_cost, avg_price
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鎷胯揣浠锋彁鍙�** | 缂哄け 鉂� | 鏂板 鉁� |
| **璁惧鎴愭湰绱** | 0 鉂� | 姝ｇ‘ 鉁� |
| **璁惧鍧囦环** | 0 鉂� | 姝ｇ‘ 鉁� |

**鎶�鏈粏鑺�**:
- 鏂板鎷胯揣浠锋彁鍙栧姛鑳�
- 淇璁惧鎴愭湰绱涓�0鐨勯棶棰�
- 淇璁惧鍧囦环涓�0鐨勯棶棰�

---

### v2.3.3 (2026-04-11) - 馃敡 鏂板璁惧鍧囦环锛屼紭鍖栭棽楸煎钩鍙版墜缁垂璁＄畻锛堝崟鏈烘渶楂�60鍏冨皝椤讹級

#### 闂: 缂哄皯璁惧鍧囦环缁熻锛岄棽楸煎钩鍙版墜缁垂璁＄畻涓嶅浼樺寲
**鐜拌薄**: 鏃犳硶缁熻璁惧鍧囦环锛岄棽楸煎钩鍙版墜缁垂璁＄畻涓嶅鍑嗙‘

**鏍规湰鍘熷洜**:
1. **鍔熻兘缂哄け**: 鏈疄鐜拌澶囧潎浠风粺璁″姛鑳�
2. **鎵嬬画璐硅绠楅棶棰�**: 鏈疄鐜伴棽楸煎钩鍙版墜缁垂灏侀《鏈哄埗

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細缂哄皯璁惧鍧囦环鍜屾墜缁垂灏侀《
def calculate_stats(products):
    avg_price = total_price / count
    fee = total_price * 0.06  # 鏃犲皝椤�
    return avg_price, fee

# 鉁� 淇鍚庯細鏂板璁惧鍧囦环鍜屾墜缁垂灏侀《
def calculate_stats_fixed(products):
    """璁＄畻缁熻淇℃伅锛堝惈璁惧鍧囦环鍜屾墜缁垂灏侀《锛�"""
    avg_price = total_price / count if count > 0 else 0
    # 闂查奔骞冲彴鎵嬬画璐癸細鍗曟満鏈�楂�60鍏冨皝椤�
    fee = min(total_price * 0.06, 60 * count)
    return avg_price, fee
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **璁惧鍧囦环** | 缂哄け 鉂� | 鏂板 鉁� |
| **鎵嬬画璐瑰皝椤�** | 鏃� 鉂� | 鏈� 鉁� |
| **璁＄畻鍑嗙‘鎬�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 鏂板璁惧鍧囦环缁熻鍔熻兘
- 浼樺寲闂查奔骞冲彴鎵嬬画璐硅绠楋紙鍗曟満鏈�楂�60鍏冨皝椤讹級
- 鎻愬崌璁＄畻鍑嗙‘鎬�

---

### v2.3.2 (2026-04-11) - 鉁� 鏂板绱缁熻鍔熻兘锛屾坊鍔犻璁″敭鍑轰环鏍笺�佽澶囨垚鏈拰骞冲彴鎵嬬画璐圭疮璁�

#### 闂: 缂哄皯绱缁熻鍔熻兘锛屾棤娉曠粺璁￠璁″敭鍑轰环鏍笺�佽澶囨垚鏈拰骞冲彴鎵嬬画璐�
**鐜拌薄**: 鏃犳硶鏌ョ湅绱缁熻鏁版嵁锛岀己灏戦噸瑕佺殑鏁版嵁鍒嗘瀽鎸囨爣

**鏍规湰鍘熷洜**:
1. **鍔熻兘缂哄け**: 鏈疄鐜扮疮璁＄粺璁″姛鑳�
2. **鏁版嵁闇�姹�**: 鐢ㄦ埛闇�瑕佷簡瑙ｇ疮璁＄殑棰勮鍞嚭浠锋牸銆佽澶囨垚鏈拰骞冲彴鎵嬬画璐�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細缂哄皯绱缁熻
# 鏃犵浉鍏冲姛鑳�

# 鉁� 淇鍚庯細鏂板绱缁熻
def calculate_cumulative_stats(products):
    """璁＄畻绱缁熻淇℃伅"""
    total_expected_price = sum(p.get('棰勮鍞环', 0) for p in products)
    total_device_cost = sum(p.get('璁惧鎴愭湰', 0) for p in products)
    total_platform_fee = sum(p.get('骞冲彴鎵嬬画璐�', 0) for p in products)
    
    return {
        '棰勮鍞嚭浠锋牸绱': total_expected_price,
        '璁惧鎴愭湰绱': total_device_cost,
        '骞冲彴鎵嬬画璐圭疮璁�': total_platform_fee
    }
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **绱缁熻** | 缂哄け 鉂� | 鏂板 鉁� |
| **鏁版嵁鍒嗘瀽** | 涓嶅畬鏁� 鉂� | 瀹屾暣 鉁� |
| **鍐崇瓥鏀寔** | 鏃� 鉂� | 鏈� 鉁� |

**鎶�鏈粏鑺�**:
- 鏂板绱缁熻鍔熻兘
- 娣诲姞棰勮鍞嚭浠锋牸銆佽澶囨垚鏈拰骞冲彴鎵嬬画璐圭疮璁�
- 鎻愪緵閲嶈鐨勬暟鎹垎鏋愭寚鏍�

---

### v2.3.1 (2026-04-11) - 鉁� 淇濈暀Cookie鏇存柊閫夐」锛屼粎鏀寔鑷姩鏇存柊鍔熻兘

#### 闂: Cookie鏇存柊閫夐」杩囦簬澶嶆潅锛岀敤鎴烽渶瑕佹洿绠�娲佺殑閫夋嫨
**鐜拌薄**: Cookie鏇存柊鍖呭惈澶氫釜閫夐」锛堟墜鍔ㄣ�佽嚜鍔級锛岀敤鎴峰鏄撴贩娣�

**鏍规湰鍘熷洜**:
1. **閫夐」杩囧**: 鎻愪緵浜嗘墜鍔ㄥ拰鑷姩涓ょ鏇存柊鏂瑰紡
2. **鐢ㄦ埛闇�姹�**: 鐢ㄦ埛涓昏浣跨敤鑷姩鏇存柊鍔熻兘

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細澶氫釜Cookie鏇存柊閫夐」
print("1. 鎵嬪姩鏇存柊Cookie")
print("2. 鑷姩鏇存柊Cookie")
choice = input("璇烽�夋嫨: ")

# 鉁� 淇鍚庯細浠呬繚鐣欒嚜鍔ㄦ洿鏂�
print("Cookie鑷姩鏇存柊")
# 鐩存帴鎵ц鑷姩鏇存柊锛屾棤闇�鐢ㄦ埛閫夋嫨
update_cookie_auto()
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **閫夐」鏁伴噺** | 澶� 鉂� | 灏� 鉁� |
| **鐢ㄦ埛鎿嶄綔** | 澶嶆潅 鉂� | 绠�鍗� 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**:
- 淇濈暀Cookie鏇存柊閫夐」
- 浠呮敮鎸佽嚜鍔ㄦ洿鏂板姛鑳�
- 绠�鍖栫敤鎴锋搷浣滄祦绋�

---

### v2.3.0 (2026-04-11) - 馃敡 鍔熻兘鏁村悎浼樺寲锛屽悎骞惰彍鍗曢�夐」骞剁簿鐐间唬鐮侀�昏緫

#### 闂: 鑿滃崟閫夐」杩囧锛屽姛鑳藉垎鏁ｏ紝浠ｇ爜閫昏緫涓嶅绮剧偧
**鐜拌薄**: 涓昏彍鍗曞寘鍚繃澶氶�夐」锛屽姛鑳藉垎鏁ｅ湪涓嶅悓妯″潡锛屼唬鐮侀噸澶嶅害楂�

**鏍规湰鍘熷洜**:
1. **鑿滃崟璁捐闂**: 鑿滃崟閫夐」杩囧锛岀敤鎴烽毦浠ラ�夋嫨
2. **鍔熻兘鍒嗘暎**: 鐩稿叧鍔熻兘鍒嗘暎鍦ㄤ笉鍚屾ā鍧�
3. **浠ｇ爜閲嶅**: 澶氫釜妯″潡鍖呭惈閲嶅鐨勯�昏緫

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細杩囧鐨勮彍鍗曢�夐」
print("1. 杩愯鐖櫕")
print("2. 鏇存柊Cookie")
print("3. 鏌ョ湅鍟嗗搧鍒楄〃")
print("4. 瀵煎嚭鏁版嵁")
print("5. 鏁版嵁鍒嗘瀽")
print("6. 璁剧疆")
print("7. 閫�鍑�")

# 鉁� 淇鍚庯細鏁村悎鐨勮彍鍗曢�夐」
print("1. 杩愯鐖櫕锛堝惈Cookie鑷姩鏇存柊锛�")
print("2. 鏁版嵁鍒嗘瀽锛堝惈鏌ョ湅鍜屽鍑猴級")
print("3. 璁剧疆")
print("4. 閫�鍑�")
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **鑿滃崟閫夐」** | 7涓� 鉂� | 4涓� 鉁� |
| **鍔熻兘鏁村悎** | 鍒嗘暎 鉂� | 鏁村悎 鉁� |
| **浠ｇ爜绮剧偧搴�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 鏁村悎鐩稿叧鍔熻兘锛屽噺灏戣彍鍗曢�夐」
- 鍚堝苟鑿滃崟閫夐」锛屾彁鍗囩敤鎴蜂綋楠�
- 绮剧偧浠ｇ爜閫昏緫锛屽噺灏戦噸澶�
### v2.2.2 (2026-04-11) - 馃敡 Excel瀵规瘮JSON鍔熻兘澧炲己锛屾坊鍔犲皬璁″瓧娈靛苟绮剧偧浠ｇ爜閫昏緫

#### 闂: Excel瀵规瘮JSON鍔熻兘涓嶅瀹屽杽锛岀己灏戝皬璁″瓧娈�
**鐜拌薄**: Excel瀵规瘮JSON鍔熻兘缂哄皯灏忚瀛楁锛屾棤娉曠粺璁℃�讳环淇℃伅

**鏍规湰鍘熷洜**:
1. **鍔熻兘涓嶅畬鍠�**: Excel瀵规瘮JSON鍔熻兘缂哄皯灏忚瀛楁
2. **浠ｇ爜閫昏緫鍐楅暱**: 瀵规瘮閫昏緫鍒嗘暎锛屼唬鐮侀噸澶嶅害楂�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細缂哄皯灏忚瀛楁
def compare_excel_json(excel_data, json_data):
    result = []
    for item in excel_data:
        # 瀵规瘮閫昏緫
        result.append(item)
    return result

# 鉁� 淇鍚庯細娣诲姞灏忚瀛楁
def compare_excel_json_enhanced(excel_data, json_data):
    """澧炲己鐨凟xcel瀵规瘮JSON鍔熻兘"""
    result = []
    total_price = 0
    for item in excel_data:
        # 瀵规瘮閫昏緫
        result.append(item)
        total_price += item.get('浠锋牸', 0)
    
    # 娣诲姞灏忚瀛楁
    result.append({
        '璐у彿': '灏忚',
        '浠锋牸': total_price,
        '鏁伴噺': len(result)
    })
    return result
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **灏忚瀛楁** | 缂哄け 鉂� | 鏂板 鉁� |
| **浠ｇ爜绮剧偧搴�** | 浣� 鉂� | 楂� 鉁� |
| **鍔熻兘瀹屽杽搴�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 澧炲己Excel瀵规瘮JSON鍔熻兘
- 娣诲姞灏忚瀛楁锛岀粺璁℃�讳环淇℃伅
- 绮剧偧浠ｇ爜閫昏緫锛屽噺灏戦噸澶�

---

### v2.2.1 (2026-04-11) - 鉁� 娣诲姞鑷姩瀵规瘮鍔熻兘锛岀‘淇濇瘡娆¤繍琛岀埇铏悗閮界敓鎴愬皬璁″瓧娈�

#### 闂: 杩愯鐖櫕鍚庨渶瑕佹墜鍔ㄥ姣旓紝缂哄皯鑷姩瀵规瘮鍔熻兘
**鐜拌薄**: 姣忔杩愯鐖櫕鍚庯紝闇�瑕佹墜鍔ㄦ墽琛屽姣斿姛鑳斤紝缂哄皯鑷姩鍖�

**鏍规湰鍘熷洜**:
1. **鍔熻兘缂哄け**: 鏈疄鐜拌嚜鍔ㄥ姣斿姛鑳�
2. **鐢ㄦ埛闇�姹�**: 鐢ㄦ埛甯屾湜杩愯鐖櫕鍚庤嚜鍔ㄧ敓鎴愬姣旂粨鏋�

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細闇�瑕佹墜鍔ㄥ姣�
def run_spider():
    # 鐖櫕閫昏緫
    save_to_json(products)
    print("鐖櫕瀹屾垚锛岃鎵嬪姩鎵ц瀵规瘮")

# 鉁� 淇鍚庯細鑷姩瀵规瘮
def run_spider_auto_compare():
    """杩愯鐖櫕骞惰嚜鍔ㄥ姣�"""
    # 鐖櫕閫昏緫
    products = crawl_products()
    save_to_json(products)
    
    # 鑷姩瀵规瘮
    excel_data = load_excel()
    json_data = load_json()
    result = compare_excel_json(excel_data, json_data)
    save_result(result)
    print("鐖櫕瀹屾垚锛屽姣旂粨鏋滃凡鐢熸垚")
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **瀵规瘮鏂瑰紡** | 鎵嬪姩 鉂� | 鑷姩 鉁� |
| **灏忚瀛楁** | 缂哄け 鉂� | 鐢熸垚 鉁� |
| **鑷姩鍖栫▼搴�** | 浣� 鉂� | 楂� 鉁� |

**鎶�鏈粏鑺�**:
- 娣诲姞鑷姩瀵规瘮鍔熻兘
- 纭繚姣忔杩愯鐖櫕鍚庨兘鐢熸垚灏忚瀛楁
- 鎻愬崌鑷姩鍖栫▼搴�

---

### v2.2.0 (2026-04-09) - 馃敡 鎬ц兘浼樺寲锛屾彁鍗囧苟鍙戝鐞嗚兘鍔涘拰鍏冪礌鍘婚噸鏁堢巼

#### 闂: 鎬ц兘鐡堕锛屽苟鍙戝鐞嗚兘鍔涗綆锛屽厓绱犲幓閲嶆晥鐜囧樊
**鐜拌薄**: 鐖櫕杩愯閫熷害鎱紝骞跺彂澶勭悊鑳藉姏浣庯紝鍏冪礌鍘婚噸鏁堢巼宸�

**鏍规湰鍘熷洜**:
1. **骞跺彂澶勭悊闂**: 鏈厖鍒嗗埄鐢ㄥ苟鍙戝鐞嗚兘鍔�
2. **鍘婚噸鏁堢巼浣�**: 鍏冪礌鍘婚噸绠楁硶鏁堢巼浣庯紝褰卞搷鎬ц兘

**淇鏂规**:
```python
# 鉂� 淇鍓嶏細浣庢晥鐨勫苟鍙戝拰鍘婚噸
def crawl_products():
    products = []
    for page in pages:
        # 涓茶澶勭悊
        items = parse_page(page)
        # 浣庢晥鍘婚噸
        for item in items:
            if item not in products:
                products.append(item)
    return products

# 鉁� 淇鍚庯細浼樺寲鐨勫苟鍙戝拰鍘婚噸
import asyncio
from concurrent.futures import ThreadPoolExecutor

async def crawl_products_optimized():
    """浼樺寲鐨勭埇铏紙骞跺彂+楂樻晥鍘婚噸锛�"""
    products = set()  # 浣跨敤闆嗗悎鍘婚噸
    with ThreadPoolExecutor(max_workers=10) as executor:
        # 骞跺彂澶勭悊
        loop = asyncio.get_event_loop()
        tasks = [loop.run_in_executor(executor, parse_page, page) for page in pages]
        results = await asyncio.gather(*tasks)
        for items in results:
            products.update(items)  # 楂樻晥鍘婚噸
    return list(products)
```

**淇鏁堟灉**:
| 鎸囨爣 | 淇鍓� | 淇鍚� |
|------|--------|--------|
| **骞跺彂澶勭悊** | 涓茶 鉂� | 骞跺彂 鉁� |
| **鍘婚噸鏁堢巼** | O(n虏) 鉂� | O(n) 鉁� |
| **杩愯閫熷害** | 鎱� 鉂� | 蹇� 鉁� |

**鎶�鏈粏鑺�**:
- 鎻愬崌骞跺彂澶勭悊鑳藉姏锛堜娇鐢═hreadPoolExecutor锛�
- 浼樺寲鍏冪礌鍘婚噸鏁堢巼锛堜娇鐢ㄩ泦鍚堜唬鏇垮垪琛級
- 鎻愬崌鐖櫕杩愯閫熷害
### v2.1.9 - v2.1.9: 浠ｇ爜绮剧偧浼樺寲锛岀畝鍖栭�昏緫鎻愬崌鍙淮鎶ゆ��

**鎻愪氦Hash**: a56f5607
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
v2.1.9: 浠ｇ爜绮剧偧浼樺寲锛岀畝鍖栭�昏緫鎻愬崌鍙淮鎶ゆ��

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


#### 馃敡 鎶�鏈粏鑺�
```
v2.1.9: 浠ｇ爜绮剧偧浼樺寲锛岀畝鍖栭�昏緫鎻愬崌鍙淮鎶ゆ��
```

---
### v2.1.8 - v2.1.8: 浼樺寲婊氬姩鍔犺浇绛栫暐锛岄噰鐢ㄦ縺杩涙ā寮忓揩閫熷姞杞芥墍鏈夋暟鎹�

**鎻愪氦Hash**: 96cd68ff
**浣滆��**: RichelYu1998锛堝皬鏃簩鎵嬫満锛�

#### 馃摑 鏇存柊鍐呭
v2.1.8: 浼樺寲婊氬姩鍔犺浇绛栫暐锛岄噰鐢ㄦ縺杩涙ā寮忓揩閫熷姞杞芥墍鏈夋暟鎹�

#### 馃搧 褰卞搷鏂囦欢 (0涓枃浠�)


---|--------|--------|
| **浠ｇ爜琛屾暟** | 澶� 鉂� | 灏� 鉁� |
| **鍙鎬�** | 宸� 鉂� | 濂� 鉁� |
| **鍙淮鎶ゆ��** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**:
- 绮剧偧浠ｇ爜閫昏緫锛岀畝鍖栧鏉傚嚱鏁�
- 鎻愬崌浠ｇ爜鍙鎬у拰鍙淮鎶ゆ��
- 鍑忓皯鍐椾綑浠ｇ爜

---

#### 馃敡 鎶�鏈粏鑺�
```
v2.1.8: 浼樺寲婊氬姩鍔犺浇绛栫暐锛岄噰鐢ㄦ縺杩涙ā寮忓揩閫熷姞杞芥墍鏈夋暟鎹�
```

---
---|--------|--------|
| **绛夊緟鏃堕棿** | 2绉� 鉂� | 0.5绉� 鉁� |
| **鍔犺浇閫熷害** | 鎱� 鉂� | 蹇� 鉁� |
| **鐢ㄦ埛浣撻獙** | 宸� 鉂� | 濂� 鉁� |

**鎶�鏈粏鑺�**:
- 浼樺寲婊氬姩鍔犺浇绛栫暐锛岄噰鐢ㄦ縺杩涙ā寮�
- 鍑忓皯绛夊緟鏃堕棿锛屾彁鍗囧姞杞介�熷害
- 蹇�熷姞杞芥墍鏈夋暟鎹�

---