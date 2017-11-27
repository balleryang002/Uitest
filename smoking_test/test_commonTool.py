# -*- coding:UTF-8 -*-

import time
from selenium import webdriver

def chooseBrower(brower):
    if brower=="chrome":
        return webdriver.Chrome()
    elif brower=="firefox":
        return webdriver.Firefox()
    elif brower=="ie":
        return webdriver.Ie()


class commonTool(object):

    def __init__(self,driver):
        self.driver = driver

    def getUrl(self,url):
        self.driver.get(url)


    def sleep(self,seconds):
        time.sleep(seconds)

    def findviewbyid(self,id):
        self.driver.find_element_by_id(id)

    def input(self,str):
        self.driver.send_keys(str)




