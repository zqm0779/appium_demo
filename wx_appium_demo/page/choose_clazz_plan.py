# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/14
@Auth ： zhangqimin
@File ：choose_clazz_plan.py
@IDE ：PyCharm

"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from wx_appium_demo.page.base_page import BasePage
# from wx_appium_demo.page.member_invite_page import MemberInviteMenuPage

# 通讯录页面
'''
编辑联系人页面
'''
class ChooseClazzPage(BasePage):
    # def __init__(self, driver:WebDriver):
    #     self.driver = driver
    #进入选课页面
    def enter_choose_clazz(self):
        choose_clazz_tag = 'com.zy.course:id/img_tap_icon'
        self.find(*self.choose_clazz_tag).click()
        # return MemberInviteMenuPage(self.driver)