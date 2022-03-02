from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import highest_flood_risk

def run():
    """Requirements for Task 2G"""

    station_list = build_station_list()
    update_water_levels(station_list)
    
    highest_flood_risk(station_list, True)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()