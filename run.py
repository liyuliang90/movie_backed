#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

import os
import tornado.ioloop
from router.router import Router

if __name__ == '__main__':
    settings = dict(
        static_path = os.path.join(os.path.dirname(__file__), "statics"),           #配置应用程序前端所需静态文件目录
        template_path = os.path.join(os.path.dirname(__file__), "templates"),       #配置html文件路径
        login_url='/login',                                                         #配置登录url
        xsrf_cookies=False,                                                          #,防止跨站请求攻击，在post请求中起效,
        cookie_secret="2hcicVu+TqShDpfsjMWQLZ0Mkq5NPEWSk9fi0zsSt3A=",               # 安全cookie用预置秘钥 base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
        debug = True   
    )
    app = tornado.web.Application(Router, **settings)
    http_server = tornado.httpserver.HTTPServer(app)                                #将应用处理逻辑 传递给HTTPServer 服务                                        #设置一个监听地址
    http_server.listen(8000)                                                #配置监听地址到 HTTPServe
    tornado.ioloop.IOLoop.current().start()
