#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from tornado.web import url
from controller.movie import MovieHandler
from controller.index import IndexHandler
from controller.cinemas import CinemaHandler 
from controller.cinemaDetail import CinemaDetailHandler
from controller.seat_select import SeatSelectHandler
from controller.movieDetail import MovieDetailHandler
from controller.movieComments import MovieCommentHandler
from controller.filterCinemas import FilterCinemasHandler

Router = [
    url(r"/ajax/movieOnInfoList", MovieHandler),
    url(r"/ajax/cinemaList", CinemaHandler),
    url(r"/ajax/filterCinemas", FilterCinemasHandler),
    url(r"/ajax/cinemaDetail", CinemaDetailHandler),
    url(r"/ajax/seat_select", SeatSelectHandler),
    url(r"/ajax/detailmovie", MovieDetailHandler),
    url(r"/mmdb/comments/movie", MovieCommentHandler),
]
