

# 默认空闲时间
import arrow as arrow
from testMongoDB.users import TimeAt, IdleItem, ServiceItem, Doctor, UsersModel
from mongoengine import *

connect('beast_test')


class Doc(DynamicEmbeddedDocument):
        doc_telephone = StringField(help_text='医生手机号')  # 用于激活流程
        work_telephone = StringField(help_text='工作手机号')  # 用于关联深瞳
        enable_endorsement = BooleanField(help_text='设置医生是否开启代言', default=False)
        idle_list = EmbeddedDocumentListField(IdleItem, help_text='医生设置的空闲时间段，没有设置的天不在列表里')
        services_list = EmbeddedDocumentListField(ServiceItem, help_text='医生开启的服务列表,关闭的或没开启的不在列表中')


slot_item_mid = TimeAt(begin_hour=12, begin_minute=30, end_hour=14, end_minute=0)
slot_item_after = TimeAt(begin_hour=19, begin_minute=0, end_hour=22, end_minute=0)
default_idle = IdleItem(day=IdleItem.D_ALL, times=[slot_item_mid, slot_item_after])
# 开启业务列表
service_item = ServiceItem(code=ServiceItem.SS_CONSULT, price=int(111), )

Doc_add = {
    Doc.doc_telephone.name: '123',
    Doc.work_telephone.name: '121',
    Doc.idle_list.name: default_idle,
    Doc.services_list.name: service_item
}

res = Doc_add.save()



