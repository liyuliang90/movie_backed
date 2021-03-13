#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

import os
import sys
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)

from core.DB import DBSession
from get_citySection import get
from models.citys import Citys

def get_all_citySection():
    session = DBSession()
    city_set = session.query(Citys).filter(Citys.ID<=486).all()
    session.close()
    for i in city_set:
       print(i.ID)
       get(i.ID)
   
if __name__ == '__main__':
    get_all_citySection()
