# Geohelper

Geohelper is a python package which contains helper functions to calculate geographical distance, bearing, and more (eventually!).  The package implements several algorithms that are of varying accuracy and efficiency and exposes them with multiple return types.

  - Distance
    - Haversine (km, m, mi, ft)
    - Equirectangular (km, m, mi, ft)
  - Bearing (will be implemented soon)

Source information for the algorithms used was obtained from [Movable Type Scripts] 

### Version
0.1.1

### Installation

```sh
$ pip install geohelper
```

### Usage

```sh
from geohelper import distance 

lat1, lng1 = 37.393589, -98.460092
lat2, lng2 = 37.288775, -95.658579
```

### get_distance
get_distance uses the haversine formula and returns the distance in meters

```
distance_in_meters = distance.get_distance(lat1, lng1, lat2, lng2)
print("Distance in m: %s" % distance_in_meters)
```

### Haversine
The haversine algorithm is fairly accurate, but can be expensive when computing
many distances. The error rate is as high as 0.55% but averages at around 0.3% 
The distances are exposed in km, m, mi, ft, and radians.

```
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
```

### Equirectangular
The equirectangular algorithm is less accurate but is more efficient.  It works
well when dealing with small distances. The distances are exposed in km, m, mi,
ft, and radians.

```
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
```

### Todo's

Write Tests
Implement more distance functionality
Add bearing functions

License
----

MIT

[Movable Type Scripts]:http://www.movable-type.co.uk/scripts/latlong.html
