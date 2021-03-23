# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/10
@Auth ： zhangqimin
@File ：get_packageName_activity.py
@IDE ：PyCharm

"""
#pip  install androguard
from androguard.core.bytecodes.apk import APK
import os
parents = os.path.dirname(os.path.abspath(__file__))
app_path = parents + '\\' + 'app' + '\\' +'course-debug-3.5.1.apk'
print(app_path)
#获取包名
def get_apkname(apk):
    a = APK(apk, False, "r")
    return a.get_package()

#获取包的activity
def get_apk_activity(apk):
    a = APK(apk, False, "r")
    return a.get_main_activity()
if __name__ == '__main__':
    apkname = get_apkname(app_path)
    apk_activity = get_apk_activity(app_path)
    print(apkname)
    print(apk_activity)