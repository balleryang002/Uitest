#coding=utf-8


import sys
import unittest

sys.path.append("D:\\auto_test")

from renminfayuan.commonuse.brower_engine import BrowerEngine
from renminfayuan.pageobject.loadingpage import LoadingPage
import renminfayuan.commonuse.common

case_2_logger=renminfayuan.commonuse.common.Logger().creat_logs(name="case2")

class Loading(unittest.TestCase):

    def setUp(self):
        case_2_logger.info("starting case2")
        brower=BrowerEngine(self)
        self.driver=brower.openbrower(self)


    def tearDown(self):
        quit()

    def test_loading_page2(self):
        loadingpage=LoadingPage(self.driver)
        loadingpage.scrolllll(150,1)
        loadingpage.sleep(3)











# if __name__ == '__main__':
#     unittest.main()