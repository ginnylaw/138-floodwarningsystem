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

    plt.legend()

    if show_plot:
        plt.show()