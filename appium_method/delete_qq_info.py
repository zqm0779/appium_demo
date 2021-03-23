# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/11
@Auth ： zhangqimin
@File ：delete_qq_info.py
@IDE ：PyCharm

"""
#appium操作qq，实现滑动删除消息。
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '8DF6R17209001170'
desired_caps['preformVersion'] = '8.0'
desired_caps['appPackage'] = 'com.tencent.mobileqq'
desired_caps['appActivity'] = '.activity.SplashActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
sleep(10)
#滑动消息到能看到删除操作
TouchAction(driver).press(x=250, y=250).wait(1000).move_to(x=5,y=235).release().perform()
sleep(6)
#操作删除，QQ消息被删
driver.find_element_by_xpath('//android.view.View[@content-desc=\"删除\"]').click()
