# import tempfile
#
# str_connect  = """
# <?xml version=\"1.0\"?>\n<msg>\n\t<appmsg appid=\"\" sdkver=\"0\">\n\t\t<title>两个“100万”的背后……</title>\n\t\t<des>学史力行，聚焦为群众办实事</des>\n\t\t<action />\n\t\t<type>5</type>\n\t\t<showtype>0</showtype>\n\t\t<soundtype>0</soundtype>\n\t\t<mediatagname />\n\t\t<messageext />\n\t\t<messageaction />\n\t\t<content />\n\t\t<contentattr>0</contentattr>\n\t\t<url>http://mp.weixin.qq.com/s?__biz=MzAwMjAwNTI5Ng==&amp;mid=2448034979&amp;idx=1&amp;sn=e97fb11d6343085e98d85b794357af49&amp;chksm=8ecfacfcb9b825eab45f0851efc7751852c61e77d7058b348da3da31fdd45b492065b533fbd7&amp;mpshare=1&amp;scene=24&amp;srcid=0416mC8dyjw1V4mTBS2sxKAB&amp;sharer_sharetime=1618503008161&amp;sharer_shareid=4db6bd1f243fb4c87df2f7f434784e91#rd</url>\n\t\t<lowurl />\n\t\t<dataurl />\n\t\t<lowdataurl />\n\t\t<songalbumurl />\n\t\t<songlyric />\n\t\t<appattach>\n\t\t\t<totallen>0</totallen>\n\t\t\t<attachid />\n\t\t\t<emoticonmd5></emoticonmd5>\n\t\t\t<fileext />\n\t\t\t<cdnthumbaeskey />\n\t\t\t<aeskey></aeskey>\n\t\t</appattach>\n\t\t<extinfo />\n\t\t<sourceusername>gh_a732738b20b8</sourceusername>\n\t\t<sourcedisplayname>中山大学附属第五医院</sourcedisplayname>\n\t\t<thumburl>https://mmbiz.qlogo.cn/mmbiz_jpg/EkGKH0jgo8jcd0icFSicvWU04HXmogCzIm1f92HD2J7rKu9fPtrD2LrvmbQfqeUHk8q1VclCfaD2SRKYuNvibFIkA/300?wx_fmt=jpeg&amp;wxfrom=4</thumburl>\n\t\t<md5 />\n\t\t<statextstr />\n\t\t<directshare>0</directshare>\n\t\t<recorditem><![CDATA[<recordinfo><edittime>0</edittime><fromscene>0</fromscene></recordinfo>]]></recorditem>\n\t\t<mmreadershare>\n\t\t\t<itemshowtype>0</itemshowtype>\n\t\t\t<nativepage>0</nativepage>\n\t\t\t<pubtime>0</pubtime>\n\t\t\t<duration>0</duration>\n\t\t\t<width>0</width>\n\t\t\t<height>0</height>\n\t\t\t<vid />\n\t\t\t<funcflag>0</funcflag>\n\t\t\t<ispaysubscribe>0</ispaysubscribe>\n\t\t</mmreadershare>\n\t</appmsg>\n\t<fromusername>wxid_zwlrpnsq706g22</fromusername>\n\t<scene>0</scene>\n\t<appinfo>\n\t\t<version>1</version>\n\t\t<appname />\n\t</appinfo>\n\t<commenturl />\n</msg>\n
# """
# str_connect_1 = """
# <msg> <appmsg appid=\"\" sdkver=\"0\"> \t<title><![CDATA[记账时间到，快来记录今日收支]]></title> \t<des><![CDATA[今日统计截至当前，总收入0.00元，总支出0.00元\n使用提醒 快来补充其他收支，坚持记录才可以查看完整账目]]></des> \t<action></action> \t<type>5</type> \t<showtype>1</showtype>     <soundtype>0</soundtype> \t<content><![CDATA[]]></content> \t<contentattr>0</contentattr> \t<url><![CDATA[]]></url> \t<lowurl><![CDATA[]]></lowurl> \t<appattach> \t\t<totallen>0</totallen> \t\t<attachid></attachid> \t\t<fileext></fileext> \t\t<cdnthumburl><![CDATA[]]></cdnthumburl> \t\t<cdnthumbaeskey><![CDATA[]]></cdnthumbaeskey> \t\t<aeskey><![CDATA[]]></aeskey> \t</appattach> \t<extinfo></extinfo> \t<sourceusername><![CDATA[]]></sourceusername> \t<sourcedisplayname><![CDATA[]]></sourcedisplayname> \t<mmreader> \t\t<category type=\"0\" count=\"1\"> \t\t\t<name><![CDATA[微信收款助手]]></name> \t\t\t<topnew> \t\t\t\t<cover><![CDATA[]]></cover> \t\t\t\t<width>0</width> \t\t\t\t<height>0</height> \t\t\t\t<digest><![CDATA[今日统计截至当前，总收入0.00元，总支出0.00元\n使用提醒 快来补充其他收支，坚持记录才可以查看完整账目]]></digest> \t\t\t</topnew> \t\t\t\t<item> \t<itemshowtype>4</itemshowtype> \t<title><![CDATA[记账时间到，快来记录今日收支]]></title> \t<url><![CDATA[]]></url> \t<shorturl><![CDATA[]]></shorturl> \t<longurl><![CDATA[]]></longurl> \t<pub_time>1620905494</pub_time> \t<cover><![CDATA[]]></cover> \t<tweetid></tweetid> \t<digest><![CDATA[今日统计截至当前，总收入0.00元，总支出0.00元\n使用提醒 快来补充其他收支，坚持记录才可以查看完整账目]]></digest> \t<fileid>0</fileid> \t<sources> \t<source> \t<name><![CDATA[微信收款助手]]></name> \t</source> \t</sources> \t<styles><topColor><![CDATA[]]></topColor>\n<style>\n<range><![CDATA[{4,22}]]></range>\n<font><![CDATA[s]]></font>\n<color><![CDATA[#E8B647]]></color>\n</style>\n<style>\n<range><![CDATA[{32,22}]]></range>\n<font><![CDATA[s]]></font>\n<color><![CDATA[#000000]]></color>\n</style>\n</styles>\t<native_url></native_url>    <del_flag>0</del_flag>     <contentattr>0</contentattr>     <play_length>0</play_length> \t<play_url><![CDATA[]]></play_url> \t<player><![CDATA[]]></player> \t<template_op_type>1</template_op_type> \t<weapp_username><![CDATA[gh_fac0ad4c321d@app]]></weapp_username> \t<weapp_path><![CDATA[pages/store_diary/bookkeeping/bookkeeping.html]]></weapp_path> \t<weapp_version>618</weapp_version> \t<weapp_state>0</weapp_state>     <music_source>0</music_source>     <pic_num>0</pic_num> \t<show_complaint_button>0</show_complaint_button> \t<vid><![CDATA[]]></vid> \t<recommendation><![CDATA[]]></recommendation> \t<pic_urls></pic_urls>\t<comment_topic_id>0</comment_topic_id>\t<cover_235_1><![CDATA[]]></cover_235_1> \t<cover_1_1><![CDATA[]]></cover_1_1>     <cover_16_9><![CDATA[]]></cover_16_9>     <appmsg_like_type>0</appmsg_like_type>     <video_width>0</video_width>     <video_height>0</video_height>     <is_pay_subscribe>0</is_pay_subscribe> \t<general_string></general_string> \t</item> \t\t</category> \t\t<publisher> \t\t\t<username><![CDATA[gh_f0a92aa7146c]]></username> \t\t\t<nickname><![CDATA[微信收款助手]]></nickname> \t\t</publisher> \t\t<template_header><title><![CDATA[记账时间到，快来记录今日收支]]></title>\n<title_color><![CDATA[]]></title_color>\n<pub_time>1620905494</pub_time>\n<first_data><![CDATA[]]></first_data>\n<first_color><![CDATA[]]></first_color>\n<hide_title_and_time>1</hide_title_and_time>\n<show_icon_and_display_name>1</show_icon_and_display_name>\n<display_name><![CDATA[门店日记]]></display_name>\n<icon_url><![CDATA[https://wximg.gtimg.com/wechat_pay_mchapp/qrapp/tmpl/icon/85d10f61-11a0-475a-a651-197517bc2274.png]]></icon_url>\n<hide_icon_and_display_name_line>0</hide_icon_and_display_name_line>\n<weapp_username><![CDATA[gh_fac0ad4c321d@app]]></weapp_username>\n<weapp_path><![CDATA[pages/store_diary/bookkeeping/bookkeeping.html]]></weapp_path>\n<weapp_state>0</weapp_state>\n<weapp_version>618</weapp_version>\n<header_jump_url><![CDATA[]]></header_jump_url>\n<shortcut_icon_url><![CDATA[]]></shortcut_icon_url>\n<ignore_hide_title_and_time>1</ignore_hide_title_and_time>\n<hide_time>1</hide_time>\n<pay_style>1</pay_style>\n<header_jump_type>0</header_jump_type>\n<display_name_desc><![CDATA[]]></display_name_desc>\n<show_right_icon_and_desc_name>0</show_right_icon_and_desc_name>\n<right_icon_url><![CDATA[]]></right_icon_url>\n<right_desc_name><![CDATA[]]></right_desc_name>\n<finder_user_name><![CDATA[]]></finder_user_name>\n<show_finder_feed_entry>0</show_finder_feed_entry>\n<finder_feedid><![CDATA[]]></finder_feedid>\n<finder_nonceid><![CDATA[]]></finder_nonceid>\n<finder_feed_thumnail><![CDATA[]]></finder_feed_thumnail>\n<transaction_id><![CDATA[]]></transaction_id>\n</template_header> \t\t<template_detail><template_show_type>1</template_show_type>\n<text_content>\n<cover><![CDATA[]]></cover>\n<text><![CDATA[]]></text>\n<color><![CDATA[]]></color>\n</text_content>\n<line_content>\n<topline>\n<key>\n<hide_dash_line>1</hide_dash_line>\n</key>\n<value>\n<small_text_count>0</small_text_count>\n</value>\n</topline>\n<lines>\n<line>\n<key>\n<word><![CDATA[今日统计]]></word>\n<color><![CDATA[#888888]]></color>\n</key>\n<value>\n<word><![CDATA[截至当前，总收入0.00元，总支出0.00元]]></word>\n<color><![CDATA[#E8B647]]></color>\n</value>\n</line>\n<line>\n<key>\n<word><![CDATA[使用提醒 ]]></word>\n<color><![CDATA[#888888]]></color>\n</key>\n<value>\n<word><![CDATA[快来补充其他收支，坚持记录才可以查看完整账目]]></word>\n<color><![CDATA[#000000]]></color>\n</value>\n</line>\n</lines>\n</line_content>\n<opitems>\n<opitem>\n<word><![CDATA[点击添加]]></word>\n<url><![CDATA[]]></url>\n<icon><![CDATA[]]></icon>\n<color><![CDATA[#000000]]></color>\n<weapp_username><![CDATA[gh_fac0ad4c321d@app]]></weapp_username>\n<weapp_path><![CDATA[pages/store_diary/bookkeeping/bookkeeping.html]]></weapp_path>\n<op_type>1</op_type>\n<weapp_version>618</weapp_version>\n<weapp_state>0</weapp_state>\n<hint_word><![CDATA[]]></hint_word>\n<is_rich_text>0</is_rich_text>\n<display_line_number>0</display_line_number>\n<general_string><![CDATA[]]></general_string>\n</opitem>\n<opitem>\n<word><![CDATA[查看全部日记]]></word>\n<url><![CDATA[]]></url>\n<icon><![CDATA[]]></icon>\n<color><![CDATA[#000000]]></color>\n<weapp_username><![CDATA[gh_fac0ad4c321d@app]]></weapp_username>\n<weapp_path><![CDATA[pages/store_diary/index/index.html]]></weapp_path>\n<op_type>1</op_type>\n<weapp_version>618</weapp_version>\n<weapp_state>0</weapp_state>\n<hint_word><![CDATA[]]></hint_word>\n<is_rich_text>0</is_rich_text>\n<display_line_number>0</display_line_number>\n<general_string><![CDATA[]]></general_string>\n</opitem>\n<show_type>1</show_type>\n</opitems>\n<new_tmpl_type>0</new_tmpl_type>\n</template_detail> \t    <forbid_forward>0</forbid_forward>         <notify_msg></notify_msg> \t</mmreader> \t<thumburl><![CDATA[]]></thumburl> \t     <template_id><![CDATA[hhBEwxiQAAY8HBHor5osXOl4zvANfBpjRKy_EkV__pg]]></template_id>                          \t </appmsg><fromusername><![CDATA[gh_f0a92aa7146c]]></fromusername><appinfo><version>0</version><appname><![CDATA[微信收款助手]]></appname><isforceupdate>1</isforceupdate></appinfo></msg>
# """
# print(str_connect_1)
#
#
# print(tempfile.gettempdir())

