# -*- coding:UTF-8 -*-


from selenium import webdriver
import test_commonTool

brower=test_commonTool.chooseBrower("chrome")

driver=test_commonTool.commonTool(brower)

driver.getUrl("http://192.168.88.3:3001/bear/")

# driver.findviewbyid("username").
# driver.sleep(1)
#
# driver.input("admin")


