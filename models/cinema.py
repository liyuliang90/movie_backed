#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from core.DB import Base

class Cinema(Base):
    __tablename__ = 'cinema'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    cinemaId = Column(String(32), name='cinema_id', nullable=False)
    cityId = Column(String(32), name='cityId', nullable=False)
    name = Column(String(32), name='name', nullable=False)
    addr = Column(String(64), name='addr', nullable=False)
    lat = Column(String(32), name='lat', nullable=False)
    lng = Column(String(32), name='lng', nullable=False)
    poiId = Column(String(32), name='poiId', nullable=False)
    shopId = Column(String(32), name='shopId', nullable=False)

