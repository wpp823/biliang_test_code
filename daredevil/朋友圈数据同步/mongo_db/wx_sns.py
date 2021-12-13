from mongoengine import DynamicDocument, StringField, IntField, ListField, DynamicEmbeddedDocument, \
    EmbeddedDocumentListField


class PraiseObj(DynamicEmbeddedDocument):
    meta = {'strict': False}
    wx_id = StringField(help_text='点赞人员id')
    wx_nick_name = StringField(help_text='点赞人员昵称')


class CommentObj(DynamicEmbeddedDocument):
    meta = {'strict': False}
    from_wx_id = StringField(help_text='评论人员id')
    from_wx_nick_name = StringField(help_text='评论人员昵称')
    content = StringField(help_text='评论内容')
    to_wx_id = StringField(help_text='被评论人员id')


class UploadUrlObj(DynamicEmbeddedDocument):
    meta = {'strict': False}
    upload_id = StringField(help_text='上传ossid')
    url = StringField(help_text='上传资源地址')

class WxSnsModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "wx_sns",
        'indexes': [
            {
                "fields": ["sns_id", "createTime", "create_at"],
                'name': '_fit_'
            }
        ]
    }

    sns_id = StringField(required=True, unique=True, help_text='朋友圈id,唯一建，系统随机生成')
    from_username = StringField(help_text='所属账号id')
    snsId = StringField(required=True, help_text='微信朋友圈id')
    username = StringField(help_text='微信id')
    nickname = StringField(help_text='昵称')
    remark_name = StringField(help_text='备注名')
    createTime = StringField(help_text='朋友圈发布时间')
    type = IntField(help_text='类型')
    shareTitle = StringField(help_text='分享标题')
    stringSeq = StringField(help_text='同步流水号')
    content = StringField(help_text='内容')
    praise = EmbeddedDocumentListField(PraiseObj, help_text='点赞好友列表')
    comment = EmbeddedDocumentListField(CommentObj, help_text='评论列表')
    url = ListField(help_text='链接列表')
    contentBuf = StringField(help_text='微信原始数据内容，二进制数据')
    attrBuf = StringField(help_text='微信原始数据评论点赞，二进制数组')
    create_at = StringField(help_text='入库时间')
