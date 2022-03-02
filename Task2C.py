from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    """Requirements for Task 2C"""

    station_list = build_station_list()
    update_water_levels(station_list)
    highest_levels = stations_highest_rel_level(station_list, 10)
    for i in highest_levels:
        print(i[0].name, i[1])

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()