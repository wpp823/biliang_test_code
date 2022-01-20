import pypinyin


# 带声调的(默认)
def yinjie(word):
    s = ''
    # heteronym=True开启多音字
    for i in pypinyin.pinyin(word, style=pypinyin.Style.TONE2):
        s = s + ''.join(i)
    return s


brands = ['森花泉','小银罐', '广御']
for word in brands:
    print(yinjie(word))