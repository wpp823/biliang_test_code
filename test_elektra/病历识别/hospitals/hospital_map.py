'''
医院名称到相应的处理类的一个映射
'''

# hospital_map = {
#     "深圳市中医院": "app.util.hospitals.szszyy.schedular_main.SzszyySchedular",
#     "广州中医药大学第四临床医学院": "app.util.hospitals.szszyy.schedular_main.SzszyySchedular",
#     "广州中医药大学深圳医院（福田）": "app.util.hospitals.gzzyydxszyy.schedular_main.GzzyydxszyySchedular",
#     "中山大学附属第八医院": "app.util.hospitals.zsdxfsd8yy.schedular_main.Zsdxfsd8yySchedular",
#     "深圳市宝安区中心医院": "app.util.hospitals.szsbaqzxyy.schedular_main.SzsbaqzxyySchedular",
#     "SHENZHENTRADITIONALCHINESEMEDICINEHOSPITA":"app.util.hospitals.szszyy.schedular_main.SzszyySchedular"
#
#     # "":"app.util.hospitals.parse_base.DefaultSchedularBase"                 # 此参数
# }

hospital_map = {
    "深圳市中医院": "szszyy.schedular_main.SzszyySchedular",
    "广州中医药大学第四临床医学院": "szszyy.schedular_main.SzszyySchedular",
    "广州中医药大学深圳医院（福田）": "gzzyydxszyy.schedular_main.GzzyydxszyySchedular",
    "中山大学附属第八医院": "schedular_main.Zsdxfsd8yySchedular",
    "深圳市宝安区中心医院": "schedular_main.SzsbaqzxyySchedular",
    "SHENZHENTRADITIONALCHINESEMEDICINEHOSPITAL":"szszyy.schedular_main.SzszyySchedular"

    # "":"app.util.hospitals.parse_base.DefaultSchedularBase"                 # 此参数
}

DEFAULT_HOSTPITAL_CLASS_NAME = "parse_base.DefaultSchedularBase"
# DEFAULT_HOSTPITAL_CLASS_NAME = "app.util.hospitals.parse_base.DefaultSchedularBase"
'''
# 对于增加一个新的表格支持步骤：
1. 先判断其是否在当前支持的医院列表中。
2. 如在医院列表中，请在 医院的Schedular 类中增加对此类表格的解析。
3. 如不医院列表中，则先创建 医院的Schedular  假设为 BSchedular
4. 再在hospital_map 中增加相应对应的映射
5. 实现相对应表格的parse, 再在 BSchedular 中增加 地些Parse的调用。

最后实在多了，这个映射可以考虑放到数据库中。
'''
