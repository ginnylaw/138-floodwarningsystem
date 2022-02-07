"""Unit test for the geo module"""

import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list
from haversine import haversine
import plotly

station_list = build_station_list()
assert len(station_list) > 0

def test_stations_by_distance():
    check = geo.stations_by_distance(station_list, (52.2053, 0.1218))
    assert check[0][2] > 0
    assert check[-1][2] < 1300

    assert len(geo.stations_by_distance(station_list, (52.2053, 0.1218))) == len(station_list)

    test_centres = [(52.2053, 0.1218), (51.2704, 0.5227), (55.9533, 3.1883), (51.3544, 0.3989)]
    for centre in test_centres:
        for station in geo.stations_by_distance(station_list, centre):
            lst = geo.stations_by_distance(station_list, centre)
            assert [x[2] for x in lst] == haversine(station.coord, centre)

    

def test_stations_within_radius():
    assert len(geo.stations_within_radius(station_list, (52.2053, 0.1218), -1)) == 0
    assert len(geo.stations_within_radius(station_list, (52.2053, 0.1218), 0)) == 0

    assert len(geo.stations_within_radius(station_list, (52.2053, 0.1218), 1300)) == len(station_list)

    test_radii = [1, 10, 100, 1000]
    test_centres = [(52.2053, 0.1218), (51.2704, 0.5227), (55.9533, 3.1883), (51.3544, 0.3989)]

    for radius in test_radii:
        for centre in test_centres:
            for station in geo.stations_within_radius(station_list, centre, radius):
                assert haversine(station.coord, centre) <= radius

def test_rivers_with_station():
    assert len(geo.rivers_with_station(station_list)) != 0
    assert geo.rivers_with_station(station_list)[0] < geo.rivers_with_station(station_list)[1]

def test_stations_by_river():
    test_rivers = ['River Aire', 'River Cam', 'River Thames']
    riverlist = geo.stations_by_river(station_list)
    for r in test_rivers:
        riverstosort = riverlist[r]
        riverstosort = sorted(riverstosort)
        assert riverstosort[0] < riverstosort[1]

def test_rivers_by_station_number():
    test_n = [1,5,20,100,500]
    for n in test_n:
        data = geo.rivers_by_station_number(station_list, n)
        assert len(data) >= n
        # test whether the last element of the result has a number of stations equal to the nth element
        assert data[-1][1] == data[n-1][1]
        # test whether the elements are in descending numerical order
        assert all(data[x][1] >= data[x+1][1] for x in range(len(data) - 1))