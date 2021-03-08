#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from core.DB import Base

class CityBrand(Base):
    __tablename__ = 'city_brand'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    CityId = Column(String(32), name='city_id', nullable=False)
    Name = Column(String(32), name='name', nullable=False)
    Count = Column(String(32), name='count', nullable=False)

class CityDistrict(Base):
    __tablename__ = 'city_district'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    CityId = Column(String(32), name='city_id', nullable=False)
    Name = Column(String(32), name='name', nullable=False)
    Count = Column(String(32), name='count', nullable=False)

class CityDistrictSub(Base):
    __tablename__ = 'city_district_sub'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    DistrictId = Column(String(32), name='district_id', nullable=False)
    Name = Column(String(32), name='name', nullable=False)
    Count = Column(String(32), name='count', nullable=False)
    
class CitySubway(Base):
    __tablename__ = 'city_subway'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    CityId = Column(String(32), name='city_id', nullable=False)
    Name = Column(String(32), name='name', nullable=False)
    Count = Column(String(32), name='count', nullable=False)
    
class CitySubwayStation(Base):
    __tablename__ = 'city_subway_station'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    SubwayId = Column(String(32), name='subway_id', nullable=False)
    Name = Column(String(32), name='name', nullable=False)
    Count = Column(String(32), name='count', nullable=False)