from geohelper import distance

lat1, lng1 = 37.393589, -98.460092
lat2, lng2 = 37.288775, -95.658579

### The get_distance function calls the haversine_m function by default
distance_in_meters = distance.get_distance(lat1, lng1, lat2, lng2)
print("Distance in m: %s" % distance_in_meters)


### The haversine formula is fairly accurate but expensive
### It exposes the distance in km, m, mi, and ft 
hav_distance_km = distance.haversine_km(lat1, lng1, lat2, lng2)
print("Haversine distance in km: %s" % hav_distance_km)

hav_distance_m = distance.haversine_m(lat1, lng1, lat2, lng2)
print("Haversine distance in m: %s" % hav_distance_m)

hav_distance_mi = distance.haversine_mi(lat1, lng1, lat2, lng2)
print("Haversine distance in mi: %s" % hav_distance_mi)

hav_distance_ft = distance.haversine_ft(lat1, lng1, lat2, lng2)
print("Haversine distance in ft: %s" % hav_distance_ft)

hav_distance_rad = distance.haversine_rad(lat1, lng1, lat2, lng2)
print("Haversine distance in radians: %s" % hav_distance_rad)

### The equirectangular formula is less accurate but is more efficient
equirect_dist_km = distance.equirectangular_km(lat1, lng1, lat2, lng2)
print("Equirectangular distance in km: %s" % equirect_dist_km)

equirect_dist_m = distance.equirectangular_m(lat1, lng1, lat2, lng2)
print("Equirectangular distance in m: %s" % equirect_dist_m)

equirect_dist_mi = distance.equirectangular_mi(lat1, lng1, lat2, lng2)
print("Equirectangular distance in mi: %s" % equirect_dist_mi)

equirect_dist_ft = distance.equirectangular_ft(lat1, lng1, lat2, lng2)
print("Equirectangular distance in ft: %s" % equirect_dist_ft)

equirect_dist_rad = distance.equirectangular_rad(lat1, lng1, lat2, lng2)
print("Haversine distance in radians: %s" % equirect_dist_rad)