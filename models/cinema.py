#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from sqlalchemy import Column, Integer, String, Float, DateTime, Text, DECIMAL
from sqlalchemy import func, Computed
from sqlalchemy.types import UserDefinedType
from core.DB import Base

class Geometory(UserDefinedType):
    def get_col_spec(self):
        return "GEOMETRY"

    def bind_expression(self, bindvalue):
        return func.GeomFromText(bindvalue, type_=self)

    def column_expression(self, col):
        return func.ASTEXT(col, type_=self)

class Cinema(Base):
    __tablename__ = 'cinema'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    cityId = Column(String(8), name='cityId', nullable=False)
    districtId = Column(String(32), name='districtId', nullable=True)
    name = Column(String(32), name='name', nullable=False)
    addr = Column(String(128), name='addr', nullable=False)
    lat = Column(String(32), name='lat', nullable=False)
    lng = Column(String(32), name='lng', nullable=False)
    poiId = Column(String(32), name='poiId', nullable=False)
    shopId = Column(String(32), name='shopId', nullable=False)
    endorse = Column(Integer, name='endorse', nullable=True)
    allowRefund = Column(Integer, name='allowRefund', nullable=True)
    snack = Column(Integer, name='snack', nullable=True)
    hallType = Column(String(32), name='hallType', nullable=True)
    vipDesc = Column(String(64), name='vipDesc', nullable=True)
    showTimes = Column(String(8), name='showTimes', nullable=True)
    cardPromotionTag = Column(String(64), name='cardPromotionTag', nullable=True)
    gis = Column(Geometory, name='gis', comment='经纬度', nullable=True)
    geoHash = Column(String(50), Computed("st_geohash(`gis`,8)"), index=True)
