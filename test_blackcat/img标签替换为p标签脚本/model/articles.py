# coding:utf-8
__author__ = 'xzc'

import arrow
from mongoengine import *



class WikiDataObj(DynamicEmbeddedDocument):
    """
    百科类型数据
    """
    url = StringField(help_text="文章来源链接")
    title = StringField(required=True, help_text="标题")
    desc = StringField(help_text="描述")
    content = StringField(required=True, help_text="内容")

class DiaryDataObj(DynamicEmbeddedDocument):
    """
    日记类型数据
    """
    content = StringField(required=True, help_text="内容")

class CoverImgObj(DynamicEmbeddedDocument):
    """
    封面图片
    """
    upload_id = StringField(help_text="资源id")
    url = StringField(help_text="图片链接")

# class TagObj(DynamicEmbeddedDocument):
#     """
#     标签
#     """
#     TAG_TYPE_ART_CATEGORY = 'art_category'   # 文章分类
#     TAG_TYPES = [
#         TAG_TYPE_ART_CATEGORY
#     ]
# 
#     type = StringField(help_text="类型", choices=TAG_TYPES)
#     tag_id = StringField(help_text="标签id")
#     name = StringField(required=True, help_text="标签名称")

class CreatorObj(DynamicEmbeddedDocument):
    """
    创建者信息
    """
    user_id = StringField(required=True, help_text="用户id")
    name = StringField(required=True, help_text="名称")

class ArticlesModel(DynamicDocument):
    """
    媒体文章
    """
    meta = {
        'strict': False,
        "collection": "articles",
        'indexes': [
            {
                "fields": ["article_id", "article_type", "author_id", "title_md5", "tags", "status", "security_type",
                           "create_at", "update_at"],
                'name': '_fit_'
            },
        ]
    }

    SYSTEM_AUTHOR_ID = '_system_'   # 系统作者id

    # 类型
    ARTICLE_TYPE_WIKI = 'wiki'          # 百科
    ARTICLE_TYPE_DIARY = 'diary'        # 日记
    ARTICLE_TYPE_QA = 'qa'        # 问答
    ARTICLE_TYPES = [
        ARTICLE_TYPE_WIKI,
        ARTICLE_TYPE_DIARY
    ]

    # 样式
    CSS_TYPE_WECHAT = 'wehcat'  # 微信
    CSS_TYPES = [
        CSS_TYPE_WECHAT
    ]

    # 状态
    STATUS_NORMAL = 'normal'
    STATUS_TYPES = [
        STATUS_NORMAL
    ]

    # 加密类型
    SECURITY_TYPE_PRIVATE = 'private'   # 私密
    SECURITY_TYPE_PUBLIC = 'public'     # 公开
    SECURITY_TYPES = [
        SECURITY_TYPE_PRIVATE,
        SECURITY_TYPE_PUBLIC
    ]

    # 标签
    TAG_AD = 'ad'   # 广告

    article_id = StringField(required=True, unique=True, help_text='文章id，唯一')
    article_type = StringField(required=True, help_text='类型', choices=ARTICLE_TYPES)
    author_id = StringField(required=True, help_text='作者id')
    publish_at = StringField(help_text='发布时间')
    title_md5 = StringField(help_text='标题md5，文章类型时唯一')
    css_type = StringField(required=True, help_text='样式类型', choices=CSS_TYPES, default=CSS_TYPE_WECHAT)
    wiki_data = EmbeddedDocumentField(WikiDataObj, help_text='百科类型数据')
    diary_data = EmbeddedDocumentField(DiaryDataObj, help_text='日记类型数据')
    cover_img = EmbeddedDocumentField(CoverImgObj, help_text='封面图片')
    share_img = EmbeddedDocumentField(CoverImgObj, help_text='分享图片')
    img_list = EmbeddedDocumentListField(CoverImgObj, help_text='内容图片列表')
    tags = ListField(help_text='标签列表')
    status = StringField(required=True, help_text='状态', choices=STATUS_TYPES)
    security_type = StringField(required=True, help_text='加密类型', choices=SECURITY_TYPES)
    creator = EmbeddedDocumentField(CreatorObj, required=True, help_text='创建者信息')
    create_at = StringField(required=True, help_text='创建时间')
    update_at = StringField(required=True, help_text='更新时间')

    @staticmethod
    def build_preview_article_id(author_id, article_type):
        """
        生成预览文章id
        :param author_id:
        :param article_type:
        :return:
        """
        return 'art_preview_{}_{}'.format(article_type, author_id)

    @property
    def cover_img_url(self):
        if not self.cover_img or not self.cover_img.url:
            return []
        return [self.cover_img.url]
