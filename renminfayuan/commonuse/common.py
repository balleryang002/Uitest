# -*- coding:utf8 -*-

'''
commonuse method


'''


import time
from selenium.common.exceptions import NoSuchElementException
from log import Logger
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.commonuse.action_chains import ActionChains

commonlogger=Logger().creat_logs(name="COMMON")


class Common(object):

    def __init__(self,driver):
        self.driver=driver

    def quit(self):
        commonlogger.info("Quit brower!!")
        self.driver.quit()

    def forward(self):
        self.driver.forward()
        commonlogger.info("Click forward on current page.")

    def back(self):
        self.driver.back()
        commonlogger.info("Click back on current page.")

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        commonlogger.info("Wait for %d seconds." % seconds)

    def sleep(self,seconds):
        time.sleep(seconds)
        commonlogger.info("sleep for %d seconds." % seconds)

    def close(self):
        try:
            self.driver.close()
            commonlogger.info("Close and quit the browser.")
        except NameError as e:
            commonlogger.error("Failed to quit the browser with %s" % e)


    #获取单个唯一元素方法
    def findElement(self,selector,index=0):
        '''
        "id=>su"
        "xpath=>/html/body/div[3]/div/div/form/fieldset/div[3]/div[1]/input"

        :param selector: 元素的属性和值
        index:需要返回第几个元素
        :return:返回元素对象
        '''
        selector_key=selector.split("=>")[0]
        selector_value=selector.split("=>")[1]

        #获取index类型
        index_type=str(type(index))


        #如果是整形，则进入判断
        if "int" in index_type:

            #页面上某元素某属性是唯一值，获取其控件S
            if index== 0 :
                if selector_key=="id" or selector_key=="i":
                    try:
                        #element = self.driver.find_element_by_id(selector_value)
                        element=WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_id(selector_value))
                        commonlogger.info("Had find the elemet %s" % selector_key)
                    except NoSuchElementException as e:
                        commonlogger.warning("No such a Element")

                elif selector_key == "name" or selector_key == "n":
                    try:
                        element = self.driver.find_element_by_name(selector_value)
                        commonlogger.info("Had find the elemet %s" % selector_key)
                    except NoSuchElementException as e:
                        commonlogger.warning("No such a Element")


                elif selector_key == "class_name" or selector_key == "c":
                    try:
                        element = self.driver.find_element_by_class_name(selector_value)
                        commonlogger.info("Had find the elemet %s" % selector_key)
                    except NoSuchElementException as e:
                        commonlogger.warning("No such a Element")


                elif selector_key == "xpath" or selector_key == "x":
                    try:
                        element = self.driver.find_element_by_xpath(selector_value)
                        commonlogger.info("Had find the elemet %s" % selector_key)
                    except NoSuchElementException as e:
                        commonlogger.warning("No such a Element")

                elif selector_key == "link_text" or selector_key == "l":
                    try:
                        element = self.driver.find_element_by_link_text(selector_value)
                        commonlogger.info("Had find the elemet %s" % selector_key)
                    except NoSuchElementException as e:
                        commonlogger.warning("No such a Element")


                #遗留几个方法，待以后补充

                else:
                    raise NameError("Please enter a valid type of targeting elements.")

            #页面上存在多个元素的某个属性值相同，通过index去判断获取哪一个
            elif index>0:
                if selector_key == "id" or selector_key == "i":
                    try:
                        element = self.driver.find_element_by_id(selector_value)
                        commonlogger.info("Had find the elemet %s" % selector_key)
                    except NoSuchElementException as e:
                        commonlogger.warning("No such a Element")

                elif selector_key == "xpath" or selector_key == "x":
                    try:
                        element = self.driver.find_elements_by_xpath(selector_value)[index]
                        commonlogger.info("Had find the elemet %s" % selector_key)

                    except NoSuchElementException as e:
                        commonlogger.warning("No such a Element,maybe the value of index is too large")

                elif selector_key == "class_name" or selector_key == "c":
                    try:
                        element = self.driver.find_elements_by_class_name(selector_value)[index]
                        commonlogger.info("Had find the elemet %s" % selector_key)
                    except NoSuchElementException as e:
                        commonlogger.warning("No such a Element,maybe the value of index is too large")

                elif selector_key == "name" or selector_key == "n":
                    try:
                        element = self.driver.find_element_by_name(selector_value)[index]
                        commonlogger.info("Had find the elemet %s" % selector_key)
                    except NoSuchElementException as e:
                        commonlogger.warning("No such a Element,maybe the value of index is too large")

                elif selector_key == "tag" or selector_key == "t":
                    try:
                        element = self.driver.find_elements_by_tag_name(selector_value)[index]
                        commonlogger.info("Had find the elemet %s" % selector_key)
                    except NoSuchElementException as e:
                        commonlogger.warning("No such a Element,maybe the value of index is too large")

                # 遗留几个方法，待以后补充

                else:
                    raise NameError("Please enter a valid type of targeting elements.")


            else:
                commonlogger.warning("Err!Please make sure the argument of 'index' is more than 0")

        #如果不是整形，则进行告警
        else:
            commonlogger.warning("TYPEERR,Please give the 'int' type")



        return element

    #获取单个唯一元素方法
    # def find2Element(self,selector,index=0):
    #     '''
    #     "id=>su"
    #     "xpath=>/html/body/div[3]/div/div/form/fieldset/div[3]/div[1]/input"
    #
    #     :param selector: 元素的属性和值
    #     index:需要返回第几个元素
    #     :return:返回元素对象
    #     '''
    #     selector_key=selector.split("=>")[0]
    #     selector_value=selector.split("=>")[1]
    #
    #     #获取index类型
    #     index_type=type(index)
    #
    #     #如果是整形，则进入判断
    #     if index_type=="int":
    #
    #         #页面上某元素某属性是唯一值，获取其控件S
    #         if index== 0 :
    #             if selector_key=="id" or selector_key=="i":
    #                 try:
    #                     #element = self.driver.find_element_by_id(selector_value)
    #                     element=WebDriverWait(self.driver,10).until(lambda driver: driver.find_element_by_id(selector_value))
    #                     commonlogger.info("Had find the elemet %s" % selector_key)
    #                 except NoSuchElementException as e:
    #                     commonlogger.warning("No such a Element")
    #
    #             elif selector_key == "name" or selector_key == "n":
    #                 try:
    #                     element = self.driver.find_element_by_name(selector_value)
    #                     commonlogger.info("Had find the elemet %s" % selector_key)
    #                 except NoSuchElementException as e:
    #                     commonlogger.warning("No such a Element")
    #
    #
    #             elif selector_key == "class_name" or selector_key == "c":
    #                 try:
    #                     element = self.driver.find_element_by_class_name(selector_value)
    #                     commonlogger.info("Had find the elemet %s" % selector_key)
    #                 except NoSuchElementException as e:
    #                     commonlogger.warning("No such a Element")
    #
    #
    #             elif selector_key == "xpath" or selector_key == "x":
    #                 try:
    #                     element = self.driver.find_element_by_xpath(selector_value)
    #                     commonlogger.info("Had find the elemet %s" % selector_key)
    #                 except NoSuchElementException as e:
    #                     commonlogger.warning("No such a Element")
    #
    #             elif selector_key == "link_text" or selector_key == "l":
    #                 try:
    #                     element = self.driver.find_element_by_link_text(selector_value)
    #                     commonlogger.info("Had find the elemet %s" % selector_key)
    #                 except NoSuchElementException as e:
    #                     commonlogger.warning("No such a Element")
    #
    #
    #             #遗留几个方法，待以后补充
    #
    #             else:
    #                 raise NameError("Please enter a valid type of targeting elements.")
    #
    #         #页面上存在多个元素的某个属性值相同，通过index去判断获取哪一个
    #         elif index>0:
    #             if selector_key == "id" or selector_key == "i":
    #                 try:
    #                     element = self.driver.find_element_by_id(selector_value)
    #                     commonlogger.info("Had find the elemet %s" % selector_key)
    #                 except NoSuchElementException as e:
    #                     commonlogger.warning("No such a Element")
    #
    #             elif selector_key == "xpath" or selector_key == "x":
    #                 try:
    #                     element = self.driver.find_elements_by_xpath(selector_value)[index]
    #                     commonlogger.info("Had find the elemet %s" % selector_key)
    #
    #                 except NoSuchElementException as e:
    #                     commonlogger.warning("No such a Element,maybe the value of index is too large")
    #
    #             elif selector_key == "class_name" or selector_key == "c":
    #                 try:
    #                     element = self.driver.find_elements_by_class_name(selector_value)[index]
    #                     commonlogger.info("Had find the elemet %s" % selector_key)
    #                 except NoSuchElementException as e:
    #                     commonlogger.warning("No such a Element,maybe the value of index is too large")
    #
    #             elif selector_key == "name" or selector_key == "n":
    #                 try:
    #                     element = self.driver.find_element_by_name(selector_value)[index]
    #                     commonlogger.info("Had find the elemet %s" % selector_key)
    #                 except NoSuchElementException as e:
    #                     commonlogger.warning("No such a Element,maybe the value of index is too large")
    #
    #             elif selector_key == "tag" or selector_key == "t":
    #                 try:
    #                     element = self.driver.find_elements_by_tag_name(selector_value)[index]
    #                     commonlogger.info("Had find the elemet %s" % selector_key)
    #                 except NoSuchElementException as e:
    #                     commonlogger.warning("No such a Element,maybe the value of index is too large")
    #
    #             # 遗留几个方法，待以后补充
    #
    #             else:
    #                 raise NameError("Please enter a valid type of targeting elements.")
    #
    #
    #         else:
    #             commonlogger.warning("Err!Please make sure the argument of 'index' is more than 0")
    #
    #     #如果不是整形，则进行告警
    #     else:
    #         commonlogger.warning("TYPEERR,Please give the 'int' type")
    #
    #
    #
    #     return element


    def input(self,selector,text):
        element=self.findElement(selector)
        element.clear()
        try:
            element.send_keys(text)
            commonlogger.info("Input the text to the box")

        except NameError as e :
            commonlogger.warning("Fail to input the text")






    def clear(self,selector):
        element=self.findElement(selector)
        try:
            element.clear()
            commonlogger().info("Clear the text in the box")
        except NameError as e:
            commonlogger.warning("Fail to clear the text")

    def click(self,selector):
        element = self.findElement(selector)
        try:
            element.click()
            commonlogger.info("Click Successfully!!")
        except NoSuchElementException as e:
            commonlogger.warning("Fail to click ")


    def rightClick(self,selector):
        element = self.findElement(selector)
        ActionChains(self.driver).context_click(element).perform()
        commonlogger.info("click the right click-button successfully")



    def movetoElement(self,selector):
        element = self.findElement(selector)
        ActionChains(self.driver).move_to_element(element).perform()
        commonlogger.info("move to the element successfully")

    def doubleClick(self,selector):
        element = self.findElement(selector)
        ActionChains(self.driver).double_click(element).perform()
        commonlogger.info("double click the element successfully")








    def refresh(self):
        commonlogger.info("refresh the web !")
        self.refresh()


    def getBrowerInfo(self,attribute):


        if attribute=="url":
            try:
                browerinfo = self.driver.current_url
                commonlogger.info("Had find the url: %s" % browerinfo)
            except NoSuchElementException as e:
                commonlogger.warning("No such a Element")

        elif attribute=="title":
             try:
                 browerinfo = self.driver.title
                 commonlogger.info("Had find the title: %s" % browerinfo)
             except NoSuchElementException as e:
                 commonlogger.warning("No such a Element")

        elif attribute == "version":
            try:
                element_attribute = self.driver.capabilities['version']
                commonlogger.info("Had find the version: %s" % element_attribute)
            except NoSuchElementException as e:
                commonlogger.warning("No such a Element")

        # elif attribute=="text":
        #     try:
        #         element=self.findElements(selector)
        #         element_attribute=element.text
        #         commonlogger.info("The attribute text of element is %s" %element_attribute)
        #     except NoSuchElementException as e:
        #         commonlogger.warning("No such a Element")
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return browerinfo

    def getAttribute(self,attribute,selector):

        element=self.findElement(selector)

        if attribute=="text":
            try:
                element_attribute = element.text
                commonlogger.info("The attribute text of element is %s" % element_attribute)

            except NoSuchElementException as e:
                commonlogger.warning("No such a Element")

        elif attribute=="value":
            try:
                element_attribute=element.get_attribute("value")
                commonlogger.info("The attribute value of element is %s" % element_attribute)
            except NoSuchElementException as e:
                commonlogger.warning("No such a Element")

        elif attribute=="href":
            try:
                element_attribute = element.get_attribute("href")
                commonlogger.info("The attribute href of element is %s" % element_attribute)
            except NoSuchElementException as e:
                commonlogger.warning("No such a Element")



        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element_attribute



    def setwindowsize(self,length,width):
        self.driver.set_window_size(length,width)
        commonlogger.info("Had set the windows size")

    def switchtoWindow(self,num):
        '''页面打开顺序和窗口句柄列表索引的关系
        1 2 3
        0 2 1
        '''
        all_handle=self.driver.window_handles
        self.driver.switch_to_window(all_handle[num])
        commonlogger.info("swich to the window successfully")

    #执行js脚本
    def executeJscript(self,js):
        self.driver.execute_script(js)
        commonlogger.info("execute the Javascript successfully")

    #拖动主滑动条
    def scrollTo(self,width,height):
        '''
        :param width: 拖动条的宽度值，即横向滑动条需要拖动到的位置
        :param height:拖动条的高度值，即竖向滑动条需要拖动到的位置
        '''
        js = "window.scrollTo(%d,%d)" %(width,height)
        self.executeJscript(js)
        commonlogger.info("scroll to the %d,%d successfully" %(width,height) )

    #拖动竖向内嵌滑动条
    def scrollTotop(self,height,selector,index=0):
        '''
        :param height: 内嵌拖动条的高度值，即需要拖动到的位置
        :param selector:内嵌拖动条的元素值
        :param index:页面上该属性值的序列
        :return:
        '''
        selector_key = selector.split("=>")[0]
        selector_value = selector.split("=>")[1]

        if selector_key == "id" or selector_key == "i":
            js="document.getElementById('%s').scrollTop=%d"%(selector_value,height)

        elif selector_key == "class" or selector_key == "c":
            js="document.getElementsByClassName('%s')[%d].scrollTop=%d"%(selector_value,index,height)



        print js
        self.executeJscript(js)
        commonlogger.info("Had scroll the bar to the height %d" % height)

    #拖动横向内嵌滑动条
    def scrollToleft(self,width,selector,index=0):
        '''
        :param width:内嵌拖动条的高度值，即需要拖动到的位置
        :param selector:内嵌拖动条的元素值
        :param index:页面上该属性值的序列
        :return:
        '''
        selector_key = selector.split("=>")[0]
        selector_value = selector.split("=>")[1]

        if selector_key == "id" or selector_key == "i":
            js="document.getElementById('%s').scrollLeft=%d"%(selector_value,width)

        elif selector_key == "class" or selector_key == "c":
            js="document.getElementsByClassName('%s')[%d].scrollLeft=%d"%(selector_value,index,width)



        self.executeJscript(js)
        commonlogger.info("Had scroll the bar to the width %d" % width)






    def scrollIntoView(self,selector):
        element = self.findElement(selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)




















