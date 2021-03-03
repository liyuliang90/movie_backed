#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from tornado.web import url
from controller.index import IndexHandler


Router = [
    url(r"/ajax/movieOnInfoList", IndexHandler),
]
