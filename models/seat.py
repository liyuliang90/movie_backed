#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from core.DB import Base

class Seat(Base):
    __tablename__ = 'seat'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    seatNo = Column(String(32), name='seatNo', nullable=True)
    columnId = Column(String(16), name='columnId', nullable=True)
    rowId = Column(String(16), name='rowId', nullable=False)
    seatStatus = Column(Integer, name='seatStatus', nullable=False)
    seatType = Column(String(16), name='seatType', nullable=True)
    seationId = Column(String(16), name='seationId', nullable=True)