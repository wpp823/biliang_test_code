
import xmltodict

content = """<?xml version="1.0"?>
<msg>
	<appmsg appid="" sdkver="0">
		<title>黄龙的聊天记录</title>
		<des>黄龙: [图片]
黄龙: [图片]
黄龙: 位置消息
黄龙: [位置] 恒和中心(人民东路313号泰峰电器旁)</des>
		<action />
		<type>19</type>
		<showtype>0</showtype>
		<soundtype>0</soundtype>
		<mediatagname />
		<messageext />
		<messageaction />
		<content />
		<contentattr>0</contentattr>
		<url>https://support.weixin.qq.com/cgi-bin/mmsupport-bin/readtemplate?t=page/favorite_record__w_unsupport</url>
		<lowurl />
		<dataurl />
		<lowdataurl />
		<appattach>
			<totallen>0</totallen>
			<attachid />
			<emoticonmd5 />
			<fileext />
			<cdnthumburl>308183020100047730750201000204d186456c02032f591902042da66971020461775a420450777875706c6f61645f77616e67383336363631323331315f313633353231313834325f6d73675468756d625f36363661653932632d626336622d343466322d393161342d3264333336353332313932340204011800030201000405004c56f900</cdnthumburl>
			<cdnthumbmd5>86032db89f3266334ec56ea9c88e9e7d</cdnthumbmd5>
			<cdnthumblength>15506</cdnthumblength>
			<cdnthumbwidth>0</cdnthumbwidth>
			<cdnthumbheight>0</cdnthumbheight>
			<cdnthumbaeskey>12c963491072e1d028995c4ea4d7a4a3</cdnthumbaeskey>
			<aeskey />
		</appattach>
		<extinfo />
		<sourceusername />
		<sourcedisplayname />
		<thumburl />
		<md5 />
		<statextstr />
		<recorditem><![CDATA[<recordinfo><fromscene>3</fromscene><favusername>wxid_8ws1b2octolm21</favusername><title>黄龙的聊天记录</title><desc>黄龙: [图片]
黄龙: [图片]
黄龙: 位置消息
黄龙: [位置] 恒和中心(人民东路313号泰峰电器旁)</desc><info>黄龙: [图片]
黄龙: [图片]
黄龙: 位置消息
黄龙: [位置] 恒和中心(人民东路313号泰峰电器旁)</info><datalist count = "7"><dataitem datatype="2" dataid="88d0273920d92a45fccc48daa53e04e3" htmlid="88d0273920d92a45fccc48daa53e04e3"><datafmt>pic</datafmt><sourcename>黄龙</sourcename><sourcetime>2021-10-26 09:28</sourcetime><thumbsourcepath>/var/mobile/Containers/Data/Application/50BADF8F-0EF9-417A-82CE-0359CCFA1DA0/Documents/2bdc4403b34415fdfc0c5b8280196251/Img/85c50f025438de457310244ed7837be4/2738.pic_thum</thumbsourcepath><thumbsize>4145</thumbsize><cdndataurl>3070020100046430620201000204d186456c02032f5919020451a6697102046176948c043d66696c6568656c7065723733315f313633353136313232385f37373666393232352d646532322d343166352d393235362d3366356462303366643439620204011800010201000405004c56f900</cdndataurl><cdndatakey>b5d1c1937ac1140c6bae9802e6c60a3a</cdndatakey><cdnthumburl>3081a30201000481963081930201000204d186456c02032f591902042da66971020461775a42046e777875706c6f61645f77616e67383336363631323331315f313633353231313834325f38386430323733393230643932613435666363633438646161353365303465335f7468756d625f30653735636538332d633833352d343735332d386130372d3337393933636336636330620204011800010201000405004c56f900</cdnthumburl><cdnthumbkey>5c3b689558e0da171c518197f0cad9c7</cdnthumbkey><datasourcepath>/var/mobile/Containers/Data/Application/50BADF8F-0EF9-417A-82CE-0359CCFA1DA0/Documents/2bdc4403b34415fdfc0c5b8280196251/Img/85c50f025438de457310244ed7837be4/2738.pic</datasourcepath><fullmd5>0f3496473c247e7d080efa24a6804bfe</fullmd5><thumbfullmd5>32f5a18a3e2b85d3fcbbc609724120ab</thumbfullmd5><datasize>1052626</datasize><cdnencryver>1</cdnencryver><srcChatname>wxid_mm8pbznz6ezt22</srcChatname><srcMsgLocalid>2738</srcMsgLocalid><srcMsgCreateTime>1635211685</srcMsgCreateTime><messageuuid>5e98028755e15677d6447499f2376096_</messageuuid><dataitemsource><fromusr>wxid_8ws1b2octolm21</fromusr></dataitemsource></dataitem><dataitem datatype="2" dataid="1c9b6be95e6c8e00335e6af0e7bf39f9" htmlid="1c9b6be95e6c8e00335e6af0e7bf39f9"><datafmt>pic</datafmt><sourcename>黄龙</sourcename><sourcetime>2021-10-26 09:28</sourcetime><thumbsourcepath>/var/mobile/Containers/Data/Application/50BADF8F-0EF9-417A-82CE-0359CCFA1DA0/Documents/2bdc4403b34415fdfc0c5b8280196251/Img/85c50f025438de457310244ed7837be4/2739.pic_thum</thumbsourcepath><thumbsize>4145</thumbsize><cdndataurl>3070020100046430620201000204d186456c02032f5919020451a6697102046176948c043d66696c6568656c7065723733325f313633353136313232385f35663565396561362d333333352d343831312d396432322d3532383463626364666431640204011800010201000405004c56f900</cdndataurl><cdndatakey>bc1aa64170ca47f2a577d84151995e93</cdndatakey><cdnthumburl>3081a30201000481963081930201000204d186456c02032f591902042da66971020461775a42046e777875706c6f61645f77616e67383336363631323331315f313633353231313834325f31633962366265393565366338653030333335653661663065376266333966395f7468756d625f38666235393338372d623262632d343064622d396339342d3933656130363466633130330204011800010201000405004c56f900</cdnthumburl><cdnthumbkey>31426a9fd6e315177db73f3d8e445e8f</cdnthumbkey><datasourcepath>/var/mobile/Containers/Data/Application/50BADF8F-0EF9-417A-82CE-0359CCFA1DA0/Documents/2bdc4403b34415fdfc0c5b8280196251/Img/85c50f025438de457310244ed7837be4/2739.pic</datasourcepath><fullmd5>6543dbcee7990b2e2cbfe4403ae277de</fullmd5><thumbfullmd5>0ec2e1e6d13d48e8f2c66610307da2fd</thumbfullmd5><datasize>1040717</datasize><cdnencryver>1</cdnencryver><srcChatname>wxid_mm8pbznz6ezt22</srcChatname><srcMsgLocalid>2739</srcMsgLocalid><srcMsgCreateTime>1635211694</srcMsgCreateTime><messageuuid>bdf58cfd4d3b1968bc2bbb70cc59fca7_</messageuuid><dataitemsource><fromusr>wxid_8ws1b2octolm21</fromusr></dataitemsource></dataitem><dataitem datatype="1" dataid="0a60a68f4f8140d9833c684e080efd89" htmlid="0a60a68f4f8140d9833c684e080efd89"><sourcename>黄龙</sourcename><sourcetime>2021-10-26 09:28</sourcetime><datadesc>位置消息</datadesc><cdnencryver>1</cdnencryver><srcChatname>wxid_mm8pbznz6ezt22</srcChatname><srcMsgLocalid>2740</srcMsgLocalid><srcMsgCreateTime>1635211707</srcMsgCreateTime><dataitemsource><fromusr>wxid_8ws1b2octolm21</fromusr></dataitemsource></dataitem><dataitem datatype="6" dataid="81dad1553bad516b6a4a16cb5fe88ef5" htmlid="81dad1553bad516b6a4a16cb5fe88ef5"><sourcename>黄龙</sourcename><sourcetime>2021-10-26 09:28</sourcetime><cdnencryver>1</cdnencryver><srcChatname>wxid_mm8pbznz6ezt22</srcChatname><srcMsgLocalid>2741</srcMsgLocalid><srcMsgCreateTime>1635211712</srcMsgCreateTime><dataitemsource><fromusr>wxid_8ws1b2octolm21</fromusr></dataitemsource><locitem><lng>113.551855</lng><lat>22.269614</lat><scale>15.000000</scale><label>广东省珠海市香洲区人民东路313号恒和中心</label><poiname>恒和中心(人民东路313号泰峰电器旁)</poiname></locitem></dataitem><dataitem datatype="1" dataid="125fef9043199f29511096ce06f071ac" htmlid="125fef9043199f29511096ce06f071ac"><sourcename>黄龙</sourcename><sourcetime>2021-10-26 09:28</sourcetime><datadesc>[语音]</datadesc><cdnencryver>1</cdnencryver><srcChatname>wxid_mm8pbznz6ezt22</srcChatname><srcMsgLocalid>2742</srcMsgLocalid><srcMsgCreateTime>1635211716</srcMsgCreateTime><dataitemsource><fromusr>wxid_8ws1b2octolm21</fromusr></dataitemsource></dataitem><dataitem datatype="8" dataid="23e5c3c5b5fde6722603337ea7e306bb" htmlid="23e5c3c5b5fde6722603337ea7e306bb"><datafmt>md</datafmt><appid>wx6618f1cfc6c132f8</appid><sourcename>黄龙</sourcename><sourcetime>2021-10-26 09:28</sourcetime><datatitle>MySQL - 笔记.md</datatitle><cdndataurl>308183020100047730750201000204d186456c02032f591902042da669710204617759d80450777875706c6f61645f777869645f6d6d3870627a6e7a36657a743232323734335f313633353231313733365f32346337346464302d663363652d343766612d393661302d6430303737623038383964370204011800050201000405004c56f900</cdndataurl><cdndatakey>27f37e0e34bd93cec761f1e784934eea</cdndatakey><datasourcepath>/var/mobile/Containers/Data/Application/50BADF8F-0EF9-417A-82CE-0359CCFA1DA0/Documents/2bdc4403b34415fdfc0c5b8280196251/OpenData/85c50f025438de457310244ed7837be4/2743.md</datasourcepath><fullmd5>30c705f2e7d9284d046a97cc8abc981f</fullmd5><datasize>68186</datasize><cdnencryver>1</cdnencryver><srcChatname>wxid_mm8pbznz6ezt22</srcChatname><srcMsgLocalid>2743</srcMsgLocalid><srcMsgCreateTime>1635211736</srcMsgCreateTime><dataitemsource><fromusr>wxid_8ws1b2octolm21</fromusr></dataitemsource></dataitem><dataitem datatype="2" dataid="28b9c5f8c76103f5d896be014e918354" htmlid="28b9c5f8c76103f5d896be014e918354"><datafmt>pic</datafmt><sourcename>黄龙</sourcename><sourcetime>2021-10-26 09:29</sourcetime><thumbsourcepath>/var/mobile/Containers/Data/Application/50BADF8F-0EF9-417A-82CE-0359CCFA1DA0/Documents/2bdc4403b34415fdfc0c5b8280196251/Img/85c50f025438de457310244ed7837be4/2744.pic_thum</thumbsourcepath><thumbsize>5962</thumbsize><cdndataurl>30780201000471306f02010002047ffbe4e602032f59190204aa9a6971020461762cfe044a617570696d675f326335613835363036373437363063665f313633353133343731353136365f61373939316332352d333566342d343537652d626331362d666534626263373964623839020401192a010201000400</cdndataurl><cdndatakey>fde3b5941ac3434a53bc5bfcbd14a2fe</cdndatakey><cdnthumburl>3081a30201000481963081930201000204d186456c02032f591902042da66971020461775a42046e777875706c6f61645f77616e67383336363631323331315f313633353231313834325f32386239633566386337363130336635643839366265303134653931383335345f7468756d625f30613535323963622d626566662d346365322d383765342d3264393563396365363666630204011800010201000405004c56f900</cdnthumburl><cdnthumbkey>2f11d02832e02be41a3d00a62e9b3161</cdnthumbkey><datasourcepath>/var/mobile/Containers/Data/Application/50BADF8F-0EF9-417A-82CE-0359CCFA1DA0/Documents/2bdc4403b34415fdfc0c5b8280196251/Img/85c50f025438de457310244ed7837be4/2744.pic</datasourcepath><fullmd5>b218439710e785dc3eb5535ce86c2927</fullmd5><thumbfullmd5>ebd44c69e331793f366d8c259b0eb66a</thumbfullmd5><datasize>699286</datasize><cdnencryver>1</cdnencryver><srcChatname>wxid_mm8pbznz6ezt22</srcChatname><srcMsgLocalid>2744</srcMsgLocalid><srcMsgCreateTime>1635211755</srcMsgCreateTime><messageuuid>e2398ce5923510cf601609d927c01574_</messageuuid><dataitemsource><fromusr>wxid_8ws1b2octolm21</fromusr></dataitemsource></dataitem></datalist></recordinfo>]]></recorditem>
	</appmsg>
	<fromusername>wxid_8ws1b2octolm21</fromusername>
	<scene>0</scene>
	<appinfo>
		<version>1</version>
		<appname></appname>
	</appinfo>
	<commenturl></commenturl>
</msg>
"""
# data_msg = xmltodict.parse(xml_input=xml_data)
content = content.replace('\n', '').replace('\t', '')
xml_str = content[content.find('<msg'):content.rfind('msg>') + 4]
xml_dict = xmltodict.parse(xml_str, encoding='utf-8')
# content = self._content

reccord = xml_dict['msg']['appmsg']['recorditem']

print(reccord)

reccord_dict = xmltodict.parse(reccord,encoding='utf8')

type = xml_dict['msg']['appmsg']['type']
title = xml_dict['msg']['appmsg']['title']
desc = xml_dict['msg']['appmsg']['des']
url = xml_dict['msg']['appmsg']['url']
thumburl = xml_dict['msg']['appmsg'].get('thumburl', '')

print()