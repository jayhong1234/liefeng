#coding:utf-8
import logging, unittest, time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import xlwt, xlrd
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

    def test_household_more(self):
        try:
            self.log()
            data = pd.read_excel("D:\\liefeng\\liefeng2\\log\\app.xls")
            logging.info(self.driver.contexts)
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
            # 打开家居
            self.driver.find_element_by_accessibility_id(u"家居").click()
            self.wait()
            time.sleep(3)
            self.wait()
            logging.info(self.driver.contexts)

            time.sleep(10)
            try:
                a = self.driver.find_element_by_accessibility_id(u"选择家庭")
                logging.info("into__________________%s" % a.get_attribute("name"))
            except:
                logging.info(u"进入家居失败，请检查吧，别想了")
            # 选择家庭
            a = self.driver.find_element_by_accessibility_id(u"列丰科技010101")
            logging.info("into__________________%s" % a.get_attribute("name"))
            # 直接点击父亲
            a.click()
            self.wait()
            time.sleep(3)
            self.wait()
            time.sleep(5)
            self.driver.find_element_by_accessibility_id(u"更多").click()
            self.wait()
            time.sleep(5)
            try:
                a=self.driver.find_element_by_accessibility_id(u"更多").get_attribute("name")
                logging.info(u"Into_house___________%s"%a)
            except:
                logging.info(u"Into_house_ 更多__________Flase" )

            #定时
            self.driver.find_element_by_accessibility_id(u"定时任务 Link").click()
            self.wait()
            time.sleep(2)
            try:
                a = self.driver.find_element_by_accessibility_id(u"定时任务").get_attribute("name")
                logging.info(u"Into_house___________%s" % a)
            except:
                logging.info(u"Into_house 定时任务___________Flase")
            self.driver.find_element_by_accessibility_id(u"新 建").click()
            self.wait()
            time.sleep(2)
            try:
                a = self.driver.find_element_by_accessibility_id(u"新增定时").get_attribute("name")
                logging.info(u"Into_house___________%s" % a)
            except:
                logging.info(u"Into_house_新增定时___________Flase")
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(2)
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(2)

            #设备管理 
            a=self.driver.find_elements_by_class_name("android.view.View")
            a[4].click()
            # self.driver.find_element_by_accessibility_id(u"设备管理 Link").click()
            self.wait()
            time.sleep(3)
            self.is_search(u"我的设备")
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(2)
            #中继设备
            a = self.driver.find_elements_by_class_name("android.view.View")
            a[5].click()
            self.wait()
            time.sleep(5)
            try:
                a = self.driver.find_element_by_accessibility_id(u"中继设备").get_attribute("name")
                logging.info(u"Into_house___________%s" % a)
            except:
                logging.info(u"Into_house_中继设备___________Flase")
            self.driver.find_element_by_accessibility_id(u"设为中继").click()
            self.wait()
            time.sleep(2)
            a=self.driver.find_element_by_accessibility_id(u"是否设为中继设备").get_attribute("name")
            logging.info(a)
            self.driver.find_element_by_accessibility_id(u"取 消").click()
            self.wait()
            time.sleep(2)
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(2)
            #联动设置
            self.driver.find_elements_by_class_name("android.view.View")[6].click()
            self.wait()
            time.sleep(5)
            try:
                a = self.driver.find_element_by_accessibility_id(u"联动设置").get_attribute("name")
                logging.info(u"Into_house___________%s" % a)
            except:
                logging.info(u"Into_house_联动设置___________Flase")
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(2)
            #我的家庭
            a = self.driver.find_elements_by_class_name("android.view.View")
            a[7].click()
            self.wait()
            time.sleep(5)
            try:
                a = self.driver.find_element_by_accessibility_id(u"我的家庭").get_attribute("name")
                logging.info(u"Into_house___________%s" % a)
                self.is_search(u"叶婷婷")
            except:
                logging.info(u"Into_house_我的家庭___________Flase")
            self.driver.find_element_by_accessibility_id(u"申请列表").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(2)
            try:
                a = self.driver.find_element_by_accessibility_id(u"申请详情").get_attribute("name")
                logging.info(u"Into_house___________%s" % a)
                self.is_search(u"叶婷婷")
            except:
                logging.info(u"Into_house_申请详情___________Flase")
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(2)
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(2)
            self.wait()
            time.sleep(2)

            # a=self.driver.find_elements_by_class_name("android.view.View")
            # a[4].click()
            # self.driver.find_element_by_accessibility_id(" ").click()
            # self.driver.tap([(982,92),(1038,156)])
            # self.wait()
            # time.sleep(2)
            # self.driver.find_element_by_accessibility_id(u"扫一扫加入").click()
            # try:
            #     a = self.driver.find_element_by_name(u"扫一扫").text
            #     logging.info(u"Into_house___________%s" % a)
            #
            # except:
            #     logging.info(u"Into_house_扫一扫___________Flase")
            # self.driver.find_element_by_class_name("android.widget.Button").click()
            # self.wait()
            # time.sleep(2)
            # a = self.driver.find_elements_by_class_name("android.view.View")
            # a[2].click()
            # self.wait()
            # time.sleep(2)
            # self.driver.find_element_by_accessibility_id(u"申请加入").click()
            # self.driver.swipe(100,100,100,400)
            #选择家庭
            numb=8
            titletext=u"选择家庭"
            self.column(numb,titletext)

            #历史操作
            numb = 9
            titletext = u"历史操作"
            self.column(numb, titletext)

            #设备操作说明
            numb = 10
            titletext = u"设备操作说明"
            self.column(numb, titletext)

            #常见问题
            numb = 11
            titletext = u"常见问题"
            self.column(numb, titletext)

            #退出
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(3)
            self.wait()
            time.sleep(3)
            self.driver.find_element_by_class_name("android.widget.Button").click()
            self.wait()
            time.sleep(5)
            self.wait()
            time.sleep(3)

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
            logging.info("家居更多出错，详见截图")
            self.driver.get_screenshot_as_file("D:\\liefeng\\liefeng2\\Sreenshots\\error_housemore.png")
            self.driver.close_app()
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()