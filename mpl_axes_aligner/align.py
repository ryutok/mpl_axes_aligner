from mpl_axes_aligner import shift


def _calc_rorg(org, ival, fval):
    rorg = (org - ival) / (fval - ival)
    if rorg < 0:
        rorg = 0
        ival = org
    elif rorg > 1:
        rorg = 1
        fval = org
    return rorg, ival, fval


def _calc_pos(org1, org2, lim1, lim2):
    ival1, fval1 = lim1
    ival2, fval2 = lim2

    rorg1, ival1, fval1 = _calc_rorg(org1, ival1, fval1)
    rorg2, ival2, fval2 = _calc_rorg(org2, ival2, fval2)
    pos = (rorg1 + rorg2) / 2

    if pos == 0 or pos == 1:
        raise ValueError("When pos=None, at least one origin should be "
                         "within the initial plotting range.")

    return pos


def yaxes(ax1, org1, ax2, org2, pos=None):
    """
    Adjust the plotting range of two y axes to align the origins with
    the position.

    Parameters
    ----------
    ax1 : matplotlib.axes.Axes
        First axis object of matplotlib.
    org1 : float
        Origin of first axis to be aligned.
    ax2 : matplotlib.axes.Axes
        Second axis object of matplotlib.
    org2 : float
        Origin of second axis to be aligned.
    pos : float or None, optional
        Relative position to align the origins [0 < pos < 1].
        When pos is None, the origins are aligned to the middle of them.

    Returns
    -------

    Raises
    ------
    TypeError
        If 'ax1' and/or 'ax2' are not the Axes object of matplotlib.
    ValueError
        If 'pos' is less than or equal to 0, or more than or equal to 1.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> from mpl_axes_aligner import align
    >>> fig = plt.figure()
    >>> ax1 = fig.add_subplot(111)
    >>> ax2 = ax1.twinx()
    >>> ax1.set_ylim(-1.0, 0.0)
    (-1.0, 0.0)
    >>> ax2.set_ylim(0.0, 1.0)
    (0.0, 1.0)
    >>> align.yaxes(ax1, -0.3, ax2, 0.3, 0.5)
    >>> ax1.get_ylim()
    (-1.0, 0.4)
    >>> ax2.get_ylim()
    (-0.4, 1.0)
    """

    if pos is None:
        # Get plotting ranges
        try:
            lim1 = list(ax1.get_ylim())
            lim2 = list(ax2.get_ylim())
        except AttributeError or TypeError:
            raise TypeError("'ax1' and 'ax2' should be Axes objects of "
                            "matplotlib.")

        # Calculate the position
        pos = _calc_pos(org1, org2, lim1, lim2)

    elif pos <= 0 or pos >= 1:
        raise ValueError("The position to align the origins should be "
                         "0 < pos < 1.")

    # Apply the new ranges
    shift.yaxis(ax1, org1, pos, True)
    shift.yaxis(ax2, org2, pos, True)


def xaxes(ax1, org1, ax2, org2, pos=None):
    """
    Adjust the plotting range of two x axes to align the origins with
    the position.

    Parameters
    ----------
    ax1 : matplotlib.axes.Axes
        First axis object of matplotlib.
    org1 : float
        Origin of first axis to be aligned.
    ax2 : matplotlib.axes.Axes
        Second axis object of matplotlib.
    org2 : float
        Origin of second axis to be aligned.
    pos : float or None, optional
        Relative position to align the origins [0 < pos < 1].
        When pos is None, the origins are aligned to the middle of them.

    Returns
    -------

    Raises
    ------
    TypeError
        If 'ax1' and/or 'ax2' are not the Axes object of matplotlib.
    ValueError
        If 'pos' is less than or equal to 0, or more than or equal to 1.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> from mpl_axes_aligner import align
    >>> fig = plt.figure()
    >>> ax1 = fig.add_subplot(111)
    >>> ax2 = ax1.twiny()
    >>> ax1.set_xlim(-1.0, 0.0)
    (-1.0, 0.0)
    >>> ax2.set_xlim(0.0, 1.0)
    (0.0, 1.0)
    >>> align.xaxes(ax1, -0.3, ax2, 0.3, 0.5)
    >>> ax1.get_xlim()
    (-1.0, 0.4)
    >>> ax2.get_xlim()
    (-0.4, 1.0)
    """

    if pos is None:
        # Get plotting ranges
        try:
            lim1 = list(ax1.get_xlim())
            lim2 = list(ax2.get_xlim())
        except AttributeError or TypeError:
            raise TypeError("'ax1' and 'ax2' should be Axes objects of "
                            "matplotlib.")

        # Calculate the position
        pos = _calc_pos(org1, org2, lim1, lim2)

    elif pos <= 0 or pos >= 1:
        raise ValueError("The position to align the origins should be "
                         "0 < pos < 1.")

    # Apply the new ranges
    shift.xaxis(ax1, org1, pos, True)
    shift.xaxis(ax2, org2, pos, True)
