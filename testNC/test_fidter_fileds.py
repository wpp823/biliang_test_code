import json

data = '''{
    "product_id" : 56479595,
    "out_product_id" : "",
    "title" : "绽妍氨基酸洁面慕斯100ml 敏肌毛孔清洁控油温和不紧绷泡沫绵密",
    "sub_title" : "",
    "head_img" : [ 
        "https://mmbizurl.cn/p/wxe6b89bd3689d4f57/HH8PHDDttyjfpyDWbOOurh36e2JQalH5VNaZTj59bA", 
        "https://mmbizurl.cn/p/wxe6b89bd3689d4f57/HMntOVJSLKuT_dBh6tmcxsvF5GAl1VGu7kmARZZt2A", 
        "https://mmbizurl.cn/p/wxe6b89bd3689d4f57/HDlYKXgC7XLk7q8NLhYF_JkhAaYcs4xbDh_CjAbXXQ", 
        "https://mmbizurl.cn/p/wxe6b89bd3689d4f57/HAO72Yg0VFRVwDGkM3rRXzO4YP7wihroAm7Tm6DkaQ", 
        "https://mmbizurl.cn/p/wxe6b89bd3689d4f57/HPWd5IEvsXx6FjvQZcZhLCI7lz3f1XKxxIQJXksrbA"
    ],
    "desc_info" : {
        "imgs" : [ 
            "https://mmbizurl.cn/p/wxe6b89bd3689d4f57/HPaXAuCdMCwsv3ahp7RHpaR98suiJggk2wjQgeasKA", 
            "https://mmbizurl.cn/p/wxe6b89bd3689d4f57/HAH_VH7aul8ND7t-xG2wRBbK4oAMpGUzdXZ3pAxGlg", 
            "https://mmbizurl.cn/p/wxe6b89bd3689d4f57/HJn-PoWdyOemUitTC_LJLsETKRAGsVW2EPndZWPa2w"
        ]
    },
    "brand_id" : 2100000000,
    "status" : 5,
    "edit_status" : 4,
    "min_price" : 12800,
    "path" : "plugin-private://wx34345ae5855f892d/pages/productDetail/productDetail?productId=56479595",
    "cats" : [ 
        {
            "cat_id" : 6870,
            "level" : 0
        }, 
        {
            "cat_id" : 6896,
            "level" : 0
        }, 
        {
            "cat_id" : 6903,
            "level" : 0
        }
    ],
    "attrs" : [ 
        {
            "attr_key" : "品牌",
            "attr_value" : "JUYOU/绽妍"
        }, 
        {
            "attr_key" : "产品类别",
            "attr_value" : "洁面摩丝"
        }, 
        {
            "attr_key" : "是否进口",
            "attr_value" : "否"
        }, 
        {
            "attr_key" : "产品系列",
            "attr_value" : "洁面"
        }, 
        {
            "attr_key" : "产品名称",
            "attr_value" : "绽妍氨基酸洁面慕斯 100ml"
        }, 
        {
            "attr_key" : "适用人群",
            "attr_value" : "通用"
        }, 
        {
            "attr_key" : "适用肤质",
            "attr_value" : "通用"
        }, 
        {
            "attr_key" : "起泡程度",
            "attr_value" : "泡沫洁面"
        }, 
        {
            "attr_key" : "货号",
            "attr_value" : "P2021073002"
        }, 
        {
            "attr_key" : "规格",
            "attr_value" : "正常规格"
        }, 
        {
            "attr_key" : "品牌类型",
            "attr_value" : "精品国货"
        }, 
        {
            "attr_key" : "上市时间",
            "attr_value" : "2019"
        }, 
        {
            "attr_key" : "特殊用途化妆品",
            "attr_value" : "否"
        }, 
        {
            "attr_key" : "保质期",
            "attr_value" : "三年"
        }, 
        {
            "attr_key" : "产地",
            "attr_value" : "西安"
        }, 
        {
            "attr_key" : "净含量",
            "attr_value" : "100"
        }, 
        {
            "attr_key" : "是否跨境出口专供货源",
            "attr_value" : "否"
        }, 
        {
            "attr_key" : "非特化妆品备案证号",
            "attr_value" : "川G妆网备字2019001247"
        }, 
        {
            "attr_key" : "化妆品功效",
            "attr_value" : "控油,深层清洁"
        }, 
        {
            "attr_key" : "成分原料",
            "attr_value" : "氨基酸"
        }, 
        {
            "attr_key" : "类别",
            "attr_value" : "洁面皂/洗面奶/洁面乳"
        }
    ],
    "model" : "",
    "source" : 1,
    "skus" : [ 
        {
            "product_id" : 56479595,
            "out_product_id" : "4097926",
            "out_sku_id" : "4097927",
            "thumb_img" : "",
            "sale_price" : 12800,
            "market_price" : 0,
            "stock_num" : 485,
            "code" : "",
            "barcode" : "",
            "sku_id" : 112974253,
            "sku_attrs" : [ 
                {
                    "attr_key" : "颜色",
                    "attr_value" : "默认"
                }
            ],
            "status" : 5,
            "sku_code" : "",
            "expect_hot_value" : 123
        }
    ],
    "collection_doctors" : [],
    "kind" : [],
    "function" : [],
    "disease" : [],
    "expect_hot_value" : 123,
    "brand" : {
        "cate_id" : "BR_WLkeBhW4ha",
        "name" : "绽妍"
    },
    "sales_volume" : 0,
    "express_info" : {
        "template_id" : 29466502,
        "weight" : 0
    },
    "shopcat" : []
}
'''

data_dict = json.loads(data.replace("\n",""))
filter_fields = ["shopcat","express_info.template_id"]
for filter_name in filter_fields:
    if "." in filter_name:
        filter_list = filter_name.split('.')


    res = data_dict.pop(filter_name, "404")

    print(res)

print(data_dict)
