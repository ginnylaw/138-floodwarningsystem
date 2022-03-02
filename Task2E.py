from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run():
    """Requirements for Task 2E"""

    station_list = build_station_list()
    update_water_levels(station_list)
   
    dt = 10 

    topstations = stations_highest_rel_level(station_list, 5)
    
    for station in topstations:
        dates, levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station[0], dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()