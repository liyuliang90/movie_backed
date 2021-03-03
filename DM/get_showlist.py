import json
import requests
from models.filminfo import FilmInfo
from core.DB import db_save

def get():
    url = 'https://qt2.qingting123.com/CinemaAction.do'
    form = { 'dispatch':'getShowList',
             'key':'CinemaAction.getShowList',
             'appId':'wxb2c309d723a7c7ac',
             'cinemaOrigin':2,
             'cityId':20,
             'filmId':123031,
             'date':'2021-03-01',
             'longitude':120.39629,
             'latitude':36.30744,
             't':1614575699660,
             'isJson':1
    }
    r = requests.get(url, params=form)
    #r = requests.get(url)
    if r.status_code != 200:
        print(r.status_code)
        return
    r_json = json.loads(r.text)
    print(r_json)
    return
    movie_list = r_json['list']
    print(movie_list)
    return
    for filminfo in movie_list:
        film = FilmInfo()
        film.ID = filminfo['id']
        film.like = filminfo['like']
        film.publishDate = filminfo['publishDate']
        film.publish_date = filminfo['publish_date']
        film.showStatus = filminfo['showStatus']
        film.pic = filminfo['pic']
        film.cast = filminfo['cast']
        film.filmId = filminfo['filmId']
        film.film_id = filminfo['film_id']
        film.grade = filminfo['grade']
        film.name = filminfo['name']
        db_save(film)
   

if __name__ == '__main__':
    get()
