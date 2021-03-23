# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/14
@Auth ： zhangqimin
@File ：test_contact.py
@IDE ：PyCharm

"""
from wx_appium_demo.page.app import App

class TestWX:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def test_addcontact(self):
        name = "hogwarts_00004"
        gender = "男"
        phonenum = "13812121215"

        result = self.main.goto_contactlist(). \
            add_member().add_member_manul(). \
            edit_contact(name, gender, phonenum).verify_toast()
        assert '添加成功' == result

    def test_addcontact1(self):
        name = "hogwarts_00003"
        gender = "男"
        phonenum = "13812121214"

        result = self.main.goto_contactlist(). \
            add_member().add_member_manul(). \
            edit_contact(name, gender, phonenum).verify_toast()
        assert '添加成功' == result

    def teardown_class(self):
        self.app.stop()

