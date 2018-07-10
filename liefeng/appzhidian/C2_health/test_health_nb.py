#coding:utf-8
#Lih06-12
import logging,unittest,time
from appium import webdriver
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait


class applogin(unittest.TestCase):
    @classmethod
    def setUp(self):
        time.sleep(100)
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
                            filename='D:\\liefeng\\liefeng1\\log\\appzhidian.log',
                            filemode='w')

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

    def is_excit(self,text):
        try:
            me = self.driver.find_element_by_accessibility_id(text)
            print me.text
            return True
        except:
            return False

    def swipeUp(self, t=500, n=1):
        x1 = self.l['width'] * 0.5
        y1 = self.l['height'] * 0.75
        y2 = self.l['height'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def is_search(self, text):
        search = self.driver.find_elements_by_class_name("android.view.View")
        for i in range(len(search)):
            c = search[i].get_attribute("name")
            logging.info(c.strip())

    def link_check(self,text_check):
        self.wait()
        time.sleep(2)
        self.wait()
        time.sleep(2)
        self.is_search(text_check)
        self.driver.get_screenshot_as_file("D:\\liefeng\\liefeng2\\Sreenshots\\health_xy.png")
        time.sleep(1)
        self.driver.find_element_by_class_name("android.widget.Button").click()
        self.wait()
        time.sleep(2)

    def test_health_nb(self):
        try:
            self.log()
            logging.info("Test_Choose_And_Open_Health!")
            data = pd.read_excel("D:\\liefeng\\liefeng2\\log\\app.xls")
            logging.info(self.driver.contexts)
            try:
                self.driver.find_element_by_accessibility_id(u"健康体检").click()
            except:
                # 登录
                username = int(data.iloc[9, 1])
                password = int(data.iloc[9, 2])
                self.login(username, password)
                self.wait()
                time.sleep(15)
                logging.info(u"Login_account____________%s" % username)
                self.wait()
                try:
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_name(u"验证"))
                    logging.info(u"put identify login")
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
                    logging.info("skip put identify and login success")
                    self.wait()
                    time.sleep(2)
                #健康数据
                self.driver.find_element_by_accessibility_id(u"健康体检").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(5)
            self.wait()
            time.sleep(1)
            self.is_search(u"健康数据")


            # 血压 Link
            self.driver.find_element_by_accessibility_id("血压 Link").click()
            text_check = u"血压"
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(5)
            self.is_search(text_check)
            self.driver.get_screenshot_as_file("D:\\liefeng\\liefeng2\\Sreenshots\\health_xy.png")
            time.sleep(1)
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(10)
            self.wait()
            time.sleep(2)
            # 体温 Link
            a=self.driver.find_elements_by_class_name("android.view.View")
            a[15].click()
            text = u" 体温 Link"
            text_check = u"体温"
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(5)
            self.is_search(text_check)
            self.driver.get_screenshot_as_file("D:\\liefeng\\liefeng2\\Sreenshots\\health_tw.png")
            time.sleep(1)
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(10)
            self.wait()
            time.sleep(2)
            # 脂肪
            a = self.driver.find_elements_by_class_name("android.view.View")
            a[16].click()
            text = u" 脂肪 Link"
            text_check = u"脂肪"
            # self.link_check(text, text_check)
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(5)
            self.is_search(text_check)
            self.driver.get_screenshot_as_file("D:\\liefeng\\liefeng2\\Sreenshots\\health_zf.png")
            time.sleep(1)
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(10)
            self.wait()
            time.sleep(2)
            # 体重 Link
            a = self.driver.find_elements_by_class_name("android.view.View")
            a[17].click()
            text = u" 体重 Link"
            text_check = u"体重"
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(5)
            self.is_search(text_check)
            self.driver.get_screenshot_as_file("D:\\liefeng\\liefeng2\\Sreenshots\\health_tz.png")
            time.sleep(1)
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(2)

            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(10)
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
            time.sleep(2)
            self.swipeUp()
            self.wait()
            time.sleep(2)
            self.driver.find_element_by_accessibility_id(u"设置").click()
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
            logging.info("健康检测数据出错，详见截图")
            self.driver.get_screenshot_as_file("D:\\liefeng\\liefeng2\\Sreenshots\\error_healthnumber.png")
            self.driver.close_app()
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
