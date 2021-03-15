#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean
from core.DB import Base

class Movie(Base):
    __tablename__ = 'movie'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(32), name='name', nullable=False)
    enm = Column(String(32), name='enm', nullable=True)#
    Star = Column(String(32), name='star', nullable=False)
    Director = Column(String(64), name='director', nullable=False)
    rt = Column(String(16), name='rt', nullable=False)
    img = Column(String(128), name='img', nullable=False)
    version = Column(String(64), name='version', nullable=True)
    sc = Column(String(8), name='sc', nullable=True)
    globalReleased = Column(Boolean, name='globalReleased', nullable=True)
    snum = Column(String(8), name='snum', nullable=True)#
    cat = Column(String(16), name='cat', nullable=True)#
    wish = Column(String(16), name='wish', nullable=True)
    showInfo = Column(String(32), name='showInfo', nullable=True)
    showst = Column(Integer, name='showst', nullable=True)
    wishst = Column(String(16), name='wishst', nullable=True)
    showCinemaNum = Column(Integer, name='showCinemaNum', nullable=True)
    dur = Column(String(8), name='dur', nullable=False)
    desc = Column(String(64), name='desc', nullable=True)
    dra = Column(Text, name='dra', nullable=True)
    videoImg = Column(String(128), name='videoImg', nullable=True)
    pubDesc = Column(String(64), name='pubDesc', nullable=True)
    src =  Column(String(16), name='src', nullable=True)

