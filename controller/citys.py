#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from core.logger import logger
from core.base_controller import BaseHandler
from core.DB import DBSession
from models.citys import Citys

class CitysHandler(BaseHandler):
    def get(self, *args, **kwargs):
        logger.info('this is in CitysHandler')
        session = DBSession()
        citys_set = session.query(Citys).all()
        session.close()
        citys_list = []
        for i in citys_set:
            item = {
                "id":i.ID,
                "city_name":i.name,
                "city_pre":i.PyPre,
                "city_pinyin":i.py,
            }
            citys_list.append(item)
        data = {
            "citys": citys_list
        }
        self.JsonResponse(data)