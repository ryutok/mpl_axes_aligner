=======================
Matplotlib Axes Aligner
=======================

.. image:: https://travis-ci.org/ryutok/mpl_axes_aligner.svg?branch=master
   :target: https://travis-ci.org/ryutok/mpl_axes_aligner
.. image:: https://api.codeclimate.com/v1/badges/86a7122db1585d63fcb9/maintainability
   :target: https://codeclimate.com/github/ryutok/mpl_axes_aligner/maintainability
   :alt: Maintainability
.. image:: https://api.codeclimate.com/v1/badges/86a7122db1585d63fcb9/test_coverage
   :target: https://codeclimate.com/github/ryutok/mpl_axes_aligner/test_coverage
   :alt: Test Coverage
.. image:: https://img.shields.io/pypi/v/nine.svg
   :target: https://pypi.org/project/mpl-axes-aligner/
   :alt: PyPI
.. image:: https://readthedocs.org/projects/matplotlib-axes-aligner/badge/?version=latest
   :target: https://matplotlib-axes-aligner.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. image:: http://img.shields.io/badge/license-MIT-blue.svg?style=flat
   :target: https://github.com/ryutok/mpl_axes_aligner/blob/master/LICENSE


Introduction
============

*Matplotlib axes aligner* (:py:mod:`mpl_axes_aligner`) package contains the modules which adjust the plotting range of `matplotlib.axes.Axes <https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes>`_ objects to align their origins.

When you want to align the y = 0 of plot 1 and plot 2 with the center of the figure, it is done by introducing the function :py:func:`mpl_axes_aligner.align.yaxes`.

.. code-block:: python
   :emphasize-lines: 3,17

   import numpy as np
   import matplotlib.pyplot as plt
   from mpl_axes_aligner import align

   x = np.arange(0.0, 30, 0.1)
   y1 = 0.1 * x * np.sin(x)
   y2 = 0.001*x**3 - 0.03*x**2 + 0.12*x

   fig = plt.figure()
   ax1 = fig.add_subplot(111)
   ax2 = ax1.twinx()

   ax1.plot(x, y1, color='blue', label='Plot 1')
   ax2.plot(x, y2, color='red', label='Plot 2')

   # Align y = 0 of ax1 and ax2 with the center of figure.
   align.yaxes(ax1, 0, ax2, 0, 0.5)

   plt.show()

.. image:: img/intro_plt.png


Table of contents
=================

.. toctree::
   :maxdepth: 2

   installation
   usage
   genindex
   py-modindex

