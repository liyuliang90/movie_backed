#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from tornado.web import url
from controller.movie import MovieHandler
from controller.cinemas import CinemaHandler 
from controller.cinemaDetail import CinemaDetailHandler
from controller.seat_select import SeatSelectHandler
from controller.movieDetail import MovieDetailHandler
from controller.movieComments import MovieCommentHandler
from controller.filterCinemas import FilterCinemasHandler
from controller.mostExpected import MostExpectedHandler
from controller.comingList import ComingListHandler
from controller.ajax_movie import AjaxMovieHandler
from controller.cityLocation import CityLocationHandler
from controller.citys import CitysHandler
from controller.actor import ActorHandler

Router = [
    url(r"/ajax/movieOnInfoList", MovieHandler),
    url(r"/ajax/mostExpected", MostExpectedHandler),
    url(r"/ajax/comingList", ComingListHandler),
    url(r"/ajax/cinemaList", CinemaHandler),
    url(r"/ajax/movie", AjaxMovieHandler),
    url(r"/ajax/filterCinemas", FilterCinemasHandler),
    url(r"/ajax/cinemaDetail", CinemaDetailHandler),
    url(r"/ajax/seat_select", SeatSelectHandler),
    url(r"/ajax/detailmovie", MovieDetailHandler),
    url(r"/mmdb/comments/movie", MovieCommentHandler),
    
    url(r"/ajax/cityLocation", CityLocationHandler),
    url(r"/ajax/citys", CitysHandler),
    url(r"/ajax/actor", ActorHandler),
    
]
