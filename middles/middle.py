#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

class MiddleWare(object):
    '''
    中间件基类
    '''
    def process_request(self, handler):
        pass
    
class CheckLogin(MiddleWare):
    def is_login(self, handler):
        pwd = handler.get_argument("pwd", "")
        if not pwd:
            raise Exception("login required")
        else:
            return True
 
    def process_request(self, handler):
        self.is_login(handler)
