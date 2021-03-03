#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

import os
import sys
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from core.DB import DBSession
from get_cinemas import get
from models.citys import Citys

def get_all_cinema():
    session = DBSession()
    city_set = session.query(Citys).all()
    session.close()
    for i in city_set:
       print(i.ID)
   
if __name__ == '__main__':
    get_all_cinema()
