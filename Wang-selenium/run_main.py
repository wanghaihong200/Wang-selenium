# coding:utf-8
import unittest
import os
import HTMLTestReportCN
import HTMLTestRunner_jpg
from case.happy_public.public_smtp import smtp_163
import time

# python2.7要是报编码问题，就加这三行，python3不用加
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# cur_path = os.path.dirname(os.path.realpath(__file__))  #原始脚本__file__所在绝对路径   os.getcwd(),执行脚本所在目录
# case_path = os.path.join(cur_path, "login_all")        # 测试用例的路径
# report_path = os.path.join(cur_path, "report")  # 报告存放路径
case_path = os.path.join(os.getcwd(),"case")
report_path = os.path.join(os.getcwd(),"report")

#verbosity:  0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共100个 失败20 成功80
#           1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.”  每个失败的用例前面有个 “F”
#           2 (详细模式):测试结果会显示每个测试用例的所有相关的信息
if __name__ == "__main__":
    discover = unittest.defaultTestLoader.discover(case_path,"test*.py")
    print(discover)
    fp = report_path+"\\result"+"%s.html"%time.strftime("%Y_%m_%d_%H_%M_%p")
    runner = HTMLTestRunner_jpg.HTMLTestRunner(title="汇幸福测试报告",
                                            description="测试框架版",
                                            stream=open(fp, "wb"),
                                            verbosity=2,
                                            retry=1)

    runner.run(discover)
    smtp_163(fp).send_email()


