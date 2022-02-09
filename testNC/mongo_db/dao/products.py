from typing import Set, List

import arrow

from mongo_db.model.product import ProductModel, DescInfoObj, CatsObj, SkuMsgObj, AttrsObj, CategoryObj, \
    SORT_DICT, ProductActionModel

SS_SPU_STATUS_ON = 5
TEST_PRODUCT = False


class SpuItem(dict):
    '''
    每个产品
    '''

    @property
    def title(self):
        return self.get('title')

    @property
    def head_img_first(self):
        return self.get('head_img')[0]

    @property
    def product_id(self):
        return self.get('product_id')

    @property
    def min_price(self):
        return self.get('min_price')

    @property
    def skus(self):
        return self.get('skus')

    @property
    def attrs(self):
        return self.get('attrs')

    def to_simple_dict(self):
        '''
        返回一个简单结构的字典
        :return:
        '''
        fields = ['title', 'head_img_first', 'product_id', 'min_price']

        ret_dict = {}
        for tmp_field in fields:
            ret_dict['tmp_field'] = self.__getattribute__(tmp_field)

        return ret_dict

class NoExistsProduct(Exception):
    pass


class ProductDao():

    def __init__(self, log):
        self.log = log
        self.collection = 'products'

    def add(self, spu_item: SpuItem):
        """
        添加商品
        :param spu_item: 商品dict对象
        :return:
        """
        res = True
        try:
            # 商品不存在，进行添加
            product_obj = ProductModel()
            product_obj.product_id = spu_item.get('product_id', None)
            product_obj.out_product_id = spu_item.get('out_product_id', None)
            product_obj.edit_status = spu_item.get('edit_status', None)
            product_obj.title = spu_item.get('title', None)
            product_obj.sub_title = spu_item.get('sub_title', None)
            product_obj.head_img = spu_item.get('head_img', None)
            product_obj.desc_info = DescInfoObj(**spu_item.get('desc_info', None))
            product_obj.brand_id = spu_item.get('brand_id', None)
            product_obj.status = spu_item.get('status', None)
            # product_obj.min_price = spu_item.get('min_price', None)
            product_obj.path = spu_item.get('path', None)
            if spu_item.get('cats'):
                product_obj.cats = [CatsObj(**cat) for cat in spu_item.get('cats', None)]
            if spu_item.get('attrs'):
                product_obj.attrs = [AttrsObj(**attr) for attr in spu_item.get('attrs', None)]
            product_obj.model = spu_item.get('model', None)
            product_obj.source = spu_item.get('source', None)

            price_list = []
            # 获取skus中的attr
            if spu_item.skus:

                sku_list = spu_item.skus
                for sku_item in sku_list:
                    if sku_item.sku_attrs:
                        sku_attr_list = [
                            AttrsObj(attr_key=item.get("attr_key", ""), attr_value=item.get("attr_value", ""))
                            for item in sku_item.sku_attrs]
                        sku_item[SkuMsgObj.sku_attrs.name] = sku_attr_list

                    if int(sku_item.stock_num) > 0:
                        price_list.append(sku_item.sale_price)
                product_obj.skus = [SkuMsgObj(**sku) for sku in sku_list]
            # 更新最大最小价格
            if price_list:
                product_obj.min_price = min(price_list)
                product_obj.max_price = max(price_list)

            product_obj.create_time = spu_item.get('create_time', None)
            product_obj.update_time = spu_item.get('update_time', None)

            res = ProductModel.save(product_obj)


        except:
            if self.log:
                self.log.exception("[ProductDao.add_fail][spu_item:{}]".format(spu_item))
                res = False
            return res

    def update(self, product_id: int, spu_item: SpuItem, filter_fields=[]):
        """
        更新商品信息

        :return:
        """

        fit = {
            ProductModel.product_id.name: product_id
        }
        update_time = arrow.utcnow().datetime

        if update_time:
            spu_item["update_time"] = update_time

        # 导入价格
        my_price = spu_item.get('my_price', None)
        # 产品种类
        kind = spu_item.get('kind', '')
        # 功效
        function = spu_item.get('function', '')
        # 病症
        disease = spu_item.get('disease', '')
        # 品牌名称
        brand = spu_item.get('brand', '')
        # 最大热力值
        max_expect_hot_value = spu_item.get('max_expect_hot_value', '')
        # 最小热力值
        min_expect_hot_value = spu_item.get('min_expect_hot_value', '')

        if my_price:
            spu_item['{}'.format(ProductModel.my_price.name)] = int(my_price)
        if kind:
            spu_item['{}'.format(ProductModel.kind.name)] = kind

        if function:
            spu_item['{}'.format(ProductModel.function.name)] = function

        if disease:
            spu_item['{}'.format(ProductModel.disease.name)] = disease

        if brand:
            spu_item['{}'.format(ProductModel.brand.name)] = brand

        # 更新最大热力值
        if max_expect_hot_value:
            spu_item['{}'.format(ProductModel.max_expect_hot_value.name)] = max_expect_hot_value
        # 更新最小热力值
        if min_expect_hot_value:
            spu_item['{}'.format(ProductModel.min_expect_hot_value.name)] = min_expect_hot_value

        if not spu_item:
            return False
        # 过滤不被更新的字段
        if filter_fields:
            for field_name in filter_fields:
                spu_item.pop(field_name, "404")
        # 判断sku热力值是否存在，避免覆盖
        if spu_item.skus:
            price_list = []

            sku_list = spu_item.skus
            for sku_item in sku_list:
                expect_hot_value = self.get_hotval_by_sku_id(sku_id=sku_item.sku_id, product_id=product_id)
                if expect_hot_value:
                    sku_item[SkuMsgObj.expect_hot_value.name] = expect_hot_value
                # 更新最大最小价格
                if int(sku_item.stock_num) > 0:
                    price_list.append(sku_item.sale_price)
                if price_list:
                    spu_item[ProductModel.min_price.name] = min(price_list)
                    spu_item[ProductModel.max_price.name] = max(price_list)

        update_info = {
            "$set": spu_item,
        }

        res = None
        try:
            res = ProductModel.objects(__raw__=fit).update(__raw__=update_info)
        except:
            self.log.exception(
                "[ProductDao.update_fail][product_id:{},spu_item:{}]".format(product_id, len(spu_item)))
        return res

    def get_with_no_con(self, product_id: int):
        """
        判断产品是否存在库中，无过滤条件
        :param product_id:
        :return:
        """
        fit = {
            ProductModel.product_id.name: int(product_id)
        }
        fields = [ProductModel.product_id.name]
        res = None
        try:

            res = ProductModel.objects(__raw__=fit).only(*fields).first()

        except:
            self.log.exception('[ProductDao.get_with_no_con_fail][product_id:{}]'.format(product_id))

        return res

    def get_by_product_id(self, product_id: int, fields=[]):
        """
        通过product_id获取到产品，默认过滤下架商品，sku为空，以及库存为0的商品
        :param product_id:
        :param fields:
        :return:
        """

        fit = {
            ProductModel.product_id.name: int(product_id),
            ProductModel.status.name: SS_SPU_STATUS_ON,
            ProductModel.skus.name: {
                "$exists": True,
                "$ne": []
            },
            "{}.{}".format(ProductModel.skus.name, SkuMsgObj.stock_num.name): {"$gt": 0}
        }

        res = None
        try:
            if fields:
                res = ProductModel.objects(__raw__=fit).only(*fields).first()
            else:
                res = ProductModel.objects(__raw__=fit).first()
        except:
            self.log.exception('[ProductDao.get_by_product_id_fail][product_id:{}]'.format(product_id))

        return res

    def update_sku_custom_data_by_id(self, product_id: int, sku_id: int, data: dict):
        """
        更新自定义数据
        :param product_id:
        :param sku_id:
        :param data: 数据内容
        :return:
        """
        fit = {
            ProductModel.product_id.name: product_id,
            "{}.{}".format(ProductModel.skus.name, SkuMsgObj.sku_id.name): sku_id
        }

        # 热力值
        expect_hot_value = data.get('expect_hot_value', None)
        my_price = data.get('my_price', None)
        update_info = {}

        if expect_hot_value:
            update_info['{}.$.{}'.format(ProductModel.skus.name, SkuMsgObj.expect_hot_value.name)] = int(
                expect_hot_value)
        if my_price:
            update_info['{}.$.{}'.format(ProductModel.skus.name, SkuMsgObj.my_price.name)] = int(
                my_price)

        self.log.info("[ProductDao.update_sku_custom_data_by_id][sku_id:{},data:{}]".format(sku_id, data))
        if not update_info:
            return False

        update_info = {
            "$set": update_info
        }

        return ProductModel.objects(__raw__=fit).update(__raw__=update_info)

    def get_min_hot_val(self, product_id: int):
        """
        获取最小热力值
        :param product_id:
        :return:
        """
        fit = {
            ProductModel.product_id.name: product_id
        }
        min_expect_hot_value = None
        fields = [ProductModel.min_expect_hot_value.name]
        res = ProductModel.objects(__raw__=fit).only(*fields).first()
        if res:
            min_expect_hot_value = res.min_expect_hot_value
        return min_expect_hot_value

    def get_max_hot_val(self, product_id: int):
        """
        获取最小热力值
        :param product_id:
        :return:
        """
        fit = {
            ProductModel.product_id.name: product_id
        }
        fields = [ProductModel.max_expect_hot_value.name]
        max_expect_hot_value = None
        res = ProductModel.objects(__raw__=fit).only(*fields).first()
        if res:
            max_expect_hot_value = res.max_expect_hot_value
        return max_expect_hot_value

    def set_collect(self, product_id: int, doctor_id: str):
        """
        医生添加收藏商品
        :param doctor_id:
        :param product_id:
        :return:
        """
        fit = {
            ProductModel.product_id.name: product_id
        }
        update_info = {
            "$addToSet": {
                ProductModel.collection_doctors.name: doctor_id
            }
        }
        return ProductModel.objects(__raw__=fit).update(__raw__=update_info)

    def del_collect(self, product_id: int, doctor_id: str):
        """
        医生取消收藏商品
        :param doctor_id:
        :param product_id:
        :return:
        """
        fit = {
            ProductModel.product_id.name: product_id
        }
        update_info = {
            "$pull": {
                ProductModel.collection_doctors.name: doctor_id
            }
        }
        return ProductModel.objects(__raw__=fit).update(__raw__=update_info)

    def aggregate_type(self, field_name, fit: dict = {}) -> List:
        '''
        聚合某个字段，返回去重后的值。
        :param fit: 过滤条件
        :param field_name:
        :return:
        [
        {
            name:xxxx,      #分类名称。
            cate_id:xxx     #分类ID
        },
        .....
        ]
        '''
        if not fit:
            fit = {
                ProductModel.status.name: SS_SPU_STATUS_ON,
                ProductModel.skus.name: {
                    "$exists": True,
                    "$ne": []
                },
            }

        if field_name not in [
            ProductModel.kind.name,
            ProductModel.disease.name,
            ProductModel.function.name,
            ProductModel.brand.name
        ]:
            raise NotImplementedError('The field({}) not supported'.format(field_name))

        kind_name_field_name = "{}.{}".format(field_name, CategoryObj.name.name)
        kind_id_field_name = "{}.{}".format(field_name, CategoryObj.cate_id.name)

        pipeline = [
            {"$match": fit},
            {"$project": {field_name: True}},
            {"$unwind": "${}".format(field_name)},
            {"$group": {"_id": {CategoryObj.name.name: '${}'.format(kind_name_field_name),
                                CategoryObj.cate_id.name: '${}'.format(kind_id_field_name)}}}
        ]
        res = ProductModel.objects.aggregate(*pipeline)

        res_list = []

        if res:
            res_list = [cate_item["_id"] for cate_item in res]
            sort_keys = []
            if field_name == ProductModel.kind.name:  # 按种类
                sort_keys = ['面膜', '爽肤水', '精华']
            elif field_name == ProductModel.brand.name:  # 按品牌
                sort_keys = ['森花泉', '小银罐', '广御']
            if sort_keys:
                res_list = self._type_sort_by_appoint(before_list=res_list, sort_keys=sort_keys)

        return res_list

    def _type_sort_by_appoint(self, before_list: List, sort_keys: List) -> List:
        """
        排序整理，按照指定顺序排序

        :param before_list: 未指定内容的队列
        :param sort_keys:  指定排在前面的分类名称 ，例如 ['面膜', '爽肤水', '精华']
        :return:
        """
        ret_list = []
        tmp_head_list = []
        for item in before_list:
            if item[CategoryObj.name.name] in sort_keys:  # 将这几个分类放在最前面。
                tmp_head_list.append(item)
            else:
                ret_list.append(item)
        if ret_list:
            # 不排在前面的按拼音排序,按union码排序
            ret_list = sorted(ret_list, key=lambda x: x[CategoryObj.cate_id.name][2:])
        return tmp_head_list + ret_list

    def search(self, keyword: str, page: int, page_size: int, sort_by: str, keyword_cate: str, doc_id: str,
               fields=[]) -> Set[ProductModel]:
        """
        从mongodb中过滤商品

        :param doc_id:
        :param keyword:
        :param page:
        :param page_size:
        :param sort_by:
        :param keyword_cate:
        :param fields:
        :return:
        """
        # 检索商品搜索

        # 默认过滤掉下架的商品和sku不存在的
        fit = {
            ProductModel.status.name: SS_SPU_STATUS_ON,
            ProductModel.skus.name: {
                "$exists": True,
                "$ne": []
            },
            "{}.{}".format(ProductModel.skus.name, SkuMsgObj.stock_num.name): {"$gt": 0}
        }

        page = int(page)

        if page == 0: page = 1
        begin = (page - 1) * int(page_size)
        # 默认排序
        if not sort_by: sort_by = "normal"

        # 过滤是否是测试商品
        if not TEST_PRODUCT:
            fit[ProductModel.is_test_product.name] = TEST_PRODUCT

        if keyword_cate == ProductModel.kind.name:
            fit["{}.{}".format(ProductModel.kind.name, CategoryObj.cate_id.name)] = keyword
        if keyword_cate == ProductModel.function.name:
            fit["{}.{}".format(ProductModel.function.name, CategoryObj.cate_id.name)] = keyword
        if keyword_cate == ProductModel.brand.name:
            fit["{}.{}".format(ProductModel.brand.name, CategoryObj.cate_id.name)] = keyword
        if keyword_cate == ProductModel.disease.name:
            fit["{}.{}".format(ProductModel.disease.name, CategoryObj.cate_id.name)] = keyword
        if doc_id:
            fit["{}".format(ProductModel.collection_doctors.name)] = doc_id
        if sort_by:
            sort = SORT_DICT.get(sort_by, None)

        res = None

        try:
            if fields:
                res = ProductModel.objects(__raw__=fit).only(*fields).skip(
                    int(begin)).limit(int(page_size)).order_by(sort)
            else:
                res = ProductModel.objects(__raw__=fit).skip(
                    int(begin)).limit(int(page_size)).order_by(sort)

            self.log.info(
                "[ProductDao.search_ok],[keyword:{},doc_id:{},page:{},page_size:{},keyword_cate:{}],[res_len:{}]"
                    .format(keyword, doc_id, page, page_size, keyword_cate, len(res)))
        except:
            self.log.exception(
                '[ProductDao.search_fail],[keyword:{},doc_id:{},page:{},page_size:{},keyword_cate:{}],[res_len:{}]'
                    .format(keyword, doc_id, page, page_size, keyword_cate, len(res)))

        return res

    def search_by_offset(self, keyword: str, offset: int, count: int, sort_by: str, doc_id: str, fields=[]):
        '''
        使用offset进行搜索。

        :param keyword:
        :param offset:
        :param count:
        :param sort_by:
        :param doc_id:
        :param fields:
        :return:
        '''

        # 默认过滤掉下架的商品和sku不存在的
        fit = {
            ProductModel.status.name: SS_SPU_STATUS_ON,
            ProductModel.skus.name: {
                "$exists": True,
                "$ne": []
            },
            "{}.{}".format(ProductModel.skus.name, SkuMsgObj.stock_num.name): {"$gt": 0}
        }

        # 过滤是否是测试商品(false时不进行过滤)
        if not TEST_PRODUCT:
            fit[ProductModel.is_test_product.name] = TEST_PRODUCT
        # 关键词搜索
        if keyword:
            fit[ProductModel.title.name] = {
                '$regex': keyword,
                '$options': 'i'
            }

        if doc_id:
            fit[ProductModel.collection_doctors.name] = doc_id
        sort = ""
        if sort_by:
            sort = SORT_DICT.get(sort_by, None)
        res = None
        try:
            if fields:
                res = ProductModel.objects(__raw__=fit).only(*fields).skip(
                    int(offset)).limit(int(count)).order_by(sort)

            else:
                res = (ProductModel.objects(__raw__=fit)).skip(
                    int(offset)).limit(int(count)).order_by(sort)
            self.log.info(
                "[ProductDao.search_by_offset_ok],[keyword:{},doc_id:{},offset:{},count:{}],[res_len:{}]"
                    .format(keyword, doc_id, offset, count, len(res)))
        except:
            self.log.exception('[ProductDao.search_by_offset_fail],[keyword:{},doc_id:{},offset:{},count:{}]'
                               .format(keyword, doc_id, offset, count))

        return res

    def search_from_title(self, keyword: str, page: int, page_size: int, doc_id: str, sort_by: str, fields=[]):
        """
        从标题中搜索商品
        :param sort_by:
        :param keyword: 关键词
        :param page:
        :param page_size:
        :param doc_id:
        :param fields:
        :return:
        """

        page = int(page)
        if page == 0: page = 1

        # 转换分页开始
        begin = (page - 1) * int(page_size)
        sort = ""
        if not sort_by: sort_by = "normal"
        res = None
        # 默认过滤掉下架的商品和sku不存在的
        fit = {
            ProductModel.status.name: SS_SPU_STATUS_ON,
            ProductModel.skus.name: {
                "$exists": True,
                "$ne": []
            },
            "{}.{}".format(ProductModel.skus.name, SkuMsgObj.stock_num.name): {"$gt": 0}
        }
        # 过滤是否是测试商品(false时不进行过滤)
        if not TEST_PRODUCT:
            fit[ProductModel.is_test_product.name] = TEST_PRODUCT
        # 关键词搜索
        if keyword:
            fit[ProductModel.title.name] = {
                '$regex': keyword,
                '$options': 'i'
            }

        if doc_id:
            fit[ProductModel.collection_doctors.name] = doc_id
        if sort_by:
            sort = SORT_DICT.get(sort_by, None)

        try:
            if fields:
                res = ProductModel.objects(__raw__=fit).only(*fields).skip(
                    int(begin)).limit(int(page_size)).order_by(sort)

            else:
                res = (ProductModel.objects(__raw__=fit)).skip(
                    int(begin)).limit(int(page_size)).order_by(sort)
            self.log.info(
                "[ProductDao.search_from_title_ok],[keyword:{},doc_id:{},page:{},page_size:{}],[res_len:{}]"
                    .format(keyword, doc_id, page, page_size, len(res)))
        except:
            self.log.exception('[ProductDao.search_from_title_fail],[keyword:{},doc_id:{},page:{},page_size:{}，begin:{}]'
                               .format(keyword, doc_id, page, page_size, begin))

        return res

    def get_keyword_code(self, keyword_name: str, field_name: str) -> str:
        """
        获取已存在的属性编码
        :param keyword_name:
        :param field_name:
        :return:
        """
        fit = {}
        res_list = self.aggregate_type(field_name=field_name, fit=fit)

        if res_list:
            self.log.info("[get_keyword_code][keyword_name:{},field_name:{}][res_list:{}]".format(keyword_name, field_name, res_list))
            for item in res_list:
                if keyword_name == item.get("name"):
                    return item.get("cate_id")
        return ""

    def del_product(self, product_id: int):
        """
        删除商品

        :param product_id:
        :return:
        """
        fit = {
            ProductModel.product_id.name: product_id
        }
        return ProductModel.objects(__raw__=fit).delete()

    def update_status_by_product_id(self, product_id: int, status: int = 11):
        """
        更新产品状态

        :param product_id:
        :param status: 默认更改为11下架状态
        :return:
        """
        fit = {
            ProductModel.product_id.name: product_id
        }
        update_info = {
            "$set": {
                ProductModel.status.name: status
            }
        }

        return ProductModel.objects(__raw__=fit).update(__raw__=update_info)

    def get_price_by_sku_id(self, product_id: int, sku_id: int) -> int:
        '''
        获取某个SKU的价格
        :param product_id:
        :param sku_id:
        :return:    返回-1代表错误。
        '''

        price = -1
        cond = {
            ProductModel.product_id.name: int(product_id),
            "{}.{}".format(ProductModel.skus.name, SkuMsgObj.sku_id.name): int(sku_id)
        }

        fields = ["{}.{}".format(ProductModel.skus.name, SkuMsgObj.sku_id.name),
                  "{}.{}".format(ProductModel.skus.name, SkuMsgObj.sale_price.name),
                  ]
        res = ProductModel.objects(__raw__=cond).only(*fields).first()

        for sku_item in res.skus:
            if sku_item.sku_id == int(sku_id):
                price = sku_item.sale_price
                break

        if price == -1:  # 状态不存在。
            raise NoExistsProduct("[product_id:{}, sku_id:{}]".format(product_id, sku_id))

        return price

    def get_hotval_by_sku_id(self, product_id: int, sku_id: int) -> int:
        """
        获取sku的热力值

        :param product_id:
        :param sku_id:
        :return:
        """
        hotval = 0

        fit = {
            ProductModel.product_id.name: int(product_id),
            "{}.{}".format(ProductModel.skus.name, SkuMsgObj.sku_id.name): int(sku_id)
        }
        fields = [ProductModel.skus.name]
        res = ProductModel.objects(__raw__=fit).only(*fields).first()

        if res:
            for sku_item in res.skus:
                if sku_item.sku_id == int(sku_id):
                    hotval = sku_item.expect_hot_value if sku_item.expect_hot_value else 0
                    break

        return hotval

    def get_product_list(self, fields=[]):
        """
        获取正常上架商品数据

        :return:
        """
        fit = {
            ProductModel.status.name: SS_SPU_STATUS_ON,
            ProductModel.skus.name: {
                "$exists": True,
                "$ne": []
            }
        }

        res = ProductModel.objects(__raw__=fit).only(*fields)

        return res

    def del_sku(self, product_id: int, sku_id: int):
        """
        删除商品的sku

        :param product_id:
        :param sku_id:
        :return:
        """
        fit = {
            ProductModel.product_id.name: product_id
        }
        update_info = {
            "$pull": {
                ProductModel.skus.name: {
                    SkuMsgObj.sku_id.name: sku_id
                }
            }
        }
        res = ProductModel.objects(__raw__=fit).update(__raw__=update_info)
        return res

    def update_brand_id(self, brand_name, new_brand_id):
        """
        更新品牌id

        :param brand_name:
        :param new_brand_id:
        :return:
        """

        fit = {
            f"{ProductModel.brand.name}.{CategoryObj.name.name}": brand_name
        }
        update_info = {
            "$set": {
                f"{ProductModel.brand.name}.{CategoryObj.cate_id.name}": new_brand_id
            }
        }
        res = ProductModel.objects(__raw__=fit).update(__raw__=update_info)

        return res

    def update_brand_type(self,product_id,new_data):
        """
        更新品牌类型
        :param product_id:
        :param new_data:
        :return:
        """
        fit = {
            f"{ProductModel.product_id.name}": product_id
        }
        update_info = {
            "$set": {
                f"{ProductModel.brand.name}": new_data
            }
        }
        res = ProductModel.objects(__raw__=fit).update(__raw__=update_info)

        return res

