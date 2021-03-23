# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/10
@Auth ： zhangqimin
@File ：Android_ios_init.py
@IDE ：PyCharm

"""
#python Android
from Tools.scripts.win_add2path import PATH
from appium import webdriver
android_desired_caps = {
            'platformName': 'Android',
            'platformVersion': '8.0',
            'deviceName': 'Android Emulator',
            'automationName': 'UiAutomator2',
            'app': PATH('/path/to/app'),
            'skipServerInstallation': True  # 解决重复安装的问题
            }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', android_desired_caps)


#python IOS 篇
from appium import webdriver
ios_desired_caps = {
    "platformName": "ios",
    "platformVersion": "13.3",
    "app": "/Users/lileilei/Library/Developer/Xcode/DerivedData/KnowingLife-algbavbxvxbalpfghgvtdxzyehwr/Build/Products/Debug-iphonesimulator/KnowingLife.app",
    "automationName": "XCUITest",
    "udid": "6A367568-AE13-49A0-BEE2-3B1AD623AB3E",
    "deviceName": "iPhone 11 Pro Max"
}
driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', ios_desired_caps)