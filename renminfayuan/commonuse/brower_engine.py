#coding=utf-8


import ConfigParser
import os

from selenium import webdriver

from renminfayuan.commonuse.log import Logger

browerenginelogger=Logger().creat_logs(name="BROWERENINE")

class BrowerEngine(object):

    def __init__(self,driver):
        self.driver=driver

    def openbrower(self,driver):
        #读取配置文件路径
        config=ConfigParser.ConfigParser()
        configpath=os.path.split(os.path.realpath(__file__))[0]+"\\..\\config\\common.ini"
        #读取配置文件
        config.read(configpath)

        browertype=config.get("webType","browserName")
        browerenginelogger.info("you have select %s" %browertype)

        url=config.get("browerurl","url")
        browerenginelogger.info("you want to study-old %s" % url)

        if browertype =="Chrome":
            driver=webdriver.Chrome()
            browerenginelogger.info("starting open chrome")
        elif browertype=="IE":
            driver=webdriver.Ie()
            browerenginelogger.info("starting open ie")
        elif browertype=="FrieFox":
            driver=webdriver.Firefox()
            browerenginelogger.info("starting opne firebox")

        driver.get(url)
        browerenginelogger.info("open url: %s" % url)

        driver.maximize_window()
        browerenginelogger.info("Maximize the current window.")

        driver.implicitly_wait(10)
        browerenginelogger.info("Set implicitly wait 10 seconds.")

        return driver

    def quitbrower(self):
        browerenginelogger.info("quit brower!")
        self.driver.quit()


