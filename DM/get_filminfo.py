import json
import requests
from models.filminfo import FilmInfo
from core.DB import db_save

def get():
    url = 'https://qt2.qingting123.com/CinemaAction.do'
    #url = 'https://qt2.qingting123.com/CinemaAction.do?dispatch=getFilmList&key=CinemaAction.getFilmList&appId=wxb2c309d723a7c7ac&cinemaOrigin=2&type=1&t=1614569137846&isJson=1'
    form = {'dispatch':'getFilmList',
            'key':'CinemaAction.getFilmList',
            'appId':'wxb2c309d723a7c7ac',
            'cinemaOrigin':2,
            'type':1,
            't':1614569137846,
            'isJson':1
    }
    r = requests.get(url, params=form)
    #r = requests.get(url)
    if r.status_code != 200:
        print(r.status_code)
        return
    r_json = json.loads(r.text)
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
