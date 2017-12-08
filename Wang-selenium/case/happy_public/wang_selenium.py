#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from case.happy_public.wang_logging import Log
from selenium.webdriver.common.keys import Keys
import time

log = Log()
success = "SUCCESS   "
fail = "FAIL   "
screen_file = "D:\\test\\happyHiiso3\\file\\"

def Browser(browser='ff', remoteAddress=None):
    t1 = time.time()
    dc = {'platform': 'ANY', 'browserName': 'chrome', 'version': '', 'javascriptEnabled': True}
    dr = None
    if remoteAddress is None:
        if browser == "firefox" or browser == "ff":
            dr = webdriver.Firefox()
        elif browser == "chrome" or browser == "Chrome":
            dr = webdriver.Chrome()
        elif browser == "internet explorer" or browser == "ie":
            dr = webdriver.Ie()
        elif browser == "opera":
            dr = webdriver.Opera()
        elif browser == "phantomjs":
            dr = webdriver.PhantomJS()
        elif browser == "edge":
            dr = webdriver.Edge()
    else:
        if browser == "RChrome":
            dr = webdriver.Remote(command_executor='http://' + remoteAddress + '/wd/hub',
                                  desired_capabilities=dc)
        elif browser == "RIE":
            dc['browserName'] = 'internet explorer'
            dr = webdriver.Remote(command_executor='http://' + remoteAddress + '/wd/hub',
                                  desired_capabilities=dc)
        elif browser == "RFirefox":
            dc['browserName'] = 'firefox'
            dc['marionette'] = False
            dr = webdriver.Remote(command_executor='http://' + remoteAddress + '/wd/hub',
                                  desired_capabilities=dc)
    try:
        driver = dr
        log.info("{0} Start a new browser: {1}, Spend {2} seconds".format(success, browser, time.time() - t1))
        return driver
    except Exception:
        raise NameError("Not found {0} browser,You can enter 'ie','ff',"
                        "'chrome','RChrome','RIe' or 'RFirefox'.".format(browser))


