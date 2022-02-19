import requests

# 要爬取的商品链接
from my_log import get_logger

URL_LIST = ['https://detail.1688.com/offer/617510835936.html',
            'https://detail.1688.com/offer/642528184608.html',
            "https://detail.1688.com/offer/641350703652.html"
            ]


class product_1688_spider():
    def __init__(self):
        self.log = get_logger()
        self.cookie = "t=9eda4dd0f4a9ed7037f711c9d41256fd; _tb_token_=7783116e58e37; cookie2=10b1eec4f6c9360d64df6cf1ea0757c9; dnk=\u5316\u7FBD\u800C\u8499; uc1=existShop=false&pas=0&cookie16=Vq8l+KCLySLZMFWHxqs8fwqnEw==&cookie14=UoewAwkrBb6brA==&cookie15=UtASsssmOIJ0bQ==&cookie21=UtASsssmeW6lpyd+B+3t; uc3=lg2=URm48syIIVrSKA==&vt3=F8dCvU11iPqOLMdb+qI=&nk2=2HdzFy1m64E=&id2=UUpjN48kKb7fmg==; tracknick=\u5316\u7FBD\u800C\u8499; lid=化羽而蒙; _l_g_=Ug==; uc4=nk4=0@2kK+x8kybn4/ugsNsCMmzEfpaw==&id4=0@U2gp9xpJ1a/8n149nGevdZX/sqMI; unb=2221680851; lgc=\u5316\u7FBD\u800C\u8499; cookie1=VAKIlZrEy18GfYt/FIpBMbAelaizc9qmpOIshC4OiUU=; login=true; cookie17=UUpjN48kKb7fmg==; _nk_=\u5316\u7FBD\u800C\u8499; sgcookie=E100ZWSBs9b27ZQcWadKcPAxTWDER/8i0xO56sK8SSmNCf9i7evUDOiBLUVhwNTpReozrc5BL6pQPp3DW6j7k8cx9l/77K7JP9R5P2PGuWEhEU8w2sAmtLpbCh4qUdTGYnDr; cancelledSubSites=empty; sg=蒙18; csg=483df1e7; cna=eL1JGu53uGQCAbcw8OxRCT/y; xlly_s=1; x5sec=7b22617365727665723b32223a223637346134336465646238323564353934363463653338663865303861643636434e627a7949384745497173774a6e6130367a4d4a686f4d4d6a49794d5459344d4467314d5473784d4b323673367743227d; pnm_cku822=098#E1hvNvvUvbpvUvCkvvvvvjiWR2MU0jYbRsqygjEUPmPOgj1RRs5wgjtUP2Fpzjl8i9hvCvvvpZpRvpvhvv2MMq9Cvm9vvhCcvvvvvvvvBGwvvUHBvvCj1Qvvv3QvvhNjvvmC/vvvBGwvvUjgkvhvC9hvpyjyz89Cvv9vvhhM4+LqsQ9CvhAvjvI8jc7xhfvAOyTDYEkOei107reYr2UpVj+O3w0AhCyXJ9kx6fItn1vDN+1l5d8rjC61D76XdiTAVA3l+b8rj8tYVVzUd34AdcUSvvhvC9mvphvvv29CvvpvvhCv; enc=CE3Q/8XOIyIqfYChUcRpyKyb7li3WjWr/Ij3HACZ3TKiMjtYn2XX7oxPc3gFDWSHBhL1xQxRYO6cEkpnpQ7KyA==; tfstk=cKaPBmVpX22XkpuCX4gFACok5udRZGFutElsqu9Imbc1iAmliV9KiSEmgXO2K0f..; l=eBIE6fG4gdn_GpMSBOfZlurza77TvIRAguPzaNbMiOCPO9CW5dvOW6L2s-TXCnGVh6KWR3Pe9lMDBeYBcIfRCSBNa6Fy_Ckmn; isg=BB4erg2t87udzyffwdwH9vZAb7Jg3-JZRyHQPcinsWFc677FMGlOa-iJ5_dnU9px"
        self.header = {
            "user-agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0",
            'Connection': 'close',
            "Accept-Encoding": "Gzip",
        }

        # self.brodwer = ''

    def download_one_page_with_no_proxy(self, url):
        """
        无代理下载网页

        :return:
        """
        response = requests.get(url, headers=self.header, cookies=self.cookie)
        filename = "test.html"
        if response:
            with open(filename, 'w') as f:
                f.write(response.text)
        print(response.text)


if __name__ == '__main__':
    tool = product_1688_spider()
    tool.download_one_page_with_no_proxy(url="https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-22228839995.44.628e79c7BnwYYA&id=606744628264")
    # for url in URL_LIST:
# download_one_page(url)
