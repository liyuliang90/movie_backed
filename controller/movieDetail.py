#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from core.logger import logger
from core.base_controller import BaseHandler

movie_detail = {
    'id':'',
    'img':'',
    'nm':'',
    'enm':'',
    'globalReleased':'',
    'sc':'',
    'stars':['img',],
    'index':'',
    'snum':'',
    'wish':'',
    'cat':'',
    'version':'',
    'src':'',
    'dur':'',
    'pubDesc':'',
    'dra':'',
    'videoImg':'',
    'photos':[],
    'rt':'',
    'onSale':'',
}

movie_detail3 = {
'detailMovie':{
    'id':1299372,
    'img':"http://p0.meituan.net/w.h/movie/48774506dc0e68805bc25d2cd087d1024316392.jpg",
    'nm':"你好，李焕英",
    'enm':"Hi, Mom",
    'globalReleased':True,
    'sc':9.5,
    'stars':["贾玲","张小斐","沈腾"],
    'index':'',
    'snum':2041921,
    'wish':1162302,
    'cat':"喜剧,剧情",
    'version':'',
    'src':"中国大陆",
    'dur':128,
    'pubDesc':"2021-02-12 08:00中国大陆上映",
    'dra':"2001年的某一天，刚刚考上大学的贾晓玲（贾玲 饰）经历了人生中的一次大起大落。一心想要成为母亲骄傲的她却因母亲突遭严重意外，而悲痛万分。在贾晓玲情绪崩溃的状态下，竟意外的回到了 1981 年，并与年轻的母亲李焕英（张小斐 饰）相遇，二人形影不离，宛如闺蜜。与此同时，也结识了一群天真善良的好朋友。晓玲以为来到了这片“广阔天地”，她可以凭借自己超前的思维，让母亲“大有作为”，但结果却让晓玲感到意外......",
    'videoImg':"https://obj.pipi.cn/friday/1f86441c20352124029f9733f766112a.jpeg",
    'photos':["http://p1.meituan.net/w.h/movie/d98dc4b1c0d71418c21d8c6605621e96369894.jpg",
                "http://p0.meituan.net/w.h/movie/f3aa4b07a7c1154f2bbaedda70ccfbab929368.jpg",
                "http://p0.meituan.net/w.h/movie/afd3c374050b440800afaf66b08b8348792642.jpg",
                "http://p0.meituan.net/w.h/movie/377a9b6d99ef2d5d6810e8e32cdeba353404715.jpg",
                "http://p0.meituan.net/w.h/movie/2465fbb62f8250d02552e1dce30ead331015459.jpg",
                "http://p1.meituan.net/w.h/movie/b3bee04d5889113777a123559fc0fc2f720116.jpg",
                "http://p1.meituan.net/w.h/movie/6a4e59a6ee1b42fe96ad70a714f31e221091878.jpg",
                "http://p1.meituan.net/w.h/movie/4c718dc3333a32d37d86131ddd400b961166832.jpg",
                "http://p0.meituan.net/w.h/movie/fbed1525e1eb86bf525709b80753b275221795.jpg",
                "http://p0.meituan.net/w.h/movie/253737fff1f3d50fe4f7e473cf8e69ce1025674.jpg",
                "http://p1.meituan.net/w.h/movie/b1645b532a150c2081e9ce6fe3164aa6840099.jpg",
                "http://p0.meituan.net/w.h/movie/41e926fe19e54b90434d77cd63e218a9884044.jpg",
                "http://p0.meituan.net/w.h/movie/d4e43e2efe5990c756b9e7df2235d8eb997053.jpg",
                "http://p0.meituan.net/w.h/mmdb/5c23189671b67255e3946b0d634ee0a51140783.jpg",
                "http://p0.meituan.net/w.h/mmdb/b17b3267e6548695e267e8e16c2721e31197683.jpg",
                "http://p0.meituan.net/w.h/movie/78a34193464041af6697fcd57c295e60972801.jpg",
                "http://p0.meituan.net/w.h/movie/2522482e487756a2cfc0b630a6f4b21d725587.jpg",
                "http://p0.meituan.net/w.h/movie/74ec9c19fe940552bb520c34375b1166989493.jpg",
                "http://p1.meituan.net/w.h/movie/82a99ce6ab861480aa9b7413db2a806a858478.jpg",
                "http://p0.meituan.net/w.h/movie/eccd6cf929684d9682ac4bc9cab7cf3d571744.jpg"
                    ],
    'rt':"2021-02-12",
    'onSale':True,
}}

