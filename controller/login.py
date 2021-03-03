#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from tornado.web import RequestHandler

class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        '''
        处理输入昵称界面get请求
        :param args:
        :param kwargs:
        :return:
        '''
        cookie_value = self.get_secure_cookie('count')
        print('cookie_value :', cookie_value)
        count = int(cookie_value) + 1 if cookie_value else 1
        self.set_secure_cookie("count", str(count))  # 设置一个带签名和时间戳的cookie，防止cookie被伪造。

        #使用ajax方法做的前端
        # self.render('login_use_ajax.html')
        #使用form表单提交数据 的前端
        self.render('login_use_form.html')
    def post(self, *args, **kwargs):
        '''
        暂时用不到
        :param args:
        :param kwargs:
        :return:
        '''
        pass