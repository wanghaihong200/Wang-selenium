#coding:utf-8
import unittest
from case.happy_public.wang_selenium import Browser
from case.happy_public.wang_selenium import Wang
from ddt import ddt,data,unpack
from case.happy_public.wang_logging import Log
from case.happy_public.public_excel import getDdtExcel
from time import sleep

log = Log()

@ddt
class developTest(unittest.TestCase):
    def setUp(self):
        self.driver = Wang(Browser())
        self.driver.open("http://localhost:8085/pos/login.html")

    @data(*getDdtExcel())
    @unpack
    def testLogin(self,sendValue1,sendValue2):
        #输入账号
        self.driver.send_keys(("name","username"),sendValue1)
        log.info("-----输入账号-----")
        #输入密码
        self.driver.send_keys(("name","password"),sendValue2)
        log.info("-----输入密码-----")
        #点击登录按钮
        self.driver.click(("tag name","button"))
        log.info("-----点击登录-----")
        sleep(2)
        #获取到返回的错误信息


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
