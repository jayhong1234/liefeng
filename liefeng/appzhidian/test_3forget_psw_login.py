#coding:utf-8
#LiH 2018-4-2
import time
from appium import webdriver
import logging,unittest
import pandas as pd

class applogin(unittest.TestCase):
    @classmethod
    def setUp(self):
        time.sleep(60)
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
        time.sleep(1)
        self.driver.find_element_by_name(u"登录").click()

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



    def test_forgetpsw(self):
        self.log()
        logging.info("APP_forget_password_modify_login start!")
        data = pd.read_excel('D:\\liefeng\\liefeng1\\log\\app.xls')
        self.driver.find_element_by_name(u"找回密码").click()
        self.wait()
        time.sleep(2)
        username = "13374892514"
        self.driver.find_element_by_name(u"请输入手机号码").send_keys(username)
        time.sleep(2)
        self.driver.find_element_by_name(u"获取验证码").click()
        self.wait()
        time.sleep(5)
        identify = self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.liefengtech.zhwy:id/edit_verifyCode']")
        logging.info("get_identity_number___________%s" % identify.text)
        self.driver.find_element_by_name(u"下一步").click()
        self.wait()
        time.sleep(2)
        password="123456798"
        logging.info("post_modify_password___________%s"%password )
        self.driver.find_element_by_id("com.liefengtech.zhwy:id/edit_pass").send_keys(password)
        self.driver.find_element_by_xpath(
            "//android.widget.Button[@resource-id='com.liefengtech.zhwy:id/img_sub']").click()
        self.wait()
        time.sleep(2)
        self.wait()
        time.sleep(10)

        self.login(username,password)
        self.wait()
        time.sleep(2)
        self.wait()
        time.sleep(25)
        logging.info(u"登录成功")

        me = self.driver.find_element_by_name(u"我")
        me.click()
        logging.info(u"open________%s" % me.text)
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