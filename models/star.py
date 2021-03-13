#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean
from core.DB import Base

class Director(Base):
    __tablename__ = 'persion_director'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    MovieId = Column(String(16), name='movie_id', nullable=False)
    PersionId = Column(String(16), name='persion_id', nullable=False)
    Name = Column(String(32), name='name', nullable=False)
    avatar = Column(String(128), name='avatar', nullable=False)
    cr = Column(String(8), name='cr', nullable=True)
    desc = Column(String(32), name='desc', nullable=False)
    ocr = Column(String(16), name='ocr', nullable=True)
    roles = Column(String(16), name='roles', nullable=True)
    still = Column(String(128), name='still', nullable=True)

class Actor(Base):
    __tablename__ = 'actor'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    MovieId = Column(String(16), name='movie_id', nullable=False)
    PersonId = Column(String(16), name='person_id', nullable=False)
    Name = Column(String(32), name='name', nullable=False)
    avatar = Column(String(128), name='avatar', nullable=False)
    cr = Column(String(8), name='cr', nullable=True)
    desc = Column(String(32), name='desc', nullable=False)
    ocr = Column(String(16), name='ocr', nullable=True)
    roles = Column(String(16), name='roles', nullable=True)
    still = Column(String(128), name='still', nullable=True)
