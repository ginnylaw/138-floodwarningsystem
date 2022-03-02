# Not Copyright (¬C) 2022 Greg S. Kurzepa

"""
This module contains functions that aid with flood prediction.
"""
import warnings
import datetime
from .datafetcher import fetch_measure_levels
from .analysis import average_gradient
from .plot import plot_water_level_with_fit


def stations_level_over_threshold(stations, tol, return_inconsistent=False):
    """Returns a list of (MonitoringStation, relative water level) tuples in descending relative water level order."""

    inconsistent = []
    stations_over_tol = []
    for station in stations:
        relative_water_level = station.relative_water_level()
        if relative_water_level != None:
            if relative_water_level >= tol:
                stations_over_tol.append( (station, relative_water_level) )
        else:
            inconsistent.append(station)

    if len(inconsistent) > 0:
        warnings.warn(f"flood.stations_level_over_threshold: Omitted {len(inconsistent)} stations due to out of date or inconsistent data")

    stations_over_tol.sort(key = lambda x : x[1], reverse=True)
    
    if not return_inconsistent:
        return stations_over_tol
    else:
        return stations_over_tol, inconsistent
      
def stations_highest_rel_level(stations, N):
    # Creates dictionary which maps each station to its relative level

    rel_level = [(station, station.relative_water_level()) for station in stations if station.relative_water_level() != None]

    # Creates list of stations sorted, in descending order, by the relative level
    sorted_stations_level = sorted(rel_level, key = lambda x : x[1], reverse=True)

    # Finds last river with relative level equivalent to Nth entry
    slice_index = N
    for index, i in enumerate(sorted_stations_level[N:]):
        if i[1] < sorted_stations_level[N-1][1]:
            slice_index += index
            break


    # Returns (station, relative level) for first N entries, 
    # as well as any subsequent ones which have a rel level equivalent to the Nth entry
    return [tuple(x) for x in sorted_stations_level[:slice_index]]

def highest_flood_risk(station_list, do_plot=False):
    """Returns a list of the stations with the highest predicted flood risk. Rivers above a relative water level of 1.2 are ranked by their average rate of water level increase over the last 12 hours."""

    station_list = [x[0] for x in stations_level_over_threshold(station_list, 1.2)]
    print(len(station_list))

    RISK_THRESHOLDS = [0.001, 0.01] # average rate of water increase thresholds for each risk level

    RISK = {
        "very high" : [],
        "high" : [],
        "medium" : []
    }

    for station in station_list:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
        avg_gradient = average_gradient(dates, levels, 12)

        if avg_gradient > RISK_THRESHOLDS[1]:
            #print(avg_gradient)
            RISK["very high"].append(station)
        elif avg_gradient > RISK_THRESHOLDS[0]:
            RISK["high"].append(station)
        else:
            RISK["medium"].append(station)

    for i in RISK:
        print(f"{i}: {[x.name for x in RISK[i]]}")

    if do_plot:
        for i in RISK["very high"]:
            dates, levels = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days=2))
            plot_water_level_with_fit(i, dates, levels, 10)