"""Unit test for the flood module"""

from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation

def test_stations_level_over_threshold():

    station_list = build_station_list()
    update_water_levels(station_list)
    tol = 0.8
    stations_over = stations_level_over_threshold(station_list, tol)

    assert all(stations_over[i][1] <= stations_over[i+1][1] for i in range(len(stations_over) - 1))
    assert all(x[1] >= tol for x in stations_over)

    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (2, 4)
    s = MonitoringStation(s_id, m_id, label, coord, trange)

    s._latest_level = -2
    assert len(stations_level_over_threshold([s])) == 0

    s._latest_level = 8
    assert stations_level_over_threshold([s])[0][1] == 3

    s._latest_level = 3
    assert stations_level_over_threshold([s])[0][1] == 0.5

    s._latest_level = 2
    assert stations_level_over_threshold([s])[0][1] == 0

    s._typical_range = (-1,4)
    assert len(stations_level_over_threshold([s])) == 0

    s._typical_range = (2,-4)
    assert len(stations_level_over_threshold([s])) == 0

    s._typical_range = (3,1)
    assert len(stations_level_over_threshold([s])) == 0