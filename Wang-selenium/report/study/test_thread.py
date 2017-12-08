#conding:utf-8
from threading import Thread
from case.happy_public.wang_selenium import browser
from case.happy_public.wang_selenium import Wang
from time import sleep
import sys

def test_baidu_search(driver, url):
    baidu_driver = Wang(browser(driver))
    baidu_driver.open(url)
    baidu_driver.send_keys(("id","kw"),"海万")
    sleep(3)
    baidu_driver.click(("id","su"))
    sleep(3)
    baidu_driver.quit()

if __name__ == "__main__":
    #浏览器和首页url
    data = {
        # 'ie':"http://www.baidu.com",
        'firefox':"http://www.baidu.com",
        'chrome':"http://www.baidu.com"
    }

    #构建线程
    threads = []
    for b,url in data.items():
        t = Thread(target=test_baidu_search,args = (b,url))
        threads.append(t)

    #启动所有线程
    for thr in threads:
        thr.start()

