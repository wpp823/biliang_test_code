from mongoengine import DynamicEmbeddedDocument, DynamicDocument, EmbeddedDocumentField, \
    StringField, IntField, ListField, EmbeddedDocumentListField, BooleanField

# 搜索范围
from Nightcrawler_client.constant import SPU_STATUS, SS_SPU_STATUS_ON, SPU_EDIT_STATUS, SS_SPU_EDIT_STATUS_SUCC, \
    SS_SOURCE, SS_SELL_OTHER

DOC_SEARCH_ACOPE_ALL = "all"
DOC_SEARCH_ACOPE_COLLECTION = "collection"

# 自定义属性名称
KEYWORD_CATE_KIND = "kind"
KEYWORD_CATE_FUNCTION = "function"
KEYWORD_CATE_BRAND = "brand"
KEYWORD_CATE_DISEASE = "disease"
KEYWORD_CATE_TITLE = "title"
# 排序关键字
SORT_KEY_NORMAL = 'normal'
SORT_KEY_SALE_ASC = 'sale_asc'
SORT_KEY_SALE_DESC = 'sale_desc'
SORT_KEY_PRICE_ASC = 'price_asc'
SORT_KEY_PRICE_DESC = 'price_desc'
SORT_KEY_HOTVAL_ASC = 'hotval_asc'
SORT_KEY_HOTVAL_DESC = 'hotval_dsec'

SORT_DICT = {
    SORT_KEY_NORMAL: "-order_id",  # 默认id排序，id大在前面。
    SORT_KEY_SALE_ASC: "+sales_volume",  # 销量升序
    SORT_KEY_SALE_DESC: "-sales_volume",  # 销量降序
    SORT_KEY_PRICE_ASC: "+min_price",  # 价格升序
    SORT_KEY_PRICE_DESC: "-max_price",  # 价格降序
    SORT_KEY_HOTVAL_ASC: "+min_expect_hot_value",  # 热力值升序
    SORT_KEY_HOTVAL_DESC: "-max_expect_hot_value"  # 热力值降序
}

# 过滤字段，列表中的字段不执行更新
# 自动同步更新过滤更新字段
SYNC_FILTER_FIELDS = []
# 手动导入过滤更新字段
IMPORT_FILTER_FIELDS = []

# is_test_product
ATTRS_IS_TEST_PRODUCT_KEY = "test"


class CatsObj(DynamicEmbeddedDocument):
    meta = {'strict': False}
    cat_id = IntField(help_text="")
    level = IntField(help_text="")


class DescInfoObj(DynamicEmbeddedDocument):
    # 商品描述信息
    meta = {'strict': False}
    imgs = ListField(help_text="描述信息")


class AttrsObj(DynamicEmbeddedDocument):
    # 产品分类信息
    meta = {'strict': False}
    attr_key = StringField(help_text='分类类别')
    attr_value = StringField(help_text='分类名称')


class CategoryObj(DynamicEmbeddedDocument):
    # 自定义产品分类信息
    meta = {'strict': False}
    cate_id = StringField(help_text='分类类别')
    name = StringField(help_text='分类名称')


