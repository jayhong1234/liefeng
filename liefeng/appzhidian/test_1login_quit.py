#coding:utf-8
#LiH 2018-4-2
import time
from appium import webdriver
import logging,unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class applogin(unittest.TestCase):
    @classmethod
    def setUp(self):
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

    def login(self,username,psw):
        self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.liefengtech.zhwy:id/edit_phone']").send_keys(username)
        time.sleep(1)
        self.driver.find_element_by_id("com.liefengtech.zhwy:id/edit_pass").send_keys(psw)
        self.driver.find_element_by_name(u"登录").click()
        #空密码

    def is_login(self):
        try:
            identifyNu = self.driver.find_element_by_name(u"验证").text
            print identifyNu
            return True
        except:
            return False

    def log(self):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)  # Log等级总开关
        logfile = 'D:\\liefeng\\liefeng2\\log\\logger.txt'
        fh = logging.FileHandler(logfile, mode='a')
        fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
        ch = logging.StreamHandler()
        ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)



    def test_login(self):
        self.log()
        logging.info("APP_login_quit_test start!")
        #验证是否输入正确密码，跳转
        username="13613132222"
        password=""
        logging.info("put psw empty")
        self.login(username,password)
        self.wait()
        a=self.is_login()
        logging.info(a)
        self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.liefengtech.zhwy:id/edit_phone']").clear()
        #短密码
        self.wait()
        password1 = "###"
        logging.info(u"put psw: %s"%password1)
        self.login(username, password1)
        self.wait()
        logging.info(self.is_login())
        self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.liefengtech.zhwy:id/edit_phone']").clear()
        self.driver.find_element_by_id("com.liefengtech.zhwy:id/edit_pass").clear()
        self.driver.find_element_by_id("com.liefengtech.zhwy:id/edit_pass").clear()
        self.driver.find_element_by_id("com.liefengtech.zhwy:id/edit_pass").clear()
        self.wait()
        #错误密码
        password2 = "1@@456789"
        logging.info( "put psw: %s"%password2)
        self.login(username, password1)
        self.wait()
        logging.info(self.is_login())
        self.driver.find_element_by_xpath(
            "//android.widget.EditText[@resource-id='com.liefengtech.zhwy:id/edit_phone']").clear()
        self.driver.find_element_by_id("com.liefengtech.zhwy:id/edit_pass").clear()
        self.driver.find_element_by_id("com.liefengtech.zhwy:id/edit_pass").clear()
        self.driver.find_element_by_id("com.liefengtech.zhwy:id/edit_pass").clear()
        self.driver.find_element_by_id("com.liefengtech.zhwy:id/edit_pass").clear()
        self.driver.find_element_by_id("com.liefengtech.zhwy:id/edit_pass").clear()
        self.driver.find_element_by_id("com.liefengtech.zhwy:id/edit_pass").clear()
        self.driver.find_element_by_id("com.liefengtech.zhwy:id/edit_pass").clear()
        self.driver.find_element_by_id("com.liefengtech.zhwy:id/edit_pass").clear()
        self.driver.find_element_by_id("com.liefengtech.zhwy:id/edit_pass").clear()

        #正确密码

        username="13577771111"
        password3="123456"
        logging.info("put right psw")
        self.login(username, password3)
        self.wait()
        time.sleep(5)
        self.wait()
        try:
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_name(u"验证"))
            logging.info(u"put empty/error/right identify login")
            logging.info(self.is_login())
            identify = self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.liefengtech.zhwy:id/edit_verifyCode']")

        #输入错误验证码
            logging.info("put error identify")
            identify.send_keys("#$$")
            self.driver.find_element_by_name(u"确定").click()


            logging.info("put empty identify")
            identify.clear()
            identify.send_keys("")
            self.driver.find_element_by_name(u"确定").click()


            #输入获取正确验证码
            logging.info("put right identify")
            self.driver.find_element_by_name(u"获取验证码").click()
            time.sleep(5)
            logging.info(u"获取验证码为___________%s" % identify.text)
            self.driver.find_element_by_name(u"确定").click()
            self.wait()
            time.sleep(5)
            self.wait()
            time.sleep(25)
            logging.info(u"登录成功")

            me=self.driver.find_element_by_name(u"我")
            me.click()
            logging.info(u"open________%s"%me.text)
            self.wait()
            time.sleep(2)
            self.driver.find_element_by_accessibility_id(u"设置").click()
            self.wait()
            time.sleep(2)
            quit=self.driver.find_element_by_name(u"退出")
            logging.info(u"click________%s" % quit.text)
            quit.click()
            self.driver.close_app()
        except:
            logging.info("skip put identify")
            me = self.driver.find_element_by_name(u"我")
            me.click()
            logging.info(u"open________%s" % me.text)
            logging.info(u"登录成功")
            self.wait()
            time.sleep(2)
            self.driver.find_element_by_accessibility_id(u"设置").click()
            self.wait()
            time.sleep(2)
            quit = self.driver.find_element_by_name(u"退出")
            logging.info(u"click________%s" % quit.text)
            quit.click()
            self.driver.close_app()

if __name__ == "__main__":
    unittest.main()
