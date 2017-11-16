#coding=utf-8


import sys
import unittest

sys.path.append("D:\\auto_test")

from renminfayuan.commonuse.brower_engine import BrowerEngine
from renminfayuan.pageobject.loadingpage import LoadingPage
import renminfayuan.commonuse.common

case_1_logger=renminfayuan.commonuse.common.Logger().creat_logs(name="case1")

class Loading(unittest.TestCase):

    def setUp(self):
        case_1_logger.info("starting case1")
        brower=BrowerEngine(self)
        self.driver=brower.openbrower(self)


    def tearDown(self):
        pass

    def test_loading_page1(self):

        loadingpage=LoadingPage(self.driver)

        loadingpage.inputyouwant("hello world")

        loadingpage.click_search()

        loadingpage.sleep(10)


        # loadingpage.scrolltodown(100,1000)
        # loadingpage.sleep(3)









# if __name__ == '__main__':
#     unittest.main()