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

# assert  driver.title=="阜宁县不动产登记网上申请系统"
# print "go on "


#预售商品房买卖预告登记
driver.find_element_by_xpath('//*[@id="content-index"]/div[2]/a[1]/div/span[2]').click()
time.sleep(1)

#共有方式为按份拥有
driver.find_element_by_xpath('//*[@id="bdcsqb-form"]/div/label[4]').click()
time.sleep(1)

#申请人情况
#===================================================================
#填写权利人1
timeFormater="%Y%m%d%H%M$S"
nowTime=time.strftime(timeFormater,time.localtime())
driver.find_element_by_id("qwrxm1").send_keys(u'张三'+str(nowTime))
time.sleep(1)

#填写共有比例
driver.find_element_by_id("gybl1").send_keys("50")
time.sleep(1)

#选择证件种类为身份证
driver.find_element_by_class_name("input-group-addon").click()
#driver.find_element_by_xpath('//*[class="dropdown-list"]/li[1]').click()
driver.find_element_by_xpath('//*[@id="bdcsqb-form"]/table/tbody/tr[3]/td[2]/div/ul/li[1]').click()
time.sleep(1)

#填写身份证号
driver.find_element_by_id("zjh1").send_keys("320104198905241424")
time.sleep(1)

#填写通讯住址
driver.find_element_by_id("txdz1").send_keys(u'南京爬山虎ajiojadjaJJSKKDFA')
time.sleep(1)

#填写邮编
driver.find_element_by_id("yb1").send_keys('125243214')
time.sleep(1)

#填写法人代表
driver.find_element_by_id("fddbr1").send_keys(u'张三三'+str(nowTime))
time.sleep(1)

#填写联系电话
driver.find_element_by_id("flxdh1").send_keys("123456789")
time.sleep(1)

#填写代理人姓名
driver.find_element_by_id("dlrxm1").send_keys(u'张三三三'+str(nowTime))
time.sleep(1)

#填写联系电话
driver.find_element_by_id("dlxdh1").send_keys("987654321")
time.sleep(1)

#填写代理机构
driver.find_element_by_id("dljg1").send_keys(u'江苏爬山虎责任有先公司南京分公司集合产品部门')
time.sleep(1)
#======================================================================
#滑动
driver.execute_script('window.scrollTo(0,500)')

#填写权利人2
driver.find_element_by_id("qwrxm2").send_keys(u'张四'+str(nowTime))
time.sleep(1)

#填写共有比例
driver.find_element_by_id("gybl2").send_keys("50")
time.sleep(1)

#选择证件种类为身份证
driver.find_elements_by_class_name("input-group-addon")[1].click()
#driver.find_element_by_xpath('//*[@id="bdcsqb-form"]/table/tbody/tr[10]/td[2]/div/span').click()
driver.find_element_by_xpath('//*[@id="bdcsqb-form"]/table/tbody/tr[10]/td[2]/div/ul/li[1]').click()
time.sleep(1)

#填写身份证号
driver.find_element_by_id("zjh2").send_keys("320104198905241415")
time.sleep(1)

#填写通讯住址
driver.find_element_by_id("txdz2").send_keys(u'南京爬山虎ajiojadjaJJSKKDFA上纠结发肌肤大海')
time.sleep(1)

#填写邮编
driver.find_element_by_id("yb2").send_keys('125243214')
time.sleep(1)

#填写法人代表
driver.find_element_by_id("fddbr2").send_keys(u'张三三'+str(nowTime))
time.sleep(1)

#填写联系电话
driver.find_element_by_id("flxdh2").send_keys("123456789")
time.sleep(1)

#填写代理人姓名
driver.find_element_by_id("dlrxm2").send_keys(u'张三三三'+str(nowTime))
time.sleep(1)

#填写联系电话
driver.find_element_by_id("dlxdh2").send_keys("987654321")
time.sleep(1)

#填写代理机构
driver.find_element_by_id("dljg2").send_keys(u'江苏爬山虎案件点击阿达')
time.sleep(1)


#======================================================================
#滑动
driver.execute_script('window.scrollTo(0,500)')

#填写义务人1
driver.find_element_by_id("ywrxm1").send_keys(u'李四'+str(nowTime))
time.sleep(1)

#填写共有比例
driver.find_element_by_id("ygybl1").send_keys("80")
time.sleep(1)

#选择证件种类为身份证
driver.find_elements_by_class_name("input-group-addon")[2].click()
driver.find_element_by_xpath('//*[@id="bdcsqb-form"]/table/tbody/tr[17]/td[2]/div/ul/li[1]').click()
time.sleep(1)

#填写身份证号
driver.find_element_by_id("yzjh1").send_keys("320107199898765432")
time.sleep(1)

#滑动
driver.execute_script('window.scrollTo(0,500)')

#填写通讯住址
driver.find_element_by_id("ytxdz1").send_keys(u'浙江爬山虎ajiojadjaJJSKKDFA')
time.sleep(1)

#填写邮编
driver.find_element_by_id("yyb1").send_keys('125243214')
time.sleep(1)

#填写法人代表
driver.find_element_by_id("yfddbr1").send_keys(u'李四四'+str(nowTime))
time.sleep(1)

#填写联系电话
driver.find_element_by_id("yflxdh1").send_keys("123456789")
time.sleep(1)

#填写代理人姓名
driver.find_element_by_id("ydlrxm1").send_keys(u'李四四四'+str(nowTime))
time.sleep(1)

#填写联系电话
driver.find_element_by_id("ydlxdh1").send_keys("987654321")
time.sleep(1)

#填写代理机构
driver.find_element_by_id("ydljg1").send_keys(u'浙江爬山虎')
time.sleep(1)

