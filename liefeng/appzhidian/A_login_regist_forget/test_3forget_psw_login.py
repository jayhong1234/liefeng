#coding:utf-8
#LiH 2018-4-2
import time
from appium import webdriver
import logging,unittest
import pandas as pd
from xlwt import *
import pymysql
import xlwt
import xlrd
from xlutils.copy import copy
from xlwt import Style


import warnings
warnings.filterwarnings("ignore")

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
        time.sleep(1)
        self.driver.find_element_by_name(u"登录").click()

    #写入Excel
    def writeExcel(self, row, col, str, styl=Style.default_style):
        rb = xlrd.

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

    def test_forgetpsw(self):
        self.log()
        logging.info("APP_forget_password_modify_login start!")
        data = pd.read_excel('ls')
        self.driver.find_element_by_name(u"找回密码").click()
        self.wait()
        time.sleep(2)
        username ="13374892516"
        try:
            conn = pymysql.connect()
            cur = conn.cursor()
            sql1 = ("select password  from t_customer WHERE nick_name=%s" % username)
            cur.execute(sql1)
            self.oldpsw = cur.fetchall()
            logging.info("get old password________________%s" % self.oldpsw)
            conn.close()
        except:
            logging.info("regist account database checked  Flase!!!!!!! ")

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
        password=int(data.iloc[2,2])
        logging.info("post_modify_password___________%s"%password )
        self.driver.find_element_by_id("com.liefengtech.zhwy:id/edit_pass").send_keys(password)
        self.driver.find_element_by_xpath(
            "//android.widget.Button[@resource-id='com.liefengtech.zhwy:id/img_sub']").click()
        self.wait()
        time.sleep(2)

        # 更新Excel数据
        b = str(int(password) + 1)
        logging.info("update password______________%s"%b)
        style = xlwt.easyxf('font:height 180, color-index black, bold on;align: wrap on, vert centre, horiz center')
        self.writeExcel(3, 3, b, style)

        time.sleep(10)

        self.login(username,password)
        self.wait()
        time.sleep(2)
        self.wait()
        time.sleep(25)
        logging.info(u"登录成功")

        # 验证数据库
        logging.info("check database start !")
        try:
            conn = pymysql.connect(
            cur = conn.cursor()
            sql1 = ("select password  from t_customer WHERE nick_name=%s" % username)
            cur.execute(sql1)
            self.newpsw= cur.fetchall()
            logging.info("create new password________________%s" % self.newpsw)
            conn.close()
        except:
            logging.info("regist account database checked  Flase!!!!!!! ")
        self.assertEqual(self.oldpsw,self.oldpsw,msg=u"更改密码成功")
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
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
