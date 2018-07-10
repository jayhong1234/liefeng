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
            if c == text:
                logging.info("True")

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

    def test_health_more(self):
        try:
            self.log()
            logging.info("Test_Choose_And_Open_Health!")
            data = pd.read_excel("D:\\liefeng\\liefeng2\\log\\app.xls")
            logging.info(self.driver.contexts)
            # 登录
            try:
                self.driver.find_element_by_accessibility_id(u"健康体检").click()
            except:
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
                # 健康数据
                self.driver.find_element_by_accessibility_id(u"健康体检").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(5)
            self.wait()
            time.sleep(1)


            #更多
            logging.info(u"更多")
            self.driver.find_element_by_accessibility_id(u"更多").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(5)
            self.wait()
            time.sleep(1)
            self.driver.find_element_by_accessibility_id(u"领取健康数据 Link").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(5)
            self.driver.find_element_by_accessibility_id(u"我测量的").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(3)
            self.is_search(u"保存")
            self.driver.find_element_by_accessibility_id(u"取消").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(5)
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(5)

            #医生建议
            self.driver.find_element_by_accessibility_id(u"医生建议 Link").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(5)
            self.is_search(u"医生建议")
            #饮食建议
            # self.driver.find_element_by_name(u"饮食建议").click()
            # self.wait()
            # time.sleep(3)
            # self.wait()
            # time.sleep(1)
            # #聊天记录
            # text=u"我吃完饭再吃"
            # self.driver.find_element_by_name(u"请输入回复内容...").send_keys(text)
            # time.sleep(1)
            # self.driver.find_elements_by_class_name("android.widget.Button")[1].click()
            # self.wait()
            # time.sleep(1)
            # self.is_search(text)
            # self.driver.find_elements_by_class_name("android.widget.Button")[0].click()
            # self.wait()
            # time.sleep(2)
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(6)

            #家人关怀
            self.driver.find_element_by_accessibility_id(u"家人关怀 Link").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(3)
            self.is_search(u"家人关怀 Link")
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(5)

            #我的授权
            self.driver.find_element_by_accessibility_id(u"我的授权 Link").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(3)
            self.is_search(u"我的授权 Link")
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(5)

            #我的设备
            self.driver.find_element_by_accessibility_id(u"我的设备 Link").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(3)
            self.is_search(u"我的设备 Link")
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(5)

            #基本设置
            self.driver.find_element_by_accessibility_id(u"基本设置 Link").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(3)
            #目标心率设置
            self.driver.find_element_by_accessibility_id(u"目标心率设置 Link").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(3)
            self.is_search(u"目标心率设置")
            self.driver.find_element_by_accessibility_id(u"保 存").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(2)
            title=self.driver.find_element_by_id("android:id/alertTitle").text
            message=self.driver.find_element_by_id("android:id/message").text
            logging.info(title)
            logging.info(message)
            self.driver.find_element_by_name(u"确定").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(5)

            #目标步数设置
            self.driver.find_elements_by_class_name("android.view.View")[3].click()
            # self.driver.find_element_by_accessibility_id(u"目标步数设置 Link").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(3)
            self.is_search(u"目标步数设置")
            self.driver.find_element_by_accessibility_id(u"保 存").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(2)
            title = self.driver.find_element_by_id("android:id/alertTitle").text
            message = self.driver.find_element_by_id("android:id/message").text
            logging.info(title)
            logging.info(message)
            self.driver.find_element_by_name(u"确定").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(5)

            #紧急电话设置
            self.driver.find_elements_by_class_name("android.view.View")[4].click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(3)
            self.is_search(u"紧急电话设置")
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(5)

            #个人资料设置
            self.driver.find_element_by_accessibility_id(u"个人资料设置 Link").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(3)
            self.is_search(u"个人资料设置")
            self.driver.find_element_by_accessibility_id(u"保 存").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(2)
            title = self.driver.find_element_by_id("android:id/alertTitle").text
            message = self.driver.find_element_by_id("android:id/message").text
            logging.info(title)
            logging.info(message)
            self.driver.find_element_by_name(u"确定").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(5)

            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(3)
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(5)
            self.wait()
            time.sleep(10)

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
            time.sleep(3)
            self.driver.find_element_by_accessibility_id(u"设置").click()
            self.wait()
            time.sleep(2)
            quit = self.driver.find_element_by_name(u"退出")
            logging.info(u"click________%s" % quit.text)
            quit.click()
            self.driver.close_app()
            self.driver.quit()
        except:
            self.log()
            logging.info("健康检查更多，详见截图")
            self.driver.get_screenshot_as_file("D:\\liefeng\\liefeng2\\Sreenshots\\error_healthmore.png")
            self.driver.close_app()
            self.driver.quit()
if __name__ == "__main__":
    unittest.main()