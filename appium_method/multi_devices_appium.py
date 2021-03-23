# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/10
@Auth ： zhangqimin
@File ：multi_devices_appium.py
@IDE ：PyCharm
地址：https://mp.weixin.qq.com/s/PJ9IR-VrPKa8ymylKU1TIA
"""

import os

#查询所有连接PC的设备id
import random

#手机连接PC的所有设备
from androguard.core.bytecodes.apk import APK

def apk_path():
    parents = os.path.dirname(os.path.abspath(__file__))
    appPath = parents + '\\' + 'app' + '\\' +'course-debug-3.5.1.apk'
    return appPath

def get_devices() -> list:
    all_devices= []
    cmd = "adb devices"
    result = os.popen(cmd).readlines()[1:]
    for item in result:
        if item != "\n":
            all_devices.append(str(item).split("\t")[0])
    return all_devices

def get_platform(dev:str) -> str:
    cmd = 'adb -s {} shell getprop ro.build.version.release'.format(dev)
    result = os.popen(cmd).readlines()[0]
    return str(result).split("\n")[0]

def get_port():
    all_port = []
    port = random.randint(1000,6000)
    #判断生成的端口是否已生成过，已生成的port不处理，继续随机生成
    if port in all_port:
        get_port()
    else:
        all_port.append(port)
    return all_port

def get_apkname(apk):
    a = APK(apk,False, "r")
    return a.get_package()
def get_apk_activity(apk):
    a = APK(apk, False, "r")
    return a.get_main_activity()

def start_devices_app():
    all_devices = get_devices()
    if len(all_devices) >0:
        for item in all_devices:
            desired_caps = {
                'platformName': 'Android',
                'deviceName': item,
                'platformVersion': get_platform(item),
                'appPackage': get_apkname(apk_path()),  # 包名
                'appActivity': get_apk_activity(apk_path()),  # apk的launcherActivity
                'skipServerInstallation': True
            }

if __name__ == '__main__':
    start_devices_app()