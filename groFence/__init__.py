from geopy import Point
from geopy.distance import great_circle



def is_within_geofence(target_lat, target_lon, center_lat, center_lon, radius_km):
    center_point = Point(center_lat, center_lon)
    target_point = Point(target_lat, target_lon)

    distance = great_circle(center_point, target_point).km
    print(distance)
    return distance <= radius_km




center_lat, center_lon = (28.5626627,77.3749961)
target_lat, target_lon = (28.5615227,77.3878941)

radius_km = 3

result = is_within_geofence(target_lat, target_lon, center_lat, center_lon, radius_km)
print(result)