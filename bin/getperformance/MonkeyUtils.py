

import subprocess
#######################
# 获取设备的devices
#######################
def get_devices():
    devices = []
    cmd = 'adb devices'
    res = str(subprocess.check_output(cmd, shell=True))
    for txt in res.split("\\r\\n"):
        sub = txt.split("\\t")
        if len(sub) > 1:
            devices.append(sub[0])
    return devices