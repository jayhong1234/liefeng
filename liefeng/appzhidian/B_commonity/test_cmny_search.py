#coding:utf-8
import time
from appium import webdriver
import logging,unittest
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait

class commonuty(unittest.TestCase):

    @classmethod
    def setUp(self):
        time.sleep(120)
        desired_caps = {
            'platformName': "Android",
            'deviceName': "127.0.0.1:62001",
            'platformVersion': '6.0',
            'appPackage': 'com.liefengtech.zhwy',
            'appActivity': 'com.liefengtech.zhwy.ui.LauncherActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset': True,
            'automationName': 'Uiautomator2'
        }
        # "127.0.0.1:62001"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.wait_activity(".base.ui.MainActivity", 15)
        self.l = self.driver.get_window_size()
    @classmethod
    def tearDown(self):
        time.sleep(1)
        print  ("end!")
    #打开app
    def wait(self):
        ac = self.driver.current_activity
        print ac

    def login(self, username, psw):
        self.driver.find_element_by_xpath(
            "//android.widget.EditText[@resource-id='com.liefengtech.zhwy:id/edit_phone']").send_keys(username)
        time.sleep(1)
        self.driver.find_element_by_id("com.liefengtech.zhwy:id/edit_pass").send_keys(psw)
        self.driver.find_element_by_name(u"登录").click()
        # 空密码
    def log(self):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='D:\\liefeng\\liefeng2\\log\\logger.txt',
                            filemode='w')

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

    def is_excit(self,text):
        try:
            me = self.driver.find_element_by_accessibility_id(text)
            logging.info(me.get_attribute("name"))
            return True
        except:
            return False
    def is_search(self,text):
        search = self.driver.find_elements_by_class_name("android.view.View")
        for i in range(len(search)):
            c = search[i].get_attribute("name")
            logging.info(c.strip())
            if c==text:
                logging.info("True")

    def swipeUp(self, t=500, n=1):
        x1 = self.l['width'] * 0.5
        y1 = self.l['height'] * 0.75
        y2 = self.l['height'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)
    def test_cmny_search(self):
        try:
            self.log()
            logging.info("test_CommunityHomePasge_and_Classify")
            try:
                self.driver.find_element_by_accessibility_id(u"社区服务").click()
            except:
                username = "13613132222"
                password3 = "123456"
                logging.info("login account %s" % username)
                self.login(username, password3)
                self.wait()
                time.sleep(5)
                self.wait()
                try:
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_name(u"验证"))
                    logging.info(u"put empty/error/right identify login")
                    identify = self.driver.find_element_by_xpath(
                        "//android.widget.EditText[@resource-id='com.liefengtech.zhwy:id/edit_verifyCode']")

                    # 输入获取正确验证码
                    logging.info("put right identify")
                    self.driver.find_element_by_name(u"获取验证码").click()
                    time.sleep(5)
                    logging.info(u"获取验证码为___________%s" % identify.text)
                    self.driver.find_element_by_name(u"确定").click()
                    self.wait()
                    time.sleep(5)
                    self.wait()
                    time.sleep(25)
                    logging.info("login success")
                except:
                    time.sleep(15)
                    logging.info("skip put identify and login success")

                self.driver.find_element_by_accessibility_id(u"社区服务").click()
            self.wait()
            time.sleep(30)
            text = u"便利店"
            # 判断是否正常打开社区首页
            logging.info("Is_Verify Community Home Page Open normal_____")
            logging.info(self.is_excit(text))
            #点击搜索
            aa=self.driver.find_elements_by_class_name("android.view.View")
            aa[1].click()
            self.wait()
            time.sleep(5)
            #历史搜索
            text=u"历史搜索"
            self.is_excit(text)
            try:
                a=self.driver.find_element_by_accessibility_id(u"苹果")
                text=a.get_attribute("name")
                logging.info("oder search history___________%s"%text)
                a.click()
                self.wait()
                time.sleep(5)
                self.is_search(text)
            except:
                logging.info(u"没有商存在")

            #热门搜索
            aa = self.driver.find_elements_by_class_name("android.view.View")
            aa[1].click()
            self.wait()
            time.sleep(25)
            aa = self.driver.find_elements_by_class_name("android.view.View")
            aa[1].click()
            text = u"热门搜索"
            self.is_excit(text)

            try:
                a = self.driver.find_element_by_accessibility_id(u"白萝卜")
                text = a.get_attribute("name")
                logging.info("oder search history___________%s" % text)
                a.click()
                self.wait()
                time.sleep(5)
                self.is_search(text)
            except:
                logging.info(u"没有商存在")


            # 输入搜索
            aa = self.driver.find_elements_by_class_name("android.view.View")
            aa[1].click()
            self.wait()
            time.sleep(15)
            self.wait()
            time.sleep(5)
            self.wait()
            time.sleep(5)
            aa = self.driver.find_elements_by_class_name("android.view.View")
            aa[1].click()
            text=u"索尼"
            logging.info(u"输入搜索")
            self.driver.find_element_by_class_name("android.widget.EditText").send_keys(text)
            self.driver.find_element_by_accessibility_id(u"搜索").click()
            self.wait()
            time.sleep(5)
            self.is_search(text)

            aa = self.driver.find_elements_by_class_name("android.view.View")
            aa[1].click()
            self.wait()
            time.sleep(5)
            self.wait()
            time.sleep(10)
            self.wait()
            time.sleep(10)
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(2)
            try:
                text = self.driver.find_element_by_name(u"您确定退出智联商城吗？").text
            except:
                text = self.driver.find_element_by_name(u"您确定退出社区服务吗？").text
            logging.info(text)
            self.driver.find_element_by_id("android:id/button1").click()
            self.wait()
            time.sleep(5)
            self.wait()
            time.sleep(5)
            self.wait()
            time.sleep(5)

            # 退出账号
            me = self.driver.find_element_by_name(u"我")
            me.click()
            logging.info(u"open________%s" % me.text)
            logging.info(u"Quit Community success")
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(5)
            self.swipeUp()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(2)
            quit = self.driver.find_element_by_name(u"退出")
            logging.info(u"click________%s" % quit.text)
            quit.click()
            self.driver.close_app()
            self.driver.quit()
        except:
            self.log()
            logging.info("商城搜索出错")
            self.driver.get_screenshot_as_file("D:\\liefeng\\liefeng2\\Sreenshots\\error_cmny_search.png")
            self.driver.close_app()
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()