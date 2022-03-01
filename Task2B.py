# Not Copyright (¬C) 2022 Greg S. Kurzepa

from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    """Requirements for Task 2B"""

    station_list = build_station_list()
    update_water_levels(station_list)
    stations_over = stations_level_over_threshold(station_list, 0.8)
    for i in stations_over:
        print(i[0].name, i[1])

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()