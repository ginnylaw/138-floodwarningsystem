# Not Copyright (¬C) 2022 Greg S. Kurzepa

from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1E"""

    station_list = build_station_list()
    output = rivers_by_station_number(station_list, 9)
    print(output)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()