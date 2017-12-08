#coding:utf-8
import unittest
from case.happy_public.wang_selenium import Wang
from case.happy_public.wang_logging import Log
from case.happy_public.wang_selenium import Browser
from case.happy_public.public_excel import getDdtExcel
from ddt import ddt,data,unpack
from case.login.login_bussiness_page import LoginBussinessPage
import time

log = Log()

# @ddt
class Login_test(unittest.TestCase):
    def setUp(self):
        self.driver = Wang(Browser())
        # 调用bussiness_login方法
        self.bussiness_login()
        log.info('############################### START ###############################')

    # @data(*getDdtExcel())
    # @unpack
    def test_add_goods(self):
        '''添加商品'''
        #店铺管理-》商品管理
        self.driver.click(('css selector', "#side-menu li:nth-child(2)"))
        self.driver.click(('link text', "商品管理"))
        #添加商品
        self.driver.switch_to_frame(('name','iframe4'))
        self.driver.click(('css selector', 'button[type="button"]:nth-child(5)'))
        # time.sleep(3)
        #第一步：填写基本信息
        time.sleep(2)
        self.driver.js_click('#categoryName')
        time.sleep(2)
        self.driver.click(('css selector', 'input[value="婚晏酒晏"]'))
        time.sleep(2)
        self.driver.click(('css selector', 'input[name="className"][value="10"]'))
        js_str = "document.getElementById('productName').value = '海霸王无底价单'"
        self.driver.js_execute(js_str)
        self.driver.js_execute("document.getElementById('price').value = '63'")
        self.driver.click(('css selector', 'input[name="support"][value="Y"]'))
        self.driver.send_keys(('css selector', 'input[name="description"]'),"等哈复健科")
        self.driver.send_keys(('css selector', 'input[type="file"]'),"C:\\Users\\Public\\Pictures\\Sample Pictures\\1.jpg")
        # self.driver.js_focus_element(('id','#detail'))
        self.driver.send_keys(('name','detail'), "胆红素会发的撒客家话")
        self.driver.click(('css selector', 'input[name="recommend"][value="Y"]'))
        self.driver.click(('id', 'enterButton'))

        #第二步
        time.sleep(2)
        self.driver.send_keys(('id','propertyName'),"套餐A")
        self.driver.js_execute("document.getElementById('price').value='63'")
        self.driver.send_keys(('id','number'),"客户发的撒哈哈")
        self.driver.js_click('[value="保存商品规格"]')
        self.driver.click(('xpath','//button[text()="设置阶段信息"]'))
        self.driver.click(('id',"pay_type_onetime"))
        self.driver.click(('id',"deposit_Y"))
        self.driver.click(('css selector','input[value="保存"]'))
        self.driver.js_focus_element(('id','wrapper'))
        self.driver.click(('id', "complate_button"))
        self.driver.click(('tag name', "input"))

        #提交审核
        self.driver.click(('css selector','#productTable tr.odd'))
        self.driver.click(('xpath','//button[text()="确认操作"]'))
        self.driver.click(('xpath','//button[text()="关闭"]'))





    def tearDown(self):
        self.driver.quit()
        log.info('############################### END ###############################')

    def bussiness_login(self):
        self.driver.open(LoginBussinessPage.base_url)
        self.driver.send_keys(LoginBussinessPage.username_loc,"13391387810")
        self.driver.send_keys(LoginBussinessPage.password_loc,"qaz12340")
        self.driver.click(LoginBussinessPage.submit_loc)

if __name__ == "__main__":
    #unittest.main()是为了在cmd中也可以执行该py文件
    unittest.main()