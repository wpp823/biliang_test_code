import base64
import poplib

import imaplib
import email

import email.parser
from pprint import pprint

auth_code = 'SOBQPXPHHQKCLXSL'
user_name = 'wpp_work_mail@163.com'
user_pwd = "Wy836289789"

qq_mail_auth_code = 'rlsvlozatxacbbgj'

qq_user_name = '836289789@qq.com'
qq_imap_server = "imap.qq.com"

pop_server = 'pop.163.com'
imap_server = "imap.163.com"

# 连接到POP3服务器:
server = imaplib.IMAP4(qq_imap_server)

server.login(qq_user_name,qq_mail_auth_code)
# server.xatom("ID",'("name" "wyy" "version" "1.0.0")')
#
server.select()
#
word= "出库单".encode('unicode_escape').decode('ascii')
# typ,data = server.search(None,'ALL')
typ,msg_ids = server.search('utf-8','SUBJECT "出库单"'.encode('utf-8'))

count = 1
pcount = 1
for num in msg_ids[0].split()[::-1]:
    typ,msg_data= server.fetch(num,'(RFC822)')
    # typ,data= server.fetch(num,'(BODY.PEEK[HEADER])')
    # typ,data= server.fetch(num,'(BODY.PEEK[TEXT])')

    for response_part in msg_data:
        if isinstance(response_part, tuple):
            email_parser = email.parser.BytesFeedParser()
            email_parser.feed(response_part[1])
            msg = email_parser.close()
            for header in ['subject', 'to', 'from']:
                print('{:^8}: {}'.format(
                    header.upper(), msg[header]))


    #
    # email.parser.Parser
    #
    # text = data[0][1]
    #
    # message = email.message_from_string(str(text,encoding='utf-8'))
    #
    #
    # #
    # main= message.get_payload()[0].get_payload()
    # str_main = base64.b64decode(main)
    # subject = message.get("subject")


pass

# typ, data = server.list()
# print('Response code:', typ)
# print('Response:')
# pprint(data)


