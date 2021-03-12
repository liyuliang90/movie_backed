from math import radians, cos, sin, asin, sqrt

#公式计算两点间距离（m）

def geodistance(lng1,lat1,lng2,lat2):
    #lng1,lat1,lng2,lat2 = (120.12802999999997,30.28708,115.86572000000001,28.7427)
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)])
    dlon=lng2-lng1
    dlat=lat2-lat1
    a=sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2 
    distance=2*asin(sqrt(a))*6371*1000 # 地球平均半径，6371km
    distance=round(distance/1000,3)
    print(distance)
    return distance


from geopy.distance import geodesic


if __name__ == '__main__':
    lat1 = 36.30744
    lng1 = 120.39629
    lat2 = 36.307068
    lng2 = 120.403305
    lat3 = 36.40744
    lng3 = 120.39629

    lat4 = 36.30744
    lng4 = 120.49629
    geodistance(lng1,lat1,lng2,lat2)
    a=(lat1,lng1)
    b=(lat2,lng2)
    c=(lat3,lng3)
    d=(lat4,lng4)
    print(geodesic(a,c))
