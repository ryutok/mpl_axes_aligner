import os
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0, os.path.abspath('../../'))

from mpl_axes_aligner import shift


def main1():
    x = np.arange(0.0, 12, 0.1)
    y = 0.1 * x * np.sin(x)

    fig = plt.figure(figsize=(3.4, 2.55), dpi=100)
    ax = fig.add_subplot(111)

    ax.plot(x, y, color='blue', label='plot 1')
    ax.hlines(y=0, xmin=0, xmax=30, linewidth=1)

    ax.set_title('Original')
    ax.set_ylabel('Plot 1', color='blue')
    ax.set_xlim(0.0, 12.0)

    plt.tight_layout()
    plt.savefig("shift_plt1.png")


def main2():
    x = np.arange(0.0, 12, 0.1)
    y = 0.1 * x * np.sin(x)

    fig = plt.figure(figsize=(3.4, 2.55), dpi=100)
    ax = fig.add_subplot(111)

    ax.plot(x, y, color='blue', label='plot 1')
    ax.hlines(y=0, xmin=0, xmax=30, linewidth=1)

    ax.set_title('shift.yaxis(ax, 0, 0.5, True)')
    ax.set_ylabel('Plot 1', color='blue')
    ax.set_xlim(0.0, 12.0)

    shift.yaxis(ax, 0, 0.5, True)
    plt.tight_layout()
    plt.savefig("shift_plt2.png")


def main3():
    x = np.arange(0.0, 12, 0.1)
    y = 0.1 * x * np.sin(x)

    fig = plt.figure(figsize=(6.8, 2.55), dpi=100)

    ax1 = fig.add_subplot(121)
    ax1.plot(x, y, color='blue', label='plot 1')
    ax1.hlines(y=-0.5, xmin=0, xmax=30, linewidth=1)

    ax1.set_title('shift.yaxis(ax, -0.5, 0.5, True)')
    ax1.set_ylabel('Plot 1', color='blue')
    ax1.set_xlim(0.0, 12.0)
    shift.yaxis(ax1, -0.5, 0.5, True)

    ax2 = fig.add_subplot(122)
    ax2.plot(x, y, color='blue', label='plot 1')
    ax2.hlines(y=0.2, xmin=0, xmax=30, linewidth=1)

    ax2.set_title('shift.yaxis(ax, 0.2, 0.5, True)')
    ax2.set_ylabel('Plot 1', color='blue')
    ax2.set_xlim(0.0, 12.0)
    shift.yaxis(ax2, 0.2, 0.5, True)

    plt.tight_layout()
    plt.savefig("shift_plt3.png")


def main4():
    x = np.arange(0.0, 12, 0.1)
    y = 0.1 * x * np.sin(x)

    fig = plt.figure(figsize=(6.8, 2.55), dpi=100)

    ax1 = fig.add_subplot(121)
    ax1.plot(x, y, color='blue', label='plot 1')
    ax1.hlines(y=0, xmin=0, xmax=30, linewidth=1)

    ax1.set_title('shift.yaxis(ax, 0, 0.2, True)')
    ax1.set_ylabel('Plot 1', color='blue')
    ax1.set_xlim(0.0, 12.0)
    shift.yaxis(ax1, 0, 0.2, True)

    ax2 = fig.add_subplot(122)
    ax2.plot(x, y, color='blue', label='plot 1')
    ax2.hlines(y=0, xmin=0, xmax=30, linewidth=1)

    ax2.set_title('shift.yaxis(ax, 0, 0.8, True)')
    ax2.set_ylabel('Plot 1', color='blue')
    ax2.set_xlim(0.0, 12.0)
    shift.yaxis(ax2, 0, 0.8, True)

    plt.tight_layout()
    plt.savefig("shift_plt4.png")


def main5():
    x = np.arange(0.0, 12, 0.1)
    y = 0.1 * x * np.sin(x)

    fig = plt.figure(figsize=(6.8, 2.55), dpi=100)

    ax1 = fig.add_subplot(121)
    ax1.plot(x, y, color='blue', label='plot 1')
    ax1.hlines(y=0, xmin=0, xmax=30, linewidth=1)

    ax1.set_title('shift.yaxis(ax, 0, 0.2, True)')
    ax1.set_ylabel('Plot 1', color='blue')
    ax1.set_xlim(0.0, 12.0)
    shift.yaxis(ax1, 0, 0.2, True)

    ax2 = fig.add_subplot(122)
    ax2.plot(x, y, color='blue', label='plot 1')
    ax2.hlines(y=0, xmin=0, xmax=30, linewidth=1)

    ax2.set_title('shift.yaxis(ax, 0, 0.2, False)')
    ax2.set_ylabel('Plot 1', color='blue')
    ax2.set_xlim(0.0, 12.0)
    shift.yaxis(ax2, 0, 0.2, False)

    plt.tight_layout()
    plt.savefig("shift_plt5.png")


if __name__ == '__main__':
    main1()
    main2()
    main3()
    main4()
    main5()
