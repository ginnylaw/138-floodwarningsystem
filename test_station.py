# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    catchment_name = "This river is bigger than that Chris, it's large"
    max_on_record = 9001
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town, catchment_name, max_on_record)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town
    assert s.catchment_name == catchment_name
    assert s.max_on_record == max_on_record