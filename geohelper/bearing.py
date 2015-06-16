# Source information from http://www.movable-type.co.uk/scripts/latlong.html
import timeit
import math

def initial_compass_bearing(lat1, lng1, lat2, lng2):
    """
    Calculates the initial bearing (forward azimuth) of a great-circle arc.
    Note that over long distances the bearing may change.
    The bearing is represented as the compass bearing (North is 0 degrees)

    Args:
        lat1 (str): The latitude of the first coordinate pair.
        lng1 (str): The longitude of the first coordinate pair.
        lat2 (str): The latitude of the second coordinate pair.
        lng2 (str): The longitude of the second coordinate pair.

    Returns:
        compass_bearing: The initial compass bearing.
    """

    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    deltaLng = math.radians(lng2 - lng1)
 
    x = math.sin(deltaLng) * math.cos(lat2)
    y = (math.cos(lat1) * math.sin(lat2)) - (math.sin(lat1)
        * math.cos(lat2) * math.cos(deltaLng))
 
    initial_bearing = math.atan2(x, y)
 
    # Normalize the initial bearing (-180 degrees to 180 degrees) 
    # to a compass bearing (360 degrees)
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

if __name__ == '__main__':
    lat1, lng1 = 37.393589, -98.460092
    lat2, lng2 = 37.288775, -95.658579

    bearing = initial_compass_bearing(lat1, lng1, lat2, lng2)
    print(bearing)

    #wrapped = wrapper(initial_compass_bearing, lat1, lng1, lat2, lng2)
    #print(timeit.timeit(wrapped,number=1000000))




