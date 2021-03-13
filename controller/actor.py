#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from core.logger import logger
from core.base_controller import BaseHandler
from core.DB import DBSession
from models.star import Actor

class ActorHandler(BaseHandler):
    def get(self, *args, **kwargs):
        logger.info('this is in CitysHandler')
        movie_id = self.get_argument('movie_id',0)
        if not movie_id:
            data = {'success':False}
            self.JsonResponse(data)
            return 
        session = DBSession()
        actor_set = session.query(Actor).filter(Actor.MovieId==movie_id).all()
        session.close()
        actor_list = []
        for i in actor_set:
            item = {
                "id":i.PersonId,
                'avatar':i.avatar.replace('w.h','80.128'),
                "name":i.Name,
                'cr': i.cr,
                'desc': i.desc,
                'roles': i.roles,
            }
            actor_list.append(item)
        data = {
            'success': True,
            "actor": actor_list
        }
        self.JsonResponse(data)