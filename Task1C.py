# Not Copyright (¬C) 2022 Greg S. Kurzepa

from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1C"""

    station_list = build_station_list()
    within_radius = stations_within_radius(station_list, (52.2053, 0.1218), 10)
    output = sorted([x.name for x in within_radius])
    print(output)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()