movie_detail2 = {
    "data":{
        "movie":{
            "albumImg":"http://p0.meituan.net/moviemachine/223a025c08f587dcdb96e99b9c6626826718072.jpg",
            "availableEpisodes":0,
            "awardUrl":"",
            "backgroundColor":"#662E29",
            "bingeWatch":0,
            "bingeWatchst":0,
            "cat":"喜剧,剧情",
            "comScorePersona":True,
            "commented":False,
            "dir":"贾玲",
            "distributions":[
                {
                    "movieScoreLevel":"9-10分",
                    "proportion":"87.69"
                },
                {
                    "movieScoreLevel":"5-8分",
                    "proportion":"10.06"
                },
                {
                    "movieScoreLevel":"1-4分",
                    "proportion":"2.25"
                }
            ],
            "dra":"2001年的某一天，刚刚考上大学的贾晓玲（贾玲 饰）经历了人生中的一次大起大落。一心想要成为母亲骄傲的她却因母亲突遭严重意外，而悲痛万分。在贾晓玲情绪崩溃的状态下，竟意外的回到了 1981 年，并与年轻的母亲李焕英（张小斐 饰）相遇，二人形影不离，宛如闺蜜。与此同时，也结识了一群天真善良的好朋友。晓玲以为来到了这片“广阔天地”，她可以凭借自己超前的思维，让母亲“大有作为”，但结果却让晓玲感到意外......",
            "dur":128,
            "egg":False,
            "enm":"Hi, Mom",
            "episodeDur":128,
            "episodes":0,
            "globalReleased":True,
            "guideToWish":False,
            "id":1299372,
            "img":"http://p0.meituan.net/w.h/movie/48774506dc0e68805bc25d2cd087d1024316392.jpg",
            "latestEpisode":0,
            "modcsSt":False,
            "movieType":0,
            "multiPub":False,
            "musicName":"依兰爱情故事",
            "musicNum":4,
            "musicStar":"方磊;贾玲",
            "nm":"你好，李焕英",
            "onSale":True,
            "onlinePlay":False,
            "orderSt":0,
            "oriLang":"国语",
            "photos":[
                "http://p1.meituan.net/w.h/movie/d98dc4b1c0d71418c21d8c6605621e96369894.jpg@2500w_2500h_1l_0e",
                "http://p0.meituan.net/w.h/movie/f3aa4b07a7c1154f2bbaedda70ccfbab929368.jpg@2500w_2500h_1l_0e",
                "http://p0.meituan.net/w.h/movie/afd3c374050b440800afaf66b08b8348792642.jpg@2500w_2500h_1l_0e",
                "http://p0.meituan.net/w.h/movie/377a9b6d99ef2d5d6810e8e32cdeba353404715.jpg@2500w_2500h_1l_0e",
                "http://p0.meituan.net/w.h/movie/2465fbb62f8250d02552e1dce30ead331015459.jpg@2500w_2500h_1l_0e",
                "http://p1.meituan.net/w.h/movie/b3bee04d5889113777a123559fc0fc2f720116.jpg@2500w_2500h_1l_0e",
                "http://p1.meituan.net/w.h/movie/6a4e59a6ee1b42fe96ad70a714f31e221091878.jpg@2500w_2500h_1l_0e",
                "http://p1.meituan.net/w.h/movie/4c718dc3333a32d37d86131ddd400b961166832.jpg@2500w_2500h_1l_0e",
                "http://p0.meituan.net/w.h/movie/fbed1525e1eb86bf525709b80753b275221795.jpg@2500w_2500h_1l_0e",
                "http://p0.meituan.net/w.h/movie/253737fff1f3d50fe4f7e473cf8e69ce1025674.jpg@2500w_2500h_1l_0e",
                "http://p1.meituan.net/w.h/movie/b1645b532a150c2081e9ce6fe3164aa6840099.jpg@2500w_2500h_1l_0e",
                "http://p0.meituan.net/w.h/movie/41e926fe19e54b90434d77cd63e218a9884044.jpg@2500w_2500h_1l_0e",
                "http://p0.meituan.net/w.h/movie/d4e43e2efe5990c756b9e7df2235d8eb997053.jpg@2500w_2500h_1l_0e",
                "http://p0.meituan.net/w.h/mmdb/5c23189671b67255e3946b0d634ee0a51140783.jpg",
                "http://p0.meituan.net/w.h/mmdb/b17b3267e6548695e267e8e16c2721e31197683.jpg",
                "http://p0.meituan.net/w.h/movie/78a34193464041af6697fcd57c295e60972801.jpg@2500w_2500h_1l_0e",
                "http://p0.meituan.net/w.h/movie/2522482e487756a2cfc0b630a6f4b21d725587.jpg@2500w_2500h_1l_0e",
                "http://p0.meituan.net/w.h/movie/74ec9c19fe940552bb520c34375b1166989493.jpg@2500w_2500h_1l_0e",
                "http://p1.meituan.net/w.h/movie/82a99ce6ab861480aa9b7413db2a806a858478.jpg@2500w_2500h_1l_0e",
                "http://p0.meituan.net/w.h/movie/eccd6cf929684d9682ac4bc9cab7cf3d571744.jpg@2500w_2500h_1l_0e"
            ],
            "pn":82,
            "preScorePersona":False,
            "proScore":0,
            "proScoreNum":1,
            "pubDate":1613059200000,
            "pubDesc":"2021-02-12 08:00中国大陆上映",
            "rt":"2021-02-12",
            "sc":9.5,
            "scm":"穿越遇见妈，重新选个爸",
            "scoreLabel":"猫眼购票评分",
            "shareInfo":{
                "channel":1,
                "content":"简介|2001年的某一天，刚刚考上大学的贾晓玲（贾玲 饰）经历了人生中的一次大起大落。一心想要成为母亲骄傲的她却因母亲突遭严重意外，而悲痛万分。在贾晓玲情绪崩溃的状态下，竟意外的回到了 1981 年，并与年轻的母亲李焕英（张小斐 饰）相遇，二人形影不离，宛如闺蜜。与此同时，也结识了一群天真善良的好朋友。晓玲以为来到了这片“广阔天地”，她可以凭借自己超前的思维，让母亲“大有作为”，但结果却让晓玲感到意外......",
                "img":"http://p0.meituan.net/w.h/movie/48774506dc0e68805bc25d2cd087d1024316392.jpg",
                "title":"《你好，李焕英》猫眼购票评分9.5，2021-02-12 08:00中国大陆上映",
                "url":"https://m.maoyan.com/asgard/movie/1299372"
            },
            "showst":3,
            "snum":2041921,
            "src":"中国大陆",
            "star":"贾玲,张小斐,沈腾",
            "type":0,
            "vd":"https://vod.pipi.cn/43903a81vodtransgzp1251246104/133f0ba05285890812700936200/v.f42905.mp4",
            "ver":"2D/中国巨幕2D/CINITY 2D/杜比影院 2D/全景声",
            "videoImg":"https://obj.pipi.cn/friday/1f86441c20352124029f9733f766112a.jpeg",
            "videoName":"《你好，李焕英》“我能让你更高兴”版预告",
            "videourl":"https://vod.pipi.cn/43903a81vodtransgzp1251246104/133f0ba05285890812700936200/v.f42905.mp4",
            "viewedSt":0,
            "vnum":17,
            "vodFreeSt":0,
            "vodPlay":False,
            "vodSt":0,
            "watched":111075795,
            "wish":1162302,
            "wishst":0
        }
    }
}
class MovieDetailHandler(BaseHandler):
    def get(self, *args, **kwargs):
        logger.info('this is in CinemaHandler')
        self.JsonResponse(movie_detail3)
