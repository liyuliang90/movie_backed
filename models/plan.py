#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Date, Time
from core.DB import Base


class PlanMovie(Base):
    __tablename__ = 'plan_movie'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    CinemaId = Column(String(16), name='cinema_id', nullable=False)
    MovieId = Column(String(16), name='movie_id', nullable=True)
    
class PlanMovieDate(Base):
    __tablename__ = 'plan_movie_date'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    PlanMovieId = Column(String(16), name='plan_movie_id', nullable=False)
    ShowDate = Column(Date, name='showdate', nullable=False)
    
class Plan(Base):
    __tablename__ = 'plan'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    pmdId = Column(String(16), name='pmd_id', nullable=False)
    seqNo = Column(String(16), name='seqNo', nullable=False, unique=True)
    dt = Column(Date, name='dt', nullable=False)
    tm = Column(Time, name='tm', nullable=False)
    th = Column(String(32), name='th', nullable=False)#厅名字
    lang = Column(String(8), name='lang', nullable=False)
    tp = Column(String(8), name='tp', nullable=False)
    vipPrice = Column(String(8), name='vipPrice', nullable=False)
    vipPriceName = Column(String(8), name='vipPriceName', nullable=False)
    vipPriceNameNew = Column(String(8), name='vipPriceNameNew', nullable=False)
    extraDesc = Column(String(64), name='extraDesc', nullable=False)