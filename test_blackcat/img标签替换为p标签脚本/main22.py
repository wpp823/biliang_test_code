from bs4 import BeautifulSoup
from mongoengine import register_connection, connection

from dao.articles import ArticlesDao
from model.articles import ArticlesModel
from my_log import get_logger

MONGO_HOST_AUTH_DB = "admin"
MONGO_HOST_REPLICA_SET = None

MONGO_HOST = MONGO_HOST_PART + "/" + MONGO_HOST_AUTH_DB
MONGO_DB_NAME = 'blackcat'

register_connection(db=MONGO_DB_NAME, host=MONGO_HOST_PART, authentication_source=MONGO_HOST_AUTH_DB, replicaset=None, alias=connection.DEFAULT_CONNECTION_NAME)

if __name__ == "__main__":
    log = get_logger()
    article_dao = ArticlesDao(log=log)
    fields = [ArticlesModel.wiki_data.name, ArticlesModel.article_id.name]
    # 获取所有内容

    contents = article_dao.get_ad_content(fields=fields)
    # 替换内容


    if contents:
        for item in contents:

            source_str = item.wiki_data.content
            article_id = item.article_id
            if article_id == 'art_DWpGjPog4y9m':
                continue
            # log.info(article_id)
            # log.info(source_str)
            soup = BeautifulSoup(source_str, "html.parser")
            # log.info(soup.prettify())
            xlkk_img_tag = soup.find_all("imgs", attrs={'xlkk': True})
            for i in xlkk_img_tag:
                replacement = '<p class="shop_link"><span class="shop_link_icon"></span></p><a href="a_link">{text}</a>'
                log.info(i)
                xlkk_url = i.attrs.get("xlkk").replace("xlkk://product?","/pages/user_product/user_product?")
                log.info(i["xlkk"])
                del i["xlkk"]
                replacement = replacement.replace("a_link",xlkk_url)
                log.info(replacement)
                i.replace_with(BeautifulSoup(replacement.format(text=i), 'html.parser'))
                # i.replace_with(BeautifulSoup(replacement.format(a_link=xlkk_url), 'html.parser'))
                log.info(i)

            log.info(str(soup))
            # break
            log.info(source_str)
            update_res = article_dao.update_wiki_data_content(article_id=article_id, new_content=str(soup))
            if update_res:
                log.info(f'{article_id}_update_wiki_data_content_ok')
            else:
                log.info(f'{article_id}_update_wiki_data_content_fail')
            break
            # 更新内容
