def _expand_range(org, pos, ival, fval):
    if pos <= 0 or pos >= 1:
        raise ValueError("When expand=True, the position to align the origin "
                         "should be 0 < pos < 1.")

    rorg = (org - ival) / (fval - ival)
    if rorg > pos:
        fval = (org - ival + pos*ival) / pos
    else:
        ival = (org - pos*fval) / (1 - pos)
    return ival, fval


def _shift_range(org, pos, ival, fval):
    if pos < 0 or pos > 1:
        raise ValueError("The position to align the origin should be "
                         "0 <= pos <= 1.")

    rorg = (org - ival) / (fval - ival)
    diff = rorg - pos
    return ival+diff, fval+diff


def yaxis(ax, org, pos, expand=False):
    """
    Adjust the plotting range of y axis to shift the origin to the
    position.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Matplotlib axes object.
    org : float
        Origin be shifted.
    pos : float
        Relative position of the shifted origin [0 < pos < 1].
    expand : bool
        When it is True, the plotting range is expanded to remain the
        initial range. Otherwise, the range is simply shifted.

    Returns
    -------
    None
    """

    try:
        bottom, top = ax.get_ylim()
    except AttributeError or TypeError:
        raise TypeError("'ax' should be Axes objects of matplotlib.")

    if expand:
        bottom, top = _expand_range(org, pos, bottom, top)
    else:
        bottom, top = _shift_range(org, pos, bottom, top)
    ax.set_ylim(bottom, top)


def xaxis(ax, org, pos, expand=False):
    """
    Adjust the plotting range of x axis to shift the origin to the
    position.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Matplotlib axes object.
    org : float
        Origin be shifted.
    pos : float
        Relative position of the shifted origin [0 < pos < 1].
    expand : bool
        When it is True, the plotting range is expanded to remain the
        initial range. Otherwise, the range is simply shifted.

    Returns
    -------
    None
    """

    try:
        bottom, top = ax.get_xlim()
    except AttributeError or TypeError:
        raise TypeError("'ax' should be Axes objects of matplotlib.")

    if expand:
        bottom, top = _expand_range(org, pos, bottom, top)
    else:
        bottom, top = _shift_range(org, pos, bottom, top)
    ax.set_xlim(bottom, top)
