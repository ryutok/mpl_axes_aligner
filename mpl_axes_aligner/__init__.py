"""Adjust the plotting range of `matplotlib.axes.Axes` objects to align
the origins with the given position.
"""

from . import shift
from . import align

name = 'mpl_axes_aligner'

__all__ = ["shift", "align"]
