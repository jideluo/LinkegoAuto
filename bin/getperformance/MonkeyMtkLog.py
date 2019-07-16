

import time
import threading
from  bin.getperformance import MonkeyTest
import os

class MonkeyLog(threading.Thread):
    def __init__(self,sn,delay):
        super(MonkeyLog, self).__init__()
        self.ls = []
        self.sn = sn
        self.delay=delay

    def run(self):
        while True:
            print("导出日志线程开始休眠共 {} 秒".format(self.delay))
            time.sleep(self.delay)
            arr = self.sn.split(',')
            for arg in arr:
                print(arg)
                self.stop_mtklog(arg)
                self.pull_mtklog(arg)
                self.start_mtklog(arg)
            if MonkeyTest.Utils.stop != True:
                break

    def start_mtklog(self,sn):
        os.system(
            r"adb -s %s shell am broadcast -a com.mediatek.mtklogger.ADB_CMD -e cmd_name start --ei cmd_target 23" % sn)
        print("hello" + sn);
        os.system(r"ping localhost -n 5 > nul")

    def stop_mtklog(self,sn):
        print(sn)
        os.system(
            r"adb -s %s shell am broadcast -a com.mediatek.mtklogger.ADB_CMD -e cmd_name stop --ei cmd_target 23" % sn)
        os.system(r"ping localhost -n 5 > nul")

    def pull_mtklog(self,sn):
        timestamp = time.strftime(r"%Y%m%d_%H%M%S", time.localtime())

        # Copy Mtklog to PC
        filepath = r"E:\S33";
        os.chdir(r'%s' % filepath)
        mtklogdir = "%s\%s" % (os.getcwd(), timestamp)
        if not os.path.exists(mtklogdir):
            os.makedirs(r'%s' % mtklogdir)
        print(mtklogdir);
        os.system(r"adb -s %s pull /sdcard/mtklog %s" % (sn, mtklogdir))
        os.system(r"adb -s %s pull /data %s" % (sn, mtklogdir))
        os.system(r"adb -s %s shell rm -rf /sdcard/mtklog" % sn)
        os.system(r"adb -s %s shell rm -rf /data" % sn)


if __name__ == '__main__':
    # Set Script dir
    sn = "8681-M02-0x729bcc98"
    delay = 1 * 1
    Mlog = MonkeyLog(sn,delay)
    Mlog.start()
    Mlog.join()
