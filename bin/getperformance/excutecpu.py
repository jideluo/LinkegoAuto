# coding=utf-8
import unittest
from time import sleep
import threading
from bin.scriptUtils import utils
from  report import HTMLTestReportCN

import unittest
# from htmlRunner import HTMLTestReportCN
from  bin.case.CaseMode import TestLogin
import bin.case.CaseMode
import unittest

# suite = unittest.TestSuite()  # 创建测试套件
# all_cases = unittest.defaultTestLoader.discover('.', '../testCass/TestLogin.py')
# # 找到某个目录下所有的以test开头的Python文件里面的测试用例
# for case in all_cases:
#     suite.addTests(case)  # 把所有的测试用例添加进来
# fp = open('res.html', 'wb')
#
# runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title='all_tests', description='所有测试情况')
# runner.run(suite)


# 运行测试



class WeiFuHua(threading.Thread):
    def __init__(self):
        super(WeiFuHua, self).__init__()
        # self.driver = MeThod()
        # self.driver.api.implicitly_wait(60)  # 查找元素超时，秒
    #
    # def tearDown(self):
    #     self.driver.api.quit()
    #
    # def swipeToDown(self):
    #     width = self.driver.api.get_window_size()["width"]  # 屏幕宽度
    #     height = self.driver.api.get_window_size()["height"]  # 屏幕高度
    #     self.driver.api.swipe(width / 2, float(height / 1.02), width / 2, height / 8, 2000)  # 滑动轨

    def run(self):
        # TestLogin.run

        # unittest.main(defaultTest='suite')
        suite1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
        # suite2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)
        filename = "./report/testCass.html"  # 定义个报告存放路径，支持相对路径
        fp = open(filename, 'wb')  # 结果写入HTML 文件
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title="自动化测试报告", description="Test",
                                                 tester="LIKEFU")
        suite = unittest.TestSuite([suite1])
        runner.run(suite)
        # unittest.TextTestRunner(verbosity=2).run(suite)
        utils.stop = False



        # TestTool.TestTool;
        # try:
        #     d.press.home()
        #     os.system("adb shell am start -n com.example.app/com.example.app.MainActivity")  # 启动智能短信DemoAPK
        # except Exception as e:
        #     print (u"Error: 开启APP失败\n", e)
        #
        # try:
        #     d(text="本机短信列表").wait.exists(timeout=3000)
        #     d(text="本机短信列表").click()
        #     d(text="通知类短信").click()
        #     judge = 1
        #     while judge >100:
        #         d.swipe(200, 500, 200, 0, steps=5)
        #         time.sleep(1)
        #         judge=judge+1
        # except Exception as  e:
        #         self.assertFalse("初始化失败", e)

        # utils.stop = False
        # try:
        #     attestation = 0
        #     d.open.quick_settings()
        #     d(resourceId="com.android.systemui:id/settings_button").click()
        #     time.sleep(2)
        #     for num in range(10):
        #         if (d(text="应用管理").exists):
        #             d(text="应用管理").click()
        #             attestation = 1
        #             break
        #         else:
        #             d.swipe(200, 500, 200, 0, steps=10)
        #         if (attestation == 1):
        #             for x in range(30):
        #                 if (d(text="Demo智能短信").exists):
        #                     d(text="Demo智能短信").click()
        #                     time.sleep(1)
        #                     d(text="清除数据").click()
        #                     time.sleep(1)
        #                     d(text="确定").click()
        #                     break
        #                 else:
        #                     d.swipe(200, 500, 200, 0, steps=10)
        #         uistate = d.info
        #         if (uistate["currentPackageName"] != "com.yulong.android.launcher3"):
        #             d.press.back()
        #             d.press.back()
        #             d.press.home()
        # except Exception as e:
        #     self.assertFalse("清除APP缓存失败", e)

        # self.driver.findElement("xpath", "7").click()  # 点击资讯按钮
        # i = 0
        # while True:
        #     if utils.stop != True:
        #         break
        #     i += 1
        #     print "执行第：%d 次" % i
        #     self.driver.findElement("xpath", "8").click()  # 进入资讯详情
        #     sleep(1)
        #     for n in range(2):  # 滑动资讯详情页面到底部
        #         self.swipeToDown()
        #     self.driver.api.keyevent(4)  # 点击返回按钮
        #
        # self.tearDown()


if __name__ == '__main__':
    wfh = WeiFuHua()
    wfh.start()
    wfh.join()
