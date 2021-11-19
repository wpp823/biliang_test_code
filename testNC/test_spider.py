import urllib3
import urllib.request
import requests
url = 'https://detail.1688.com/offer/617510835936.html?spm=a261y.7663282.10811813088311.5.5dea6d19ODCO3U&sk=consign'

# print(dir(urllib3))
#
# response = urllib3.request.RequestMethods().urlopen(url=product_url,method="GET")
#
# result = response.read()
# print(result)


from urllib import request
import ssl
#
ssl._create_default_https_context = ssl._create_unverified_context
#
response = request.urlopen(url, data=None, timeout=10)
page = response.read().decode('utf-8')

print(page)

