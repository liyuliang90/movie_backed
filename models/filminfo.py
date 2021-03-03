#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from core.DB import Base

class FilmInfo(Base):
    __tablename__ = 'filminfo'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    like = Column(String(32), name='like', nullable=False)
    publishDate = Column(DateTime, name='publishDate', nullable=False)
    publish_date = Column(DateTime, name='publish_date', nullable=False)
    showStatus = Column(String(16), name='showStatus', nullable=False)
    pic = Column(String(128), name='pic', nullable=False)
    cast = Column(String(64), name='cast', nullable=False)
    filmId = Column(String(16), name='filmId', nullable=False)
    film_id = Column(String(16), name='film_id', nullable=False)
    grade = Column(String(16), name='grade', nullable=False)
    name = Column(String(32), name='name', nullable=False)

