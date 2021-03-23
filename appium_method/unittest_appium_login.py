# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/11
@Auth ： zhangqimin
@File ：unittest_appium_login.py
@IDE ：PyCharm

"""
from time import sleep

from appium import webdriver
from androguard.core.bytecodes.apk import APK
import os
import unittest

# apk_path = "/Users/lileilei/Downloads/iBiliPlayer-bili.apk"
#获取安装包apk路径
def apk_path():
    parents = os.path.dirname(os.path.abspath(__file__))
    appPath = parents + '\\' + 'app' + '\\' +'iBiliPlayer-bili.apk'
    return appPath

def get_devices() -> list:
    all_devices = []
    cmd = "adb devices"
    result = os.popen(cmd).readlines()[1:]
    for item in result:
        if item !="\n":
            all_devices.append(str(item).split("\t")[0])
    return all_devices

def getPlatForm(dev: str) -> str:
    cmd = 'adb -s {} shell getprop ro.build.version.release'.format(dev)
    result = os.popen(cmd).readlines()[0]
    return str(result).split("\n")[0]

def get_apkname(apk):
    a =APK(apk, False,"r")
    return a.get_package()

def get_apk_lautc(apk):
    a = APK(apk, False, "r")
    return a.get_main_activity()

def isinstallapk(packname: str, devname: str) -> bool:
    cmd = 'adb -s {} shell pm list packages -3'.format(devname)
    result = os.popen(cmd).readlines()
    all_apkname = []
    for i in result:
        apkname = str(i).split("\n")[0].split(":")[1]
        all_apkname.append(apkname)
    if packname in all_apkname:
        return True
    return False

def uninstallapk(packname: str, devname: str) -> bool:
    cmd = 'adb -s {} shell pm list packages -3'.format(devname)
    result = os.popen(cmd).readlines()
    all_apkname = []
    for i in result:
        apkname = str(i).split("\n")[0].split(":")[1]
        all_apkname.append(apkname)
    if packname in all_apkname:
        cmd = 'adb -s %s uninstall %s' % (devname, packname)
        os.system(cmd)
        return True
    return False

def installapk(paknamepath: str, devname: str) -> bool:
    cmd = 'adb -s %s install %s' %(devname,paknamepath)
    os.system(cmd)
    return True

class testCaseLogin(unittest.TestCase):
    def setUp(self) -> None:
        packname = get_apkname(apk_path())
        dev = get_devices()[0]
        is_first_install = False
        #判断是否安装app
        is_install = isinstallapk(packname, dev)
        if is_install is False:
            #如果没有安装，则安装
            installapk(apk_path(),dev)
            is_first_install = True

        #启动apk测试
        apkname = get_apkname(apk_path())
        launcheractivity = get_apk_lautc(apk_path())
        desired_caps = {
            'platformName': 'Android',
            'deviceName': dev,  # adb  deivces
            'platformVersion': getPlatForm(dev),  # 从设置中可以获取
            'appPackage': apkname,  # 包名
            'appActivity': launcheractivity,  # apk的launcherActivity
            # 'skipServerInstallation': True
        }
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
        sleep(10)
        # 启动同意用户协议
        self.driver.find_element_by_id("tv.danmaku.bili:id/agree").click()
        if is_first_install:
            # 首次安装需要加载文件
            sleep(50)
        sleep(10)
        self.driver.find_element_by_id("tv.danmaku.bili:id/avatar_layout").click()
        sleep(5)
        self.driver.find_element_by_xpath("//*[@text='登录']").click()

    def tearDown(self) -> None:
        self.driver.close()

    def testlogin(self):
        username = self.driver.find_element_by_id('tv.danmaku.bili:id/username')
        username.clear()
        username.send_keys("name")
        password = self.driver.find_element_by_id('tv.danmaku.bili:id/passport_tag')
        password.clear()
        password.send_keys("123456")
        login = self.driver.find_element_by_id('tv.danmaku.bili:id/btn_login')
        login.click()
        try:
            self.driver.find_element_by_id('tv.danmaku.bili:id/btn_login')
            self.assertTrue(False, msg="测试失败")
        except:
            self.assertTrue(True, msg="测试成功")

    def testloginerror(self):
        username = self.driver.find_element_by_id('tv.danmaku.bili:id/username')
        username.clear()
        username.send_keys("shibai")
        password = self.driver.find_element_by_id('tv.danmaku.bili:id/passport_tag')
        password.clear()
        password.send_keys("123456")
        login = self.driver.find_element_by_id('tv.danmaku.bili:id/btn_login')
        login.click()
        try:
            self.driver.find_element_by_id('tv.danmaku.bili:id/btn_login')
            self.assertTrue(True, msg="测试成功")
        except:
            self.assertTrue(False, msg="测试失败")


if __name__ == "__main__":
    unittest.main()