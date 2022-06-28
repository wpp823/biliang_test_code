    import logging
    import time
    from asyncio import get_event_loop
    from urllib.parse import urlparse, parse_qs

    import requests
    from pyppeteer import launch

    from my_log import get_logger

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log = get_logger()


    class OrderExtInfo():
        """订单扩数据工具"""

        def __init__(self):
            self.width, self.height = 1500, 800

            # get_event_loop().run_until_complete(self.init())
            # get_event_loop().run_until_complete(self.get_login_qrcode())
            # get_event_loop().run_until_complete(self.get_admin_cookie())
            # get_event_loop().run_until_complete(self.get_price())

        async def init(self):
            # noinspection PyAttributeOutsideInit
            self.browser = await launch(headless=False,
                                        args=['--disable-infobars', f'--window-size={self.width},{self.height}'],
                                        userDataDir='./userdata')
            # noinspection PyAttributeOutsideInit
            self.page = await self.browser.newPage()
            await self.page.setViewport({'width': self.width, 'height': self.height})
            await self.page.evaluate('()=>{Object.defineProperties(navigator,{webdriver:{get:()=>false}})}')

        # def __init__(self):
        #     self.wx_shop_admin_url = "https://shop.weixin.qq.com/"

        def get_wx_user(self, order_id):
            cookie = "pgv_pvi=3137840128; pgv_pvid=3824864103; _ga=GA1.2.1421120412.1587969099; RK=CIQM3ft2eT; ptcz=fa9d266a5ab861d0b7ab02bf11d4f3053d78c56f8eeb17c7e9a107081143fa9d; ua_id=qjEHe2qTZOqna9jDAAAAAD7_mWehftPnLZc0PVBk1Rw=; rewardsn=; wxtokenkey=777; pgv_si=s2700695552; mm_lang=zh_CN; wxuin=89286201079361; pgv_info=ssid=s6230829088; _tucao_userinfo=VkFHQ2FyRlRKZE1oeng2OEVkV3FsYStoMlJMRDRZdElHUURjbG5DbjQ5RWo0YlN0UHltUDNtcENSbUxyeHBHNldtTzNCWUppU0FwRWNRcW8yMGZvem1UcEFjeUdYRE5uMzArUkpVd21mczFQMzlMRXdNcXVsYmVEWHlrM1M2QmRYVFFSZ29ma25VSHNKcWNhbjFzWWpXR2s0LytSNDlzeDNlNExaOXhnVkJEdFFQV09zNkh1Z09uSVJ3eDQzMmlF--HQW3Ev%2Fj9BpIRmEjB33eZQ%3D%3D; iip=0; sig_login=h01b58ad7c9cd150b120adf97fa3038b56665a8d02bc6a24b5efdfbf196ea9773dd24f71f5c657480f4; tvfe_boss_uuid=b2c861ebd79d0734; cert=Y_dU_t2o1shO15_17rWzLlbUQk3KGS5E; o_cookie=441990625; pac_uid=1_441990625; ptui_loginuin=441990625@qq.com; wedrive_uin=13102661466865121; wedrive_sid=zeFReow9LUwuWEZ0ABp2egAA; wedrive_sids=13102661466865121&zeFReow9LUwuWEZ0ABp2egAA; wedrive_skey=13102661466865121&5d42d03fe3495f9c4db8a519b3adbe3d; wedrive_ticket=13102661466865121&CAESIHMk9TdHY3aX-aPqZ_v9mWy1PA8OiayF6nc1arQ6pl-l; xm_oidb_sid=441990625&48e665a8234268dd4c1bb51895bb8249qNE5pdXB5azB3OXFJNVJvRjRBbDR6bWpYbGF2dHBoMXRQNkdaRCp5UWFsa18.|397199018&4980866e29a3b1eda3130065ab4921dbqeUJDZFF3VDRxd3U1M0EqbFVSR1gqRjdpVzRVUVc0Rm0zSk4zZE5jeXlnQV8.; sig=h017900f8ca5eddbf847699c70e7aeadaaf0c89c197b1a3db086cb5be9c28ac791928934f7fa0370954; skey=@BK8nMQuSd; uin=o441990625; verifysession=h01d4d1a9e4451126f19f57c7bd359360efb0c51864a6364ed6a29886b8d10faf1d22b81e5cfcc9cc9d; wwapp.vid=; wwapp.cst=; wwapp.deviceid=; uuid=e01b4c2e0609a8f5e1fd965bbc821b0d; rand_info=CAESIHLz9P9aixa3eBzXSli/UFljpjL2i1E+yCM4ZxhdImvv; slave_bizuin=3507974520; data_bizuin=3507974520; bizuin=3507974520; data_ticket=j3bCyAoJ7YpknMt/E6wrgV8nlrT65mJGj9Cr8VCtuBUgKI+UPdK1SAVYagWLGxNj; slave_sid=XzFwQm9UWUVUUnZQVnIzNFg0Zl9VeDM2WGxhZ2R2MGpJSnREZXN5QnU1RVN4bkpuWDBHMW5rVjVneE85Uk9UTFhzQ1dsbXdBT3F3TnZyTW5ocHNZdVloNUJWSGRNV1piM19CNHJQYlZTWXBCWWtvSWdiQ2RXRmFQbVZlejVpSFhJakFFekxuR0I4eUN5UjVB; slave_user=gh_ddf5f31c2caf; xid=f2f96bfd24601c48446179287f1c9b5a"
            headers = {
                "cookie": cookie,
            }
            token = "438264078"
            url = f"https://mp.weixin.qq.com/faas/wxatrade/order/cgi/getOrder?orderid={order_id}&token={token}&lang=zh_CN&random=0.727970927606715"
            res = requests.get(url=url, headers=headers)
            order_data = res.json()
            order_user_info = order_data['order']['userInfo']

        async def get_login_qrcode(self):
            await self.page.goto('https://shop.weixin.qq.com/')
            await self.page.screenshot(path="./login_qrcode2.png")

        async def get_admin_cookie(self):
            time.sleep(3)
            await self.page.reload()
            page_url = self.page.frames[0].url
            url_obj = urlparse(page_url)

            page_params = parse_qs(url_obj.query)
            # https://mp.weixin.qq.com/wxatrade/home?token=258988448&lang=zh_CN
            # https://mp.weixin.qq.com/wxatrade/order/detail?orderid=3203963628518375936&token=258988448&lang=zh_CN
            # tag_url = f"{page_urls}"
            token = "".join(page_params.get("token"))
            lang = "".join(page_params.get("lang"))
            order_list_page_url = f"https://mp.weixin.qq.com/wxatrade/order/list?token={token}&lang={lang}"
            await self.page.goto(order_list_page_url)
            time.sleep(3)
            cookies = await self.page.cookies()
            print(cookies)
            return token, cookies

        def get_order_info(self, order_id, token, cookies):
            """获取订单扩展数据"""
            cookies = {
                item["name"]: item["value"] for item in cookies
            }
            # token = "438264078"
            url = f"https://mp.weixin.qq.com/faas/wxatrade/order/cgi/getOrder?orderid={order_id}&token={token}&lang=zh_CN"
            res = requests.get(url=url, cookies=cookies)
            order_data = res.json()
            order_user_info = order_data['order']['userInfo']

            print(order_user_info)


    if __name__ == '__main__':
        order_ext_info = OrderExtInfo()
        get_event_loop().run_until_complete(order_ext_info.init())
        get_event_loop().run_until_complete(order_ext_info.get_login_qrcode())
        token, cookies = get_event_loop().run_until_complete(order_ext_info.get_admin_cookie())
        order_ids = ["3203964946221105664"]
        for order_id in order_ids:
            order_ext_info.get_order_info(order_id=order_id, token=token, cookies=cookies)