class SkuMsgObj(DynamicEmbeddedDocument):
    # 商品sku信息

    meta = {'strict': False}

    # sku状态
    SS_SKU_STATUS_ING = 5  # 上架中
    SS_SKU_STATUS_FALSE_DEL = 21  # 假删除
    SS_SKU_STATUS_UNKNOW_1 = 1  # 未知状态，猜测为草稿状态
    SS_SKU_STATUS = [SS_SKU_STATUS_ING, SS_SKU_STATUS_FALSE_DEL, SS_SKU_STATUS_UNKNOW_1]

    # sku库存类型 默认0: 获取草稿库存, 1: 获取线上真实库存
    SS_SKU_NEED_REAL_STOCK_DRAFT = 0  # 草稿库存
    SS_SKU_NEED_REAL_STOCK_ONLINE = 1  # 线上真实库存

    # sku数据类型 默认0: 获取线上数据, 1: 获取草稿数据
    SS_SKU_NEED_EDIT_ONLINE = 0  # 线上数据
    SS_SKU_NEED_EDIT_DRAFT = 1  # 草稿数据

    sku_id = IntField(help_text="交易组件内部skuID")
    out_sku_id = StringField(help_text="商家定义skuID")
    thumb_img = StringField(help_text="sku小图")
    sale_price = IntField(help_text="售卖价格（分）")
    market_price = IntField(help_rext="市场价格（分）")
    stock_num = IntField(help_text="库存")
    barcode = StringField(help_text="条形码")
    sku_code = StringField(help_text="商品编码")
    status = IntField(help_text="sku状态", choices=SS_SKU_STATUS, default=SS_SKU_STATUS_ING)
    sku_attrs = EmbeddedDocumentListField(AttrsObj, help_text="sku信息")

    create_time = StringField(help_text="创建时间")  # utc
    update_time = StringField(elp_text="更新时间")  # utc

    expect_hot_value = IntField(help_text="预估热力值")  # 医生端可见
    my_price = IntField(help_text="导入价格")

    @property
    def hot_value(self):
        """
        热力值
        :return:
        """
        return self.expect_hot_value if self.expect_hot_value else 0


# class HotValueObj(DynamicEmbeddedDocument):
#     doctor_id = StringField(help_text="")
#     value = StringField(help_text="热力值")

class RegionHotValueObj(DynamicEmbeddedDocument):
    """
    区域热力值详情

    """
    region_id = StringField(help_text="代理商id")
    partner_id = StringField(help_text="合伙人id")
    region_hot_val = IntField(help_text="区域产品热力值")  # 导入时更新
    product_max_hot_val = IntField(help_text="区域最大热力值")
    product_min_hot_val = IntField(help_text="区域最小热力值")

class ProductModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "products",
        'indexes': [
            {
                "fields": ["product_id", "title", "out_product_id", "status", "edit_status"],
                'name': '_product_fit_'
            }
        ]
    }
    # 自定义属性名称
    KEEYWORD_CATE_KIND = "kind"
    KEEYWORD_CATE_FUNCTION = "function"
    KEEYWORD_CATE_BRAND = "brand"
    KEEYWORD_CATE_DISEASE = "disease"

    # # 商品状态
    # SS_SPU_STATUS_ON = 5  # 上架
    # SS_SPU_STATUS_INIT = 0  # 初始值
    # SS_SPU_STATUS_RECY = 6  # 回收站
    # SS_SPU_STATUS_DELE = 9  # 逻辑删除
    # SS_SPU_STATUS_OFF = 11  # 自主下架
    # SS_SPU_STATUS_VIOL = 13  # 违规下架/风控系统下架
    # SS_SPU_STATUS_OUT = 12  # 售磬下架
    #
    # SPU_STATUS = [
    #     SS_SPU_STATUS_ON,
    #     SS_SPU_STATUS_INIT,
    #     SS_SPU_STATUS_RECY,
    #     SS_SPU_STATUS_DELE,
    #     SS_SPU_STATUS_OFF,
    #     SS_SPU_STATUS_VIOL,
    #     SS_SPU_STATUS_OUT
    # ]
    #
    # # 商品编辑状态
    # SS_SPU_EDIT_STATUS_ON = 0  # 初始值
    # SS_SPU_EDIT_STATUS_INIT = 1  # 编辑中
    # SS_SPU_EDIT_STATUS_ING = 2  # 审核中
    # SS_SPU_EDIT_STATUS_FAIL = 3  # 审核失败
    # SS_SPU_EDIT_STATUS_SUCC = 4  # 审核成功
    #
    # SPU_EDIT_STATUS = [
    #     SS_SPU_EDIT_STATUS_ON,
    #     SS_SPU_EDIT_STATUS_INIT,
    #     SS_SPU_EDIT_STATUS_ING,
    #     SS_SPU_EDIT_STATUS_FAIL,
    #     SS_SPU_EDIT_STATUS_SUCC,
    # ]
    #
    # # 商品来源
    # SS_SELL_SELF = 1  # 自营
    # SS_SELL_OTHER = 2  # 带货

    # SS_SOURCE = [SS_SELL_SELF, SS_SELL_OTHER]

    product_id = IntField(help_text="小商店内部商品ID")
    out_product_id = StringField(help_text="商家自定义商品ID")
    title = StringField(help_text="标题")
    sub_title = StringField(help_text="副标题")
    head_img = ListField(help_text="主图, 多张, 列表")
    desc_info = EmbeddedDocumentField(DescInfoObj, help_text="商品详情，图文(目前只支持图片)")
    brand_id = IntField(help_text="品牌,商家需要申请")
    status = IntField(choices=SPU_STATUS, help_text="商品线上状态", default=SS_SPU_STATUS_ON)
    edit_status = IntField(help_text="商品草稿状态", choices=SPU_EDIT_STATUS, default=SS_SPU_EDIT_STATUS_SUCC)
    min_price = IntField(help_text="商品SKU最小价格（单位：分）")
    max_price = IntField(help_text="商品SKU最大价格（单位：分）")
    path = StringField(help_text="小程序页面路径")
    cats = EmbeddedDocumentListField(CatsObj, help_text="类目信息")
    attrs = EmbeddedDocumentListField(AttrsObj, help_text="属性信息")
    model = StringField(help_text="商品型号")

    source = IntField(help_text="默认1, 1: 小商店自营商品, 2:带货商品", choices=SS_SOURCE, default=SS_SELL_OTHER)
    skus = EmbeddedDocumentListField(SkuMsgObj, help_text="skuID")

    create_time = StringField(help_text="创建时间")  # utc
    update_time = StringField(elp_text="更新时间")  # utc

    collection_doctors = ListField(help_text="收藏医生列表")
    # 自定义字段
    kind = EmbeddedDocumentListField(CategoryObj, help_text="种类")
    my_price = IntField(help_text="导入价格")
    function = EmbeddedDocumentListField(CategoryObj, help_text="功效")
    disease = EmbeddedDocumentListField(CategoryObj, help_text="病症")

    brand = EmbeddedDocumentListField(CategoryObj, help_text="品牌名称")
    sales_volume = IntField(help_text="销量")
    is_test_product = BooleanField(default=False, help_text="是否测试商品")

    min_expect_hot_value = IntField(help_text="商品最大热力值")  # 数据导入时进行对比更新
    max_expect_hot_value = IntField(help_text="商品最小热力值")  # 数据导入时进行对比更新

    order_id = IntField(help_text="默认排序id")  # 默认排序id 数据导入时进行

    region_hot_values = EmbeddedDocumentListField(RegionHotValueObj,help_text="区域热力值列表")


class ProductActionModel(DynamicDocument):
    '''
    此模型用于记录基于产品的操作纪录，
    原则上"product_id", "user_id",'action'这三个字段联合唯一键。
    '''
    meta = {
        'strict': False,
        "collection": "product_action",
        'indexes': [
            {
                "fields": ["product_id", "user_id", 'action'],
                'name': '_product_user_',
                # 'unique': True
            }
        ]
    }

    AN_VIEW = 'view'  # 查看,只纪录了某个产品的推荐人。
    AN_SHARE = 'share'  # 分享

    AN_LIST = [
        AN_VIEW,  # user_id 查看了 doctor_id 给的product_id产品。
        AN_SHARE
    ]
    create_time = StringField(help_text="创建时间")  # +08
    product_id = IntField(help_text="小商店内部商品ID", required=True)
    doctor_id = StringField(help_text='医生ID', default=None)  # 可为空
    user_id = StringField(help_text='患者ID', required=True)  # 不可为空
    action = StringField(help_text='动作名称', required=True, choices=AN_LIST, default=AN_VIEW)  # 不可为空
