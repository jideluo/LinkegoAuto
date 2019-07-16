# -*- coding: utf-8 -*-
from time import sleep
from bin.scriptUtils import utils, excel
import threading
import xlsxwriter as wx
import matplotlib.pyplot as plt
import re
import subprocess

class CpuData(threading.Thread):
    def __init__(self, pkg):
        super(CpuData, self).__init__()
        self.total_before = None
        self.total_after = None
        self.process_before = None
        self.process_after = None
        self.ls = []
        self.pkg = pkg

    # 获取APP的PID
    def get_pid(self):
        pid = utils.get_app_pid(self.pkg)
        return pid

    # 获取总CPU时间
    @staticmethod
    def get_total_cpu_time():
        user = nice = system = idle = iowait = irq = softirq = 0
        '''
        user:从系统启动开始累计到当前时刻，处于用户态的运行时间，不包含 nice值为负进程。
        nice:从系统启动开始累计到当前时刻，nice值为负的进程所占用的CPU时间
        system 从系统启动开始累计到当前时刻，处于核心态的运行时间
        idle 从系统启动开始累计到当前时刻，除IO等待时间以外的其它等待时间
        iowait 从系统启动开始累计到当前时刻，IO等待时间(since 2.5.41)
        irq 从系统启动开始累计到当前时刻，硬中断时间(since 2.6.0-test4)
        softirq 从系统启动开始累计到当前时刻，软中断时间(since 2.6.0-test4)
        stealstolen  这是时间花在其他的操作系统在虚拟环境中运行时（since 2.6.11）
        guest 这是运行时间guest 用户Linux内核的操作系统的控制下的一个虚拟CPU（since 2.6.24）
        '''
        command="cat /proc/stat"
        time = utils.shell(command).stdout.readline().split()
        total_time = 0
        # for i in time:
        #     total_time += int(i)
        # return total_time

        for info in time:
            if info.decode() == "cpu":
                user = time[1].decode()
                nice = time[2].decode()
                system = time[3].decode()
                idle = time[4].decode()
                iowait = time[5].decode()
                irq = time[6].decode()
                softirq = time[7].decode()
                print("user=" + user)
                print("nice=" + nice)
                print("system=" + system)
                print("idle=" + idle)
                print("iowait=" + iowait)
                print("irq=" + irq)
                print("softirq=" + softirq)
                total_time = int(user) + int(nice) + int(system) + int(idle) + int(iowait) + int(irq) + int(softirq)
                print("totalCpuTime:" + str(total_time))
                return total_time

    # 获取进程cpu时间
    def get_process_cpu_time(self):
        '''

        pid     进程号
        utime   该任务在用户态运行的时间，单位为jiffies
        stime   该任务在核心态运行的时间，单位为jiffies
        cutime  所有已死线程在用户态运行的时间，单位为jiffies
        cstime  所有已死在核心态运行的时间，单位为jiffies
        '''
        utime = stime = cutime = cstime = 0
        time = utils.shell(
            "cat /proc/%s/stat" % self.get_pid()).stdout.readline().split()
        pro_time = 0
        utime = time[13].decode()
        stime = time[14].decode()
        cutime = time[15].decode()
        cstime = time[16].decode()
        print("utime=" + utime)
        print("stime=" + stime)
        print("cutime=" + cutime)
        print("cstime=" + cstime)
        pro_time = int(utime) + int(stime) + int(cutime) + int(cstime)
        print("processCpuTime=" + str(pro_time))
        # for i in time:
        #     pro_time += int(i)
        return pro_time

    # 得到几核cpu
    def get_cpu_kel(self):
        cmd = "adb  shell cat /proc/cpuinfo"
        print(cmd)
        output = subprocess.check_output(cmd).split()
        sitem = ".".join([x.decode() for x in output])  # 转换为string

    '''
    计算某进程的cpu使用率
    100*( processCpuTime2 – processCpuTime1) / (totalCpuTime2 – totalCpuTime1) (按100%计算，如果是多核情况下还需乘以cpu的个数);
    cpukel cpu几核
    pid 进程id
    '''
    def run(self):
        self.total_before = self.get_total_cpu_time()
        self.process_before = self.get_process_cpu_time()
        while True:
            if utils.stop != True:
                break
            y = []
            sleep(1)
            tm = utils.timestamp()
            self.total_after = self.get_total_cpu_time()
            self.process_after = self.get_process_cpu_time()
            usage = str(
                round(float(self.process_after - self.process_before) / float(self.total_after - self.total_before),
                      4) * 100)
            y.append(tm)
            y.append(usage)
            print ("CPU占用率：%s\n" % usage)
            self.total_before = self.total_after
            self.process_before = self.process_after
            self.ls.append(y)


    def get_cpu(self):
        return self.ls


if __name__ == '__main__':
    cpu = CpuData("com.example.app")
    cpu.start()
    cpu.join()
