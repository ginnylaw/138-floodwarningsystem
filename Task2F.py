# Not Copyright (¬C) 2022 Greg S. Kurzepa

from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
import datetime

def run():
    """Requirements for Task 2F"""
    
    p = 4
    dt = 2

    station_list = build_station_list()
    update_water_levels(station_list)
    input_stations = stations_level_over_threshold(station_list, .8)[:5]

    #dates, levels = fetch_measure_levels(input_stations[0][0].measure_id, dt=datetime.timedelta(days=dt))
    #plot_water_level_with_fit(input_stations[0][0], dates, levels, p)
    for x in input_stations:
        dates, levels = fetch_measure_levels(x[0].measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(x[0], dates, levels, p)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()