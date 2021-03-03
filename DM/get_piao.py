import json
import requests
from models.movie import FilmInfo
from core.DB import db_save

def get():
    #url = 'https://qt2.qingting123.com/CinemaAction.do?dispatch=getScheduleListByCinema&key=CinemaAction.getScheduleListByCinema&appId=wxb2c309d723a7c7ac&cinemaOrigin=2&cinemaId=32853&t=1614563850871&isJson=1'
    form = {
        'dispatch':'getScheduleListByCinema',
        'key':'CinemaAction.getScheduleListByCinema',
        'appId':'wxb2c309d723a7c7ac',
        'cinemaOrigin':2,
        'cinemaId':32853,
        't':1614563850871,
        'isJson':1
    }
    url = 'https://qt2.qingting123.com/CinemaAction.do'
    url = 'https://qt2.qingting123.com/CinemaAction.do?dispatch=getFilmList&key=CinemaAction.getFilmList&appId=wxb2c309d723a7c7ac&cinemaOrigin=2&type=1&t=1614569137846&isJson=1'
    #r = requests.get(url, params=form)
    r = requests.get(url)
    if r.status_code != 200:
        print(r.status_code)
        return
    r_json = json.loads(r.text)
    movie_list = r_json['list']
    for i in movie_list:
        filminfo = i['filmInfo']
        film = FilmInfo()
        film.like = filminfo['like']
        film.director = filminfo['director']
        film.publishDate = filminfo['publishDate']
        film.versionTypes = filminfo['versionTypes']
        film.language = filminfo['language']
        film.pic = filminfo['pic']
        film.filmTypes = filminfo['filmTypes']
        film.duration = filminfo['duration']
        film.cast = filminfo['cast']
        film.filmId = filminfo['filmId']
        film.grade = filminfo['grade']
        film.intro = filminfo['intro']
        film.name = filminfo['name']
        db_save(film)
   

if __name__ == '__main__':
    get()
