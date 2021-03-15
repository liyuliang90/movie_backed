#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

import os
import sys
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)

from core.DB import DBSession
from get_movieDetail import get
from models.movie import Movie

def get_all_movie():
    session = DBSession()
    movie_set = session.query(Movie).all()
    session.close()
    for i in movie_set:
       print(i.ID)
       get(i.ID)
   
if __name__ == '__main__':
    get_all_movie()
