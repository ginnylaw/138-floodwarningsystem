# Not Copyright (¬C) 2022 Greg S. Kurzepa

"""
This module contains functions that aid with flood prediction.
"""
import warnings

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