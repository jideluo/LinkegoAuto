from uiautomator import device as d
import os
import unittest
import time
# import HTMLTestRunner

class My_Test(unittest.TestCase):
    def setUp(self):#初始化
        try:
            d.press.home()
            os.system("adb shell am start -n com.example.app/com.example.app.MainActivity")  # 启动智能短信DemoAPK
        except Exception as e:
            print(u"Error: 开启APP失败\n", e)


    def test_t(self):
        try:
            d(text="本机短信列表").wait.exists(timeout=3000)
            d(text="本机短信列表").click()
            d(text="通知类信息").click()
            judge =1
            while judge ==1:
                d.swipe(200, 500, 200, 0, steps=5)
                time.sleep(1)
        except Exception as  e:
            self.assertFalse("初始化失败",e)


    def tearDown(self):
        try:
            attestation = 0
            d.open.quick_settings()
            d(resourceId="com.android.systemui:id/settings_button").click()
            time.sleep(2)
            for num in range(10):
                if (d(text="应用管理").exists):
                    d(text="应用管理").click()
                    attestation = 1
                    break
                else:
                    d.swipe(200, 500, 200, 0, steps=10)
            if (attestation == 1):
                for x in range(30):
                    if (d(text="Demo智能短信").exists):
                        d(text="Demo智能短信").click()
                        time.sleep(1)
                        d(text="清除数据").click()
                        time.sleep(1)
                        d(text="确定").click()
                        break
                    else:
                        d.swipe(200, 500, 200, 0, steps=10)
            uistate = d.info
            if (uistate["currentPackageName"] != "com.yulong.android.launcher3"):
                d.press.back()
                d.press.back()
                d.press.home()
        except Exception as e:
            self.assertFalse("清除APP缓存失败",e)

if __name__ == "__main__":
    unittest.main()
