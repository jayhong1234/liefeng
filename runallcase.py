  # coding:utf-8
import unittest, HTMLTestRunner, os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import pandas as pd
import os


# 用例保存位置-文件目录
case_path = os.path.join(os.getcwd())
# case_path="D:\\liefeng\\liefeng2\\liefeng\\appzhidian"
# 报告保存位置-文件目录
report_path = os.path.join(os.getcwd(), "report")
print case_path


def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py')
    print discover
    return discover

def email(filepath):
    subject=data.iloc[0,2]
    smtpserver='smtp.mxhichina.com'
    sender="lih@liefengtech.com"
    psw2="jayhong1234**"
    receiver="jayhong1234@163.com"
#data.iloc[range(1,14), 2]
    with open(filepath,"rb")as fp:
        mail_body=fp.read()
    msg=MIMEMultipart()
    msg["from"]=Header(sender)
    msg["to"]=",".join(receiver)
    msg["Subject"]=Header(subject, 'utf-8')
    body=MIMEText(mail_body,"html","utf-8")
    msg.attach(body)
    att=MIMEText(mail_body,"base 64","utf-8")
    att["Content-Type"]="application/octet-stream"
    att["Content-Disposition"]='attachment;filename="TestReport.html"'

    msg.attach(att)
    smtp=smtplib.SMTP()
    smtp.connect(smtpserver,25)
    smtp.login(sender, psw2)

    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()

# # 保存测试报告地址-文件目录
# if __name__=='__main__':
report_abspath = "D:\\liefeng\\liefeng1\\log\\result2.html"
fp = open(report_abspath, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"指点appUI功能测试报告", description=u"用例执行情况")
runner.run(all_case())
fp.close()

data = pd.read_excel('D:\\liefeng\\test_jmeter\\zhidian\\test_login\\jmeter_case\\sendemail.xls')
filepath=("D:\\liefeng\\liefeng1\\log\\result2.html")
email(filepath)
