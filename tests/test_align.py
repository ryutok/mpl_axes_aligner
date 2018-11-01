import pytest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from mpl_axes_aligner import align

fig = plt.figure()


@pytest.mark.parametrize('pos', [-10, 0, 1, 10])
def test_yaxes_pos_ValueError(pos):
    fig.clear()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()
    org1 = 0.0
    org2 = 0.0
    with pytest.raises(ValueError):
        align.yaxes(ax1, org1, ax2, org2, pos)


@pytest.mark.parametrize('pos', [-10, 0, 1, 10])
def test_xaxes_pos_ValueError(pos):
    fig.clear()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twiny()
    org1 = 0.0
    org2 = 0.0
    with pytest.raises(ValueError):
        align.xaxes(ax1, org1, ax2, org2, pos)


def test_yaxes_axes_TypeError():
    fig.clear()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()
    ax3 = ax1.get_yaxis()
    org1 = 0.0
    org2 = 0.0
    pos = 0.5
    with pytest.raises(TypeError):
        align.yaxes(ax3, org1, ax2, org2, pos)
    with pytest.raises(TypeError):
        align.yaxes(ax1, org1, ax3, org2, pos)


def test_xaxes_axes_TypeError():
    fig.clear()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twiny()
    ax3 = ax1.get_xaxis()
    org1 = 0.0
    org2 = 0.0
    pos = 0.5
    with pytest.raises(TypeError):
        align.xaxes(ax3, org1, ax2, org2, pos)
    with pytest.raises(TypeError):
        align.xaxes(ax1, org1, ax3, org2, pos)


# def test_calc_range_simple1():
#     org1 = 0.0
#     org2 = 0.0
#     lim1 = [-1.0, 0.0]
#     lim2 = [0.0, 1.0]
#     pos = 0.5
#     alim1, alim2 = align._calc_range(org1, org2, lim1, lim2, pos)
#     assert alim1 == [-1.0, 1.0]
#     assert alim2 == [-1.0, 1.0]


# def test_calc_range_simple2():
#     org1 = 0.0
#     org2 = 0.0
#     lim1 = [-1.0, 0.0]
#     lim2 = [0.0, 1.0]
#     pos = None
#     alim1, alim2 = align._calc_range(org1, org2, lim1, lim2, pos)
#     assert alim1 == [-1.0, 1.0]
#     assert alim2 == [-1.0, 1.0]


def test_yaxes_simple1():
    fig.clear()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()
    ax1.set_ylim(-1.0, 0.0)
    ax2.set_ylim(0.0, 1.0)
    org1 = 0.0
    org2 = 0.0
    pos = 0.5
    align.yaxes(ax1, org1, ax2, org2, pos)
    assert ax1.get_ylim() == (-1.0, 1.0)
    assert ax2.get_ylim() == (-1.0, 1.0)


def test_xaxes_simple1():
    fig.clear()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twiny()
    ax1.set_xlim(-1.0, 0.0)
    ax2.set_xlim(0.0, 1.0)
    org1 = 0.0
    org2 = 0.0
    pos = 0.5
    align.xaxes(ax1, org1, ax2, org2, pos)
    assert ax1.get_xlim() == (-1.0, 1.0)
    assert ax2.get_xlim() == (-1.0, 1.0)


def test_yaxes_simple2():
    fig.clear()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()
    ax1.set_ylim(-1.0, 0.0)
    ax2.set_ylim(0.0, 1.0)
    org1 = 0.0
    org2 = 0.0
    align.yaxes(ax1, org1, ax2, org2)
    assert ax1.get_ylim() == (-1.0, 1.0)
    assert ax2.get_ylim() == (-1.0, 1.0)


def test_xaxes_simple2():
    fig.clear()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twiny()
    ax1.set_xlim(-1.0, 0.0)
    ax2.set_xlim(0.0, 1.0)
    org1 = 0.0
    org2 = 0.0
    align.xaxes(ax1, org1, ax2, org2)
    assert ax1.get_xlim() == (-1.0, 1.0)
    assert ax2.get_xlim() == (-1.0, 1.0)


def test_yaxes_inverted():
    fig.clear()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()
    ax1.set_ylim(1.0, -1.0)
    ax2.set_ylim(1.5, 0.0)
    org1 = 0.0
    org2 = 0.0
    pos = 0.5
    align.yaxes(ax1, org1, ax2, org2, pos)
    lim1 = list(ax1.get_ylim())
    lim2 = list(ax2.get_ylim())
    assert lim1[0] > lim1[1]
    assert lim2[0] > lim2[1]


def test_xaxes_inverted():
    fig.clear()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twiny()
    ax1.set_xlim(1.0, -1.0)
    ax2.set_xlim(1.5, 0.0)
    org1 = 0.0
    org2 = 0.0
    pos = 0.5
    align.xaxes(ax1, org1, ax2, org2, pos)
    lim1 = list(ax1.get_xlim())
    lim2 = list(ax2.get_xlim())
    assert lim1[0] > lim1[1]
    assert lim2[0] > lim2[1]
