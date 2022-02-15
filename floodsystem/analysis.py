# Not Copyright (¬C) 2022 Greg S. Kurzepa

"""
This module contains functions that aid with analysis of flood data.
"""

import matplotlib
import numpy as np

def polyfit(dates, levels, p):
    """Returns the polynomial object of a degree p least-squares polynomial fit to the dates, levels input."""

    dates_float = matplotlib.dates.date2num(dates)
    d0 = -1*dates_float[0]

    p_coeff = np.polyfit(dates_float + d0, levels, p)
    poly = np.poly1d(p_coeff)

    return poly, d0