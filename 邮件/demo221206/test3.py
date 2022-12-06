import datetime
import email
import imaplib
import os
import time
from email.header import decode_header


class IMAP_Downemail(object):
    """
    imap邮箱下载附件(腾讯企业邮箱测试通过)
    """

    def __init__(self, account, pwd, serverurl, savedir, startdate, enddate, exts=['.xls', '.xlsx']):
        """
        init
        :param account:   邮箱账户
        :param pwd:       密码
        :param serverurl: 接收服务器地址
        :param savedir:   文件保存路径
        :param startdate: 邮件开始日期
        :param enddate:   邮件结束日期
        :param exts:      附件拓展名
        """
        self._account = account
        self._pwd = pwd
        self._serverurl = serverurl
        self._savedir = savedir
        self._startdate = startdate
        self._enddate = enddate
        self._exts = exts

    def __getEmailattachment(self, msg):
        """
        下载邮件中的附件
        """
        attachments = []
        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            fileName = part.get_filename()

            # 如果文件名为纯数字、字母时不需要解码，否则需要解码
            try:
                fileName = decode_header(fileName)[0][0].decode(decode_header(fileName)[0][1])
            except:
                pass

            # 只获取指定拓展名的附件
            extension = os.path.splitext(os.path.split(fileName)[1])[1]
            if extension not in self._exts:
                continue

            # 如果获取到了文件，则将文件保存在指定的目录下
            if fileName:
                if not os.path.exists(self._savedir):
                    os.makedirs(self._savedir)
                filePath = os.path.join(self._savedir, fileName)
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
                attachments.append(fileName)

        return attachments

    def scanDown(self, process_fun=None):
        if process_fun:
            process_fun("当前邮箱：{}".format(self._account))

        # 连接到qq企业邮箱，其他邮箱调整括号里的参数
        conn = imaplib.IMAP4_SSL(self._serverurl, 993)

        if process_fun:
            process_fun("身份认证...")
        try:
            # 用户名、密码，登陆
            conn.login(self._account, self._pwd)
            login_success = True
        except:
            login_success = False

        if login_success:
            if process_fun:
                process_fun("邮箱{}登录成功！".format(self._account))

            # 选定一个邮件文件夹
            # 收件箱默认名称是"INBOX"
            # 可以用conn.list()查看都有哪些文件夹
            conn.select("INBOX")

            # 提取文件夹中所有邮件的编号
            resp, mails = conn.search('utf-8','SUBJECT "出库单"'.encode('utf-8'))

            # 邮件编号列表
            msgList = mails[0].split()

            # 从最近的邮件开始获取
            for i in reversed(range(len(msgList))):
                try:
                    resp, data = conn.fetch(msgList[i], '(RFC822)')
                    emailbody = data[0][1]
                    mail = email.message_from_bytes(emailbody)

                    # # 解析邮件日期
                    # try:
                    #     mail_date = time.strptime(mail.get("Date")[0:24], '%a, %d %b %Y %H:%M:%S')  # 格式化收件时间
                    # except:
                    #     mail_date = time.strptime(mail.get("Date"), '%d %b %Y %H:%M:%S +0800')  # 格式化收件时间
                    # mail_date = time.strftime("%Y%m%d", mail_date)
                    #
                    # startdate = self._startdate
                    # stopdate = self._enddate
                    #
                    # if mail_date == (datetime.datetime.strptime(startdate, '%Y%m%d') - datetime.timedelta(days=1)).strftime('%Y%m%d'):
                    #     break
                    #
                    # if mail_date == (datetime.datetime.strptime(startdate, '%Y%m%d') - datetime.timedelta(days=3)).strftime('%Y%m%d'):
                    #     break
                    #
                    # if (mail_date < startdate) | (mail_date > stopdate):
                    #     continue

                    # 获取附件
                    attachments = self.__getEmailattachment(mail)
                    for attachment in attachments:
                        if process_fun:
                            process_fun("已下载文件：{}".format(attachment))
                except:
                    continue

            conn.close()
            conn.logout()
        else:
            if process_fun:
                process_fun("邮箱{}登录失败！".format(self._account))


if __name__ == '__main__':
    def process_msg(msg):
        print(msg)


    # 邮箱账号列表
    account_list = [
        {
            "email": "836289789@qq.com",  # 邮箱
            "password": "rlsvlozatxacbbgj",  # 授权密码
            "server": "imap.qq.com"  # 服务器地址
        }
    ]

    # 文件保存目录
    _dir = r"./"

    # 邮件开始日期和结束日期
    startdate = "20221206"
    enddate = "20221206"

    # 下载
    for account in account_list:
        _email = account['email']
        _password = account['password']
        _server = account['server']
        etool = IMAP_Downemail(_email, _password, _server, _dir, startdate, enddate)
        etool.scanDown(process_msg)

    print('Done.')
