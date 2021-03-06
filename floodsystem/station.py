# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


from urllib.parse import parse_qsl
import datetime

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, _station_id, _measure_id, _label, _coord, _typical_range,
                 _river, _town, _catchment_name, _max_on_record):

        self._station_id = _station_id
        self._measure_id = _measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self._name = _label
        if isinstance(_label, list):
            self._name = _label[0]

        self._coord = _coord
        self._typical_range = _typical_range
        self._river = _river
        self._town = _town

        self._latest_level = None
        self._latest_date = None

        # Additional interesting parameters
        self._catchment_name = _catchment_name
        self._max_on_record = _max_on_record

    def relative_water_level(self):
        """Returns latest water level as a fraction of the typical range"""

        if self.levels_consistent():
            return (self.latest_level - self.typical_range[0]) / (self.typical_range[1] - self.typical_range[0])
        else:
            return None

    # Make a property for each attribute that effectively makes it read-only, preventing accidental writes
    @property
    def station_id(self):
        return self._station_id
    @property
    def measure_id(self):
        return self._measure_id
    @property
    def name(self):
        return self._name
    @property
    def coord(self):
        return self._coord
    @property
    def typical_range(self):
        return self._typical_range
    @property
    def river(self):
        return self._river
    @property
    def town(self):
        return self._town
    @property
    def latest_level(self):
        return self._latest_level
    @property
    def catchment_name(self):
        return self._catchment_name
    @property
    def max_on_record(self):
        return self._max_on_record
    @property
    def latest_date(self):
        return self._latest_date

    def __repr__(self):
        d = f"Station name:     {self._name}\n"
        d += f"   id:             {self._station_id}\n"
        d += f"   measure id:     {self._measure_id}\n"
        d += f"   coordinate:     {self._coord}\n"
        d += f"   town:           {self._town}\n"
        d += f"   river:          {self._river}\n"
        d += f"   typical range:  {self._typical_range}\n"
        d += f"   catchment name: {self._catchment_name}\n"
        d += f"   max on record:  {self.max_on_record}\n"
        d += f"   latest level:   {self._latest_level}\n"
        d += f"   latest date:    {self._latest_date}\n\n"
        return d

    def typical_range_consistent(self):
        """Check whether typical range of station is valid. Returns True or False"""
        if self._measure_id == None:
            return False
        if self._typical_range == None:
            return False
        if self._typical_range[1] <= self._typical_range[0]:
            return False
        
        return True

    def levels_consistent(self):
        """Check whether station data is usable for flood risk analysis."""
        if self.typical_range_consistent() and self._latest_date == str(datetime.date.today()) and self.latest_level != None:
            return True
        else:
            return False

def inconsistent_typical_range_stations(stations):
    """Return list of stations with inconsistent data."""
    inconsistent_stations = []
    for x in stations:
        if not x.typical_range_consistent():
            inconsistent_stations.append(x.name)
    return inconsistent_stations
    
