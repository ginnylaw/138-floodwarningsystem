from .analysis import polyfit
import matplotlib
import matplotlib.pyplot as plt

def plot_water_level_with_fit(station, dates, levels, p, show_plot=True):
    """Plots water levels and their degree p least-squares polynomial fit at the given stations for the given dates."""

    poly, d0 = polyfit(dates, levels, p)
    dates_float = matplotlib.dates.date2num(dates) + d0

    plt.scatter(dates_float, levels, label="Water levels", s=2, color="c")
    plt.plot(dates_float, poly(dates_float), label=f"Least squares polynomial fit, n={p}", linewidth=1)
    plt.title(f"Water levels at {station.name}")

    plt.xlabel("Days from current day")
    plt.ylabel("Water level (m)")

    plt.hlines(station.typical_range[1], dates_float[0], dates_float[-1], color="palegreen", linestyles='solid', label='Typical high')
    plt.hlines(station.typical_range[0], dates_float[0], dates_float[-1], color="tomato", linestyles='solid', label='Typical low')

    plt.legend()

    if show_plot:
        plt.show()

def plot_water_levels(station, dates, levels, show_plot=True):
    """Plots water levels against time for a given station"""

    #plot lines
    plt.plot(dates, levels)
    plt.hlines(1, dates[0], dates[-1], color="palegreen", linestyles='solid', label='Typical high')
    plt.hlines(0, dates[0], dates[-1], color="tomato", linestyles='solid', label='Typical low')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Days from current day')
    plt.ylabel('relative water level')
    plt.xticks(rotation=45);
    plt.title(station.name)
    plt.xlim((dates[0], dates[-1]))

    plt.legend()

    if show_plot:
        plt.show()

    