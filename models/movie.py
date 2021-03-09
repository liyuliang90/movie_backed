#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean
from core.DB import Base

class Movie(Base):
    __tablename__ = 'movie'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(32), name='name', nullable=False)
    Star = Column(String(32), name='star', nullable=False)
    Director = Column(String(64), name='director', nullable=False)
    rt = Column(String(16), name='rt', nullable=False)
    img = Column(String(128), name='img', nullable=False)
    version = Column(String(64), name='version', nullable=True)
    sc = Column(String(8), name='sc', nullable=True)
    globalReleased = Column(Boolean, name='globalReleased', nullable=True)
    wish = Column(String(16), name='wish', nullable=True)
    showInfo = Column(String(32), name='showInfo', nullable=True)
    showst = Column(Integer, name='showst', nullable=True)
    wishst = Column(String(16), name='wishst', nullable=True)
    showCinemaNum = Column(Integer, name='showCinemaNum', nullable=True)

