#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from core.DB import Base

class Citys(Base):
    __tablename__ = 'citys'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), name='nm', nullable=False)
    py = Column(String(32), name='py', nullable=False)

