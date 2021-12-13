from mongoengine import DynamicDocument, StringField, IntField, EmbeddedDocumentListField, EmbeddedDocumentField


class WxSnsImgModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "wx_sns_img",
        'indexes': [
            {
                "fields": ["sns_img_id", "from_username", "create_at"],
                'name': '_fit_'
            }
        ]
    }

    sns_img_id = StringField(required=True, unique=True, help_text='朋友圈图片id,唯一建，系统随机生成')
    from_username = StringField(help_text='所属账号id')
    snsId = StringField(help_text='微信朋友圈id')
    createTime = StringField(help_text='朋友圈发布时间')
    img_index = IntField(help_text='图片排序')
    img_url = StringField(help_text='图片url')
    upload_id = StringField(help_text='图片资源id')
    create_at = StringField(required=True)
    update_at = StringField(required=True)
    device_id = StringField(required=True, help_text='设备id')
    batch_id = StringField(required=True, help_text='批次id')
