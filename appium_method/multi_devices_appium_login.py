# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/10
@Auth ： zhangqimin
@File ：multi_devices_appium_login.py
@IDE ：PyCharm

"""
from time import sleep
from appium import webdriver
from androguard.core.bytecodes.apk import APK
import os

#获取安装包apk路径
def apk_path():
    parents = os.path.dirname(os.path.abspath(__file__))
    appPath = parents + '\\' + 'app' + '\\' +'course-debug-3.5.1.apk'
    return appPath
#获取多设备连接PC
def get_devices() -> list:
    all_devices = []
    cmd = "adb devices"
    result = os.popen(cmd).readlines()[1:]
    for item in result:
        if item !="\n":
            all_devices.append(str(item).split("\t")[0])
    return all_devices

#获取手机系统版本
def get_platform(dev: str) -> str:
    cmd = 'adb -s {} shell getprop ro.build.version.release'.format(dev)
    result = os.popen(cmd).readlines()[0]
    return str(result).split("\n")[0]

#获取apk包名称
def get_apkname(apk):
    a = APK(apk, False, "r")
    return a.get_package()
#获取apk包的activity
def get_apk_activity(apk):
    a = APK(apk, False, "r")
    return a.get_main_activity()

#判断手机是否已安装apk包
def isinstallapk(packagename: str, devicename: str) -> bool:
    cmd = "adb -s {} shell pm list packages -3".format(devicename)
    result = os.popen(cmd).readlines()
    all_apkname = []
    for i in result:
        apkname = str(i).split('\n')[0].split(":")[1]
        all_apkname.append(apkname)
    if packagename in all_apkname:
        return True
    return False

#卸载掉apk包
def uninstallapk(packname: str, devicename: str) -> bool:
    cmd = 'adb -s {} shell pm list packages -3'.format(devicename)
    result = os.popen(cmd).readlines()
    all_apkname = []
    for i in result:
        apkname = str(i).split('\n')[0].split(":")[1]
        all_apkname.append(apkname)
    if packname in all_apkname:
        cmd = 'adb -s %s uninstall %s' % (devicename, packname)
        os.system(cmd)
        return True
    return False

#安装apk包
def installapk(packnamepath: str, devicename: str) -> bool:
    cmd = 'adb -s %s install %s' % (devicename, packnamepath)
    os.system(cmd)
    return True

#登录
def test_login():
    packname = get_apkname(apk_path())
    dev = get_devices()[0]
    is_first_install = False
    #判断是否安装app
    is_install = isinstallapk(packname, dev)
    if is_install is False:
        #没有安装，则安装
        installapk(apk_path(), dev)
        is_first_install = True

    #启动apk测试
    apkname = get_apkname(apk_path())
    launcheractivity = get_apk_activity(apk_path())
    desired_caps = {
        'platformName': 'Android',
        'deviceName': dev,  # adb  deivces
        'platformVersion': get_platform(dev),  # 从设置中可以获取
        'appPackage': apkname,  # 包名
        'appActivity': launcheractivity,  # apk的launcherActivity
        # 'skipServerInstallation': True
    }
    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
    sleep(10)
    #启动同意用户协议
    driver.find_element_by_id("tv.danmaku.bili:id/agree").click()
    if is_first_install:
        #首次安装需加载文件
        sleep(50)
    sleep(10)
    driver.find_element_by_xpath("//*[@text='登录']").click()
    driver.find_element_by_id('tv.danmaku.bili:id/btn_change_account').click()

    username = driver.find_element_by_id('tv.danmaku.bili:id/username')
    username.clear()
    username.send_keys("name")
    password = driver.find_element_by_id('tv.danmaku.bili:id/passport_tag')
    password.clear()
    password.send_keys("123456")
    login = driver.find_element_by_id('tv.danmaku.bili:id/btn_login')
    login.click()
    driver.close()


if __name__ == '__main__':
    print(apk_path())
    test_login()