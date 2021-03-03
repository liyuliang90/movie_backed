#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from core.DB import Base

class Test(Base):
    __tablename__ = 'test'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    like = Column(String(32), name='like', nullable=False)
    director = Column(String(32), name='director', nullable=True)
    publishDate = Column(DateTime, name='publishDate', nullable=False)
    versionTypes = Column(String(32), name='versionType', nullable=False)
    language = Column(String(32), name='language', nullable=False)
    pic = Column(String(128), name='pic', nullable=False)
    filmTypes = Column(String(64), name='filmTypes', nullable=False)
    duration = Column(String(16), name='duration', nullable=False)
    cast = Column(String(64), name='cast', nullable=False)
    filmId = Column(String(16), name='filmId', nullable=False)
    grade = Column(String(16), name='grade', nullable=False)
    intro = Column(Text, name='intro', nullable=False)
    name = Column(String(32), name='name', nullable=False)

