# -*- coding: utf-8 -*-
from bin.scriptUtils import utils, excel
from time import sleep
import threading


class MemoryData(threading.Thread):
    def __init__(self, pkg):
        super(MemoryData, self).__init__()
        self.ls = []
        self.pkg = pkg

    def run(self):
        mem_command = '"dumpsys meminfo %s |grep TOTAL"' % self.pkg
        # print mem_command
        while True:
            if utils.stop != True:
                break
            sleep(1)
            y = []
            tm = utils.timestamp()
            results = (utils.shell(mem_command).stdout.readline()).decode('UTF-8').split()[1:8]
            print ("内存：%s" % results)
            y.append(tm)
            for index in results:
                y.append(index)
            self.ls.append(y)
            print (self.ls)
    def get_mem(self):
        return self.ls


if __name__ == '__main__':
    mem = MemoryData( "com.example.app")
    mem.start()
    mem.join()
