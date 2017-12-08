#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

class smtp_163():
    def __init__(self,file_path):
        # 发送邮件相关的参数
        self.smtpserver = "smtp.163.com"
        self.port = 0
        self.sender = "wanghaihong200@163.com"
        self.psw = "whh200792"
        self.receiver = "296701193@qq.com"

        # 编辑邮件的内容
        #读文件
        self.file_path = file_path
        with open(file_path,'rb') as fp:
            self.mail_body = fp.read()

        self.msg = MIMEMultipart()
        self.msg['from'] = self.sender
        self.msg['to'] = self.receiver
        self.msg['subject'] = "测试报告"
        #正文
        self.body = MIMEText(self.mail_body, 'html', 'utf-8')
        self.msg.attach(self.body)

        #附件
        self.att = MIMEText(self.mail_body, "base64", "utf-8")
        self.att["Content-Type"] = "application/octet-stream"
        self.att["Content-Disposition"] = "attachment;filename=%s.html"%time.strftime("%Y_%m_%d_%H_%M_%p")
        self.msg.attach(self.att)


    def  send_email(self):
        # 发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(self.smtpserver)
        smtp.login(self.sender, self.psw)
        smtp.sendmail(self.sender, self.receiver, self.msg.as_string())
        smtp.quit()

    def error_mail(self,res):
        if res:
            self.send_email()