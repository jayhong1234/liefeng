#coding:utf-8
import logging,unittest,time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import xlwt,xlrd
from xlutils.copy import copy
from xlwt import Style
class household(unittest.TestCase):
    time.sleep(60)
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

    def house(self):
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
        logging.info(self.driver.contexts)
        # self.swipeUp(t=500, n=4)
        self.wait()
        time.sleep(3)
        # 打印设备列表
        text = u"空调"
        self.is_search(text)

        # 点击设备
        text1 = u"电灯"
        # data.iloc[10, 1]=111
        self.driver.find_element_by_accessibility_id(text1).click()
        self.wait()
        time.sleep(2)
        logging.info(self.driver.contexts)

        # 验证输入输出
        logging.info(u"Test_Input_EquipmentName_____!!!!这里有需求bug，名称输入空的，特殊符号，可怕")
        # 清除与输入
        logging.info("clear and input")
        a1 = self.driver.find_element_by_class_name("android.widget.EditText")
        a2 = a1.get_attribute("name")
        logging.info("Change________________%s" % a2)
        # strtext1=str(text1)
        # for b in range(len(strtext1)):
        self.driver.find_element_by_class_name("android.widget.EditText").clear()
        time.sleep(1)
        # a1.clear()
        # time.sleep(1)
        # a1.clear()
        # time.sleep(1)
        # a1.send_keys("")
        # a3=a1.get_attribute("name")
        # logging.info(a3)
        # if a2 !=a3:
        logging.info("清除功能正常")
        # 更新Excel，设备名字
        # text_apdate= str(int(text1) + 1)
        # style = xlwt.easyxf('font:height 180, color-index black, bold on;align: wrap on, vert centre, horiz center')
        # self.writeExcel(11, 2, text_apdate, style)
        # a1.send_keys(text1)
        # 提交
        self.wait()
        time.sleep(3)
        logging.info(self.driver.contexts)
        a = self.driver.find_element_by_accessibility_id(u"提交")
        logging.info(a.get_attribute("name"))
        a.click()
        self.wait()
        time.sleep(3)
        self.driver.find_element_by_id("android:id/button1").click()
        self.wait()
        time.sleep(2)
        text2 = self.driver.find_element_by_accessibility_id(text1).get_attribute("name")
        logging.info(self.assertEqual(text1, text2, msg=u"更改成功"))

        # 长度长
        logging.info("Test Input TooLong Name")
        self.driver.find_element_by_accessibility_id(text1).click()
        self.wait()
        time.sleep(2)
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys("1111111111111111111111111111@@")
        self.driver.find_element_by_accessibility_id(u"提交").click()
        self.wait()
        time.sleep(2)
        tittle = self.driver.find_element_by_id("android:id/alertTitle")
        massage = self.driver.find_element_by_id("android:id/message")
        tittletext = tittle.text
        massagetext = massage.text
        logging.info("%s" % tittletext)
        logging.info("%s" % massagetext)
        self.driver.find_element_by_id("android:id/button1").click()
        self.wait()
        time.sleep(2)
        # 设备添加
        # self.driver.find_element_by_xpath("//android.view.View/android.widget.Image[1]").click()
        #         self.driver.tap([(972,90),(1038,156)])
        #         self.wait()
        #         time.sleep(2)
        #         self.is_search(u"扫码添加")
        #         self.driver.find_element_by_accessibility_id(u"扫码添加")
        #         self.wait()
        #         time.sleep(5)
        #         self.driver.find_element_by_accessibility_id(u"转到上一层级")
        #         self.wait()
        #         time.sleep(2)
        # #按类型添加
        #         self.driver.find_element_by_class_name("android.widget.Image").click()
        #         self.wait()
        #         time.sleep(2)
        #         self.driver.find_element_by_accessibility_id(u"按类型添加").click()
        #         self.wait()
        #         time.sleep(2)
        #         try:
        #             a=self.driver.find_element_by_accessibility_id(u"设备类型")
        #             logging.info(a.get_attribute("name"))
        #         except:
        #             logging.info(u"Into 设备类型 Flase")
        #         self.driver.find_element_by_accessibility_id(u"转到上一层级").click()
        #         self.wait()
        #         time.sleep(2)
        # # wifi连接
        #         self.driver.find_element_by_class_name("android.widget.Image").click()
        #         self.wait()
        #         time.sleep(2)
        #         self.driver.find_element_by_accessibility_id(u"WiFi连接").click()
        #         self.wait()
        #         time.sleep(2)
        #         try:
        #             a = self.driver.find_element_by_accessibility_id(u"插座网络配置")
        #             logging.info(a.get_attribute("name"))
        #         except:
        #             logging.info(u"Into 插座网络配置 Flase")
        #         #蓝灯已闪烁.wifi配置
        #         self.driver.find_element_by_class_name(u"蓝灯已闪烁").click()
        #         self.wait()
        #         time.sleep(2)
        #         a=self.driver.find_element_by_name(u"配置WiFi")
        #         logging.info("Into______________________%s"%a.text)
        #         self.driver.find_element_by_id("com.liefengtech.zhwy:id/et_wifi_psd").send_keys("123456")
        #         self.driver.find_element_by_name(u"下一步").click()
        #         self.wait()
        #         time.sleep(1)
        #         a=self.driver.find_element_by_id("com.liefengtech.zhwy:id/tv_config_status")
        #         status1=a.text
        #         time.sleep(5)
        #         a = self.driver.find_element_by_id("com.liefengtech.zhwy:id/tv_config_status")
        #         status2=a.text
        #         logging.info(self.assertEqual(status1,status2,msg=u"配置WiFi状态正在读取"))
        #         time.sleep(26)
        #         a = self.driver.find_element_by_id("com.liefengtech.zhwy:id/tv_config_status")
        #         logging.info(u"配置31s____________%s"%a.text)
        #         try:
        #             if a.text==(u"配置失败"):
        #                 self.driver.find_element_by_accessibility_id(u"重新配置").click()
        #         except:
        #             time.sleep(5)
        #             self.driver.find_element_by_accessibility_id(u"重新配置").click()
        #         self.wait()
        #         time.sleep(1)
        #         a=self.driver.find_element_by_id("com.liefengtech.zhwy:id/tv_config_status")
        #         status4=a.text
        #         logging.info(u"重新配置_____________________%s"%status4)
        #         self.driver.find_element_by_accessibility_id(u"转到上一层级").click()
        #         self.wait()
        #         time.sleep(2)
        #         self.driver.find_element_by_accessibility_id(u"转到上一层级").click()
        #         self.wait()
        #         time.sleep(2)
        #         self.driver.find_element_by_accessibility_id(u"转到上一层级").click()
        #         self.wait()
        #         time.sleep(2)
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
        self.wait()
        time.sleep(2)
        quit = self.driver.find_element_by_name(u"退出")
        logging.info(u"click________%s" % quit.text)
        quit.click()
        self.driver.close_app()
        self.driver.quit()
    def test_household_first(self):
        try:
            try:
                self.wait()
                time.sleep(15)
                self.wait()
                time.sleep(10)
                self.house()
            except:
                self.log()
                logging.info("Test_Choose_And_Open_Household_First!")
                data=pd.read_excel("D:\\liefeng\\liefeng2\\log\\app.xls")
                logging.info(self.driver.contexts)
                #登录
                username=int(data.iloc[9,1])
                password=int(data.iloc[9,2])
                self.login(username,password)
                self.wait()
                time.sleep(15)
                logging.info(u"Login_account____________%s" % username)
                self.wait()
                try:
                    WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_name(u"验证"))
                    logging.info("put identify login")
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
                self.house()
        except:
            self.log()
            logging.info("家居控制出错")
            self.driver.get_screenshot_as_file("D:\\liefeng\\liefeng2\\Sreenshots\\error_housecontrol.png")
            self.driver.close_app()
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()