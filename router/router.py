#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from tornado.web import url
from controller.index import IndexHandler
from controller.cinemas import CinemaHandler 
from controller.cinemaDetail import CinemaDetailHandler
from controller.seat_select import SeatSelectHandler
from controller.movieDetail import MovieDetailHandler
from controller.movieComments import MovieCommentHandler

Router = [
    url(r"/ajax/movieOnInfoList", IndexHandler),
    url(r"/ajax/cinemaList", CinemaHandler),
    url(r"/ajax/cinemaDetail", CinemaDetailHandler),
    url(r"/ajax/seat_select", SeatSelectHandler),
    url(r"/ajax/detailmovie", MovieDetailHandler),
    url(r"/mmdb/comments/movie", MovieCommentHandler),
]
