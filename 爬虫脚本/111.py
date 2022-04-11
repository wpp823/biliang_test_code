import pandas as pd

pd.set_option('display.width', 1000)
pd.set_option('colheader_justify', 'center')
xd = pd.ExcelFile('weibo_result.xls')
df = xd.parse()

pd.set_option('colheader_justify', 'center')

# 设置html文件格式
html_string = '''
  <!DOCTYPE html>
    <head>
    <meta charset="UTF-8">
    <title></title>
    </head>
    <link rel="stylesheet" type="text/css" href="df_style.css"/>
    <body>
      {table}
    </body>
  </html>.
  '''
with open('table_2018.html', encoding='utf-8', mode='w') as f:
    f.write(html_string.format(table=df.to_html()))
