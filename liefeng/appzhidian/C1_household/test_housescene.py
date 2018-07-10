#coding:utf-8
import logging,unittest,time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import xlwt,xlrd
from xlutils.copy import copy
from xlwt import Style
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

    def swipeUp(self,t=500, n=1):
        x1 = self.l['width'] * 0.5
        y1 = self.l['height'] * 0.75
        y2 = self.l['height'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def wait(self):
        wait=self.driver.current_activity
        print wait

    def is_search(self, text):
        search = self.driver.find_elements_by_class_name("android.view.View")
        for i in range(len(search)):
            c = search[i].get_attribute("name")
            logging.info(c.strip())
            if c == text:
                logging.info("True")

    def writeExcel(self, row, col, str, styl=Style.default_style):
        rb = xlrd.open_workbook('D:\\liefeng\\liefeng2\\log\\app.xls', formatting_info=True)
        wb = copy(rb)
        ws = wb.get_sheet(0)
        ws.write(row, col, str, styl)
        wb.save('D:\\liefeng\\liefeng2\\log\\app.xls')

    def login(self,username,psw):
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

        console=logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

    def refresh(self):
# 重新进
        logging.info(u"这里有个bug，新建场景，不刷新，所以退出重进,还得多几次")
        self.driver.find_element_by_class_name("android.widget.Button").click()
        self.wait()
        time.sleep(7)
        a = self.driver.find_element_by_accessibility_id(u"列丰科技010101")
        logging.info("into__________________%s" % a.get_attribute("name"))
        # 直接点击父亲
        a.click()
        self.wait()
        time.sleep(3)
        self.wait()
        time.sleep(5)
        a = self.driver.find_element_by_accessibility_id(u"场景")
        logging.info(a.get_attribute("name"))
        a.click()
        self.wait()
        time.sleep(5)
        self.wait()
        time.sleep(5)
#长按
    def long_pass(self):
        c1 = self.driver.find_element_by_accessibility_id(u"每天起床干嘛")
        logging.info(c1.get_attribute("name"))
        TouchAction(self.driver).long_press(c1).wait(4000).perform()

    def test_household_first(self):
        try:
            self.log()
            logging.info("Test_Choose_And_Open_Household_First!")
            data=pd.read_excel("D:\\liefeng\\liefeng2\\log\\app.xls")
            logging.info(self.driver.contexts)
            #登录
            try:
                self.driver.find_element_by_accessibility_id(u"家居").click()
            except:
                username=int(data.iloc[9,1])
                password=int(data.iloc[9,2])
                self.login(username,password)
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
                #打开家居
                self.driver.find_element_by_accessibility_id(u"家居").click()
            self.wait()
            time.sleep(3)
            self.wait()
            logging.info(self.driver.contexts)

            time.sleep(10)
            try:
                a=self.driver.find_element_by_accessibility_id(u"选择家庭")
                logging.info("into__________________%s"%a.get_attribute("name"))
            except:
                logging.info(u"进入家居失败，请检查吧，别想了")
            #选择家庭
            a=self.driver.find_element_by_accessibility_id(u"列丰科技010101")
            logging.info("into__________________%s"%a.get_attribute("name"))
            #直接点击父亲
            a.click()
            self.wait()
            time.sleep(3)
            self.wait()
            time.sleep(5)
            a=self.driver.find_element_by_accessibility_id(u"场景")
            logging.info(a.get_attribute("name"))
            a.click()
            self.wait()
            time.sleep(5)
            self.wait()
            time.sleep(5)
            try:
                self.driver.find_element_by_accessibility_id(u"下一步").click()
                self.wait()
                time.sleep(2)
                self.driver.find_element_by_accessibility_id(u"下一步").click()
                self.wait()
                time.sleep(2)
                self.driver.find_element_by_accessibility_id(u"知道了").click()
                self.wait()
                time.sleep(2)
                a = self.driver.find_element_by_accessibility_id(u"添加场景")
                logging.info(a.get_attribute("name"))
                a.click()
            except:
                a = self.driver.find_element_by_accessibility_id(u"添加场景")
                logging.info(a.get_attribute("name"))
                a.click()

            self.wait()
            time.sleep(5)
            self.wait()
            time.sleep(5)
            a = self.driver.find_element_by_accessibility_id(u"添加场景")
            logging.info("into_________________%s"%a.get_attribute("name"))
            # self.driver.find_element_by_name(u"请输入场景名称").send_keys(u"每天起床干嘛")
            self.driver.find_element_by_class_name("android.widget.EditText").send_keys(u"每天起床干嘛")
            #//android.widget.EditText[@text=\"请输入场景名称\"]
            a=self.driver.find_elements_by_class_name("android.view.View")
            a[5].click()
            # self.driver.tap([(363,438),(609,672)])
            #图片上传
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(1)
            self.driver.find_element_by_id("com.liefengtech.zhwy:id/picture").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(2)
            self.driver.find_element_by_name(u"使用").click()
            # self.driver.find_element_by_id("com.liefengtech.zhwy:id/done_text").cilck()
            self.wait()
            time.sleep(5)
            a[7].click()
            # self.driver.tap([(0,948),(1080,1248)])
            # TouchAction(self.driver).press(self.driver.find_elements_by_class_name("android.view.View")[0]).perform()
            self.wait()
            time.sleep(5)
            a=self.driver.find_element_by_accessibility_id(u"添加场景")
            logging.info(a.get_attribute("name"))
            try:
                self.driver.find_elements_by_class_name("android.view.View")[7].click()
            except:
                self.driver.find_elements_by_class_name("android.view.View")[10].click()
            self.driver.find_element_by_accessibility_id(u"确 定").click()
            self.wait()
            time.sleep(5)
            self.driver.find_element_by_accessibility_id("添加").click()
            self.wait()
            time.sleep(5)
            self.is_search(u"房间")
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(2)
            self.driver.find_element_by_accessibility_id(u"完成").click()
            self.wait()
            time.sleep(5)
            self.wait()
            time.sleep(10)
            #打印提示，确认
            tittle = self.driver.find_element_by_id("android:id/alertTitle")
            massage = self.driver.find_element_by_id("android:id/message")
            tittletext = tittle.text
            massagetext = massage.text
            logging.info("%s" % tittletext)
            logging.info("%s" % massagetext)
            self.driver.find_element_by_id("android:id/button1").click()
            self.wait()
            time.sleep(5)
            tittle = self.driver.find_element_by_id("android:id/title_template")
            massage = self.driver.find_element_by_id("android:id/message")
            tittletext = tittle.text
            massagetext = massage.text
            logging.info("%s" % tittletext)
            logging.info("%s" % massagetext)
            self.driver.find_element_by_id("android:id/button1").click()
            self.wait()
            time.sleep(5)
            #重新进
            self.refresh()
            self.refresh()
            #进入编辑场景
            self.long_pass()
            # c2 = self.driver.find_element_by_xpath("//android.view.View[@content-desc='每天起床干嘛']")
            # logging.info(c2.get_attribute("name"))
            # TouchAction(self.driver).move_to(c2).release()
    #定时
            self.wait()
            time.sleep(2)
            a=self.driver.find_element_by_accessibility_id(u"定时")
            a.click()
            try:
                self.wait()
                time.sleep(2)
                self.driver.find_element_by_accessibility_id(u"开始时间").click()
            except:
                self.long_pass()
            a=self.driver.find_elements_by_class_name("android.view.View")[6]
            a.click()
            self.wait()
            time.sleep(2)
            self.driver.find_element_by_accessibility_id(u"开始时间").click()
            self.wait()
            time.sleep(2)
            a=self.driver.find_element_by_accessibility_id(u"选择时间")
            logging.info(a.get_attribute("name"))
            self.driver.find_element_by_accessibility_id(u"确定").click()
            self.wait()
            time.sleep(2)
            # self.driver.find_elements_by_class_name("android.view.View")[2].click()
            self.driver.find_element_by_accessibility_id(u"请选择重复时间").click()
            self.wait()
            time.sleep(2)
            a=self.driver.find_element_by_accessibility_id(u"重复")
            logging.info(a.get_attribute("name"))
            self.driver.find_element_by_accessibility_id(u"星期一").click()
            self.driver.find_element_by_accessibility_id(u"确 定").click()
            self.wait()
            time.sleep(2)
            self.driver.find_element_by_accessibility_id(u"保 存").click()
            self.wait()
            time.sleep(5)
            tittle = self.driver.find_element_by_id("android:id/title_template")
            massage = self.driver.find_element_by_id("android:id/message")
            tittletext = tittle.text
            massagetext = massage.text
            logging.info("%s" % tittletext)
            logging.info("%s" % massagetext)
            self.driver.find_element_by_id("android:id/button1").click()
            self.wait()
            time.sleep(5)
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(2)
        #编辑
            self.long_pass()
            self.driver.find_element_by_accessibility_id(u"编辑").click()
            self.wait()
            time.sleep(5)
            self.driver.find_element_by_class_name("android.widget.EditText").send_keys("1")
            self.driver.find_element_by_accessibility_id(u"上 传").click()
            self.wait()
            time.sleep(1)
            self.driver.find_element_by_id("com.liefengtech.zhwy:id/picture").click()
            self.wait()
            time.sleep(5)
            self.driver.find_element_by_name(u"使用").click()
            # self.driver.find_element_by_id("com.liefengtech.zhwy:id/done_text").cilck()
            self.wait()
            time.sleep(5)
            self.driver.find_element_by_accessibility_id(u"添加").click()
            self.wait()
            time.sleep(5)
            a = self.driver.find_element_by_accessibility_id(u"添加设备")
            logging.info(a.get_attribute("name"))
            # try:
            #     self.driver.find_elements_by_class_name("android.view.View")[13].click()
            # except:
            #     self.driver.find_elements_by_class_name("android.view.View")[16].click()
            self.driver.find_element_by_accessibility_id(u"确 定").click()
            self.wait()
            time.sleep(5)
            self.driver.find_element_by_accessibility_id(u"完成").click()
            self.wait()
            time.sleep(3)
            tittle = self.driver.find_element_by_id("android:id/title_template")
            massage = self.driver.find_element_by_id("android:id/message")
            tittletext = tittle.text
            massagetext = massage.text
            logging.info("%s" % tittletext)
            logging.info("%s" % massagetext)
            self.driver.find_element_by_id("android:id/button1").click()
            self.wait()
            time.sleep(5)
            self.wait()
            time.sleep(5)
            self.driver.get_screenshot_as_png()
            self.refresh()
            self.wait()
            time.sleep(1)
            self.wait()
            time.sleep(1)
        #删除delete
            c1 = self.driver.find_element_by_accessibility_id(u"1每天起床干嘛")
            logging.info(c1.get_attribute("name"))
            TouchAction(self.driver).long_press(c1).wait(4000).perform()
            self.wait()
            self.driver.find_element_by_accessibility_id(u"删除").click()
            self.wait()
            time.sleep(3)
            self.is_search(u"删除")
            self.driver.find_element_by_accessibility_id(u"确定").click()
            self.wait()
            time.sleep(3)
            tittle = self.driver.find_element_by_id("android:id/title_template")
            massage = self.driver.find_element_by_id("android:id/message")
            tittletext = tittle.text
            massagetext = massage.text
            logging.info("%s" % tittletext)
            logging.info("%s" % massagetext)
            self.driver.find_element_by_id("android:id/button1").click()
            self.wait()
            time.sleep(5)
            self.wait()
            time.sleep(10)


            #退出家居
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(2)
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(2)
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
            quit = self.driver.find_element_by_name(u"退出")
            logging.info(u"click________%s" % quit.text)
            quit.click()
            self.driver.close_app()
            self.driver.quit()
        except:
            self.log()
            logging.info("家居场景出错，详见截图")
            self.driver.get_screenshot_as_file("D:\\liefeng\\liefeng2\\Sreenshots\\error_housescene.png")
            self.driver.close_app()
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()