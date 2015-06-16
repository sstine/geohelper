# Geohelper

Geohelper is a python package which contains helper functions to calculate geographical distance and bearing.  The package implements several algorithms that are of varying accuracy and efficiency and exposes them with multiple return types.

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
>>> distance.get_distance(lat1, lng1, lat2, lng2)
247930.318661 # Distance in meters
```

### Haversine
The haversine algorithm is fairly accurate, but can be expensive when computing
many distances. The error rate is as high as 0.55% but averages at around 0.3% 
The distances are exposed in km, m, mi, ft, and radians.

```
>>> distance.haversine_km(lat1, lng1, lat2, lng2)
247.930318661 # Distance in kilometers

>>> distance.haversine_m(lat1, lng1, lat2, lng2)
247930.318661 # Distance in meters

>>> distance.haversine_mi(lat1, lng1, lat2, lng2)
153.949511948 # Distance in miles

>>> distance.haversine_ft(lat1, lng1, lat2, lng2)
812853.423086 # Distance in feet

>>> distance.haversine_rad(lat1, lng1, lat2, lng2)
0.0389154479141 # Distance in radians
```

### Equirectangular
The equirectangular algorithm is less accurate but is more efficient.  It works
well when dealing with small distances. The distances are exposed in km, m, mi,
ft, and radians.

```
>>> distance.equirectangular_km(lat1, lng1, lat2, lng2)
247.93948162 # Distance in kilometers

>>> distance.equirectangular_m(lat1, lng1, lat2, lng2)
247939.48162 # Distance in meters

>>> distance.equirectangular_mi(lat1, lng1, lat2, lng2)
153.955201584 # Distance in miles

>>> distance.equirectangular_ft(lat1, lng1, lat2, lng2)
812883.464362 # Distance in feet

>>> distance.equirectangular_rad(lat1, lng1, lat2, lng2)
0.0389168861435 # Distance in radians
```

### Bearing
Calculates a compass bearing (North being 0 degrees) for two given coordinate
pairs.  

```
from geohelper import bearing
>>> bearing.initial_compass_bearing(lat1, lng1, lat2, lng2)
91.8439843971
```

### Todo's
  - Implement Vincenty algorithm (distance)
  - Implement bearing algorithms

License
----

MIT

[Movable Type Scripts]:http://www.movable-type.co.uk/scripts/latlong.html
