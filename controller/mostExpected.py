#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from core.logger import logger
from core.base_controller import BaseHandler
from core.DB import DBSession
from models.movie import Movie

result = {
    "coming":[
        {
            "id":1229308,
            "img":"http://p0.meituan.net/w.h/movie/fb5cf831b50e845121fd207b01c066801817376.jpg",
            "wish":73806,
            "wishst":0,
            "nm":"第十一回",
            "comingTitle":"4月2日 周五"
        },
        {
            "id":1212538,
            "img":"http://p1.meituan.net/w.h/movie/b7383bb5a78d70f0a1ef35b4b0f295f43266884.jpg",
            "wish":39256,
            "wishst":0,
            "nm":"合法伴侣",
            "comingTitle":"3月12日 周五"
        },
        {
            "id":345006,
            "img":"http://p0.meituan.net/w.h/movie/8e5dadbb51a762ac594407d42e77f5fc2698011.jpg",
            "wish":160860,
            "wishst":0,
            "nm":"西游记之再世妖王",
            "comingTitle":"4月2日 周五"
        },
        {
            "id":343568,
            "img":"http://p0.meituan.net/w.h/moviemachine/58732574fbc2f64c04c3e825c058da7f16742753.jpg",
            "wish":164415,
            "wishst":0,
            "nm":"哥斯拉大战金刚",
            "comingTitle":"3月26日 周五"
        },
        {
            "id":1222234,
            "img":"http://p0.meituan.net/w.h/movie/e2ecb7beb8dadc9f07f2fad9820459f92275588.jpg",
            "wish":194007,
            "wishst":0,
            "nm":"我的姐姐",
            "comingTitle":"4月2日 周五"
        },
        {
            "id":1320283,
            "img":"http://p0.meituan.net/w.h/movie/1c4745fb09d88a8531ab62cebd573b782177426.jpg",
            "wish":178759,
            "wishst":0,
            "nm":"你的婚礼",
            "comingTitle":"5月20日 周四"
        },
        {
            "id":1359285,
            "img":"http://p1.meituan.net/w.h/moviemachine/e13580e0f2ab15df84389243af31722610557797.png",
            "wish":57258,
            "wishst":0,
            "nm":"世间有她",
            "comingTitle":"4月30日 周五"
        },
        {
            "id":1322057,
            "img":"http://p1.meituan.net/w.h/movie/2659af22eee890e9c2da77c03617757f2588432.jpg",
            "wish":19409,
            "wishst":0,
            "nm":"明天会好的",
            "comingTitle":"4月2日 周五"
        },
        {
            "id":1241385,
            "img":"http://p0.meituan.net/w.h/movie/5c63513c7545c15ae829bc786305976a4866588.jpg",
            "wish":115909,
            "wishst":0,
            "nm":"秘密访客",
            "comingTitle":"5月1日 周六"
        },
        {
            "id":1212303,
            "img":"http://p0.meituan.net/w.h/movie/addd3573cf7266d3ca54887bdb00bb192164382.jpg",
            "wish":78075,
            "wishst":0,
            "nm":"古董局中局",
            "comingTitle":"4月30日 周五"
        }
    ],
    "paging":{
        "hasMore":True,
        "limit":10,
        "offset":0,
        "total":43
    }
}

class MostExpectedHandler(BaseHandler):
    def get(self, *args, **kwargs):
        logger.info('this is in MostExpectedHandler')
        
        self.JsonResponse(result)