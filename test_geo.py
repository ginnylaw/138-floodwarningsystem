import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list
from haversine import haversine

def test_stations_within_radius():
    station_list = build_station_list()
    assert len(station_list) > 0

    assert len(geo.stations_within_radius(station_list, (52.2053, 0.1218), -1)) == 0
    assert len(geo.stations_within_radius(station_list, (52.2053, 0.1218), 0)) == 0

    assert len(geo.stations_within_radius(station_list, (52.2053, 0.1218), 1300)) == len(station_list)

    test_radii = [1, 10, 100, 1000]
    test_centres = [(52.2053, 0.1218), (51.2704, 0.5227), (55.9533, 3.1883), (51.3544, 0.3989)]

    for radius in test_radii:
        for centre in test_centres:
            for station in geo.stations_within_radius(station_list, centre, radius):
                assert haversine(station.coord, centre) <= radius