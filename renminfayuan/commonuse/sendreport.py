#coding=utf-8


import os,sys
import time
import smtplib
import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

reportpath=os.path.split(os.path.realpath(__file__))[0]+ "\\..\\testreports\\"

now_time=time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())
reportFile=reportpath + now_time +".html"

class Sendreport(object):

    def creat_report_folder(self):
        if  not os.path.exists(reportpath):
            os.makedirs(reportpath)
        if not os.path.exists(reportpath):
            return None

    def creat_test_report(self):
        rp=file(reportFile,"wb")
        report=HTMLTestRunner.HTMLTestRunner(stream=rp,title=u"自动化测试报告",description=u"用例测试情况")
        #rp.close()
        return report



#reportpath = os.path.join(os.getcwd(), 'testReports')  # 测试报告的路径
class SendMail(object):

    def get_report(self):  # 该函数的作用是为了在测试报告的路径下找到最新的测试报告

        dirs = os.listdir(reportpath)
        dirs.sort()
        newreportname = dirs[-1]
        print('The new report name: {0}'.format(newreportname))
        return newreportname  # 返回的是测试报告的名字

    def take_messages(self):  # 该函数的目的是为了 准备发送邮件的的消息内容
        newreport = self.get_report()
        self.msg = MIMEMultipart()
        self.msg['Subject'] = u'自动化测试报告'  # 邮件的标题
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        newpath=os.path.join(reportpath, newreport)

        with open(newpath, 'rb') as f:
            mailbody = f.read()  # 读取测试报告的内容
        html = MIMEText(mailbody, _subtype='html', _charset='utf-8')  # 将测试报告的内容放在 邮件的正文当中
        self.msg.attach(html)  # 将html附加在msg里

        # html附件    下面是将测试报告放在附件中发送
        att1 = MIMEText(mailbody, 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'

        att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'  # 这里的filename可以任意写，写什么名字，附件的名字就是什么
        self.msg.attach(att1)

    def send(self):

        receivr='yangzhuo@pashanhoo.com'
        #receivr='yangzhuo@pashanhoo.com,zhujiacheng@pashanhoo.com'
        cc='yangzhuo@pashanhoo.com'
        sender = 'yangzhuo@pashanhoo.com'

        self.take_messages()

        self.msg['from'] =sender  # 发送邮件的人，这种是公司邮箱转发
        self.msg['to'] = receivr  # 收件人和发送人必须这里定义一下，执行才不会报错。
        self.msg['Cc']=cc

        smtp = smtplib.SMTP()
        smtp.connect('smtp.exmail.qq.com')
        smtp.ehlo()
        smtp.login('yangzhuo@pashanhoo.com', 'Yz1234')
        #smtp.sendmail(sender, receivr+cc, self.msg.as_string())  # 发送邮件
        smtp.sendmail(sender, receivr.split(",") , self.msg.as_string())  # 发送邮件
        smtp.close()
        print('sendmail success')


# if __name__ == '__main__':
#     sendMail = SendMail()
#     sendMail.send()


