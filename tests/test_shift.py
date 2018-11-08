import pytest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from mpl_axes_aligner import shift

fig = plt.figure()


def test_expand_range_simple():
    org = 0.0
    ival = 0.0
    fval = 2.0
    pos = 0.5
    ival, fval = shift._expand_range(org, pos, ival, fval)
    assert round(ival, 15) == -2.0
    assert round(fval, 15) == 2.0


def test_expand_range_inverted():
    org = 0.0
    ival = 2.0
    fval = 0.0
    pos = 0.5
    ival, fval = shift._expand_range(org, pos, ival, fval)
    assert round(ival, 15) == 2.0
    assert round(fval, 15) == -2.0


def test_expand_range_outrange_n():
    org = -1.0
    ival = 0.0
    fval = 2.0
    pos = 0.5
    ival, fval = shift._expand_range(org, pos, ival, fval)
    assert round(ival, 15) == -4.0
    assert round(fval, 15) == 2.0


def test_expand_range_outrange_p():
    org = 3.0
    ival = 0.0
    fval = 2.0
    pos = 0.5
    ival, fval = shift._expand_range(org, pos, ival, fval)
    assert round(ival, 15) == 0.0
    assert round(fval, 15) == 6.0


def test_shift_range_simple():
    org = 0.5
    ival = 0.0
    fval = 2.0
    pos = 0.5
    ival, fval = shift._shift_range(org, pos, ival, fval)
    assert round(ival, 15) == -0.5
    assert round(fval, 15) == 1.5


def test_shift_range_inverted():
    org = 0.5
    ival = 2.0
    fval = 0.0
    pos = 0.5
    ival, fval = shift._shift_range(org, pos, ival, fval)
    assert round(ival, 15) == 1.5
    assert round(fval, 15) == -0.5


def test_shift_range_outrange_n():
    org = -1.0
    ival = 0.0
    fval = 2.0
    pos = 0.5
    ival, fval = shift._shift_range(org, pos, ival, fval)
    assert round(ival, 15) == -2.0
    assert round(fval, 15) == 0.0


def test_shift_range_outrange_p():
    org = 3.0
    ival = 0.0
    fval = 2.0
    pos = 0.5
    ival, fval = shift._shift_range(org, pos, ival, fval)
    assert round(ival, 15) == 2.0
    assert round(fval, 15) == 4.0


@pytest.mark.parametrize('pos', [-2, 2])
def test_yaxis_shift_ValueError(pos):
    fig.clear()
    ax = fig.add_subplot(111)
    org = 0.5
    with pytest.raises(ValueError):
        shift.yaxis(ax, org, pos)


@pytest.mark.parametrize('pos', [-2, 2])
def test_xaxis_shift_ValueError(pos):
    fig.clear()
    ax = fig.add_subplot(111)
    org = 0.5
    with pytest.raises(ValueError):
        shift.xaxis(ax, org, pos)


@pytest.mark.parametrize('pos', [0, 1])
def test_yaxis_shift_NoError(pos):
    fig.clear()
    ax = fig.add_subplot(111)
    org = 0.5
    shift.yaxis(ax, org, pos)


@pytest.mark.parametrize('pos', [0, 1])
def test_xaxis_shift_NoError(pos):
    fig.clear()
    ax = fig.add_subplot(111)
    org = 0.5
    shift.xaxis(ax, org, pos)


@pytest.mark.parametrize('pos', [-2, 0, 1, 2])
def test_yaxis_expand_ValueError(pos):
    fig.clear()
    ax = fig.add_subplot(111)
    org = 0.5
    with pytest.raises(ValueError):
        shift.yaxis(ax, org, pos, True)


@pytest.mark.parametrize('pos', [-2, 0, 1, 2])
def test_xaxis_expand_ValueError(pos):
    fig.clear()
    ax = fig.add_subplot(111)
    org = 0.5
    with pytest.raises(ValueError):
        shift.xaxis(ax, org, pos, True)


def test_yaxes_expand_simple():
    fig.clear()
    ax = fig.add_subplot(111)
    ax.set_xlim(0.0, 1.0)
    org = 0.0
    pos = 0.5
    shift.yaxis(ax, org, pos, True)
    assert ax.get_ylim() == (-1.0, 1.0)


def test_xaxes_expand_simple():
    fig.clear()
    ax = fig.add_subplot(111)
    ax.set_xlim(0.0, 1.0)
    org = 0.0
    pos = 0.5
    shift.xaxis(ax, org, pos, True)
    assert ax.get_xlim() == (-1.0, 1.0)
