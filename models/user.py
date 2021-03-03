#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from sqlalchemy import Column, Integer, String, Float
from core.DB import Base

class User(Base):
    __tablename__ = 'user'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), name='name', nullable=False)
    passwd = Column(String(32), name='passwd', nullable=False)
