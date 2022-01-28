from typing import List

import arrow
import shortuuid

from model.articles import ArticlesModel, CreatorObj, CoverImgObj, WikiDataObj, DiaryDataObj


class ArticlesDao():

    def __init__(self, log):
        self.log = log
        self.collection = 'articles'

    def add_wiki_article(self, wiki_url: str, author_id: str, title: str, title_md5: str, publish_at: str, desc: str,
                         content: str, cover_img_upload_id: str, cover_img_url: str, img_list: list, tags: list,
                         security_type: str, create_user_id: str, create_user_name: str, share_img_upload_id: str,
                         share_img_url: str, article_id: str = None, ):
        """
        添加百科文章
        :param wiki_url:
        :param author_id:
        :param title:
        :param title_md5:
        :param publish_at:
        :param desc:
        :param content:
        :param cover_img_upload_id:
        :param cover_img_url:
        :param img_list:
        :param tags:
        :param security_type:
        :param create_user_id:
        :param create_user_name:
        :param article_id:
        @param share_img_url:
        @param share_img_upload_id:
        :return:

        """

        try:
            now_at = arrow.now(tz='+08:00').strftime('%Y-%m-%d %H:%M:%S')

            wiki_data = {
                WikiDataObj.url.name: wiki_url if wiki_url else '',
                WikiDataObj.title.name: title,
                WikiDataObj.desc.name: desc,
                WikiDataObj.content.name: content,
            }

            cover_img = {
                CoverImgObj.upload_id.name: cover_img_upload_id,
                CoverImgObj.url.name: cover_img_url,
            }
            share_img = {
                CoverImgObj.upload_id.name: share_img_upload_id,
                CoverImgObj.url.name: share_img_url,
            }

            img_obj_list = []
            if img_list:
                for img in img_list:
                    img_obj = CoverImgObj(**{
                        CoverImgObj.upload_id.name: img.get('upload_id', ''),
                        CoverImgObj.url.name: img['url'],
                    })
                    img_obj_list.append(img_obj)

            if not tags:
                tags = []

            creator = {
                CreatorObj.user_id.name: create_user_id,
                CreatorObj.name.name: create_user_name,
            }

            info = {
                ArticlesModel.article_id.name: article_id if article_id else 'art_{}'.format(shortuuid.random(12)),
                ArticlesModel.article_type.name: ArticlesModel.ARTICLE_TYPE_WIKI,
                ArticlesModel.author_id.name: author_id,
                ArticlesModel.publish_at.name: publish_at if publish_at else now_at,
                ArticlesModel.title_md5.name: title_md5,
                ArticlesModel.css_type.name: ArticlesModel.CSS_TYPE_WECHAT,
                ArticlesModel.wiki_data.name: WikiDataObj(**wiki_data),
                ArticlesModel.cover_img.name: CoverImgObj(**cover_img),
                ArticlesModel.img_list.name: img_obj_list,
                ArticlesModel.tags.name: tags,
                ArticlesModel.status.name: ArticlesModel.STATUS_NORMAL,
                ArticlesModel.security_type.name: security_type,
                ArticlesModel.creator.name: CreatorObj(**creator),
                ArticlesModel.create_at.name: now_at,
                ArticlesModel.update_at.name: now_at,
                ArticlesModel.share_img.name: CoverImgObj(**share_img),

            }
            info_obj = ArticlesModel(**info)

            res = ArticlesModel.save(info_obj)

        except Exception as e:
            if self.log:
                self.log.exception('[add_wiki_article]')
            return False
        return res

    def add_diary_article(self, author_id: str, content: str, publish_at: str, img_list: list, tags: list,
                          security_type: str, create_user_id: str, create_user_name: str, share_img_upload_id: str,
                          share_img_url: str):
        """
        添加日记文章
        :param author_id:
        :param content:
        :param publish_at:
        :param img_list:
        :param tags:
        :param security_type:
        :param create_user_id:
        :param create_user_name:
        :return:
        @param share_img_url:
        @param share_img_upload_id:
        """

        try:
            now_at = arrow.now(tz='+08:00').strftime('%Y-%m-%d %H:%M:%S')

            diary_data = {
                DiaryDataObj.content.name: content,
            }

            img_obj_list = []
            if img_list:
                for img in img_list:
                    img_obj = CoverImgObj(**{
                        CoverImgObj.upload_id.name: img.get('upload_id', ''),
                        CoverImgObj.url.name: img['url'],
                    })
                    img_obj_list.append(img_obj)

            if not tags:
                tags = []

            creator = {
                CreatorObj.user_id.name: create_user_id,
                CreatorObj.name.name: create_user_name,
            }

            share_img = {
                CoverImgObj.upload_id.name: share_img_upload_id,
                CoverImgObj.url.name: share_img_url,
            }

            info = {
                ArticlesModel.article_id.name: 'art_{}'.format(shortuuid.random(12)),
                ArticlesModel.article_type.name: ArticlesModel.ARTICLE_TYPE_DIARY,
                ArticlesModel.author_id.name: author_id,
                ArticlesModel.publish_at.name: publish_at if publish_at else now_at,
                ArticlesModel.css_type.name: ArticlesModel.CSS_TYPE_WECHAT,
                ArticlesModel.diary_data.name: DiaryDataObj(**diary_data),
                ArticlesModel.img_list.name: img_obj_list,
                ArticlesModel.tags.name: tags,
                ArticlesModel.status.name: ArticlesModel.STATUS_NORMAL,
                ArticlesModel.security_type.name: security_type,
                ArticlesModel.creator.name: CreatorObj(**creator),
                ArticlesModel.create_at.name: now_at,
                ArticlesModel.update_at.name: now_at,
                ArticlesModel.share_img.name: CoverImgObj(**share_img),

            }
            info_obj = ArticlesModel(**info)

            res = ArticlesModel.save(info_obj)

        except Exception as e:
            if self.log:
                self.log.exception('[add_wiki_article]')
            return False
        return res

    def update_wiki_article(self, author_id: str, article_id: str, wiki_url: str = None, title: str = None,
                            title_md5: str = None, publish_at: str = None, desc: str = None, content: str = None,
                            cover_img_upload_id: str = None, cover_img_url: str = None, img_list: list = None,
                            tags: list = None, share_img_upload_id: str = None, share_img_url: str = None, security_type: str = None):
        """
        更新百科文章，只更新非NONE字段
        :param article_id:
        :param wiki_url:
        :param author_id:
        :param title:
        :param title_md5:
        :param publish_at:
        :param desc:
        :param content:
        :param cover_img_upload_id:
        :param cover_img_url:
        :param img_list:
        :param tags:
        :param security_type:
        :return:
        @param share_img_url:
        @param share_img_upload_id:
        """

        try:
            now_at = arrow.now(tz='+08:00').strftime('%Y-%m-%d %H:%M:%S')

            fit = {
                ArticlesModel.article_id.name: article_id,
                ArticlesModel.article_type.name: ArticlesModel.ARTICLE_TYPE_WIKI,
                ArticlesModel.author_id.name: author_id,
            }

            update_info = {}
            if wiki_url is not None:
                update_info.update({
                    '{}.{}'.format(ArticlesModel.wiki_data.name, WikiDataObj.url.name): wiki_url
                })
            if title is not None:
                update_info.update({
                    '{}.{}'.format(ArticlesModel.wiki_data.name, WikiDataObj.title.name): title
                })
            if title_md5 is not None:
                update_info.update({
                    ArticlesModel.title_md5.name: title_md5
                })
            if publish_at is not None:
                update_info.update({
                    ArticlesModel.publish_at.name: publish_at
                })
            if desc is not None:
                update_info.update({
                    '{}.{}'.format(ArticlesModel.wiki_data.name, WikiDataObj.desc.name): desc
                })
            if content is not None:
                update_info.update({
                    '{}.{}'.format(ArticlesModel.wiki_data.name, WikiDataObj.content.name): content
                })
            if cover_img_upload_id is not None:
                update_info.update({
                    '{}.{}'.format(ArticlesModel.cover_img.name, CoverImgObj.upload_id.name): cover_img_upload_id
                })
            if cover_img_url is not None:
                update_info.update({
                    '{}.{}'.format(ArticlesModel.cover_img.name, CoverImgObj.url.name): cover_img_url
                })
            if share_img_upload_id is not None:
                update_info.update({
                    '{}.{}'.format(ArticlesModel.share_img.name, CoverImgObj.upload_id.name): share_img_upload_id
                })
            if share_img_url is not None:
                update_info.update({
                    '{}.{}'.format(ArticlesModel.share_img.name, CoverImgObj.url.name): share_img_url
                })
            if img_list is not None:
                update_info.update({
                    ArticlesModel.img_list.name: img_list
                })
            if tags is not None:
                update_info.update({
                    ArticlesModel.tags.name: tags
                })
            if security_type is not None:
                update_info.update({
                    ArticlesModel.security_type.name: security_type
                })

            if not update_info:
                return False

            update_info[ArticlesModel.update_at.name] = now_at
            update = {
                "$set": update_info
            }
            return ArticlesModel.objects(__raw__=fit).update(__raw__=update)

        except Exception as e:
            if self.log:
                self.log.exception('[update_wiki_article]')
            return False

    def update_diary_article(self, author_id: str, article_id: str, publish_at: str = None, content: str = None,
                             img_list: list = None, tags: list = None, security_type: str = None,
                             share_img_upload_id: str = None, share_img_url: str = None, ):
        """
        更新日记文章，只更新非NONE字段
        :param article_id:
        :param author_id:
        :param publish_at:
        :param content:
        :param img_list:
        :param tags:
        :param security_type:
        :return:
        @param share_img_url:
        @param share_img_upload_id:
        """

        try:
            now_at = arrow.now(tz='+08:00').strftime('%Y-%m-%d %H:%M:%S')

            fit = {
                ArticlesModel.article_id.name: article_id,
                ArticlesModel.article_type.name: ArticlesModel.ARTICLE_TYPE_DIARY,
                ArticlesModel.author_id.name: author_id,
            }

            update_info = {}

            if publish_at is not None:
                update_info.update({
                    ArticlesModel.publish_at.name: publish_at
                })

            if content is not None:
                update_info.update({
                    '{}.{}'.format(ArticlesModel.diary_data.name, WikiDataObj.content.name): content
                })

            if img_list is not None:
                update_info.update({
                    ArticlesModel.img_list.name: img_list
                })
            if tags is not None:
                update_info.update({
                    ArticlesModel.tags.name: tags
                })
            if security_type is not None:
                update_info.update({
                    ArticlesModel.security_type.name: security_type
                })

            if share_img_upload_id is not None:
                update_info.update({
                    '{}.{}'.format(ArticlesModel.share_img.name, CoverImgObj.upload_id.name): share_img_upload_id
                })
            if share_img_url is not None:
                update_info.update({
                    '{}.{}'.format(ArticlesModel.share_img.name, CoverImgObj.url.name): share_img_url
                })

            if not update_info:
                return False

            update_info[ArticlesModel.update_at.name] = now_at
            update = {
                "$set": update_info
            }
            return ArticlesModel.objects(__raw__=fit).update(__raw__=update)

        except Exception as e:
            if self.log:
                self.log.exception('[update_diary_article]')
            return False

    def get_wiki_by_title_md5(self, title_md5: str, fields: list, security_type: str = None,
                              exclude_article_id: str = None):
        """
        标题获取百科文章
        :param title_md5:
        :param fields:
        :param exclude_article_id: 排除的文章id
        :param security_type: 私密类型
        :return:
        """
        fit = {
            ArticlesModel.article_type.name: ArticlesModel.ARTICLE_TYPE_WIKI,
            ArticlesModel.title_md5.name: title_md5
        }
        if security_type:
            fit[ArticlesModel.security_type.name] = security_type

        if exclude_article_id:
            fit[ArticlesModel.article_id.name] = {"$ne": exclude_article_id}

        res = ArticlesModel.objects(__raw__=fit).only(*fields).first()

        return res

    def get_wiki_by_id(self, article_id: str, fields: list, author_id: str = None):
        """
        获取百科文章

        :param author_id:
        :param article_id:
        :param fields:
        :return:
        """
        fit = {
            ArticlesModel.article_id.name: article_id,
            ArticlesModel.article_type.name: ArticlesModel.ARTICLE_TYPE_WIKI,
        }
        if author_id:
            fit[ArticlesModel.author_id.name] = author_id

        res = ArticlesModel.objects(__raw__=fit).only(*fields).first()

        return res

    def del_wiki_by_id(self, article_id: str, author_id: str = None):
        '''
        删除百科 日记文章

        :param article_id:
        :param author_id:
        :return:
        '''
        fit = {
            ArticlesModel.article_id.name: article_id,
        }
        if author_id:
            fit[ArticlesModel.author_id.name] = author_id

        res = ArticlesModel.objects(__raw__=fit).delete()
        return res

    def get_author_wiki_articles(self, author_id, fields: list, security_type: str = None, sort='-create_at',
                                 begin=0, limit=0, get_count=False, max_create_at: str = None):
        """
        获取用户百科文章列表
        :param author_id: 用户id
        :param fields:
        :param security_type:
        :param sort:
        :param begin:
        :param limit:
        :param get_count:
        :param max_create_at:
        :return:
        """

        fit = {
            ArticlesModel.author_id.name: author_id,
            ArticlesModel.article_type.name: ArticlesModel.ARTICLE_TYPE_WIKI,
        }
        if security_type:
            fit[ArticlesModel.security_type.name] = security_type

        if max_create_at:
            fit[ArticlesModel.create_at.name] = {'$lt': max_create_at}

        if get_count:
            return ArticlesModel.objects(__raw__=fit).count()

        if int(limit) == 0:
            res = ArticlesModel.objects(__raw__=fit).only(*fields).order_by(sort)
        else:
            res = ArticlesModel.objects(__raw__=fit).only(*fields).order_by(sort).skip(int(begin)).limit(int(limit))

        return res

    def get_author_diary_articles(self, author_id, fields: list, security_type: str = None, sort='-create_at',
                                  begin=0, limit=0, get_count=False, max_create_at: str = None):
        """
        获取用户日记文章列表
        :param author_id: 用户id
        :param fields:
        :param security_type:
        :param sort:
        :param begin:
        :param limit:
        :param get_count:
        :param max_create_at:
        :return:
        """

        fit = {
            ArticlesModel.author_id.name: author_id,
            ArticlesModel.article_type.name: ArticlesModel.ARTICLE_TYPE_DIARY,
        }
        if security_type:
            fit[ArticlesModel.security_type.name] = security_type

        if max_create_at:
            fit[ArticlesModel.create_at.name] = {'$lt': max_create_at}

        if get_count:
            return ArticlesModel.objects(__raw__=fit).count()

        if int(limit) == 0:
            res = ArticlesModel.objects(__raw__=fit).only(*fields).order_by(sort)
        else:
            res = ArticlesModel.objects(__raw__=fit).only(*fields).order_by(sort).skip(int(begin)).limit(int(limit))

        return res

    def get_diary_by_id(self, article_id: str, fields: list, author_id: str = None):
        """
        获取日记文章
        :param author_id:
        :param article_id:
        :param fields:
        :return:
        """
        fit = {
            ArticlesModel.article_id.name: article_id,
            ArticlesModel.article_type.name: ArticlesModel.ARTICLE_TYPE_DIARY,
        }
        if author_id:
            fit[ArticlesModel.author_id.name] = author_id

        res = ArticlesModel.objects(__raw__=fit).only(*fields).first()

        return res

    def get_by_article_ids(self, article_ids: list, fields: list):
        """
        批量获取文章
        :param article_ids:
        :param fields:
        :return:
        """
        fit = {
            ArticlesModel.article_id.name: {"$in": article_ids},
        }
        res = ArticlesModel.objects(__raw__=fit).only(*fields)
        return res

    def get_articles(self, article_type: str, exclude_article_ids: list, count: int, fields: list,
                     security_type: str = None, exclude_author_ids: list = None, author_id: str = None,
                     sort='-create_at'):
        """
        获取文章列表
        :param article_type:
        :param exclude_article_ids:
        :param exclude_author_ids:
        :param count:
        :param fields:
        :param security_type:
        :param author_id:
        :param sort:
        :return:
        """

        fit = {
            ArticlesModel.article_type.name: article_type,
        }
        if security_type:
            fit[ArticlesModel.security_type.name] = security_type

        if exclude_article_ids:
            fit[ArticlesModel.article_id.name] = {"$nin": exclude_article_ids}

        if exclude_author_ids:
            fit[ArticlesModel.author_id.name] = {"$nin": exclude_author_ids}

        if author_id:
            fit[ArticlesModel.author_id.name] = author_id

        res = ArticlesModel.objects(__raw__=fit).only(*fields).order_by(sort).skip(0).limit(int(count))
        return res

    def get_by_author_id(self, author_id: str, article_type: str, fields: List, pos: int, count: int):
        """
        获取指定作者用户的文章信息
        """
        fit = {
            ArticlesModel.author_id.name: author_id,
            ArticlesModel.article_type.name: article_type,
            ArticlesModel.security_type.name: ArticlesModel.SECURITY_TYPE_PUBLIC,
        }
        sort_key = "-{}".format(ArticlesModel.create_at.name)

        res = ArticlesModel.objects(__raw__=fit).only(*fields).order_by(sort_key).skip(pos).limit(count)

        return res

    def get_all_author_ids(self, article_type: str = None):
        """
        获取所有作者id
        :return:
        """
        fit = {}
        if article_type:
            fit[ArticlesModel.article_type.name] = article_type

        pipeline = [
            {'$match': fit},
            {
                '$group': {
                    '_id': "$author_id"
                }
            },
        ]
        res = ArticlesModel.objects().aggregate(*pipeline)

        author_ids = []
        if res:
            for data in res:
                author_ids.append(data['_id'])

        return author_ids

    def update_share_img(self, article_id: str, upload_id: str, url: str):
        """
        更新分享缩略图内容

        @param article_id:
        @param upload_id:
        @param url:
        @return:
        """
        fit = {
            ArticlesModel.article_id.name: article_id
        }
        update_info = {
            "$set": {
                f"{ArticlesModel.share_img.name}.{CoverImgObj.upload_id.name}": upload_id,
                f"{ArticlesModel.share_img.name}.{CoverImgObj.url.name}": url
            }
        }

        return ArticlesModel.objects(__raw__=fit).update(__raw__=update_info)

    def get_share_img(self, article_id: str):
        """
        获取分享缩略图内容

        @param article_id:
        @return:
        """
        fit = {
            ArticlesModel.article_id.name: article_id
        }
        fields = [
            f"{ArticlesModel.share_img.name}.{CoverImgObj.upload_id.name}",
            f"{ArticlesModel.share_img.name}.{CoverImgObj.url.name}"
        ]

        return ArticlesModel.objects(__raw__=fit).only(*fields).first()

    def get_ad_content(self,fields:List):
        """
        获取tag为ad的内容
        :return:
        """
        fit = {
            ArticlesModel.tags.name: "ad",
            ArticlesModel.article_type.name: ArticlesModel.ARTICLE_TYPE_WIKI
        }


        return ArticlesModel.objects(__raw__=fit).only(*fields)

    def update_wiki_data_content(self,article_id:str,new_content:str):
        """
        更新文章内容的content数据

        :param article_id:
        :param new_content:
        :return:
        """
        fit = {
            ArticlesModel.article_id.name: article_id,
            ArticlesModel.article_type.name: ArticlesModel.ARTICLE_TYPE_WIKI
        }
        update_info = {
            "$set":{
                f"{ArticlesModel.wiki_data.name}.{WikiDataObj.content.name}":new_content
            }
        }

        return ArticlesModel.objects(__raw__=fit).update(__raw__=update_info)

