
import re
from mongoengine import DynamicDocument, StringField,  IntField, ListField

class WxContactsModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "wx_contacts",
        'indexes': [
            {
                "fields": ["type", "from_username", "username", "contactLabel", "create_at", 'nickname', "country",
                           "province", "city", "last_chat_at", "add_friend_at", "conRemark"],
                'name': '_fit2_'
            },
        ]
    }

    contact_id = StringField(required=True, unique=True, help_text='唯一id')
    type = IntField(required=True, help_text='微信联系人类型，-1为自定义特殊类型，表示未在用户联系人列表')
    from_username = StringField(required=True, unique_with='username', help_text='所属帐号id')
    username = StringField(required=True, help_text='微信id')
    alis = StringField(help_text='别名')
    nickname = StringField(required=True, help_text='昵称')
    conRemark = StringField(help_text='备注名')
    smallheadimgurl = StringField(help_text='头像小图')
    bigheadimgurl = StringField(help_text='头像大图')
    lastupdatetime = IntField(help_text='头像最后更新时间')
    contactLabel = ListField(help_text='标签列表')
    regionCode = StringField(help_text='地区码')
    regionName = StringField(help_text='地区名称')
    signature = StringField(help_text='个性签名')
    sex = IntField()
    country = StringField()  # 国家
    province = StringField()  # 省份
    city = StringField()  # 城市
    create_at = StringField(required=True)
    update_at = StringField(required=True)
    create_user_id = StringField(required=True, help_text='操作用户id')
    device_id = StringField(required=True, help_text='设备id')
    batch_id = StringField(required=True, help_text='批次id')
    last_chat_at = StringField(help_text='最近聊天时间')
    add_friend_at = StringField(help_text='添加好友时间，无则使用首次聊天时间')


    @property
    def show_name(self):
        if self.conRemark:
            return self.conRemark
        return self.nickname


    @property
    def tag_telephone(self):
        """
        获取标签手机号
        :return:
        """
        telephone = None
        if self.contactLabel:
            for tag in self.contactLabel:
                find_data = re.findall(r'(1\d{10})(?!\d)', tag)
                if find_data:
                    telephone = find_data[0]
                    break
        return telephone