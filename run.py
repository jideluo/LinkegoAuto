# coding=utf-8
from time import sleep
from bin.scriptUtils import excel, utils
from bin.getperformance import cpu, memory, fps, net, excutecpu, batteryTemp, cpuTemp,getDeviceInfo
import logging



ex = excel.WriteDate()  # 实例化一个ex写入对象
# er = excel.ReadDate()   #实例化一个ex读取对象
# pkg = er.read_app_name() #从文件中读取APP包名
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='./report/test.log',
#                     filemode='w')

# 启动采集数据线程
# testcase =CaseMode.CaseMode()        #启动程序
ecpu = excutecpu.WeiFuHua()          #启动程序
# cpuinfo = cpu.CpuData(pkg)           #获取CPU
# meminfo = memory.MemoryData(pkg)     #获取内存
# fpsinfo = fps.RootFpsData()          #获取FPS
# netinfo = net.NetData(pkg)           #获取数据流量
# bttinfo = batteryTemp.BatteryTempData() #获取电池温度
ctpinfo = cpuTemp.CpuTempData()      #获取CPU温度
#deviceinfo = getDeviceInfo.DeviceInfo()

# utils.stop = (bool(input("敲回车停止：")))
ecpu.start()
# testcase.start()
sleep(2)
# deviceinfo.start()
# cpuinfo.start()
# meminfo.start()
# fpsinfo.start()
# netinfo.start()
# bttinfo.start()
ctpinfo.start()
# utils.stop = (bool(input("敲回车停止：")))
# testcase.join()
ecpu.join()
# cpuinfo.join()
# meminfo.join()
# fpsinfo.join()
# netinfo.join()
# bttinfo.join()
ctpinfo.join()

#
# # 写入数据
# ex.writeData(sheet_name=u"设备信息", heads=[u"Pss Total(KB)", u"Private Dirty"], data=[])
#
# ex.writeData(sheet_name=u"CPU使用率", heads=[u"CPU(%)"], data=cpuinfo.get_cpu())
# # #
# ex.writeData(sheet_name=u"内存占用率",
#              heads=[u"Pss Total(KB)", u"Private Dirty", u"Private Clean", u"Swapped Dirty", u"Heap Size", u"Heap Alloc",
#                     u"Heap Free"], data=meminfo.get_mem())
# # #
# ex.writeData(sheet_name=u"FPS帧率", heads=[u"fps"], data=fpsinfo.get_fps())
# # #
# ex.writeData(sheet_name=u"流量", heads=[u"net(KB)"], data=netinfo.get_net())
# #
# ex.writeData(sheet_name=u"电池温度", heads=[u"battery temp(℃)"], data=bttinfo.get_battery_temp())
# #
ex.writeData(sheet_name=u"CPU温度", heads=[u"cpu temp(℃)"], data=ctpinfo.get_cpu_temp())
#
#
# # 关闭excel
ex.close()
