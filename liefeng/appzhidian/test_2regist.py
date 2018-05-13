#coding:utf-8
#lihong 2018-5-6
import time
from appium import webdriver
import logging,unittest
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class applogin(unittest.TestCase):
    @classmethod
    def setUp(self):
        time.sleep(60)
        desired_caps = {
            'platformName': "Android",
            'deviceName': "127.0.0.1:62001",
            'platformVersion': '4.4',
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
    @classmethod
    def tearDown(self):
        time.sleep(1)
        print  ("end!")
    #打开app
    def wait(self):
        ac = self.driver.current_activity
        print ac

    def is_regist(self):
        try:
            me = self.driver.find_element_by_name(u"我")
            print me.text
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


    def test_regist_quit(self):
        self.log()
        logging.info("APP_regist_right_telst start!")
        data = pd.read_excel('D:\\liefeng\\liefeng1\\log\\app.xls')
        #注册

        a=self.driver.find_element_by_name(u"立即注册")
        time.sleep(3)
        a.click()
        a.click()
        self.wait()
        time.sleep(2)
        regist=self.driver.find_element_by_xpath("//android.widget.TextView[@text='注册']")
        regist_tittle=regist.text
        logging.info(u"into___________%s"%regist_tittle)
        #输入手机
        self.driver.find_element_by_name(u"请输入手机号码").send_keys(data.iloc[18,1])
        time.sleep(2)
        self.driver.find_element_by_name(u"获取验证码").click()
        self.wait()
        time.sleep(5)
        identify = self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.liefengtech.zhwy:id/edit_verifyCode']")
        logging.info(u"get identity number___________%s"%identify.text)
        self.driver.find_element_by_name(u"下一步").click()
        self.wait()
        time.sleep(2)
        logging.info(u"post password___________%s"%data.iloc[18,2])
        self.driver.find_element_by_id("com.liefengtech.zhwy:id/edit_pass").send_keys(data.iloc[18,2])
        self.driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.liefengtech.zhwy:id/img_sub']").click()
        self.wait()
        time.sleep(2)
        self.wait()
        time.sleep(25)

        logging.info(u"after success regist into__________主页")

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
