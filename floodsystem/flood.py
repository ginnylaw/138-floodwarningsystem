# Not Copyright (¬C) 2022 Greg S. Kurzepa

"""
This module contains functions that aid with flood prediction.
"""

def stations_level_over_threshold(stations, tol):
    """Returns a list of (MonitoringStation, relative water level) tuples in descending relative water level order."""

    stations_over_tol = []
    for station in stations:
        relative_water_level = station.relative_water_level()
        if relative_water_level and relative_water_level > tol:
            stations_over_tol.append( (station, relative_water_level) )

    stations_over_tol.sort(key = lambda x : x[1])
    return stations_over_tol