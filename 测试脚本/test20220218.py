from urllib.parse import urlparse

from pz.tools.urlunit import RegularTool

url = 'https://detail.tmall.com/msws/wiki.html?article_id=xxxxxxx'
url_data = urlparse(url)
# url_path = url_data.path
# print(url_path)
# url_params = url_data.query
# print(url_params)

article_type = url_data.path.split('/')[-1].replace(".html","")
print(article_type)
article_id = url_data.query[url_data.query.index("=")+1:]
print(article_id)

# article_id = url_params.pw