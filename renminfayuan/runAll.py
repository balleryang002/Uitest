#coding=utf-8


import sys
import os,time
import unittest
import HTMLTestRunner

sys.path.append("D:\\auto_test")

from renminfayuan.commonuse.sendreport import SendMail

reportpath=os.path.split(os.path.realpath(__file__))[0]+ "\\testreports\\"

now_time=time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())
reportFile=reportpath + now_time +".html"
rp=file(reportFile,"wb")



casepath=os.path.split(os.path.realpath(__file__))[0]+ "\\testsuites\\"

# 构建suite
suite=unittest.defaultTestLoader.discover(casepath)


if __name__ =='__main__':


    runner = HTMLTestRunner.HTMLTestRunner(stream=rp, title=u"自动化测试报告", description=u"用例测试情况")
    runner.run(suite)
    rp.close()



    # 测试结束之后，执行邮件发送报告
    SendMail().send()



