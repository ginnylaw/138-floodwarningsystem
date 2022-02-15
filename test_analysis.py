from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.analysis import polyfit
import matplotlib
import datetime
import random
import numpy as np
from matplotlib import pyplot as plt

def sum_squared_diff(a, b):
    return np.sum( (a-b)**2 )

# applies a polyfit to n random stations, generates 500 random functions of the same degree, and ensures the polyfit has the lowest least-squares error
def test_polyfit():
    station_list = build_station_list()
    update_water_levels(station_list)

    do_plot = False
    n = 10
    # list of n non-repeating random integer indexes for station_list array
    INDEXES = random.sample(range(len(station_list)), n)
    # list of n random integer days between 1 and 21 inclusive
    DAYS = [random.randint(1,21) for i in range(n)]
    # list of n random integer polynomial degrees
    DEGREES = [random.randint(1,16) for i in range(n)]

    #print(INDEXES, DAYS, DEGREES)

    for i in range(n):
        if station_list[INDEXES[i]].levels_consistent():

            dates, levels = fetch_measure_levels(station_list[INDEXES[i]].measure_id, dt=datetime.timedelta(days=DAYS[i]))
            poly, d0 = polyfit(dates, levels, DEGREES[i])
            dates_float = matplotlib.dates.date2num(dates) + d0

            for j in range(100):
                # creates a new poly whose coefficients are randomly assigned a value within +-0.1 times the coefficients of the calculated polyfit poly.
                random_poly = np.poly1d(poly.coeffs + poly.coeffs*np.array([random.uniform(-0.01, 0.01) for x in range(DEGREES[i] + 1)]))

                assert sum_squared_diff(levels, poly(dates_float)) <= sum_squared_diff(levels, random_poly(dates_float))

                if do_plot:
                    plt.scatter(dates_float, levels, label="Water levels", s=2, color="c")
                    plt.plot(dates_float, random_poly(dates_float), label=f"Random poly, n={DEGREES[i]}", linewidth=1)
                    plt.plot(dates_float, poly(dates_float), label=f"Best fit poly, n={DEGREES[i]}", linewidth=1)
                    plt.title(f"Water levels at {station_list[INDEXES[i]].name}")

                    plt.xlabel("Days from current day")
                    plt.ylabel("Water level (m)")

                    plt.legend()
                    plt.show()

            #input()

test_polyfit()