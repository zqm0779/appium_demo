# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/14
@Auth ： zhangqimin
@File ：app.py
@IDE ：PyCharm

"""
# app.py 存放app相关的操作，启动app, 关闭app, 启动app, 进入到主页
from appium import webdriver
from wx_appium_demo.page.base_page import BasePage
from wx_appium_demo.page.main_page import MainPage

class App(BasePage):
    def start(self):
        if self.driver == None:
            print("driver == None")
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "8DF6R17209001170"
            caps["appPackage"] = "com.zy.course"
            caps["appActivity"] = "com.zy.course.base.FragmentContainerActivity"
            caps["noReset"] = "True"
            '''
            要屏蔽软键盘，只需在desired_caps{}设置里面加上两个参数
            caps['unicodeKeyboard']='True'
            caps['resetKeyboard']='True'
            unicodeKeyboard是使用unicode编码方式发送字符串
            resetKeyboard是将键盘隐藏起来
            '''
            caps['unicodeKeyboard'] = 'True'
            caps['resetKeyboard'] = 'True'
            # 最重要的代码，建立客户端与服务端的连接
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            print("driver is not None")
            # 启动app, 启动的页面是desirecaps 里面设置的activity
            self.driver.launch_app()
            # self.driver.start_activity("com.tencent.wework",".launch.LaunchSplashActivity")
        return self

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)

if __name__ == '__main__':
    case = App()
    case.start().goto_main()