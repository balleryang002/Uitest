# -*- coding:UTF-8 -*-

from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("http://192.168.88.3:3001/bear/#home")
time.sleep(1)

driver.find_element_by_id("username").send_keys("admin")
time.sleep(1)

driver.find_element_by_id("password").send_keys("1234")
time.sleep(1)

driver.find_element_by_class_name("btn").click()
time.sleep(1)

driver.find_element_by_link_text(u'办理查询').click()
