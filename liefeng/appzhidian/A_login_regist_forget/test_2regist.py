#coding:utf-8
#lihong 2018-5-6
import time
from appium import webdriver
import logging,unittest
import pandas as pd
import pymysql
import xlwt
import xlrd
from xlutils.copy import copy
from xlwt import Style


import warnings
warnings.filterwarnings("ignore")

class regist(unittest.TestCase):
    @classmethod
    def setUp(self):
        time.sleep(100)
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

#写入方法
    def writeExcel(self,row, col, str, styl=Style.default_style):
        rb = xlrd.open_workbook('D:\\liefeng\\liefeng2\\log\\app.xls', formatting_info=True)
        wb = copy(rb)
        ws = wb.get_sheet(0)
        ws.write(row, col, str, styl)
        wb.save('D:\\liefeng\\liefeng2\\log\\app.xls')

    def test_regist_quit(self):
        self.log()
        logging.info("APP_regist_right_telst start!")
        data = pd.read_excel('D:\\liefeng\\liefeng2\\log\\app.xls')
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

        sheel=int(data.iloc[3,1])
        self.driver.find_element_by_name(u"请输入手机号码").send_keys(sheel)
        time.sleep(2)

        #更新Excel数据
        b = str(int(sheel) + 1)
        style = xlwt.easyxf('font:height 180, color-index black, bold on;align: wrap on, vert centre, horiz center')
        self.writeExcel(4, 2,b, style)

        self.driver.find_element_by_name(u"获取验证码").click()
        self.wait()
        time.sleep(5)
        identify = self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.liefengtech.zhwy:id/edit_verifyCode']")
        logging.info(u"get identity number___________%s"%identify.text)
        self.driver.find_element_by_name(u"下一步").click()
        self.wait()
        time.sleep(2)
        sheel2=int(data.iloc[3,2])
        logging.info(u"post password___________%s"%sheel2)
        self.driver.find_element_by_id("com.liefengtech.zhwy:id/edit_pass").send_keys(sheel2)
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

        #验证数据库
        logging.info("check database start !")
        try:
            conn = pymysql.connect()
            cur = conn.cursor()
            sql1 = ("select global_id  from t_customer WHERE nick_name=%s"%sheel)
            cur.execute(sql1)
            a = cur.fetchall()
            logging.info("global_id______________%s"%a)
            sql1 = ("select  password  from t_customer WHERE nick_name=%s"%sheel)
            cur.execute(sql1)
            a = cur.fetchall()
            logging.info("password______________%s" % a)
            sql1 = ("select  cust_global_id  from t_cust_login_account WHERE account=%s"%sheel)
            cur.execute(sql1)
            a = cur.fetchall()
            logging.info("cust_global_id______________%s" % a)
            conn.close()
        except:
            logging.info("regist account database checked  Flase!!!!!!! ")

if __name__ == "__main__":
    unittest.main()
