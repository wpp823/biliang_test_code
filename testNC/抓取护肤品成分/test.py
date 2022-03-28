import json

import requests
from bs4 import BeautifulSoup

url = "https://www.dongchedi.com/article/7074483343471116814"
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}
res = requests.get(url=url, headers=headers)
# with open("index.html", 'w') as dd:
#     dd.write(res.content.decode("utf-8"))

print(res.content.decode("utf-8"))
soup = BeautifulSoup(res.content.decode("utf-8"), 'lxml')

tags = soup.find_all("script", {"id": "__NEXT_DATA__"})
for tag in tags:
    text_str = tag.text
    obj = json.loads(text_str)
    print(tag.text)
print(tags)
pass
