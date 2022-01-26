# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import dateutil
from .utils import sorted_by_key  # noqa
import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list
from haversine import haversine

def stations_by_distance(stations, p):
    """sort stations by distance"""
    dist_lst = []
    for x in stations:
        distance = haversine(x.coord, p)
        dist_lst += (x.name, x.town, distance)
    dist_tuple = [x for x in zip(*[iter(dist_lst)]*3)]
    dist_tuple = sorted_by_key(dist_tuple, 2)
    return dist_tuple
    
