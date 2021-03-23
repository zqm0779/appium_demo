# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/10
@Auth ： zhangqimin
@File ：get_android_devices_and_version.py
@IDE ：PyCharm

"""
from androguard.core.bytecodes.apk import APK
import os
#取里面的值。去掉第一行，并且去掉\n的行，然后得到，我们用\t切割。取第一个就可以获取
def get_devices():
    cmd = 'adb devices'
    print(os.popen(cmd).readlines())
    result = os.popen(cmd).readlines()[1:]
    print(result)
    for item in result:
        if item != "\n":
            return str(item).split("\t")[0]
#获取android的系统版本platformVersion
def get_platform():
    cmd = 'adb shell getprop ro.build.version.release'
    result = os.popen(cmd).readlines()[0]
    return str(result).split("\n")[0]

if __name__ == '__main__':
    print(get_devices())
    # print(get_platform())
