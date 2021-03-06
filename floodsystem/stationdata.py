# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides interface for extracting statiob data from
JSON objects fetched from the Internet and

"""

from . import datafetcher
from .station import MonitoringStation

def build_station_list(use_cache=True):
    """Build and return a list of all river level monitoring stations
    based on data fetched from the Environment agency. Each station is
    represented as a MonitoringStation object.

    The available data for some station is incomplete or not
    available.

    """

    # Fetch station data
    data = datafetcher.fetch_station_data(use_cache)

    # Build list of MonitoringStation objects
    stations = []
    for e in data["items"]:
        # Extract town string (not always available)
        town = None
        if 'town' in e:
            town = e['town']

        # Extract river name (not always available)
        river = None
        if 'riverName' in e:
            river = e['riverName']

        # Attempt to extract typical range (low, high)
        try:
            typical_range = (float(e['stageScale']['typicalRangeLow']),
                             float(e['stageScale']['typicalRangeHigh']))
        except Exception:
            typical_range = None

        # Aditional interesting parameters

        # Attempt to extract catchment name
        catchment_name = None
        if 'catchmentName' in e:
            catchment_name = e['catchmentName']

        # Attempt to extract maximum water level on record
        max_on_record = None
        if 'stageScale' in e and 'maxOnRecord' in e['stageScale']:
            max_on_record = e['stageScale']['maxOnRecord']['value']

        try:
            # Create mesure station object if all required data is
            # available, and add to list
            s = MonitoringStation(
                _station_id=e['@id'],
                _measure_id=e['measures'][-1]['@id'],
                _label=e['label'],
                _coord=(float(e['lat']), float(e['long'])),
                _typical_range=typical_range,
                _river=river,
                _town=town,
                _catchment_name=catchment_name,
                _max_on_record=max_on_record)
            stations.append(s)
        except Exception:
            # Not all required data on the station was available, so
            # skip over
            pass

    return stations


def update_water_levels(stations):
    """Attach level data contained in measure_data to stations"""

    # Fetch level data
    measure_data = datafetcher.fetch_latest_water_level_data()

    # Build map from measure id to latest reading (value)
    measure_id_to_value = dict()
    measure_id_to_date = dict()
    for measure in measure_data['items']:
        if 'latestReading' in measure:
            latest_reading = measure['latestReading']
            measure_id = latest_reading['measure']
            measure_id_to_value[measure_id] = latest_reading['value']
            measure_id_to_date[measure_id] = latest_reading['date']

    # Attach latest reading to station objects
    for station in stations:

        # Reset latestlevel
        station._latest_level = None
        station._latest_date = None

        # Atach new level data (if available)
        if station.measure_id in measure_id_to_value:
            if isinstance(measure_id_to_value[station.measure_id], float):
                station._latest_level = measure_id_to_value[station.measure_id]
                station._latest_date = measure_id_to_date[station.measure_id]