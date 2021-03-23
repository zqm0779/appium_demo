# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/11
@Auth ： zhangqimin
@File ：config.py
@IDE ：PyCharm

"""
'''
配置app以及测试设备的相关信息
'''
TestappPackage = 'com.hotbitmapgg.ohmybilibili'  # 被测应用名称

TestAppActivity = "com.hotbitmapgg.bilibili.module.common.SplashActivity"
TestandroidDeviceReadyTimeout = 30  # 超时时间
TestunicodeKeyboard = True
TestresetKeyboard = True
Dingtalk_access_token = ''  # 钉钉的token
Test_Project_name = ''
TiTestuser = ''
Test_user = "自动化"

testversion="2.0.0"  #测试的版本


TestIosApkPath="/Users/lileilei/Library/Developer/Xcode/DerivedData/KnowingLife-algbavbxvxbalpfghgvtdxzyehwr/Build/Products/Debug-iphonesimulator/KnowingLife.app"


Test_plan_num = 2  # 测试设备数量
Test_stf_plan = "http://localhost:7100"  # stf设备管理平台

Test_mobile_type = "Android"  # 测试设备类型。ios


Test_stf_token = '53672d758d904c9d97df5675a5f45b558957c1163c0c4397bd2dde2adcce1d08'  # 远程管理设备的token
