import json

with open(r'D:/ws/xy_ws/file/20260730微购相册(小旭数码).json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

products = data.get('商品列表', [])
print('Total products:', len(products))
print('\nFirst 5 products price fields:')
for i, p in enumerate(products[:5]):
    print(f'\nProduct {i+1}:')
    for key in p.keys():
        if key == '售价' or key == 'price':
            print(f'  {key}: {p[key]}')

count_with_cn = sum(1 for p in products if p.get('售价'))
count_with_en = sum(1 for p in products if 'price' in p)
print(f'\nWith 售价 field: {count_with_cn}')
print(f'With price field: {count_with_en}')

high_price = []
for p in products:
    price_str = p.get('售价', '').replace('￥','').replace(',','').strip()
    if price_str:
        try:
            if float(price_str) >= 599:
                high_price.append(p)
        except:
            pass

print(f'\nHigh price (>=599): {len(high_price)}')
if high_price:
    print('Examples:')
    for p in high_price[:3]:
        desc = p.get('商品描述', '')[:40]
        price = p.get('售价', '')
        print(f'  {desc} - Price: {price}')
