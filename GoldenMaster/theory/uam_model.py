
"""
UAM core cosmology primitives.

Definitions:
  - β_dev(w) = | 1 - 2 sin(w/2) / w |, with β_dev(0)=0 and small-angle limit β_dev ~ w^2 / 24.
  - Solve w(z) from the transcendental equation:
        (1 + z) * cos(w)^2 = exp( -tan(w) )
    for w ∈ (-π/2 + ε, π/2 - ε). For cosmological SN redshifts we take the branch
    that approaches w(0)=0 continuously and remains finite on z ∈ [0, 2.3].
  - E^2(z) = Ω_m (1+z)^3 + (1 - Ω_m) * sec(w(z))^2 * [ 1 / (1 + β_dev(w(z)) * z/(1+z)) ]^2
    with Ω_m,UAM = π^3 / 100 (parameter-free).
"""

from __future__ import annotations

import numpy as np
from numpy import pi
from typing import Union

# Only imported when solving; keeps import lightweight if SciPy isn’t used by caller
from scipy.optimize import brentq, root_scalar

# Numerical safety
_EPS_W = 1.0e-6        # angular bracket safety near ±π/2
_EPS_SMALL_W = 1.0e-4  # threshold for small-angle series
_EPS_Z = 1.0e-12       # treat as z≈0

def _safe_tan(w: np.ndarray) -> np.ndarray:
    return np.tan(w)

def _safe_cos(w: np.ndarray) -> np.ndarray:
    return np.cos(w)

def beta_dev(w: Union[float, np.ndarray]) -> np.ndarray:
    """
    β_dev(w) = |1 - 2 sin(w/2) / w|, with accurate small-angle evaluation.

    For |w| < 1e-4, use the series of the deviation:
      2 sin(w/2)/w ≈ 1 - w^2/24 + 7 w^4/5760 - 31 w^6/967680
      => β_dev ≈ w^2/24 - 7 w^4/5760 + 31 w^6/967680
    """
    w = np.asarray(w, dtype=float)
    out = np.empty_like(w)

    m_small = np.abs(w) < _EPS_SMALL_W
    if np.any(m_small):
        ws = w[m_small]
        w2 = ws*ws
        # series: w^2/24 - 7 w^4/5760 + 31 w^6/967680
        out[m_small] = np.abs(w2/24.0 - 7.0*w2*w2/5760.0 + 31.0*w2*w2*w2/967680.0)
    if np.any(~m_small):
        wl = w[~m_small]
        ratio = 2.0*np.sin(wl*0.5)/wl
        out[~m_small] = np.abs(1.0 - ratio)

    # Ensure exact zero at w=0
    out = np.where(w == 0.0, 0.0, out)
    return out

def _transcendental(w: float, z: float) -> float:
    """f(w; z) = (1+z) * cos(w)^2 - exp(-tan(w))."""
    c = np.cos(w)
    return (1.0+z)*c*c - np.exp(-np.tan(w))

def solve_w_of_z(z: Union[float, np.ndarray]) -> np.ndarray:
    """
    Solve (1+z) * cos(w)^2 = exp(-tan(w)) for w ∈ (-π/2+ε, π/2-ε),
    selecting the branch that is continuous from w(0)=0.

    Strategy per z:
      1) Handle very small z with w=0.
      2) Bracket on a dense grid within (-π/2+ε, π/2-ε); if a sign change exists,
         refine with Brent's method.
      3) If no sign change, pick the grid point minimizing |f| and use a secant step
         via root_scalar, falling back to that minimizer if needed.
    """
    z = np.asarray(z, dtype=float)
    out = np.empty_like(z)

    a = -pi/2 + _EPS_W
    b = +pi/2 - _EPS_W

    # Pre-make grid
    grid = np.linspace(a, b, 2049)

    for idx, zz in np.ndenumerate(z):
        if zz < _EPS_Z:
            out[idx] = 0.0
            continue

        # Evaluate on grid (mask non-finite)
        vals = _transcendental(grid, float(zz))
        finite = np.isfinite(vals)
        gg = grid[finite]
        vv = vals[finite]

        root = None

        # Try to find a sign change
        if gg.size >= 2:
            s = vv[:-1]*vv[1:]
            sign_change = np.where(s <= 0)[0]
            for k in sign_change[:3]:  # try up to a few intervals
                x0, x1 = gg[k], gg[k+1]
                if np.isfinite(_transcendental(x0, zz)) and np.isfinite(_transcendental(x1, zz)):
                    try:
                        root = brentq(_transcendental, float(x0), float(x1), args=(float(zz),), maxiter=100, xtol=1e-12)
                        break
                    except Exception:
                        pass

        if root is None:
            # Best grid point by |f|
            j = int(np.nanargmin(np.abs(vv)))
            x0 = float(gg[j])
            # Try a secant step around x0
            x1 = float(np.clip(x0 + 1e-3, a, b))
            try:
                rs = root_scalar(lambda w: _transcendental(w, float(zz)),
                                 x0=x0, x1=x1, method="secant", maxiter=100, xtol=1e-12)
                if rs.converged and np.isfinite(rs.root):
                    root = float(rs.root)
            except Exception:
                root = None

        out[idx] = float(root) if (root is not None) else x0

    # Ensure continuity near z=0 (tiny negative noise to zero)
    out = np.where(np.abs(z) < _EPS_Z, 0.0, out)
    return out

def E2_uam(z: Union[float, np.ndarray], Om: float = (pi**3)/100.0) -> np.ndarray:
    """
    UAM E^2(z) per the specified form with fixed Ω_m = π^3 / 100 by default.
    """
    z = np.asarray(z, dtype=float)
    w = solve_w_of_z(z)
    sec2 = 1.0 / (np.cos(w)**2)
    beta = beta_dev(w)
    # time/redshift modulation factor
    fac = 1.0 / (1.0 + beta * (z / (1.0 + z)))
    e2 = Om * (1.0 + z)**3 + (1.0 - Om) * sec2 * (fac**2)
    return e2
