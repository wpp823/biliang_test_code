from urllib.parse import urlparse

from furl import furl

url = 'https://allmark.puzhizhuhai.com/msws/wiki.html#/wiki?article_id=art_tP4NP7jSiz6A&author_id=d_SoBpMN5kUF&beast_session_id=bea_xsUUrW9yXUZkRe-KgFD-uZUeN4cnmFbDaG8.'
url_data = furl(url)
# url_path = url_data.path
# print(url_path)
url_params = url_data.fragment.query.params
print(url_params)

param_dict = {
    item.split("=")[0]: item.split("=")[1] if item.split("=")[1] else ""
    for item in url_params
}
print(url_params)

article_type = url_data.path.split('/')[-1].replace(".html", "")
print(article_type)
article_id = param_dict.get("article_id",None)
print(article_id)

# article_id = url_params.pw
