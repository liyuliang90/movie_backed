#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from core.logger import logger
from core.DB import DBSession

def get_cinema(city_id, districtId, limit=12, offset=0):
    pass

def get_cinema_gis(city_id, districtId, lng, lat, distance=10000, limit=12, offset=0):
    try:
        session = DBSession()
        sql_format = '''
            SELECT
                ID as ID,
                name as name,
                addr as addr,
                lat as lat,
                lng as lng,
                endorse as endorse,
                allowRefund as allowRefund, 
                snack as snack,
                vipDesc as vipDesc,
                showTimes as showTimes,
                cardPromotionTag as cardPromotionTag,
                ST_ASTEXT(gis), FLOOR(ST_DISTANCE_SPHERE(POINT({lng}, {lat}), gis)) AS distance 
            FROM cinema 
            WHERE
                cityId={city_id} AND
                {districtId}
                ST_CONTAINS(ST_MAKEENVELOPE(
                    POINT(({lng} + ({distance} / 111)),({lat} + ({distance} / 111))),
                    POINT(({lng} - ({distance} / 111)),({lat} - ({distance} / 111)))
                    ),gis
                )
            ORDER BY distance
            LIMIT {limit} OFFSET {offset}
            '''
        sql_count_format = '''
                SELECT COUNT(*) as total FROM cinema
                WHERE 
                      {districtId}
                      cityId={city_id}
                '''
        params = {
            'city_id': city_id,
            'lng':lng,
            'lat':lat,
            'distance':float(distance)/1000.0,
            'districtId':'',
            'limit':limit,
            'offset':offset
        }
        if int(districtId)>0:
            params['districtId'] = "districtId=%s AND" % districtId
        total = 0
        sql = sql_format.format(**params)
        sql_count = sql_count_format.format(**params)
        query = session.execute(sql)
        results = query.fetchall()
        query_count = session.execute(sql_count)
        total_set = query_count.fetchall()
        if total_set:
            total = total_set[0].total
        return results, total
    except Exception as e:
        logger.error('db execute sql Exception:%s' % e)
    finally:
        session.close()