#======================================================================
#滑动
driver.execute_script('window.scrollTo(0,500)')

#填写义务人2
driver.find_element_by_id("ywrxm2").send_keys(u'李五'+str(nowTime))
time.sleep(1)

#填写共有比例
driver.find_element_by_id("ygybl2").send_keys("80")
time.sleep(1)

#选择证件种类为身份证
driver.find_elements_by_class_name("input-group-addon")[3].click()
driver.find_element_by_xpath('//*[@id="bdcsqb-form"]/table/tbody/tr[24]/td[2]/div/ul/li[1]').click()
time.sleep(1)

#填写身份证号
driver.find_element_by_id("yzjh2").send_keys("320107199898765432")
time.sleep(1)


#填写通讯住址
driver.find_element_by_id("ytxdz2").send_keys(u'浙江爬山虎ajiojadjaJJSKKDFA')
time.sleep(1)

#填写邮编
driver.find_element_by_id("yyb2").send_keys('125243214')
time.sleep(1)

#填写法人代表
driver.find_element_by_id("yfddbr2").send_keys(u'李四五'+str(nowTime))
time.sleep(1)

#填写联系电话
driver.find_element_by_id("yflxdh2").send_keys("123456789")
time.sleep(1)

#填写代理人姓名
driver.find_element_by_id("ydlrxm2").send_keys(u'李四四五'+str(nowTime))
time.sleep(1)

#填写联系电话
driver.find_element_by_id("ydlxdh2").send_keys("987654321")
time.sleep(1)

#填写代理机构
driver.find_element_by_id("ydljg2").send_keys(u'浙江爬山虎责任有先公司南京分公司集合产品部门')
time.sleep(1)

#不动产情况
#===================================================================
#滑动
driver.execute_script('window.scrollTo(0,500)')

#填写坐落
driver.find_element_by_id("zl").send_keys(u'南京将军大道120号Ab座')
time.sleep(1)

#填写不动产单元号
driver.find_element_by_id("bdcdyh").send_keys("602014-221452123")
time.sleep(1)

#选择不动产类型为土地
driver.find_elements_by_class_name("input-group-addon")[4].click()
driver.find_element_by_xpath('//*[@id="bdcsqb-form"]/table/tbody/tr[30]/td[4]/div/ul/li[3]').click()
time.sleep(1)

#填写宗地面积
driver.find_element_by_id("zdzhmj").send_keys("5200")
time.sleep(1)

#选择宗地用途住宿餐饮用地
driver.find_elements_by_class_name("input-group-addon")[5].click()
driver.find_element_by_xpath('//*[@id="bdcsqb-form"]/table/tbody/tr[31]/td[4]/div/ul/li[8]').click()
time.sleep(1)

#填写定着物面积
driver.find_element_by_id("dzwmj").send_keys("3050")
time.sleep(1)

#选择定作物用途为别墅
driver.find_elements_by_class_name("input-group-addon")[6].click()
driver.find_element_by_xpath('//*[@id="bdcsqb-form"]/table/tbody/tr[32]/td[4]/div/ul/li[18]').click()
time.sleep(1)

#选择宗地权利性质为授权经营
driver.find_elements_by_class_name("input-group-addon")[7].click()
driver.find_element_by_xpath('//*[@id="bdcsqb-form"]/table/tbody/tr[33]/td[2]/div/ul/li[8]').click()
time.sleep(1)

#选择用海类型为船舶工业用海
driver.find_elements_by_class_name("input-group-addon")[8].click()
driver.find_element_by_xpath('//*[@id="bdcsqb-form"]/table/tbody/tr[33]/td[4]/div/ul/li[12]').click()
time.sleep(1)

#选择构筑物类型为海上构筑物
driver.find_elements_by_class_name("input-group-addon")[9].click()
driver.find_element_by_xpath('//*[@id="bdcsqb-form"]/table/tbody/tr[34]/td[2]/div/ul/li[8]').click()
time.sleep(1)

#选择林种为经济林
driver.find_elements_by_class_name("input-group-addon")[10].click()
driver.find_element_by_xpath('//*[@id="bdcsqb-form"]/table/tbody/tr[34]/td[4]/div/ul/li[4]').click()
time.sleep(1)

#填写原不动产权证书号
driver.find_element_by_id("ybdcqzh").send_keys("6200014-8531452332")
time.sleep(1)

#抵押情况
#=====================================================================================
#滑动
driver.execute_script('window.scrollTo(0,10000)')

#填写被担保债权数额
driver.find_element_by_id("bdbje").send_keys("250")
time.sleep(1)

driver.find_element_by_id("zwlxqx-kssj").send_keys("2018-05-15")
time.sleep(1)

driver.find_element_by_id("dyfw").send_keys("500")
time.sleep(1)

#===========================
driver.find_element_by_id("bdcsqb-nextBtn").click()
time.sleep(5)


driver.find_element_by_class_name("addcl").click()
time.sleep(2)

#driver.find_element_by_id("jqg16_clmc").send_keys(u'材料1Aa')
driver.find_element_by_name("clmc").send_keys(u'材料1Aa')
time.sleep(1)

driver.find_element_by_name("bz").send_keys(u'材料1Aa')
time.sleep(1)

driver.find_element_by_class_name("upfj").click()
time.sleep(1)

driver.find_element_by_name("file").send_keys("E:\\test-resource\\1.png")
driver.find_element_by_name("file").send_keys("E:\\test-resource\\2.jpg")
driver.find_element_by_name("file").send_keys("E:\\test-resource\\3.pdf")
time.sleep(2)

driver.find_element_by_id("startUpload_btn").click()
time.sleep(5)

driver.find_element_by_class_name("close").click()
time.sleep(1)

driver.find_element_by_class_name("submitcl").click()

