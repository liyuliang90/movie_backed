#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

import os
import sys
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)

from core.DB import DBSession, db_save
from get_cinemas import get
from models.cinema  import Cinema, CinemaGeo

def get_all_cinema():
    session = DBSession()
    cinema_set = session.query(Cinema).all()
    session.close()
    for i in cinema_set[:100]:
       print(i.ID)
       a = CinemaGeo()
       #a.geom = 'POINT(108.949871515 34.25416521)'
       a.geom = 'POINT(%s %s)' % (i.lng,i.lat)
       db_save(a)
   
if __name__ == '__main__':
    get_all_cinema()
