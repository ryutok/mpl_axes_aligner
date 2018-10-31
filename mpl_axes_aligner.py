def _calc_range(org1, org2, lim1, lim2, pos):
    left1, right1 = lim1
    left2, right2 = lim2

    # Calculate the relative position of origins
    rorg1 = (org1 - left1) / (right1 - left1)
    rorg2 = (org2 - left2) / (right2 - left2)

    if pos is None:
        pos = (rorg1 + rorg2) / 2
    elif pos <= 0 or pos >= 1:
        raise ValueError("The position to align the origins should be "
                         "0 < pos < 1.")

    if rorg1 > pos:
        right1 = (org1 - left1 + pos*left1) / pos
    else:
        left1 = (org1 - pos*right1) / (1 - pos)
    if rorg2 > pos:
        right2 = (org2 - left2 + pos*left2) / pos
    else:
        left2 = (org2 - pos*right2) / (1 - pos)

    return [left1, right1], [left2, right2]


def yaxes(ax1, org1, ax2, org2, pos=None):
    """
    Adjust the plotting range of two y axes to align the given origins
    with the given position.

    Parameters
    ----------
    ax1 : matplotlib.axes.Axes
        First axis.
    org1 : float
        Origin of first axis to be align.
    ax2 : matplotlib.axes.Axes
        Second axis.
    org2 : float
        Origin of second axis to be aligned.
    pos : float
        Relative position to align the origins [0 < pos < 1].
        When pos is None, the origins are aligned to the middle of them.

    Returns
    -------
    None
    """

    # Get plotting ranges
    try:
        lim1 = list(ax1.get_ylim())
        lim2 = list(ax2.get_ylim())
    except AttributeError or TypeError:
        raise TypeError("'ax1' and 'ax2' should be Axes objects of "
                        "matplotlib.")

    # Expand plotting ranges when org1 and/or org2 are out of the ranges
    lim1 = [min(*lim1, org1), max(*lim1, org1)]
    lim2 = [min(*lim2, org2), max(*lim2, org2)]
    if ax1.yaxis_inverted():
        lim1.reverse()
    if ax2.yaxis_inverted():
        lim2.reverse()

    # Calculate the new ranges
    lim1, lim2 = _calc_range(org1, org2, lim1, lim2, pos)

    # Apply the new ranges
    ax1.set_ylim(*lim1)
    ax2.set_ylim(*lim2)


def xaxes(ax1, org1, ax2, org2, pos=None):
    """
    Adjust the plotting range of two x axes to align the given origins
    with the given position.

    Parameters
    ----------
    ax1 : matplotlib.axes.Axes
        First axis.
    org1 : float
        Origin of first axis to be align.
    ax2 : matplotlib.axes.Axes
        Second axis.
    org2 : float
        Origin of second axis to be aligned.
    pos : float
        Relative position to align the origins [0 < pos < 1].
        When pos is None, the origins are aligned to the middle of them.

    Returns
    -------
    None
    """

    # Get plotting ranges
    try:
        lim1 = list(ax1.get_xlim())
        lim2 = list(ax2.get_xlim())
    except AttributeError or TypeError:
        raise TypeError("'ax1' and 'ax2' should be Axes objects of "
                        "matplotlib.")

    # Expand plotting ranges when org1 and/or org2 are out of the ranges
    lim1 = [min(*lim1, org1), max(*lim1, org1)]
    lim2 = [min(*lim2, org2), max(*lim2, org2)]
    if ax1.xaxis_inverted():
        lim1.reverse()
    if ax2.xaxis_inverted():
        lim2.reverse()

    # Calculate the new ranges
    lim1, lim2 = _calc_range(org1, org2, lim1, lim2, pos)

    # Apply the new ranges
    ax1.set_xlim(*lim1)
    ax2.set_xlim(*lim2)
