#coding=utf-8

'''


'''


import logging
import os
import time

path=os.path.split(os.path.realpath(__file__))[0]

logpath= path + "\\..\\log"


class Logger(object):

    def creat_logfolder(self):
        if not os.path.exists(logpath):
            os.makedirs(logpath)
        if not os.path.exists(logpath):
            return  None
        if not os.path.exists(logpath +"\\logs"):
            os.makedirs(logpath +"\\logs")
        if not os.path.exists(logpath +"\\pics"):
            os.makedirs(logpath +"\\pics")



    def creat_logs(self,name):
        #name是传入的对应模块的名字
        #在调用Logger类以及其方法的时候，用到mylogger=Logger().creat_logs(name=对应模块)
        self.creat_logfolder()
        logger=logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        timeFormater="%Y%m%d%H%M$S"
        nowTime=time.strftime(timeFormater,time.localtime())

        #将日志文件命名
        fileName=nowTime + ".log"

        #给日志文件设置路径
        logfilepath=logpath +"\\logs\\" + fileName


        fh=logging.FileHandler(logfilepath)
        fh.setLevel(logging.INFO)

        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)

        logFormater=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(logFormater)
        ch.setFormatter(logFormater)

        logger.addHandler(fh)
        logger.addHandler(ch)

        return logger




