#coding=utf-8


import sys
import unittest

sys.path.append("D:\\auto_test")

from renminfayuan.commonuse.brower_engine import BrowerEngine
from renminfayuan.pageobject.loadingpage import LoadingPage
import renminfayuan.commonuse.common

case_3_logger=renminfayuan.commonuse.common.Logger().creat_logs(name="case3")

class Loading(unittest.TestCase):

    def setUp(self):
        case_3_logger.info("starting case3")
        brower=BrowerEngine(self)
        self.driver=brower.openbrower(self)


    def tearDown(self):
        quit()

    def test_loading_page3(self):

        loadingpage=LoadingPage(self.driver)
        loadingpage.sleep(3)

        loadingpage.input_username("admin")
        loadingpage.sleep(3)

        loadingpage.input_password("1")
        loadingpage.sleep(3)

        loadingpage.click_sign()

        a=loadingpage.show_text("url")
        print type(a)

        b=loadingpage.show_text("title")
        print b

        c=loadingpage.show_text("version")
        print c







