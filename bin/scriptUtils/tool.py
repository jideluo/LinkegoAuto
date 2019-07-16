


#UIautomator2工具类

import uiautomator2 as u2
import uiautomator2.ext.htmlreport as htmlreport

class toolClass:

    def __init__(self,connectionType,addre,package):
        self.connectionType =connectionType
        self.addre =addre
        self.package =package
        self.d =self.connection_type()

    #判定连接方式
    def connection_type(self):
        if (self.connectionType=="wifi"):
            return self.connect_wifi()
        else:
            #启动点击日志
            self.cilck_Log()
            return self.connect_usb()
    # WiFi连接
    def connect_wifi(self):
        self.d = u2.connect_wifi(self.addre)
        self.d.set_fastinput_ime(True)
        return self.d


    # usb连接
    def connect_usb(self):
        self.d = u2.connect_usb(self.addre)
        self.d.set_fastinput_ime(True)
        return self.d

    # 启动APP
    def app_start(self):
        return self.d.app_start(self.package)

    #清除APP缓存
    def app_clear(self):
        return self.d.app_clear(self.package)
    #退出APP
    def app_stop(self):
        return self.d.app_stop(self.package)

    #获取Toast
    def get_toast(self):
        return self.d.toast.get_message(5.0, 10.0, "default message")

    #唤醒屏幕
    def screen_wake(self):
        if self.d.info.get('screenOn')==False:
            self.d.screen_on()
            self.d.unlock()

    #USB启动clickLog
    def cilck_Log(self):
        u = u2.connect()
        hrp = htmlreport.HTMLReport(u)
        hrp.patch_click()




if __name__ == '__main__':
    x =toolClass("wifi","192.168.31.155","com.phnixiot.homecontroller").connection_type()
    print(x)
    dx =toolClass("wifi","192.168.31.155","com.phnixiot.homecontroller")
    print("d",dx.screen_wake())
