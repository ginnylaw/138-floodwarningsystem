
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Requirements for Task 1F"""

    station_list = build_station_list()
    inconsisent = inconsistent_typical_range_stations(station_list)
    print(sorted(inconsisent))
    

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()