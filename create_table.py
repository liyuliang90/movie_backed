#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from core.DB import create_table
from models.filminfo import FilmInfo
from models.citys import Citys
from models.cinema import Cinema
from models.movie import Movie
from models.city_section import CityBrand, CityDistrict, CityDistrictSub, CitySubway, CitySubwayStation
from models.plan import PlanMovie, PlanMovieDate, Plan
if __name__ == '__main__':
    create_table()
