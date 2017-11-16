# coding=utf-8
import time
from selenium import webdriver
import random



driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)


driver.get("http://192.168.88.3:3000/boat/#home")
time.sleep(2)

driver.find_element_by_id("username").send_keys("notice")
time.sleep(2)

driver.find_element_by_id("password").send_keys("123456")
time.sleep(2)

driver.find_element_by_class_name("btn").click()
time.sleep(2)

driver.find_element_by_id("drop5").click()
time.sleep(2)


for i in range(50000):
    now_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())

    driver.find_element_by_id("notice-addBtn").click()
    time.sleep(2)

    driver.find_element_by_id("notice-bt").send_keys(now_time)
    time.sleep(2)

    #通过点击下拉菜单按钮，激活下拉菜单
    driver.find_element_by_class_name("input-group-addon").click()
    #生成一个随机的1-3的正整数
    key=random.randrange(1,4)
    print key
    if key==1:
        #随机进行下拉菜单点击
        driver.find_element_by_xpath("//ul[@class='dropdown-list']/li[1]").click()
    elif key==2:
        driver.find_element_by_xpath("//ul[@class='dropdown-list']/li[2]").click()
    elif key==3:
        driver.find_element_by_xpath("//ul[@class='dropdown-list']/li[3]").click()
    else:
        print"err"
    time.sleep(2)

    #切换进入frame
    driver.switch_to.frame("ueditor_0")

    #找到文本框的xpath属性，并且进行输入操作
    driver.find_element_by_xpath("/html/body").send_keys(now_time)
    time.sleep(2)

    #操作完毕后退出，切换到父文本框
    driver.switch_to.parent_frame()
    time.sleep(1)

    driver.find_element_by_id("notice-saveBtn").click()
    time.sleep(5)


    driver.refresh()



