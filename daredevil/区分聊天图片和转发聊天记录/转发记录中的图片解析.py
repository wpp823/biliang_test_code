import urllib.request

import furl
import requests

test_we_chart_url = 'https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/deeppupil/2022-03-05/1646485470_efc7yC2H_temp_0_1.zip'
ff = furl.furl(test_we_chart_url).path.segments[-1]
file_zip_name = ff.path.segments[-1]
if 'forward' in file_zip_name:
    print(file_zip_name)
# zip_f = urllib.request.urlopen(test_we_chart_url,)
response = requests.get(test_we_chart_url)
