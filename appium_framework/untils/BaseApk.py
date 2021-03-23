# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/14
@Auth ： zhangqimin
@File ：BaseApk.py
@IDE ：PyCharm

"""
import re
import subprocess
import os
from appium_framework.untils.log import LOG,logger
'''
apk文件的读取信息
'''

class ApkInfo():
    def __init__(self, apkPath):
        self.apkPath = apkPath

    def getApkBaseInfo(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        print(p)
        (output, err) = p.communicate()
        match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output.decode())
        if not match:
            raise Exception("can't get packageinfo")
        packagename = match.group(1)
        appKey = match.group(2)
        appVersion = match.group(3)
        LOG.info("=====getApkInfo=========")
        LOG.info('packageName:', packagename)
        LOG.info('appKey:', appKey)
        LOG.info('appVersion:', appVersion)
        return packagename, appKey, appVersion

    #得到启动类
    def getApkActivity(self):
        p =subprocess.Popen("aapt dump badging %s" % self.apkPath,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE,shell=True)
        (output, err) = p.communicate()
        match = re.compile("luanchable-activity:name=(\S+)").search(output.decode())
        if match is not None:
            return match.group(1)

    #得到应用名字
    def getApkName(self):
        cmd = "aapt dump bading " + self.apkPath + " | grep application-label:"
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output,err) = p.communicate()
        if output!="":
            result = output.split()[0].decode()[19:-1]
        return result




if __name__ == '__main__':
    apkPath = "D:\gitPersonal\appium_demo\appium_method\app\course-debug-3.5.1.apk"
    case = ApkInfo(apkPath)
    # case.getApkNamekBaseInfo()
    case.getApkName()
    case.getApkActivity()