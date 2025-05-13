def ziterations(c, max_iter):
    """
    Perform iterations of z based on c, stopping when we reach max_iter iterations.
    
    Parameters:
        c: complex
            Starting complex number.
        max_iter : int
            Maximum number of iterations.
    
    Returns:
        (0 if convergent, 1 if divergent), number of steps to divergence
    """
    z = 0
    i = 0
    while abs(z)**2 < 4 and i <= max_iter:
        z = z**2 + c
        i += 1
    if abs(z)**2 < 4:
        return 0, i # convergent
    else:
        return 1, i # divergent
    
def lorenz(t, W, sigma=10., r=28., b=8./3.):
    """
    Compute the time derivative of the Lorenz system.

    Parameters:
        W : list
            List of three variables [x, y, z].
        sigma : float
            Parameter sigma.
        r : float
            Parameter r.
        b : float
            Parameter b.

    Returns:
        Time derivative of the Lorenz system [dx/dt, dy/dt, dz/dt]. (list)
    """
    x, y, z = W
    dxdt = -1 * sigma * (x - y)
    dydt = r * x - y - x * z
    dzdt = x * y - b * z
    return [dxdt, dydt, dzdt]
