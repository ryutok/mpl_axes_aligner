import os
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0, os.path.abspath('../../'))

from mpl_axes_aligner import align


def main1():
    x = np.arange(0.0, 30, 0.1)
    y1 = 0.1 * x * np.sin(x)
    y2 = 0.001*x**3 - 0.03*x**2 + 0.12*x

    fig = plt.figure(figsize=(3.4, 2.55), dpi=100)
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()

    ax1.plot(x, y1, color='blue', label='plot 1')
    ax2.plot(x, y2, color='red', label='plot 2')
    ax1.hlines(y=0, xmin=0, xmax=30, linewidth=1)

    ax1.set_title('Original')
    ax1.set_ylabel('Plot 1', color='blue')
    ax2.set_ylabel('Plot 2', color='red')
    ax1.set_xlim(0.0, 30.0)

    plt.tight_layout()
    plt.savefig("align_plt1.png")


def main2():
    x = np.arange(0.0, 30, 0.1)
    y1 = 0.1 * x * np.sin(x)
    y2 = 0.001*x**3 - 0.03*x**2 + 0.12*x

    fig = plt.figure(figsize=(3.4, 2.55), dpi=100)
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()

    ax1.plot(x, y1, color='blue', label='plot 1')
    ax2.plot(x, y2, color='red', label='plot 2')
    ax1.hlines(y=0, xmin=0, xmax=30, linewidth=1)

    ax1.set_title('align.yaxes(ax1, 0, ax2, 0, 0.5)')
    ax1.set_ylabel('Plot 1', color='blue')
    ax2.set_ylabel('Plot 2', color='red')
    ax1.set_xlim(0.0, 30.0)

    align.yaxes(ax1, 0, ax2, 0, 0.5)
    plt.tight_layout()
    plt.savefig("align_plt2.png")


def main3():
    x = np.arange(0.0, 30, 0.1)
    y1 = 0.1 * x * np.sin(x)
    y2 = 0.001*x**3 - 0.03*x**2 + 0.12*x

    fig = plt.figure(figsize=(6.8, 2.55), dpi=100)
    ax11 = fig.add_subplot(121)
    ax12 = ax11.twinx()

    ax11.plot(x, y1, color='blue', label='plot 1')
    ax12.plot(x, y2, color='red', label='plot 2')
    ax11.hlines(y=0, xmin=0, xmax=30, linewidth=1)

    ax11.set_title('align.yaxes(ax1, 0, ax2, 0, 0.2)')
    ax11.set_ylabel('Plot 1', color='blue')
    ax12.set_ylabel('Plot 2', color='red')
    ax11.set_xlim(0.0, 30.0)

    ax21 = fig.add_subplot(122)
    ax22 = ax21.twinx()

    ax21.plot(x, y1, color='blue', label='plot 1')
    ax22.plot(x, y2, color='red', label='plot 2')
    ax21.hlines(y=0, xmin=0, xmax=30, linewidth=1)

    ax21.set_title('align.yaxes(ax1, 0, ax2, 0, 0.8)')
    ax21.set_ylabel('Plot 1', color='blue')
    ax22.set_ylabel('Plot 2', color='red')
    ax21.set_xlim(0.0, 30.0)

    align.yaxes(ax11, 0, ax12, 0, 0.2)
    align.yaxes(ax21, 0, ax22, 0, 0.8)
    plt.tight_layout()
    plt.savefig("align_plt3.png")


def main4():
    x = np.arange(0.0, 30, 0.1)
    y1 = 0.1 * x * np.sin(x)
    y2 = 0.001*x**3 - 0.03*x**2 + 0.12*x

    fig = plt.figure(figsize=(3.4, 2.55), dpi=100)
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()

    ax1.plot(x, y1, color='blue', label='plot 1')
    ax2.plot(x, y2, color='red', label='plot 2')
    ax1.hlines(y=0, xmin=0, xmax=30, linewidth=1)

    ax1.set_title('align.yaxes(ax1, 0, ax2, 0, None)')
    ax1.set_ylabel('Plot 1', color='blue')
    ax2.set_ylabel('Plot 2', color='red')
    ax1.set_xlim(0.0, 30.0)

    align.yaxes(ax1, 0, ax2, 0, None)
    plt.tight_layout()
    plt.savefig("align_plt4.png")


def main5():
    x = np.arange(0.0, 30, 0.1)
    y1 = 0.1 * x * np.sin(x)
    y2 = 0.001*x**3 - 0.03*x**2 + 0.12*x

    fig = plt.figure(figsize=(3.4, 2.55), dpi=100)
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()

    ax1.plot(x, y1, color='blue', label='plot 1')
    ax2.plot(x, y2, color='red', label='plot 2')
    ax1.hlines(y=0, xmin=0, xmax=30, linewidth=1)

    ax1.set_title('align.yaxes(ax1, 0, ax2, 2, 0.5)')
    ax1.set_ylabel('Plot 1', color='blue')
    ax2.set_ylabel('Plot 2', color='red')
    ax1.set_xlim(0.0, 30.0)

    align.yaxes(ax1, 0, ax2, 2, 0.5)
    plt.tight_layout()
    plt.savefig("align_plt5.png")


if __name__ == '__main__':
    main1()
    main2()
    main3()
    main4()
    main5()
