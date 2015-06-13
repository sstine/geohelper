# Geohelper

Geohelper is a python package which contains helper functions to calculate geographical distance, bearing, and more (eventually!).  The package implements several algorithms that are of varying accuracy and efficiency and exposes them with multiple return types.

  - Distance
    - Haversine (km, m, mi, ft)
    - Equirectangular (km, m, mi, ft)
  - Bearing (will be implemented soon)

Source information for the algorithms used was obtained from [Movable Type Scripts] 

### Version
0.0.4.dev1

### Installation

```sh
$ pip install geohelper --pre
```

### Usage

```sh
from geohelper import distance 

lat1, lng1 = 37.393589, -98.460092
lat2, lng2 = 37.288775, -95.658579

distance_km = distance.haversine_km(lat1, lng1, lat2, lng2)
print(distance_km) #

```

### Todo's

Write Tests
Implement more distance functionality
Add bearing functions

License
----

MIT

[Movable Type Scripts]:http://www.movable-type.co.uk/scripts/latlong.html