class ProductActionModelDao:
    def __init__(self, log):
        self.log = log

    def add_view_product(self, user_id, product_id: int, doctor_id=None):
        '''
        增加一条产品查看纪录。

        :param user_id:
        :param product_id:
        :param doctor_id:
        :return:
        '''
        ret_data = None

        refer_doc_id = self.get_referrer_doctor_id(product_id=product_id, user_id=user_id)
        now_str = arrow.now().format(locale='zh_cn')
        if refer_doc_id != None:  # 有推荐纪录，推荐者有可能是医生或默认推荐者
            if doctor_id:  # 又有医生推荐了，则可以进行覆盖。

                product_id = int(product_id)
                cond = {
                    ProductActionModel.user_id.name: user_id,
                    ProductActionModel.product_id.name: product_id,
                    ProductActionModel.action.name: ProductActionModel.AN_VIEW
                }

                # 存在纪录，则进行更新。
                upd_data = {
                    "$set": {
                        ProductActionModel.doctor_id.name: doctor_id,
                        ProductActionModel.create_time.name: now_str
                    }
                }
                self.log.info("[add_view_product][update_exists_item][doc_id:{}, user_id:{}, product_id:{}]".format(
                    doctor_id, user_id, product_id
                ))

                ret_data = ProductActionModel.objects(__raw__=cond).update(__raw__=upd_data)
            else:  # 没有新的医生推荐，自发的点击，则不进行覆盖。
                self.log.info(
                    "[add_view_product][skip， self_click_no_update_recomander][src_doc_id:{}, user_id:{}, product_id:{}]"
                        .format(refer_doc_id, user_id, product_id))

        else:
            # 没有纪录，则进行创建。
            action_item = ProductActionModel(product_id=product_id, user_id=user_id, doctor_id=doctor_id,
                                             create_time=now_str, action=ProductActionModel.AN_VIEW)

            self.log.info("[add_view_product][create_item][doc_id:{}, user_id:{}, product_id:{}]".format(
                doctor_id, user_id, product_id
            ))
            ret_data = ProductActionModel.save(action_item)

        return ret_data

    def get_referrer_doctor_id(self, product_id, user_id, deadline_at: arrow = None):
        '''
        获取某人购买某个产品的推荐人。
        :param product_id:
        :param user_id:
        :param deadline_at:     [arrow]截止时间，None代表当前时间。
        :return:    [str]   推荐医生的ID， 'xxxx'代表具体医生，''代表没有默认推荐者， None代表没有推荐纪录。
        '''

        product_id = int(product_id)
        cond = {
            ProductActionModel.user_id.name: user_id,
            ProductActionModel.product_id.name: product_id,
            ProductActionModel.action.name: ProductActionModel.AN_VIEW
        }

        item = ProductActionModel.objects(__raw__=cond).only(*[ProductActionModel.doctor_id.name,
                                                               ProductActionModel.create_time.name
                                                               ]).order_by("-{}".format(ProductActionModel.create_time.name)).first()

        doc_id = None
        if item:
            if not deadline_at:
                deadline_at = arrow.now(tz='+08:00')
            item_at = arrow.get(item.create_time).shift(days=+1)  # 跟踪的纪录24小时内有效。

            if deadline_at < item_at:
                doc_id = item.doctor_id
                self.log.info("[get_referrer_doctor_id][exist_item][user_id:{}, product_id:{} doc_id:{} "
                              ", create_time:{}, deadline_at:{}]".format(user_id, product_id, doc_id,
                                                                         item.create_time,
                                                                         deadline_at))
            else:
                self.log.info(
                    "[get_referrer_doctor_id][item_invalidate_create_time_than_hour][user_id:{}, product_id:{}"
                    ", create_time:{}, deadline_at:{}]".format(user_id, product_id, item.create_time, deadline_at))
        else:
            self.log.info(
                "[get_referrer_doctor_id][no_referrer][user_id:{}, product_id:{}".format(user_id, product_id))

        return doc_id




