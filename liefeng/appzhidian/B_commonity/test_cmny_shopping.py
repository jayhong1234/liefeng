#coding:utf-8
#LiH 2018-4-2
import time
from appium import webdriver
import logging,unittest
from selenium.webdriver.support.wait import WebDriverWait

class applogin(unittest.TestCase):
    @classmethod
    def setUp(self):
        time.sleep(20)
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
            print me.text
            return True
        except:
            return False

    def is_search(self):
        search = self.driver.find_elements_by_class_name("android.view.View")
        for i in range(len(search)):
            c = search[i].get_attribute("name")
            logging.info(c)

    def swipeUp(self):
        x1 = self.l['width'] * 0.5
        y1 = self.l['height'] * 0.75
        y2 = self.l['height'] * 0.25
        for i in range(1):
            self.driver.swipe(x1, y1, x1, y2, 500)

    def test_cmny_appbar(self):
        self.log()
        logging.info("APP_community_appbar_test start!")
#登录
        username = "13577771111"
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
            logging.info(u"获取验证码为_________________%s" % identify.text)
            self.driver.find_element_by_name(u"确定").click()
            self.wait()
            time.sleep(5)
            self.wait()
            time.sleep(25)
            logging.info("login success")
        except:
            time.sleep(12)
            logging.info("skip put identify and login success")
        self.driver.find_element_by_accessibility_id(u"社区服务").click()
        self.wait()
        time.sleep(15)

        #精品
        logging.info(u"下拉到精品推荐，点击商品选购")
        self.driver.find_element_by_accessibility_id(u"测试商品名称取值-精品").click()
        self.wait()
        time.sleep(12)
        self.is_search()

        #立即支付
        self.driver.find_element_by_accessibility_id(u"立即购买").click()
        self.wait()
        time.sleep(2)
        logging.info(u"立即支付")
        #返回订单，点击支付
        self.driver.find_element_by_accessibility_id(u"立即支付").click()
        self.wait()
        time.sleep(3)
        b=self.driver.find_elements_by_class_name("android.widget.CheckBox")
        b[1].click()

        logging.info(u"选择微信支付，确认支付")
        self.driver.find_element_by_accessibility_id(u"确认支付").click()
        time.sleep(5)

        self.driver.find_element_by_name(u"确定").click()
        self.wait()
        time.sleep(3)
        #退到主页
        self.driver.find_element_by_class_name("android.widget.Button").click()
        self.wait()
        time.sleep(25)
        self.driver.find_element_by_class_name("android.widget.Button").click()
        self.wait()
        time.sleep(2)
        text = self.driver.find_element_by_name(u"您确定退出社区服务吗？").text
        logging.info(text)
        self.driver.find_element_by_id("android:id/button1").click()
        self.wait()
        time.sleep(15)

        # 退出账号
        me = self.driver.find_element_by_name(u"我")
        me.click()
        logging.info(u"open________%s" % me.text)
        logging.info(u"Quit Community success")
        self.wait()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id(u"设置").click()
        self.wait()
        time.sleep(2)
        quit = self.driver.find_element_by_name(u"退出")
        logging.info(u"click________%s" % quit.text)
        quit.click()
        self.driver.close_app()
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()