from math import radians, cos, sin, asin, sqrt

radius_km = 6371
radius_mi = 3956

def haversine_rad(lat1, lng1, lat2, lng2):
  """
  Calculates the great-circle distance between 2 coordinates.
  Ignores terrain (shorest distance).

  Assumes the earth is spherical (it is ellipsoidal)

  Error rates of as much as 0.55% near the equator, but generally under 0.3%

  Source information: http://www.movable-type.co.uk/scripts/latlong.html

  Args:
    lat1 (str): The latitude of the first coordinate pair.
    lng1 (str): The longitude of the first coordinate pair.
    lat2 (str): The latitude of the second coordinate pair.
    lng2 (str): The longitude of the second coordinate pair.

  Returns:
      c: The distance between 2 points in radians.
  """
  # convert degrees to rads
  lat1, lng1, lat2, lng2 = map(radians, [lat1, lng1, lat2, lng2])

  dlon = lng2 - lng1 
  dlat = lat2 - lat1 
  a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
  c = 2 * asin(sqrt(a)) 
  return c

def haversine_km(lat1, lng1, lat2, lng2):
  """
  Calculates distance using the haversine formula.

  Args:
    lat1 (str): The latitude of the first coordinate pair.
    lng1 (str): The longitude of the first coordinate pair.
    lat2 (str): The latitude of the second coordinate pair.
    lng2 (str): The longitude of the second coordinate pair.

  Returns:
      haversine_rad: The distance between 2 points in km.
  """
  return haversine_rad(lat1, lng1, lat2, lng2) * radius_km

def haversine_m(lat1, lng1, lat2, lng2):
  return haversine_rad(lat1, lng1, lat2, lng2) * radius_km * 1000

def haversine_mi(lat1, lng1, lat2, lng2):
  return haversine_rad(lat1, lng1, lat2, lng2) * radius_mi


def equirectangular_rad(lat1, lng1, lat2, lng2):
  """
  Calculates the distance between 2 coordinates using Pythagora's theorem.
  Generally fit for small distances, but less accurate than haversine.
  Significantly more efficient than haversine.

  Ignores terrain (shorest distance).

  Assumes the earth is spherical (it is ellipsoidal)

  Error rates are complex depending on location and bearing, but are zero along
  meridians.

  Source information: http://www.movable-type.co.uk/scripts/latlong.html

  Args:
    lat1 (str): The latitude of the first coordinate pair.
    lng1 (str): The longitude of the first coordinate pair.
    lat2 (str): The latitude of the second coordinate pair.
    lng2 (str): The longitude of the second coordinate pair.

  Returns:
      d: The distance between 2 points in radians.
  """

  # convert degrees to radians 
  lat1, lng1, lat2, lng2 = map(radians, [lat1, lng1, lat2, lng2])
  x = (lng2 - lng1) * cos((lat1 + lat2)/2)
  y = lat2 - lat1
  d = sqrt(x**2 + y**2) # radians
  return d

def equirectangular_km(lat1, lng1, lat2, lng2):
  return equirectangular_rad(lat1, lng1, lat2, lng2) * radius_km

def equirectangular_m(lat1, lng1, lat2, lng2):
  return equirectangular_rad(lat1, lng1, lat2, lng2) * radius_km * 1000

def equirectangular_mi(lat1, lng1, lat2, lng2):
  return equirectangular_rad(lat1, lng1, lat2, lng2) * radius_mi


if __name__ == '__main__':
  lat1, lng1 = 37.393589, -98.460092
  lat2, lng2 = 37.288775, -95.658579

  print("haversine_rad: %s" % haversine_rad(lat1, lng1, lat2, lng2))
  print("haversine_km: %s" % haversine_km(lat1, lng1, lat2, lng2))
  print("haversine_m: %s" % haversine_m(lat1, lng1, lat2, lng2))
  print("haversine_mi: %s" % haversine_mi(lat1, lng1, lat2, lng2))

  print("equirectangular_rad: %s" % equirectangular_rad(lat1, lng1, lat2, lng2))
  print("equirectangular_km: %s" % equirectangular_km(lat1, lng1, lat2, lng2))
  print("equirectangular_m: %s" % equirectangular_m(lat1, lng1, lat2, lng2))
  print("equirectangular_mi: %s" % equirectangular_mi(lat1, lng1, lat2, lng2))

