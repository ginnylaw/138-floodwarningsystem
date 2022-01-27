from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station


def run():
    """Requirements for Task 1D"""

    station_list = build_station_list()
    rivers = rivers_with_station(station_list)

    print("First 10 rivers with stations:") 
    print(rivers[:10])
    

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()