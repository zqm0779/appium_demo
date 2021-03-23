# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/14
@Auth ： zhangqimin
@File ：main_page.py
@IDE ：PyCharm

"""
#主页
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from wx_appium_demo.page.base_page import BasePage
from wx_appium_demo.page.login_page import LoginPage

class MainPage(BasePage):
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver
    def goto_contactlist(self):
        '''
        加载页
        '''
        # 跳过广告页
        jump_adv = 'com.zy.course:id/tv_jump'

        self.find(*self.jump_adv).click()
        #点击登录，跳转到登录页面
        login_button = 'com.zy.course:id/btn_login'
        self.find(*self.login_button).click()

        return LoginPage(self.driver)
