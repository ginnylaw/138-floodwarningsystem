# Not Copyright (¬C) 2022 Greg S. Kurzepa

from distutils.command.build import build
from floodsystem.stationdata import build_station_list
from floodsystem.geo import display_stations
import random

def run():
    """Task 1 extension requirements"""

    stations = build_station_list()

    # Displays all the stations on a map of England which opens in the browser
    display_stations(stations)

    # Demonstrates the two new attributes of the MonitoringStation class
    for i in range(3):
        print(random.choice(stations), "\n")

if __name__ == "__main__":
    print("*** Task 1 Extensions: CUED Part IA Flood Warning System ***")
    run()