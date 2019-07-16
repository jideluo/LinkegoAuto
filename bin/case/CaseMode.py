# coding=utf-8
import unittest
import time
from bin.scriptUtils import tool, excel
from conf import fixedValue

er =excel.ReadDate()
#APP登录测试用例

class TestLogin(unittest.TestCase):

    #调用toolclass
    # connect= tool.toolClass("USB","8681-M02-0x729bcc98","com.phnixiot.homecontroller")
    connect = tool.toolClass("wifi", er.read_app_ip(), er.read_app_name())
    #获取连接设备
    d =connect.d
    #唤醒屏幕并解锁
    connect.screen_wake()

    def setUp(self):
        self.connect.app_start()

    #正常登陆
    def test_060_Normal(self):
        self.d(resourceId=fixedValue.PHONE).set_text("15113583610")
        self.d(resourceId=fixedValue.PASSWORD).set_text("12345678")
        time.sleep(2)
        self.d(resourceId=fixedValue.LOGINBTN).click()
        # 判定是否登录成功
        self.assertEqual(True, self.d(text="定时").exists(timeout=10.0))

    #手机号码短
    def test_010_PhoneShort(self):
        self.d(resourceId=fixedValue.PHONE).set_text("1511358")
        self.d(resourceId=fixedValue.PASSWORD).set_text("123456789")
        time.sleep(2)
        self.d(resourceId=fixedValue.LOGINBTN).click()
        self.assertEqual("先输入正确的手机号码",self.connect.get_toast())
        #清除toast缓存
        self.d.toast.reset()



     #手机号码长
    def test_020_PhoneLong(self):
        self.d(resourceId=fixedValue.PHONE).set_text("15113583610123")
        self.d(resourceId=fixedValue.PASSWORD).set_text("123456789")
        time.sleep(2)
        self.d(resourceId=fixedValue.LOGINBTN).click()
        # print(self.connect.get_toast())
        self.assertEqual("先输入正确的手机号码", self.connect.get_toast())
        self.d.toast.reset()

    #密码为空
    def test_030_PasswordNull(self):
        self.d(resourceId=fixedValue.PHONE).set_text("15113583610")
        self.d(resourceId=fixedValue.PASSWORD).set_text("")
        time.sleep(2)
        self.d(resourceId=fixedValue.LOGINBTN).click()
        self.assertEqual("密码不能为空", self.connect.get_toast())
        self.d.toast.reset()

    #密码不正确
    def test_040_PasswordFail(self):
        self.d(resourceId=fixedValue.PHONE).set_text("15113583610")
        self.d(resourceId=fixedValue.PASSWORD).set_text("1234567")
        time.sleep(2)
        self.d(resourceId=fixedValue.LOGINBTN).click()
        self.assertEqual("ERROR_API_ACCOUNT_PASSWORD_ERROR",self.connect.get_toast())
        self.d.toast.reset()

    def test_050_PhoneNull(self):
        self.d(resourceId=fixedValue.PHONE).set_text(" ")
        self.d(resourceId=fixedValue.PASSWORD).set_text("123456789")
        time.sleep(2)
        self.d(resourceId=fixedValue.LOGINBTN).click()
        self.assertEqual("先输入正确的手机号码",self.connect.get_toast())
        self.d.toast.reset()

    def tearDown(self):
        self.connect.app_clear()

# if __name__ == "__main__":
#     unittest.main()


