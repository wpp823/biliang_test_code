import arrow

#
# # end_at = arrow.now()
# begin_at = arrow.get('2022-05-11 16:37:27')
# end_at = arrow.get('2022-05-11 16:50:27')
#
# diff_time = end_at - begin_at
# print(diff_time.seconds)

msg_source_time = '2021-5-25 下午6:09'
# time_2 = time_1.replace("下午", "PM")
#
# now = arrow.now().format("YYYY-MM-DD AHH:mm")
# print(now)
# # obj = datetime.strptime(time_2,"YYYY-MM-DD AHH:mm ")
#
# obj = arrow.get(time_2,["YYYY-MM-DD AH:mm"]).format("YYYY-MM-DD HH:mm:ss")
# print(obj)
# pass

if "下午" in msg_source_time or "上午" in msg_source_time:
    time_2 = msg_source_time.replace("下午", "PM").replace("上午", "AM")
    msg_source_time = arrow.get(time_2, ["YYYY-M-DD AH:mm", "YYYY-MM-DD H:mmA"]).format("YYYY-MM-DD HH:mm:ss")

print(msg_source_time)
data = {'item_id': 582874429391,
        'title': '可痕类人胶原蛋白修复疤痕硅凝胶外科手术烧烫创伤可用官方正品',
        'category_id': '126740003', 'root_category_id': '50023721', 'currency': 'CNY', 'product_props': [{'基本信息': [
        {'品牌': '可痕'},
        {'产地': '陕西省西安市'},
        {'颜色分类': '可痕疤痕修复膏1支/15g【每2支1疗程】 可痕疤痕修复膏1支/25g【每2支1疗程】'},
        {'生产企业': '陕西巨子生物技术有限公司'}, {'注册证号': '陕械注准20152140138'},
        {'选购热点': '官方旗舰 正品保障'},
        {'医疗器械产品名称': '类人胶原蛋白疤痕修复硅凝胶'}]}],
        'main_imgs': ['https://img.alicdn.com/imgextra/i4/4292257416/O1CN01knsN7F24eZz5q1MtU_!!0-item_pic.jpg',
                      'https://img.alicdn.com/imgextra/i2/4292257416/O1CN01pZ9Zr724eZvnWHZa3_!!0-item_pic.jpg',
                      'https://img.alicdn.com/imgextra/i4/4292257416/O1CN01kCQekB24eZyozGal3_!!4292257416.jpg',
                      'https://img.alicdn.com/imgextra/i2/4292257416/O1CN01mHNRK824eZys7vgYc_!!4292257416.jpg',
                      'https://img.alicdn.com/imgextra/i4/4292257416/O1CN01THl9uB24eZvpFPx37_!!4292257416.jpg'], 'video_url': '',
        'comment_count': None,
        'shop_info': {'shop_name': '可痕旗舰店', 'shop_id': '166893332', 'shop_url': '//shop.m.taobao.com/shop/shop_index.htm?user_id=4292257416&item_id=582874429391', 'shop_rate': [],
                      'good_rate_percentage': '100.00%', 'followers': '1.5万', 'is_tmall': True, 'is_gold_seller': False,
                      'shop_logo': '//img.alicdn.com/imgextra//b9/4b/TB1s6pxKhTpK1RjSZR0SuvEwXXa.jpg', 'seller_id': '4292257416',
                      'wangwang': 'https://amos.alicdn.com/getcid.aw?groupid=0&s=1&7kRjsd&charset=utf-8&uid=%E5%8F%AF%E7%97%95%E6%97%97%E8%88%B0%E5%BA%97&site=cntaobao&wymtLt'},
        'delivery_info':
            {'area_from': ['陕西省', '西安市'], 'area_id': '1', 'postage': '0'},
        'sku_props': [{'prop_name': '颜色分类', 'pid': '1627207',
                       'values': [{'name': '可痕疤痕修复膏1支/15g【每2支1疗程】', 'vid': '28320'}, {'name': '可痕疤痕修复膏1支/25g【每2支1疗程】', 'vid': '3232480'}]}],
        'skus': [
            {'skuid': '3917342909295',
             'sale_price': '313',
             'origin_price': None, 'stock': '200', 'props_ids': '1627207:28320',
             'sub_price': '223',
             'sub_price_type': 'discounted price'},
            {'skuid': '4702956180174', 'sale_price': '358', 'origin_price': None, 'stock': '200', 'props_ids': '1627207:3232480', 'sub_price': '258',
             'sub_price_type': 'discounted price'}], 'buy_enable': True, 'cart_enable': True, 'hint_banner': {}}
