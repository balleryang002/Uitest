# -*- coding: utf-8 -*-

from renminfayuan.commonuse.common import Common
from renminfayuan.commonuse.IOexcel import IOexcel

value_baidu=IOexcel().readExcle()

class LoadingPage(Common):

    # loading_name = "id=>username"
    #
    # loading_password = "id=>password"
    #
    # loading_bt="xpath=>//div[@class='row']/div/input"

    # loading_baiduyixia="id=>su"
    #loading_input2="id=>kw"





    loading_baiduyixia=(value_baidu[1][0] + "=>" + value_baidu[1][1]).encode("utf-8")
    loading_input=IOexcel().toStr(value_baidu[0][0] + "=>" + value_baidu[0][1])


    scrollbar="class=>scroll"


    def input_username(self,text):
        self.input(self.loading_name,text)

    def input_password(self,text):
        self.input(self.loading_password,text)

    def click_sign(self):
        self.click(self.loading_bt)


    def rightclick(self):
        self.right_click(self.loading_baiduyixia)



    def getvalue(self,attribute):
        return self.getAttribute(attribute,self.loading_baiduyixia)

    def scrolltodown(self,width,height):
        self.scrollTo(width,height)

    def scrolllll(self,height,index):
        self.scrollToleft(height,self.scrollbar,index=1)

    def inputyouwant(self,text):
        self.input(self.loading_input,text)

    def click_search(self):
        self.click(self.loading_baiduyixia)