"""
 <dataitem datatype= '2' dataid= 'b5077c2667280fb655c56b278c8a0aed ' datasourceid= '988322230795631073'>
                <cdnthumburl>30818e020100048181307f020100020461afe04102032f57260204e1512777020460a4cd6d045a62353037376332363637323830666236353563353662323738633861306165645f74407265636f72645f75706c6f616440313939355f35383836643765362d313766612d346662632d616662382d6166666663333662356363650204010800010201000405004c56fa00</cdnthumburl>
                <cdndataurl>30818b020100047f307d020100020461afe04102032f57260204e1512777020460a4cd6d04586235303737633236363732383066623635356335366232373863386130616564407265636f72645f75706c6f616440313939355f30373432366430652d336235652d343939362d393134382d6231316437316536303232340204010800010201000405004c56fa00</cdndataurl>
                <cdnthumbkey>293abd3c3a6e91dc8e2694f0e00fbe78</cdnthumbkey>
                <cdndatakey>6c012f1af68180ad48c93cdbbe005f04</cdndatakey>
                <fullmd5>60494b6081f790e21f41441a999d60c1</fullmd5>
                <head256md5>cd021fe76db5211d9ffa3ab430e35b16</head256md5>
                <datasize>219262</datasize>
                <thumbfullmd5>e5fb38a659a45482f65e1419ad84e158</thumbfullmd5>
                <thumbhead256md5>fbcc636caea1cca02e708b18008fedeb</thumbhead256md5>
                <thumbsize>4526</thumbsize>
                <sourcename>Lioney</sourcename>
                <sourcetime>2021-05-19 16:23:23</sourcetime>
                <messageuuid>53fd287eb9d9a952314fb2bcdfe34567_</messageuuid>
                <dataitemsource>
                    <fromusr>wxid_zhpd6xzv7h8132</fromusr>
                </dataitemsource>
            </dataitem>
"""
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


