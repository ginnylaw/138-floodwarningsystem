#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 13:20:39 2022

@author: ginnylawrence
"""
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():
    """Requirements for Task 1B"""

    station_list = build_station_list()
    station_list = stations_by_distance(station_list, (52.2053, 0.1218))
    stations1 = station_list[:10]
    stations1 = [(x[0].name, x[0].town, x[1]) for x in stations1]
    stations2 = station_list[-10:]
    stations2 = [(x[0].name, x[0].town, x[1]) for x in stations2]

    print("10 closest stations:") 
    print(stations1)
    print("10 furthest stations:")
    print(stations2)

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()