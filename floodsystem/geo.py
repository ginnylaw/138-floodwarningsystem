# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine # distance between two locations given their latitude & longitude
import plotly.express as px

def stations_within_radius(stations, centre, r):
    """Returns a list of all input stations that are within r kilometres of a given centre (latitude, longitude) coordinate."""
    """Coordinates outside of the +=180 degree bounds wrap around. For example 190 wraps around to -170. """
    return [x for x in stations if haversine(x.coord, centre) <= r]

def rivers_by_station_number(stations, N):
    """Returns a list of the N riverse with the most monitoring stations. Any rivers with the same number of statons as the Nth entry are included."""

    # Creates dictionary which maps each river to the number of stations it has
    STATIONS_PER_RIVER = {}
    for station in stations:
        if station.river in STATIONS_PER_RIVER:
            STATIONS_PER_RIVER[station.river] += 1
        else:
            STATIONS_PER_RIVER[station.river] = 1

    # Creates list of rivers sorted, in descending order, by the number of stations each has
    sorted_stations_per_river = sorted(STATIONS_PER_RIVER.items(), key = lambda x : x[1], reverse=True)

    # Finds last river with station count equivalent to Nth entry
    slice_index = N
    for index, i in enumerate(sorted_stations_per_river[N:]):
        if i[1] < sorted_stations_per_river[N-1][1]:
            slice_index += index
            break

    # Returns (river name, station count) for first N entries, as well as any subsequent ones which have a station count equivalent to the Nth entry
    return [tuple(x) for x in sorted_stations_per_river[:slice_index]]

# Latitude and longitude range covered by England
ENG_LAT = (50.5,55.8)
ENG_LON = (-6,1.1)

def display_stations(stations):
    """Plots the locations of all given stations on a map of England"""
    # Plots all stations using their latitude and longitude
    fig = px.scatter_geo(
        [station.name for station in stations],
        [station.coord[0] for station in stations],
        [station.coord[1] for station in stations]
    )
    
    # Sets the range of the map to cover just England
    fig.update_layout(geo = dict(
        scope = "europe",
        resolution = 50,
        lataxis_range = ENG_LAT,
        lonaxis_range = ENG_LON)
    )

    # Displays plot in browser
    fig.show()