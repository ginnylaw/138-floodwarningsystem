# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, _station_id, _measure_id, _label, _coord, _typical_range,
                 _river, _town):

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

    def __repr__(self):
        d = "Station name:     {}\n".format(self._name)
        d += "   id:            {}\n".format(self._station_id)
        d += "   measure id:    {}\n".format(self._measure_id)
        d += "   coordinate:    {}\n".format(self._coord)
        d += "   town:          {}\n".format(self._town)
        d += "   river:         {}\n".format(self._river)
        d += "   typical range: {}".format(self._typical_range)
        return d
