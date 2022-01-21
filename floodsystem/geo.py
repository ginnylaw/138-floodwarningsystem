# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine # distance between two locations given their latitude & longitude

def stations_within_radius(stations, centre, r):
    """Returns a list of all input stations that are within r kilometres of a given centre (latitude, longitude) coordinate."""
    """Coordinates outside of the +=180 degree bounds wrap around. For example 190 wraps around to -170. """
    return [x for x in stations if haversine(x.coord, centre) <= r]