def add_to_16(text):

    if len(text) % 16:
        add = 16 - (len(text) % 16)
    else:
        add = 0
    text = text + ('0' * add)
    return text.encode('utf-8')

cdn_thumb_url = '30818e020100048181307f020100020461afe04102032f57260204e1512777020460a4cd6d045a62353037376332363637323830666236353563353662323738633861306165645f74407265636f72645f75706c6f616440313939355f35383836643765362d313766612d346662632d616662382d6166666663333662356363650204010800010201000405004c56fa00'

cdn_data_url = '30818b020100047f307d020100020461afe04102032f57260204e1512777020460a4cd6d04586235303737633236363732383066623635356335366232373863386130616564407265636f72645f75706c6f616440313939355f30373432366430652d336235652d343939362d393134382d6231316437316536303232340204010800010201000405004c56fa00'
cdn_thumb_key = '293abd3c3a6e91dc8e2694f0e00fbe78'
cdn_data_key = '6c012f1af68180ad48c93cdbbe005f04'
full_md5 = '60494b6081f790e21f41441a999d60c1'
head256_md5 = 'cd021fe76db5211d9ffa3ab430e35b16'

thumb_full_md5 = 'e5fb38a659a45482f65e1419ad84e158'
thumb_head256_md5 = 'fbcc636caea1cca02e708b18008fedeb'
message_uuid = '53fd287eb9d9a952314fb2bcdfe34567_'



cdn_thumb_url_16 = add_to_16(cdn_thumb_url)
# cdn_thumb_key_16 = add_to_16(cdn_thumb_key)

print(len(cdn_thumb_url_16)/16)
print(len(cdn_thumb_key))

# print(cdn_thumb_url_16)
mode = AES.MODE_ECB
# print(a2b_hex(cdn_thumb_url_16))

cryptor = AES.new(cdn_thumb_key, mode)
plain_text = cryptor.decrypt(cdn_thumb_url_16)

print(plain_text)

int_msg = [ item for item in plain_text]
map_str = map(chr,int_msg)

print(''.join(map_str))

# for item in plain_text:
#
#     print(map(chr,[item]))
    # if item.decode('gbk'):
    #     print(item.decode('gbk'))
    # elif item.decode('utf-8'):
    #     print(item.decode('utf-8'))
    # print(item)









