from geohelper import distance

lat1, lng1 = 37.393589, -98.460092
lat2, lng2 = 37.288775, -95.658579

distance_km = distance.haversine_km(lat1, lng1, lat2, lng2)
print(distance_km)