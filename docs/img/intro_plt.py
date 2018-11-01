import os
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0, os.path.abspath('../../'))

from mpl_axes_aligner import align


def main():
    x = np.arange(0.0, 30, 0.1)
    y1 = 0.1 * x * np.sin(x)
    y2 = 0.001*x**3 - 0.03*x**2 + 0.12*x

    fig = plt.figure(figsize=(10, 4))
    ax11 = fig.add_subplot(121)
    ax12 = ax11.twinx()

    ax11.plot(x, y1, color='blue', label='plot 1')
    ax12.plot(x, y2, color='red', label='plot 2')
    ax11.hlines(y=0, xmin=0, xmax=30)

    ax11.set_title('Original')
    ax11.set_ylabel('Plot 1', color='blue')
    ax12.set_ylabel('Plot 2', color='red')
    ax11.set_xlim(0.0, 30.0)

    ax21 = fig.add_subplot(122)
    ax22 = ax21.twinx()

    ax21.plot(x, y1, color='blue', label='plot 1')
    ax22.plot(x, y2, color='red', label='plot 2')
    ax21.hlines(y=0, xmin=0, xmax=30)

    ax21.set_title('Using mpl_axes_aligner.align')
    ax21.set_ylabel('Plot 1', color='blue')
    ax22.set_ylabel('Plot 2', color='red')
    ax21.set_xlim(0.0, 30.0)

    align.yaxes(ax21, 0, ax22, 0, 0.5)
    plt.tight_layout()
    plt.savefig("intro_plt.png")


if __name__ == '__main__':
    main()
