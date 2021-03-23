# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/14
@Auth ： zhangqimin
@File ：login_page.py
@IDE ：PyCharm

"""
from selenium.webdriver.remote.webdriver import WebDriver
from appium.webdriver.common.mobileby import MobileBy
from wx_appium_demo.page.base_page import BasePage
from wx_appium_demo.page.choose_clazz_plan import ChooseClazzPage


# 登录页面


class LoginPage(BasePage):
    # def __init__(self, driver:WebDriver):
    #     self.driver = driver

    def login_verify_code(self):
        '''
        登录页面
        '''
        input_phone = 'com.zy.course:id/edit_content'
        self.find(*self.input_phone).clear()
        self.find(*self.input_phone).send_keys('13710825221')
        input_code = 'com.zy.course:id/edit_text'
        self.find(*self.input_code).send_keys('11111')
        #键盘遮挡按钮
        login_button = 'com.zy.course:id/btn_login'
        self.find(*self.login_button).click()

        #权限弹窗
        right_propmt = 'com.zy.course:id/btn_bottom'
        self.find(*self.right_propmt).click()

        #允许权限勾选
        always_allow_first = 'com.android.packageinstaller:id/permission_allow_button'
        for i in range(3):
            self.find(*self.always_allow_first).click()

        return ChooseClazzPage(self.driver)

if __name__ == '__main__':
    case = LoginPage()
    case.login_verify_code()