import numpy as np

EPS = 1e-6
OM_UAM = (np.pi**3)/100.0  # ≈ 0.3101

def beta_dev(w):
    """
    Deviation: |1 - 2 sin(w/2) / w| with small-angle limit w^2/24.
    Vectorized (accepts scalar or array).
    """
    w = np.asarray(w, dtype=float)
    out = np.empty_like(w, dtype=float)
    small = np.abs(w) < 1e-6
    out[small] = (w[small]**2)/24.0
    ws = w[~small]
    if ws.size:
        out[~small] = np.abs(1.0 - (2.0*np.sin(ws/2.0))/ws)
    return out

def _f_w(w, z):
    # (1+z) cos^2 w - exp(-tan w) = 0
    return (1.0 + z)*(np.cos(w)**2) - np.exp(-np.tan(w))

def solve_w_of_z(z, eps=EPS):
    """
    Solve for w(z) on principal branch in (-pi/2+eps, pi/2-eps)
    via sign-change bracketing on a fine grid + bisection.
    Vectorized over z.
    """
    z = np.asarray(z, dtype=float)
    lo = -np.pi/2 + eps
    hi =  np.pi/2 - eps
    grid = np.linspace(lo, hi, 2049)
    res = np.empty_like(z, dtype=float)

    zr = z.ravel()
    for i, zi in enumerate(zr):
        fi = _f_w(grid, zi)
        sgn = np.sign(fi)
        idx = np.where(sgn[:-1]*sgn[1:] <= 0)[0]

        if idx.size == 0:
            # Fallback: pick grid point with smallest |f|
            res.flat[i] = grid[np.argmin(np.abs(fi))]
            continue

        # Choose interval whose midpoint is closest to zero
        mid = 0.5*(grid[idx] + grid[idx+1])
        j = idx[np.argmin(np.abs(mid))]
        a, b = grid[j], grid[j+1]
        fa, fb = _f_w(a, zi), _f_w(b, zi)

        # Bisection refinement
        for _ in range(60):
            m = 0.5*(a+b)
            fm = _f_w(m, zi)
            if fa*fm <= 0:
                b, fb = m, fm
            else:
                a, fa = m, fm
        res.flat[i] = 0.5*(a+b)

    return res.reshape(z.shape)

def E2_uam(z, Om=OM_UAM, eps=EPS):
    """
    UAM E(z)^2 with fixed Om, using beta_dev and w(z).
    """
    z = np.asarray(z, dtype=float)
    w = solve_w_of_z(z, eps=eps)
    sec2 = 1.0/(np.cos(w)**2)
    beta = beta_dev(w)
    t = 1.0 + beta * (z/(1.0+z))
    return Om*(1.0+z)**3 + (1.0-Om)*sec2*(1.0/(t*t))
