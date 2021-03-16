#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from .logger import logger
from .config import CONFIG

# 创建对象的基类:
Base = declarative_base()
PrintSql = False #是否打印sql语句

def MysqlConnect(conf):
    #mysql_connect_base = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}?charset={charset}"
    mysql_connect_base = "mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset={charset}"
    mysql_connect = mysql_connect_base.format(**mysql_config)
    # 初始化数据库连接:
    #engine = create_engine(mysql_connect, echo=True)
    engine = create_engine(mysql_connect,
                       pool_size=300, #连接池大小
                       max_overflow=50, #超出 pool_size 后可允许的最大连接数
                       pool_recycle=3600, #池中连接维持时间 单位S
                       echo=PrintSql)
    # 创建DBSession类型:
    #DBSession = sessionmaker(bind=engine)
    session_factory = sessionmaker(bind=engine, autoflush=True, autocommit=True)
    db_session = scoped_session(session_factory)
    return db_session
    
mysql_config = {
    'user': CONFIG.MYSQL_USER,
    'password': CONFIG.MYSQL_PASSWORD,
    'host': CONFIG.MYSQL_HOST,
    'port': CONFIG.MYSQL_PORT,
    'db': CONFIG.MYSQL_DB,
    'charset': 'utf8mb4'
}

DBSession = MysqlConnect(mysql_config)

def db_save(item):
    session = DBSession()
    try:
        session.begin()
        session.add(item)
        session.commit()
    except Exception as e:
        session.rollback()
        logger.error(" db save Exception:%s" % e)
    finally:
        session.close()
        
def db_sql(sql):
    session = DBSession()
    try:
        session.begin()
        session.execute(sql)
        session.commit()
    except Exception as e:
        session.rollback()
        logger.error('db execute sql Exception:%s' % e)
    finally:
        session.close()


def create_table():
    mysql_connect_base = "mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset={charset}"
    mysql_connect = mysql_connect_base.format(**mysql_config)
    # 初始化数据库连接:
    #engine = create_engine(mysql_connect, echo=True)
    engine = create_engine(mysql_connect,
                       pool_size=300, #连接池大小
                       max_overflow=50, #超出 pool_size 后可允许的最大连接数
                       pool_recycle=3600, #池中连接维持时间 单位S
                       echo=PrintSql)
    Base.metadata.create_all(engine)