class Wang(object):
    #基于原生的selenium 框架做了二次封装
    # def __init__(self, browser='ff', remoteAddress=None):
        # """
        # remote consle：
        # dr = PySelenium('RChrome','127.0.0.1:8080')
        # """
        # t1 = time.time()
        # dc = {'platform': 'ANY', 'browserName': 'chrome', 'version': '', 'javascriptEnabled': True}
        # dr = None
        # if remoteAddress is None:
        #     if browser == "firefox" or browser == "ff":
        #         dr = webdriver.Firefox()
        #     elif browser == "chrome" or browser == "Chrome":
        #         dr = webdriver.Chrome()
        #     elif browser == "internet explorer" or browser == "ie":
        #         dr = webdriver.Ie()
        #     elif browser == "opera":
        #         dr = webdriver.Opera()
        #     elif browser == "phantomjs":
        #         dr = webdriver.PhantomJS()
        #     elif browser == "edge":
        #         dr = webdriver.Edge()
        # else:
        #     if browser == "RChrome":
        #         dr = webdriver.Remote(command_executor='http://' + remoteAddress + '/wd/hub',
        #                               desired_capabilities=dc)
        #     elif browser == "RIE":
        #         dc['browserName'] = 'internet explorer'
        #         dr = webdriver.Remote(command_executor='http://' + remoteAddress + '/wd/hub',
        #                               desired_capabilities=dc)
        #     elif browser == "RFirefox":
        #         dc['browserName'] = 'firefox'
        #         dc['marionette'] = False
        #         dr = webdriver.Remote(command_executor='http://' + remoteAddress + '/wd/hub',
        #                               desired_capabilities=dc)
        # try:
        #     self.driver = dr
        #     self.my_print("{0} Start a new browser: {1}, Spend {2} seconds".format(success,browser,time.time()-t1))
        # except Exception:
        #     raise NameError("Not found {0} browser,You can enter 'ie','ff',"
        #                     "'chrome','RChrome','RIe' or 'RFirefox'.".format( browser))
    def __init__(self, driver):
        self.driver = driver

    def my_print(self,msg):
        log.info(msg)

    def open(self,url,t='',timeout=10):
        '''
        使用get打开url后，最大化窗口，判断title是否符合预期
        Usage:
            driver = Wang()
            driver.open(url,t='')

        '''
        t1 = time.time()
        try:
            self.driver.get(url)
            self.driver.maximize_window()
            self.my_print("{0} Navigated to {1}, Spend {2} seconds".format(success, url, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to load {1}, Spend {2} seconds".format(fail, url, time.time() - t1))
            raise

    def max_window(self):
        '''
        Set browser window maximized.

        Usage:
        driver.max_window()
        '''
        t1 = time.time()
        self.driver.maximize_window()
        self.my_print("{0} Set browser window maximized, Spend {1} seconds".format(success, time.time() - t1))

    def set_window(self, wide, high):
        '''
        Set browser window wide and high.

        Usage:
        driver.set_window(wide,high)
        '''
        t1 = time.time()
        self.driver.set_window_size(wide, high)
        self.my_print("{0} Set browser window wide: {1},high: {2}, Spend {3} seconds".format(
            success,wide, high,time.time() - t1))

    def find_element(self,locator,timeout=10):
        '''
        定位元素，参数locator是元祖类型
        Usage:
            locator = ("id","xxx")
            driver.find_element(locator)

            by_id= "id"
            by_xpath = "xpath"
            by_link_text = "link text"
            by_partial_text = "partial link text"
            by_name = "name"
            by_tag_name = "tag name"
            by_class_name = "class name"
            by_css_selector = "css selector"

        '''
        try:
            element = WebDriverWait(self.driver,timeout,1).until(EC.presence_of_element_located(locator))
            return element
        except Exception:
            nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
            self.driver.get_screenshot_as_file(screen_file+"%s.jpg"%nowTime)

    def find_elements(self,locator,timeout=10):
        #定位一组元素
        try:
            elements = WebDriverWait(self.driver,timeout,1).until(EC.presence_of_all_elements_located(locator))
            return elements
        except Exception:
            nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
            self.driver.get_screenshot_as_file(screen_file+"%s.jpg"%nowTime)

    def send_keys(self,locator,text):
        '''
        Operation input box.
        Usage:
            locator = ("id", "xxx")
            driver.send_keys(locator,text)
        '''
        # el = self.find_element(locator)
        # el.send_keys(text)
        t1 = time.time()
        try:
            el = self.find_element(locator)
            el.send_keys(text)
            self.my_print("{0} Typed element: <{1}> content: {2}, Spend {3} seconds".format(success,
                                                                                            locator, text,
                                                                                            time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to type element: <{1}> content: {2}, Spend {3} seconds".format(fail,
                                                                                                     locator, text,
                                                                                                     time.time() - t1))
            raise

    def clear_send_keys(self, locator, text):
        """
        Clear and input element.

        Usage:
        driver.clear_type(("id", "kw"),"selenium")
        """
        t1 = time.time()
        try:
            el = self.find_element(locator)
            el.clear()
            el.send_keys(text)
            self.my_print("{0} Clear and type element: <{1}> content: {2}, Spend {3} seconds".format(success,
                locator, text,time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to clear and type element: <{1}> content: {2}, Spend {3} seconds".format(fail,
                locator, text,time.time() - t1))
            raise

    def send_keys_and_enter(self, locator, text, secs=0.5):
        """
        Operation input box. 1、input message,sleep 0.5s;2、input ENTER.

        Usage:
        driver.type_css_keys(('id','kw'),'beck')
        """
        t1 = time.time()
        try:
            ele = self.find_element(locator)
            ele.send_keys(text)
            time.sleep(secs)
            ele.send_keys(Keys.ENTER)
            self.my_print("{0} Element <{1}> type content: {2},and sleep {3} seconds,input ENTER key, Spend {4} seconds".format(
                success,locator,text,secs,time.time() - t1))
        except Exception:
            self.my_print("{0} Unable element <{1}> type content: {2},and sleep {3} seconds,input ENTER key, Spend {4} seconds".
                format(fail, locator, text, secs, time.time() - t1))
            raise

    def click(self,locator):
        '''
        点击操作
        Usage:
            locator("id","xxx")
            driver.click(locator)
        '''
        t1 = time.time()
        try:
            el = self.find_element(locator)
            el.click()
            self.my_print("{0} Clicked element: <{1}>, Spend {2} seconds".format(success, locator, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to click element: <{1}>, Spend {2} seconds".format(fail, locator, time.time() - t1))
            raise

    def right_click(self,locator):
        '''
               Right click element.
               鼠标右击
               Usage:
               driver.right_click(("id","kw"))
        '''
        t1 = time.time()
        try:
            el = self.find_element(locator)
            ActionChains(self.driver).context_click(el).perform()
            self.my_print("{0} Right click element: <{1}>, Spend {2} seconds".format(success, locator, time.time() - t1))
        except Exception:
            self.my_print(
                "{0} Unable to right click element: <{1}>, Spend {2} seconds".format(fail, locator, time.time() - t1))
            raise

    def double_click(self, locator):
        '''
        Double click element.

        Usage:
        driver.double_click(("id","kw"))
        '''
        t1 = time.time()
        try:
            el = self.find_element(locator)
            ActionChains(self.driver).double_click(el).perform()
            self.my_print("{0} Double click element: <{1}>, Spend {2} seconds".format(success, locator, time.time() - t1))
        except Exception:
            self.my_print(
                "{0} Unable to double click element: <{1}>, Spend {2} seconds".format(fail, locator, time.time() - t1))
            raise

    def drag_and_drop(self, locator, target_locator):
        '''
        Drags an element a certain distance and then drops it.
        鼠标拖动
        Usage:
        driver.drag_and_drop(("id","kw"),("id2","kw2"))
        '''
        t1 = time.time()
        try:
            element = self.find_element(locator)
            target = self.find_element(target_locator)
            ActionChains(self.driver).drag_and_drop(element, target).perform()
            self.my_print("{0} Drag and drop element: <{1}> to element: <{2}>, Spend {3} seconds".format(success,
                                                                                                         locator, target_locator,
                                                                                                         time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to drag and drop element: <{1}> to element: <{2}>, Spend {3} seconds".format(fail,
                                                                                                                   locator,
                                                                                                                   target_locator,
                                                                                                                   time.time() - t1))
            raise

    def submit(self, locator):
        '''
        Submit the specified form.

        Usage:
        driver.submit(("id","kw"))
        '''
        t1 = time.time()
        try:
            el = self.find_element(locator)
            el.submit()
            self.my_print(
                "{0} Submit form args element: <{1}>, Spend {2} seconds".format(success, locator, time.time() - t1))
        except Exception:
            self.my_print(
                "{0} Unable to submit form args element: <{1}>, Spend {2} seconds".format(fail, locator, time.time() - t1))
            raise

    def F5(self):
        '''
        Refresh the current page.

        Usage:
        driver.F5()
        '''
        t1 = time
        self.driver.refresh()
        self.my_print("{0} Refresh the current page, Spend {1} seconds".format(success, time.time() - t1))

    def is_element_exist(self, locator):
        """
        judge element is exist,The return result is true or false.

        Usage:
        driver.element_exist(("id","kw"))
        """
        t1 = time.time()
        try:
            self.driver.find_element(locator)
            self.my_print("{0} Element: <{1}> is exist, Spend {2} seconds".format(success,locator, time.time() - t1))
            return True
        except TimeoutException:
            self.my_print("{0} Element: <{1}> is not exist, Spend {2} seconds".format(fail, locator, time.time() - t1))
            return False

    def is_text_in_element(self,locator,text,timeout=10):
        '''
        判断文本是否在元素里，返回判断结果布尔值
        usage:
            locator=(id", "xxx")
            text = ""
            result = driver.is_text_in_element(locator,text)
        '''
        try:
            result = WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element(locator,text))
        except TimeoutException:
            print("元素没定位到："+str(locator))
            nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
            self.driver.get_screenshot_as_file(screen_file + "%s.jpg" % nowTime)
            return False
        else:
            return result

    def is_value_in_element(self,locator,value,timeout=10):
        '''
        判断value值是否在元素里，返回判断结果布尔值
        usage:
            locator=(id", "xxx")
            value =
            result = driver.is_value_in_element(locator,text)
        '''
        try:
            result = WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element_value(locator,value))
        except TimeoutException:
            print("元素没定位到："+str(locator))
            nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
            self.driver.get_screenshot_as_file(screen_file + "%s.jpg" % nowTime)
            return False
        else:
            return result

    def is_title(self,title,timeout=10):
        # 判断title是否等于driver.title
        result = WebDriverWait(self.driver,timeout,1).until(EC.title_is(title))
        return result

    def is_title_contains(self,str,timeout=10):
        # 判断title包含于driver.title
        result = WebDriverWait(self.driver,timeout,1).until(EC.title_contains(str))
        return result

    def is_selected(self,locator,timeout=10):
        #判断元素是否被选中，返回布尔值
        result = WebDriverWait(self.driver,timeout,1).until(EC.element_located_to_be_selected(locator))
        return result

    def is_selected_be(self,locator,selected=True,timeout=10):
        #判断元素的状态，selected的期望值：True/False, 返回布尔值
        result = WebDriverWait(self.driver,timeout,1).until(EC.element_located_selection_state_to_be(locator,selected))
        return result

    def is_alert_present(self,timeout=10):
        #判断页面是否有alert, 有就返回alert, 没有就返回False
        result = WebDriverWait(self.driver,timeout,1).until(EC.alert_is_present())
        return result

    def is_visibility(self, locator, timeout=10):
        '''元素可见返回本身，不可见返回Fasle'''
        result = WebDriverWait(self.driver, timeout,1).until(EC.visibility_of_element_located(locator))
        return result

    def is_invisibility(self, locator, timeout=10):
        '''元素可见返回本身，不可见返回True，没找到元素也返回True'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.invisibility_of_element_located(locator))
        return result

    def is_clickable(self, locator, timeout=10):
        '''元素可以点击is_enabled返回本身，不可点击返回Fasle'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_to_be_clickable(locator))
        return result

    def is_located(self, locator, timeout=10):
        '''判断元素有没被定位到（并不意味着可见），定位到返回element,没定位到返回False'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(locator))
        return result

    def move_to_element(self,locator):
        #鼠标悬停操作
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def back(self):
        #浏览器页面回退
        self.driver.back()

    def forward(self):
        #浏览器前进
        self.driver.forward()

    def close(self):
        """
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.

        Usage:
        driver.close()
        """
        t1 = time.time()
        self.driver.close()
        self.my_print("{0} Closed current window, Spend {1} seconds".format(success, time.time() - t1))

    def quit(self):
        """
        Quit the driver and close all the windows.

        Usage:
        driver.quit()
        """
        t1 = time.time()
        self.driver.quit()
        self.my_print("{0} Closed all window and quit the driver, Spend {1} seconds".format(success, time.time() - t1))

    def get_title(self):
        #获取driver.title
        t1 = time.time()
        title = self.driver.title
        self.my_print("{0} Get current window title, Spend {1} seconds".format(success, time.time() - t1))
        return title

    def get_text(self,locator):
        """
            Get element text information.

            Usage:
            driver.get_text(("id","kw"))
        """
        t1 = time.time()
        try:
            element = self.find_element(locator)
            text = element.text
            self.my_print(
                "{0} Get element text element: <{1}>, Spend {2} seconds".format(success, locator, time.time() - t1))
            return text
        except Exception:
            self.my_print(
                "{0} Unable to get element text element: <{1}>, Spend {2} seconds".format(fail, locator, time.time() - t1))
            raise

    def get_url(self):
        '''
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        '''
        t1 = time.time()
        url = self.driver.current_url
        self.my_print("{0} Get current window url, Spend {1} seconds".format(success, time.time() - t1))
        return url

    def wait(self, secs):
        """
        Implicitly wait.All elements on the page.

        Usage:
        driver.wait(10)
        """
        t1 = time.time()
        self.driver.implicitly_wait(secs)
        self.my_print("{0} Set wait all element display in {1} seconds, Spend {2} seconds".format(success,
            secs,time.time() - t1))

    def get_screenshot(self, file_path):
        '''
        Get the current window screenshot.

        Usage:
        driver.get_screenshot('/Screenshots/foo.jpg')
        driver.get_screenshot('/Screenshots/foo.png')
        '''
        t1 = time.time()
        try:
            self.driver.get_screenshot_as_file(file_path)
            self.my_print("{0} Get the current window screenshot,path: {1}, Spend {2} seconds".format(success,
                                                                                                      file_path,
                                                                                                      time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to get the current window screenshot,path: {1}, Spend {2} seconds".format(fail,
                                                                                                                file_path,
                                                                                                                time.time() - t1))
            raise

    # def get_screenshot_as_base64(self):
    #     self.driver.get_screenshot_as_base64()

    def get_attribute(self, locator, name):
        '''获取属性'''
        t1 = time.time()
        try:
            el = self.find_element(locator)
            attribute = el.get_attribute(name)
            self.my_print("{0} Get attribute element: <{1}>,attribute: {2}, Spend {3} seconds".format(success,
                                                                                                      locator, attribute,
                                                                                                      time.time() - t1))
            return attribute
        except Exception:
            self.my_print("{0} Unable to get attribute element: <{1}>,attribute: {2}, Spend {3} seconds".format(fail,
                                                                                                                locator,
                                                                                                                attribute,
                                                                                                                time.time() - t1))
            raise

    def accept_alert(self):
        '''
        Accept warning box.

        Usage:
        driver.accept_alert()
        '''
        t1 = time.time()
        self.driver.switch_to.alert.accept()
        self.my_print("{0} Accept warning box, Spend {1} seconds".format(success, time.time() - t1))

    def dismiss_alert(self):
        '''
        Dismisses the alert available.

        Usage:
        driver.dismiss_alert()
        '''
        t1 = time.time()
        self.driver.switch_to.alert.dismiss()
        self.my_print("{0} Dismisses the alert available, Spend {1} seconds".format(success, time.time() - t1))

    def switch_to_frame(self, locator):
        '''
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame(("id","kw"))
        '''
        t1 = time.time()
        try:
            iframe_el = self.find_element(locator)
            self.driver.switch_to.frame(iframe_el)
            self.my_print(
                "{0} Switch to frame element: <{1}>, Spend {2} seconds".format(success, locator, time.time() - t1))
        except Exception:
            self.my_print(
                "{0} Unable switch to frame element: <{1}>, Spend {2} seconds".format(fail, locator, time.time() - t1))
            raise

    def switch_to_frame_out(self):
        '''
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        '''
        t1 = time.time()
        self.driver.switch_to.default_content()
        self.my_print("{0} Switch to frame out, Spend {1} seconds".format(success, time.time() - t1))


    def open_new_window(self, locator):
        '''
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.open_new_window()
        '''
        t1 = time.time()
        try:
            original_windows = self.driver.current_window_handle
            el = self.find_element(locator)
            el.click()
            all_handles = self.driver.window_handles
            for handle in all_handles:
                if handle != original_windows:
                    self.driver.switch_to.window(handle)
            self.my_print("{0} Click element: <{1}> open a new window and swich into, Spend {2} seconds".format(success,
                                                                                                                locator,
                                                                                                                time.time() - t1))
        except Exception:
            self.my_print("{0} Click element: <{1}> open a new window and swich into, Spend {2} seconds".format(fail,
                                                                                                                locator,
                                                                                                                time.time() - t1))
            raise

    def into_new_window(self):
        """
        Into the new window.

        Usage:
        dirver.into_new_window()
        """
        t1 = time.time()
        try:
            all_handle = self.driver.window_handles
            flag = 0
            while len(all_handle) < 2:
                time.sleep(1)
                all_handle = self.driver.window_handles
                flag += 1
                if flag == 5:
                    break
            self.driver.switch_to.window(all_handle[-1])
            self.my_print("{0} Switch to the new window,new window's url: {1}, Spend {2} seconds".format(success,
                self.driver.current_url,time.time() - t1))
        except Exception:
            self.my_print("{0} Unable switch to the new window, Spend {1} seconds".format(fail, time.time() - t1))
            raise

    def js_execute(self, js):
        '''执行js'''
        t1 = time.time()
        try:
            self.driver.execute_script(js)
            self.my_print(
                "{0} Execute javascript scripts: {1}, Spend {2} seconds".format(success, js, time.time() - t1))
        except Exception:
            self.my_print("{0} Unable to execute javascript scripts: {1}, Spend {2} seconds".format(fail,
                                                                                                    js,
                                                                                                    time.time() - t1))
            raise

    def js_focus_element(self, locator):
        '''聚焦元素'''
        target = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        '''滚动到底部'''
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def js_click(self, css):
        """
        Input a css selecter,use javascript click element.
        Usage:
        driver.js_click('#buttonid')
        """
        t1 = time.time()
        js_str = "$('{0}').click()".format(css)
        try:
            self.driver.execute_script(js_str)
            self.my_print("{0} Use javascript click element: {1}, Spend {2} seconds".format(success,js_str,time.time()-t1))
        except Exception:
            self.my_print("{0} Unable to use javascript click element: {1}, Spend {2} seconds".format(fail,
                js_str, time.time() - t1))
            raise

    # def js_input_value(self, css, str):
    #     """
    #     Input a css selecter,str,use javascript to set input.value.
    #
    #     Usage:
    #     driver.js_input_value('#buttonid',str)
    #     """
    #     t1 = time.time()
    #     js_str = "document.getElementById('{0}').value='{2}')".format(css,str)
    #     try:
    #         self.driver.execute_script(js_str)
    #         self.my_print("{0} Use javascript set input.value : {1}, Spend {2} seconds".format(success,js_str,time.time()-t1))
    #     except Exception:
    #         self.my_print("{0} Unable to use javascript set input.value: {1}, Spend {2} seconds".format(fail,
    #             js_str, time.time() - t1))
    #         raise

    def select_by_index(self, locator, index):
        '''通过索引,index是索引第几个，从0开始'''
        element = self.find_element(locator)
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        '''通过value属性'''
        element = self.find_element(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        '''通过文本值定位'''
        element = self.find_element(locator)
        Select(element).select_by_value(text)

if __name__ == '__main__':
    # if下面的代码都是测试调试的代码，自测内容
    # driver = browser()
    # 返回类的实例：打开浏览器
    driver_n = Wang(Browser())
    # 返回类的实例：打开浏览器
    driver_n.open("http://www.baidu.com") # 打开url，顺便判断打开的页面对不对
    #获取页面title
    input_loc = ("id", "kw")
    print(driver_n.get_title())
    #输入yoyo
    el = driver_n.find_element(input_loc)
    driver_n.send_keys(input_loc, "yoyo")
    time.sleep(2)
    #清空搜索栏，重新输入“美女图片”，点击搜索
    driver_n.clear_send_keys(input_loc,"美女图片")
    driver_n.click(("id","su"))
    # print (driver_n.is_text_in_element(("name", "tj_trmap"), "地图"))
    #鼠标悬停在设置按钮上
    set_loc = ("link text","设置")
    driver_n.move_to_element(set_loc)





