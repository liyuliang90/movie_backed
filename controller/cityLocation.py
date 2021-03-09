#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from core.logger import logger
from core.base_controller import BaseHandler
from core.DB import DBSession
from models.citys import Citys

class CityLocationHandler(BaseHandler):
    def get(self, *args, **kwargs):
        logger.info('this is in CityLocationHandler')
        city_name = self.get_argument('city_name')
        session = DBSession()
        city = session.query(Citys).filter(Citys.name==city_name).first()
        session.close()
        data = {'success': False}
        if city:
            data['success'] = True
            data['city_id'] = city.ID
        self.JsonResponse(data)