#import pytest
#import matplotlib
#matplotlib.use('Agg')
#import matplotlib.pyplot as plt
#
from mpl_axes_aligner import shift


def test_expand_range_simple():
    org = 0.0
    ival = 0.0
    fval = 1.0
    pos = 0.5
    ival, fval = shift._expand_range(org, pos, ival, fval)
    assert round(ival, 15) == -1.0
    assert round(fval, 15) == 1.0


def test_expand_range_inverted():
    org = 0.0
    ival = 1.0
    fval = 0.0
    pos = 0.5
    ival, fval = shift._expand_range(org, pos, ival, fval)
    assert round(ival, 15) == 1.0
    assert round(fval, 15) == -1.0


def test_expand_range_outrange_n():
    org = -0.5
    ival = 0.0
    fval = 1.0
    pos = 0.5
    ival, fval = shift._expand_range(org, pos, ival, fval)
    assert round(ival, 15) == -2.0
    assert round(fval, 15) == 1.0


def test_expand_range_outrange_p():
    org = 1.5
    ival = 0.0
    fval = 1.0
    pos = 0.5
    ival, fval = shift._expand_range(org, pos, ival, fval)
    assert round(ival, 15) == 0.0
    assert round(fval, 15) == 3.0


def test_shift_range_simple():
    org = 0.2
    ival = 0.0
    fval = 1.0
    pos = 0.5
    ival, fval = shift._shift_range(org, pos, ival, fval)
    assert round(ival, 15) == -0.3
    assert round(fval, 15) == 0.7


def test_shift_range_inverted():
    org = 0.2
    ival = 1.0
    fval = 0.0
    pos = 0.5
    ival, fval = shift._shift_range(org, pos, ival, fval)
    assert round(ival, 15) == 1.3
    assert round(fval, 15) == 0.3


def test_shift_range_outrange_n():
    org = -0.5
    ival = 0.0
    fval = 1.0
    pos = 0.5
    ival, fval = shift._shift_range(org, pos, ival, fval)
    assert round(ival, 15) == -1.0
    assert round(fval, 15) == 0.0


def test_shift_range_outrange_p():
    org = 1.5
    ival = 0.0
    fval = 1.0
    pos = 0.5
    ival, fval = shift._shift_range(org, pos, ival, fval)
    assert round(ival, 15) == 1.0
    assert round(fval, 15) == 2.0
