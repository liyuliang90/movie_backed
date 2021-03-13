#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

import json
import datetime
from tornado.web import RequestHandler
from middles import MIDDLEWARE_LIST

from sqlalchemy.ext.declarative import DeclarativeMeta

class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                print(type(data))
                try:
                    print(type(data))
                    if type(data) is datetime.datetime:
                        data = data.strftime("%Y-%m-%d %H:%M:%S")
                    elif type(data) is datetime.date:
                        data = data.strftime("%Y-%m-%d")
                    elif type(data) is datetime.time:
                        data = data.strftime("%H:%M:%S")
                    else:
                        json.dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            return fields

        return json.JSONEncoder.default(self, obj)

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, datetime.time):
            return obj.strftime("%H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)

class BaseHandler(RequestHandler):
    
    #def get_current_user(self):
    #    '''
    #    重写RequestHandler类中的get_current_user方法，用来判断当前是否是登录状态，请求中所有被@tornado.web.authenticated 装饰的方法，都需要此方法返回值不为None，否则给与403拒绝
     #   :return: 用户名或者None . 为None判断为非法请求，POST 时Tornado进行403禁止访问 ；GET 时 302 重定向到/login
     #   '''
    #    user = self.get_argument(name='username',default='None')
    #    if user and user != 'None':
    #        print('IndexHandler类 get_current_user获取到用户:',user)
    #        return user
    '''    
    def initialize(self):
        self.middleware = MIDDLEWARE_LIST
 
    def prepare(self):
        for middleware in self.middleware:
            middleware.process_request(self)
    '''
    def finish(self, chunk=None):
        super(BaseHandler, self).finish(chunk)
 
    def write_error(self, status_code, **kwargs):
        exc_cls, exc_instance, trace = kwargs.get("exc_info")
        if status_code != 200:
            self.set_status(status_code)
            self.write({"msg": str(exc_instance)})
                
    def JsonResponse(self, result):
        self.set_header("Content-Type","application/json;charset=utf-8")
        self.write(json.dumps(result,ensure_ascii=False,cls=DateEncoder))
