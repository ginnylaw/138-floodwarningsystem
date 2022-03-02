# Not Copyright (¬C) 2022 Greg S. Kurzepa

"""
This module contains functions that aid with analysis of flood data.
"""

import matplotlib
import numpy as np
import datetime

def polyfit(dates, levels, p):
    """Returns the polynomial object of a degree p least-squares polynomial fit to the dates, levels input."""

    dates_float = matplotlib.dates.date2num(dates)
    d0 = -1*dates_float[0]

    p_coeff = np.polyfit(dates_float + d0, levels, p)
    poly = np.poly1d(p_coeff)

    return poly, d0

def average_gradient(dates, levels, dt=6, p=10):
    """Returns average rate of increase of water level for the last dt hours using the best fit polynomial."""
    poly, d0 = polyfit(dates, levels, p)

    dy = poly(matplotlib.dates.date2num(dates[0]) + d0) - poly(matplotlib.dates.date2num(dates[0] - datetime.timedelta(hours=dt)) + d0)
    avg_gradient = dy / dt

    return avg_gradient