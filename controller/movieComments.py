#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from core.logger import logger
from core.base_controller import BaseHandler

comments = {
    'total':'',
    'hcmts':[],
    'id':'',
}
class MovieCommentHandler(BaseHandler):
    def get(self, *args, **kwargs):
        logger.info('this is in CinemaHandler')
        self.JsonResponse(comments)
