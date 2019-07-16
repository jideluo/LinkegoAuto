# -*- coding: utf-8 -*-

import threading
import os
import re
import time
from datetime import datetime
import subprocess
import sys


class MonkeyData(threading.Thread):
    def __init__(self,sn):
        super(MonkeyData, self).__init__()
        self.ls = []
        self.sn = sn

    def run(self):
        monkeycmd = "adb -s %s shell monkey --throttle 1000 --ignore-timeouts --ignore-crashes --ignore-security-exceptions -v -v -v 1000000000" % self.sn
        results = subprocess.Popen(monkeycmd, shell=True, stdout=subprocess.PIPE)
        # results = (Utils.shell(monkeycmd).stdout.readline()).decode('UTF-8')
        print("首次开启进程")
        time.sleep(5)
        while True:
            if Utils.stop != True:
                print("退出成功")
                break
            out = os.popen(r"adb -s %s shell pidof com.android.commands.monkey" % self.sn).read();
            res = re.findall(r'(\d{1,9})', out)
            print(res)
            if len(res) == 0:
                print("无进程,重新拉起进程")
                os.system(monkeycmd)
            elif len(res) >= 2:
                for i in range(len(res)):
                    os.system(r"adb -s {} shell kill {}".format(sn, res[i]))
                    print("adb -s {} shell kill {}".format(sn, res[i]))
                print("杀掉2个及以上的进程,重新拉起")
                os.system(monkeycmd)


class Utils():
    # adb shell命令

    stop = True

    def shell(args):
        cmd = "adb shell %s" % (str(args))
        print(cmd)
        # print subprocess.check_output(cmd, shell=True)
        return subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)






if __name__ == '__main__':
    sn = sys.argv[1]
    mem = MonkeyData(sn)
    mem.start()
    mem.join()


















# import os
# import re
# import time
# from datetime import datetime
# import subprocess
# import sys
#
#
# def pull_monkey(sn):
#     monkeycmd="adb -s %s shell monkey --throttle 1000 --ignore-timeouts --ignore-crashes --ignore-security-exceptions -v -v -v 1000000000"%sn
#     printinfo=subprocess.Popen(monkeycmd,shell=True,stdout=subprocess.PIPE)
#
#
#     while True:
#         out = os.popen(r"adb -s %s shell pidof com.android.commands.monkey"%sn).read();
#         res = re.findall(r'(\d{1,9})',out)
#         #print("res:%s"%res)
#
#         if len(res)==0:
#             print("无进程,重新拉起进程")
#             os.system(monkeycmd)
#         elif len(res)>=2:
#             for i in range(len(res)):
#                 os.system(r"adb -s {} shell kill {}".format(sn,res[i]))
#                 print("adb -s {} shell kill {}".format(sn,res[i]))
#             print("杀掉2个及以上的进程,重新拉起")
#             os.system(monkeycmd)
#
#
#
#
# if __name__ == '__main__':
#     #Input Serial Number
#     sn = sys.argv[1]
#     pull_monkey(sn)
#
# import os
# import re
# import time
# from datetime import datetime
# import subprocess
# import sys
#
#
# def start_mtklog(sn):
#     os.system(
#         r"adb -s %s shell am broadcast -a com.mediatek.mtklogger.ADB_CMD -e cmd_name start --ei cmd_target 23" % sn)
#     print("hello" + sn);
#     os.system(r"ping localhost -n 5 > nul")
#
#
# def stop_mtklog(sn):
#     os.system(
#         r"adb -s %s shell am broadcast -a com.mediatek.mtklogger.ADB_CMD -e cmd_name stop --ei cmd_target 23" % sn)
#     os.system(r"ping localhost -n 5 > nul")
#
#
# def pull_mtklog(sn):
#     timestamp = time.strftime(r"%Y%m%d_%H%M%S", time.localtime())
#
#     # Copy Mtklog to PC
#     os.chdir(r'%s' % filepath)
#     mtklogdir = "%s\%s" % (os.getcwd(), timestamp)
#     if not os.path.exists(mtklogdir):
#         os.makedirs(r'%s' % mtklogdir)
#     print(mtklogdir);
#     os.system(r"adb -s %s pull /sdcard/mtklog %s" % (sn, mtklogdir))
#     os.system(r"adb -s %s pull /data %s" % (sn, mtklogdir))
#     os.system(r"adb -s %s shell rm -rf /sdcard/mtklog" % sn)
#     os.system(r"adb -s %s shell rm -rf /data" % sn)
#
#
# def pull_log(sns, delay):
#     while True:
#         print("导出日志线程开始休眠共 {} 秒".format(n))
#         # print("导出日志线程开始休眠共 {name} {time}秒".format(name=name, time=time))
#         time.sleep(delay)
#         for arg in sns:
#             stop_mtklog(arg)
#             pull_mtklog(arg)
#             start_mtklog(arg)
#
#
# if __name__ == '__main__':
#     # Set Script dir
#     filepath = r"E:\S33";
#     args = sys.argv[1:]
#     n = 60*30
#     pull_log(args , n)