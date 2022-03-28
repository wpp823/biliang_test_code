
import requests

url = "https://bigsubs-api.uc.cn/api/bigsubs/48e1193d809c42a29a23be082e2526ba/frontpage?sub_type=wm&ut=AAKZrCDGNmK%2FSzZAG3vBuZiSR3VQo%2BviXPERFt7MBkHWXg%3D%3D&uc_param_str=frdnpfvecpntgibiniprdswiutmt&app=ucweb&b_version=0.4"

payload={}
headers = {
  'authority': 'bigsubs-api.uc.cn',
  'pragma': 'no-cache',
  'cache-control': 'no-cache',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
  'sec-ch-ua-platform': '"macOS"',
  'accept': '*/*',
  'origin': 'http://a.mp.uc.cn',
  'sec-fetch-site': 'cross-site',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'http://a.mp.uc.cn/',
  'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
