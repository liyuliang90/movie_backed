#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean
from core.DB import Base

class Photo(Base):
    __tablename__ = 'photo'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    MovieId = Column(String(16), name='movie_id', nullable=False)
    img = Column(String(128), name='img', nullable=False)
