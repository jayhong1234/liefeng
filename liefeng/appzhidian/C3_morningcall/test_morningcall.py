#coding:utf-8
import logging, unittest, time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from appium.webdriver.common.touch_action import TouchAction


class household(unittest.TestCase):

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
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.wait_activity(".base.ui.MainActivity", 15)
        self.l = self.driver.get_window_size()

    @classmethod
    def tearDown(self):
        time.sleep(1)
        print  ("end!")

    def swipeUp(self, t=500, n=1):
        x1 = self.l['width'] * 0.5
        y1 = self.l['height'] * 0.75
        y2 = self.l['height'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def wait(self):
        wait = self.driver.current_activity
        print wait

    def is_search(self, text):
        search = self.driver.find_elements_by_class_name("android.widget.TextView")
        for i in range(len(search)):
            c= search[i].get_attribute("name")
            logging.info(c.strip())
            if c == text:
                logging.info("True")

 
    def login(self, username, psw):
        self.driver.find_element_by_xpath(
            "//android.widget.EditText[@resource-id='com.liefengtech.zhwy:id/edit_phone']").send_keys(username)
        time.sleep(1)
        self.driver.find_element_by_id("com.liefengtech.zhwy:id/edit_pass").send_keys(psw)
        self.driver.find_element_by_name(u"登录").click()

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

    def column(self,numb,titletext):
         a = self.driver.find_elements_by_class_name("android.view.View")
         a[numb].click()
         self.wait()
         time.sleep(5)
         self.wait()
         time.sleep(3)
         try:
             a = self.driver.find_element_by_accessibility_id(titletext).get_attribute("name")
             logging.info(u"Into_house___________%s" % a)
             self.is_search(titletext)
         except:
             logging.info(u"Into_house_Flase___________%s"%titletext)
         self.driver.find_element_by_class_name("android.widget.Button").click()
         self.wait()
         time.sleep(2)
         self.wait()
         time.sleep(2)

    def test_morningcall(self):
        try:
            self.log()
            data = pd.read_excel("D:\\liefeng\\liefeng2\\log\\app.xls")
            logging.info(self.driver.contexts)
            try:
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
                self.swipeUp()
                self.swipeUp()
                self.wait()
                time.sleep(2)
                self.driver.find_element_by_accessibility_id("MorningCall").click()
            except:
                self.swipeUp()
                self.swipeUp()
                self.wait()
                time.sleep(2)
                self.driver.find_element_by_accessibility_id("MorningCall").click()
            # 打开家居
            self.wait()
            time.sleep(3)
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(2)
            self.driver.find_element_by_id("com.liefengtech.zhwy:id/toolbar_imageview").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(1)
            self.is_search("添加 Morning Call")
            self.driver.find_element_by_name(u"二").click()
            self.driver.find_element_by_name(u"五").click()
            self.driver.find_element_by_name(u"日").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(1)
            self.driver.find_element_by_name(u"请输入主题").send_keys(u"请叫我大哥")

            self.wait()
            time.sleep(2)
            #家居控制
            logging.info(u"家居控制")
            self.driver.find_element_by_name("家居控制").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(3)
            self.is_search(u"家居控制")
            self.driver.find_element_by_class_name("android.widget.ImageButton").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(2)
            #背景音乐
            self.driver.find_element_by_name("背景音乐").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(1)
            logging.info("背景音乐")
            #打印音乐列表
            search = self.driver.find_elements_by_class_name("android.widget.TextView")
            for i in range(len(search)):
                c = search[i].get_attribute("name")
                logging.info(c.strip())
            self.driver.find_element_by_class_name("android.widget.ImageButton").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(2)
            #日程备忘
            self.driver.find_element_by_name("日程备忘").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(3)
            self.is_search(u"日程备忘")
            a=self.driver.find_element_by_id("com.liefengtech.zhwy:id/btn_audioBtn")
            TouchAction(self.driver).long_press(a,duration=3000).perform()
            self.wait()
            time.sleep(3)
            try:
                self.driver.find_element_by_id("com.liefengtech.zhwy:id/tv_voicePlay").click()
                # 听录音时间
                time.sleep(5)
                self.driver.find_element_by_id("com.liefengtech.zhwy:id/tv_voiceReStar").click()
            except:
                self.driver.get_screenshot_as_file("D:\\liefeng\\liefeng2\\Sreenshots\\日程备忘—录音失败bug.png")
                logging.info(u"日程备忘—录音失败，已截图")

            self.wait()
            time.sleep(2)
            self.driver.find_element_by_name(u"切换文字").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(2)
            text1=u"今天没吃饭饿死了，求大哥请吃饭"
            self.driver.find_element_by_name(u"请编辑留言").send_keys(text1)
            time.sleep(1)
            self.driver.find_element_by_name(u"保存").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(3)
            a=self.driver.find_element_by_name(text1).text
            if a==text1:
                logging.info(u"日程备忘保存成功")
            #健康提示
            self.driver.find_element_by_name("健康提示").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(3)
            text2=u"多多保重身体，吃好喝好，不要怕"
            self.driver.find_element_by_id(u"com.liefengtech.zhwy:id/scrollView").send_keys(text2)
            self.is_search(u"健康提示")
            self.driver.find_element_by_name(u"保存").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(3)

            self.driver.find_element_by_id("com.liefengtech.zhwy:id/iv_Weatherforecast").click()
            self.wait()
            time.sleep(2)
            self.driver.find_element_by_id("com.liefengtech.zhwy:id/toolbar_imageview").click()
            self.wait()
            time.sleep(3)
            self.wait()
            time.sleep(3)
            search = self.driver.find_elements_by_class_name("android.widget.TextView")
            for i in range(len(search)):
                c = search[i].get_attribute("name")
                logging.info(c.strip())
            a = self.driver.find_element_by_id("com.liefengtech.zhwy:id/tv_time")
            TouchAction(self.driver).long_press(a,duration=2000).perform()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(2)
            a=self.driver.find_element_by_name(u"删除MorningCall").text
            b=self.driver.find_element_by_name(u"是否删除？").text
            logging.info(a)
            logging.info(b)
            self.driver.find_element_by_name(u"是").click()
            self.wait()
            time.sleep(5)
            self.wait()
            time.sleep(3)
            self.wait()
            time.sleep(2)

            #点击右上角或这里
            text3=u"点击右上角或这里"
            self.driver.find_element_by_name(u"点击右上角或这里").click()
            self.wait()
            time.sleep(5)
            self.wait()
            time.sleep(3)
            self.wait()
            time.sleep(2)
            logging.info("Cilck_———————%s" % text3)
            try:
                a=self.driver.find_element_by_name(u"添加 Morning Call").text
                logging.info("Into_———————%s" % a)
            except:
                logging.info('Into_———————退出')
            try:
                self.driver.find_element_by_class_name("android.widget.ImageButton").click()
                self.wait()
                time.sleep(3)
                self.wait()
                time.sleep(2)
                logging.info("Quit_———————%s" % a)
            except:
                logging.info(u"退出")
                self.driver.find_element_by_class_name("android.widget.ImageButton").click()
                self.wait()
                time.sleep(3)
                self.wait()
                time.sleep(2)
                logging.info("Quit_———————%s" % a)
            self.driver.find_element_by_class_name("android.widget.ImageButton").click()
            self.wait()
            time.sleep(3)
            self.wait()
            logging.info("Quit_———————Morningcall")
            time.sleep(2)
            self.wait()
            time.sleep(6)

            # 退出账号
            me = self.driver.find_element_by_name(u"我")
            me.click()
            logging.info(u"open________%s" % me.text)
            logging.info(u"Quit Community success")
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(3)
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
            logging.info("morningcall出错，详见截图")
            self.driver.get_screenshot_as_file("D:\\liefeng\\liefeng2\\Sreenshots\\error_morning.png")
            self.driver.close_app()
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
