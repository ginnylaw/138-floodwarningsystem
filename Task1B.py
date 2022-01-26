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
    
    print("10 closest stations:") 
    print(station_list[:10])
    print("10 furthest stations:")
    print(station_list[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()