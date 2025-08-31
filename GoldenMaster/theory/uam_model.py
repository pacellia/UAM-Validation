
import numpy as np
from scipy.optimize import brentq

# Geometric deviation: beta_dev(w) = |1 - 2 sin(w/2)/w|, with beta_dev(0)=0 and ~ w^2/24
def beta_dev(w):
    """Deviation form: |1 - 2*sin(w/2)/w|
    Robust near w→0 using series branch for |w|<1e-4 so that beta_dev ≈ w^2/24.
    Returns scalar for scalar input.
    """
    import numpy as _np
    w_arr = _np.asarray(w, dtype=float)
    out   = _np.empty_like(w_arr, dtype=float)

    small = _np.abs(w_arr) < 1e-4  # widened cutoff to avoid cancellation at 1e-6
    out[small] = (w_arr[small]*w_arr[small]) / 24.0

    mask = ~small
    if _np.any(mask):
        ws = w_arr[mask]
        out[mask] = _np.abs(1.0 - 2.0*_np.sin(0.5*ws)/ws)

    if out.shape == ():  # preserve scalar in -> scalar out
        return float(out)
    return out
def solve_w_of_z
    Solve (1+z)cos^2(w) = exp(-tan(w)) for w in (-pi/2+eps, 0] (non-increasing)
    Vectorized over z, with continuation to ensure monotonicity.
    
def solve_w_of_z(z_arr, eps=1e-6, rtol=1e-12, atol=1e-12, maxiter=200):
    """
    Solve (1+z)cos^2(w) = exp(-tan(w)) for w in (-pi/2+eps, 0] (non-increasing)
    Vectorized over z, with continuation to ensure monotonicity.
    """
    z = np.asarray(z_arr, dtype=float)
    w = np.empty_like(z)
    w_lower = -np.pi/2 + eps
    
    for i, zi in enumerate(z):
        # Upper bound: 0 for first z, else previous w (non-increasing)
        w_upper = 0.0 if i == 0 else min(w[i-1], 0.0)
        
        # Ensure sign change: h(w_lower) < 0, h(w_upper) >= 0
        h_lower = (1.0 + zi) * (np.cos(w_lower)**2) - np.exp(-np.tan(w_lower))
        h_upper = (1.0 + zi) * (np.cos(w_upper)**2) - np.exp(-np.tan(w_upper))
        if not (np.isfinite(h_lower) and np.isfinite(h_upper) and h_lower < 0 and h_upper >= 0):
            w_upper = 0.0  # Reset to ensure sign change if needed
        
        # Brentq with tight tolerances
        w[i] = brentq(lambda w: (1.0 + zi) * (np.cos(w)**2) - np.exp(-np.tan(w)),
                      w_lower, w_upper, xtol=atol, rtol=rtol, maxiter=maxiter)
        
        # Safety clamp (optional, remove if unnecessary)
        if i > 0 and w[i] > w[i-1]:
            w[i] = w[i-1] - 1e-12  # Small downward adjustment
    
    return w
def solve_w_of_z(z_arr, eps=1e-6, rtol=1e-12, atol=1e-12, maxiter=200):
    """
    Solve (1+z)cos^2(w) = exp(-tan(w)) for w in (-pi/2+eps, 0] (non-increasing)
    Vectorized over z, with continuation to ensure monotonicity.
    """
    z = np.asarray(z_arr, dtype=float)
    w = np.empty_like(z)
    w_lower = -np.pi/2 + eps
    
    for i, zi in enumerate(z):
        # Upper bound: 0 for first z, else previous w (non-increasing)
        w_upper = 0.0 if i == 0 else min(w[i-1], 0.0)
        
        # Ensure sign change: h(w_lower) < 0, h(w_upper) >= 0
        h_lower = (1.0 + zi) * (np.cos(w_lower)**2) - np.exp(-np.tan(w_lower))
        h_upper = (1.0 + zi) * (np.cos(w_upper)**2) - np.exp(-np.tan(w_upper))
        if not (np.isfinite(h_lower) and np.isfinite(h_upper) and h_lower < 0 and h_upper >= 0):
            w_upper = 0.0  # Reset to ensure sign change if needed
        
        # Brentq with tight tolerances
        w[i] = brentq(lambda w: (1.0 + zi) * (np.cos(w)**2) - np.exp(-np.tan(w)),
                      w_lower, w_upper, xtol=atol, rtol=rtol, maxiter=maxiter)
        
        # Safety clamp (optional, remove if unnecessary)
        if i > 0 and w[i] > w[i-1]:
            w[i] = w[i-1] - 1e-12  # Small downward adjustment
    
    return w
def root_one(zi):
        if zi < -1.0:
            raise ValueError("z must satisfy z >= -1")
        # h(t) = (1+t^2) e^{-t} - (1+z) ; h(0) = 1 - (1+z) = -z <= 0
        def h(t): return (1.0 + t*t)*np.exp(-t) - (1.0 + zi)
        lo = -50.0
        hlo = h(lo)
        # Ensure sign change: h(lo) > 0 and h(0) <= 0
        tries = 0
        while hlo <= 0.0 and tries < 40:
            lo *= 2.0   # push further negative if needed
            hlo = h(lo)
            tries += 1
        t = brentq(h, lo, 0.0, xtol=xtol, rtol=rtol, maxiter=maxiter)
        return np.arctan(t)

    # vectorize over z
    return np.vectorize(root_one, otypes=[float])(z)

# E^2(z) for UAM:
# E^2 = Ωm (1+z)^3 + (1-Ωm) * sec^2(w(z)) * [ 1 / (1 + beta_dev(w) * z/(1+z)) ]^2
def E2_uam(z, Om=np.pi**3/100.0):
    z = np.asarray(z, dtype=float)
    w = solve_w_of_z(z)
    beta = beta_dev(w)
    fac = 1.0 / (1.0 + beta * (z/(1.0+z)))
    sec2 = 1.0 / (np.cos(w)**2)
    return Om * (1.0+z)**3 + (1.0-Om) * sec2 * (fac*fac)


# === patched beta_dev and solve_w_of_z (2025-08-31) ===
import numpy as _np
from scipy.optimize import brentq

def beta_dev(w):
    """
    Deviation: |1 - 2*sin(w/2)/w| with high-accuracy small-angle series.
    Series up to O(w^8) keeps rel. error vs w^2/24 < 1e-6 near 1e-4.
    """
    w = _np.asarray(w, dtype=float)
    a = _np.abs(w)
    out = _np.empty_like(a)
    small = a < 1e-3
    if small.any():
        wsq = a[small]**2
        out[small] = wsq/24.0 - (wsq**2)/1920.0 + (wsq**3)/322560.0 - (wsq**4)/92897280.0
    if (~small).any():
        ww = a[~small]
        out[~small] = _np.abs(1.0 - (2.0*_np.sin(ww/2.0))/ww)
    return out

def solve_w_of_z(z, eps=1e-6, xtol=1e-12, rtol=1e-12, maxiter=200):
    """
    Solve (1+z)cos^2 w = exp(-tan w) via log-domain root:
      g(w;z) = ln(1+z) + 2 ln cos w + tan w = 0
    Bracket in (-pi/2+eps, -eps), relax eps if needed.
    Enforce non-increasing w with increasing z to suppress tiny numeric wiggles.
    """
    z = _np.asarray(z, dtype=float)
    out = _np.empty_like(z)
    ln1p = _np.log1p
    cos = _np.cos
    tan = _np.tan

    def g(w, zi):
        return ln1p(zi) + 2.0*_np.log(cos(w)) + tan(w)

    for i, zi in enumerate(z):
        if not _np.isfinite(zi) or zi < 0:
            out[i] = _np.nan
            continue
        if zi == 0.0:
            out[i] = 0.0
            continue
        lo = -_np.pi/2 + eps
        hi = -eps
        # relax bracket if needed
        for _ in range(8):
            glo = g(lo, zi)
            ghi = g(hi, zi)
            if _np.isfinite(glo) and _np.isfinite(ghi) and (glo < 0.0) and (ghi > 0.0):
                break
            eps *= 2.0
            lo = -_np.pi/2 + eps
            hi = -max(eps, 1e-9)
        else:
            out[i] = _np.nan
            continue
        out[i] = brentq(lambda w: g(w, zi), lo, hi, xtol=xtol, rtol=rtol, maxiter=maxiter)

    # enforce non-increasing w with increasing z
    if out.size > 1:
        idx = _np.argsort(z, kind="mergesort")
        w_sorted = out[idx].copy()
        # fill NaNs with previous finite to keep monotone pass
        for j in range(w_sorted.size):
            if not _np.isfinite(w_sorted[j]):
                w_sorted[j] = w_sorted[j-1] if j>0 else 0.0
        w_sorted = _np.minimum.accumulate(w_sorted)
        out[idx] = w_sorted
        out[z == 0.0] = 0.0

    return out

# --- PATCH: robust solve_w_of_z (monotonic, bracketing) ---
def solve_w_of_z(z, eps=1e-6, maxiter=200):
    """
    Solve h(w; z) = ln(1+z) + 2*ln(cos w) + tan w = 0 for each z in (-pi/2, pi/2).

    Notes:
      - On (-pi/2, pi/2), h(w) is continuous with limits:
          w -> (-pi/2)+  => h -> -inf
          w -> ( +pi/2)- => h -> +inf
        so there is a unique root in (lo, hi) for any z >= 0.
      - After solving, enforce monotonicity of w(z):
        if median slope dw/dz >= 0 -> project to non-decreasing,
        else -> project to non-increasing.
    """
    import numpy as _np
    from math import pi as _pi, tan as _tan, cos as _cos, log as _log, log1p as _log1p
    from scipy.optimize import brentq as _brentq

    z_arr  = _np.asarray(z, dtype=float)
    z_flat = z_arr.ravel()
    w_flat = _np.empty_like(z_flat)

    lo = -_pi/2 + eps
    hi =  _pi/2 - eps

    def h(w, zval):
        return _log1p(zval) + 2.0*_log(_cos(w)) + _tan(w)

    for i, zi in enumerate(z_flat):
        w_flat[i] = _brentq(h, lo, hi, args=(zi,), xtol=1e-12, rtol=1e-12, maxiter=maxiter)

    if z_flat.size > 1:
        order = _np.argsort(z_flat)
        w_sorted = w_flat[order]
        diffs = _np.diff(w_sorted)
        if _np.nanmedian(diffs) >= 0:
            w_sorted = _np.maximum.accumulate(w_sorted)
        else:
            w_sorted = _np.minimum.accumulate(w_sorted)
        w_flat[order] = w_sorted

    return w_flat.reshape(z_arr.shape)


# --- patched monotone solver for w(z) ---
def solve_w_of_z(z, eps=1e-6):
    """
    Solve for w in (-pi/2, pi/2) from: (1+z) * cos(w)^2 = exp(-tan(w))
    Using g(w;z) = log(1+z) + 2*log(cos w) + tan w = 0 (monotone in w).
    Continuation: march z in ascending order; bracket around previous root and expand if needed.
    """
    import numpy as _np
    from scipy.optimize import brentq as _brentq

    z = _np.asarray(z, dtype=float)
    w = _np.empty_like(z)

    wmax = _np.pi/2 - eps
    wmin = -wmax

    def _g(wval, zval):
        # Stable evaluation of g(w; z)
        c = _np.cos(wval)
        # clip cos to avoid log(0); stay strictly inside domain
        c = _np.clip(c, 1e-300, None)
        return _np.log1p(zval) + 2.0*_np.log(c) + _np.tan(wval)

    order = _np.argsort(z)
    last_w = 0.0  # at z=0, w=0 is exact root of g(w;0)=0

    for idx in order:
        zval = float(z[idx])

        # Start with a tight bracket around last_w and expand geometrically until sign change
        step = 0.3
        a = max(last_w - step, wmin + 1e-9)
        b = min(last_w + step, wmax - 1e-9)
        ga = _g(a, zval)
        gb = _g(b, zval)

        tries = 0
        while ga * gb > 0.0 and tries < 50:
            step *= 1.5
            a = max(last_w - step, wmin + 1e-9)
            b = min(last_w + step, wmax - 1e-9)
            ga = _g(a, zval)
            gb = _g(b, zval)
            tries += 1

        # If still no sign change (extreme z), fall back to full domain
        if ga * gb > 0.0:
            a, b = (wmin + 1e-9, wmax - 1e-9)
            ga, gb = _g(a, zval), _g(b, zval)

        # Root-find
        root = _brentq(lambda w_: _g(w_, zval), a, b, xtol=1e-12, rtol=1e-10, maxiter=200)
        root = float(_np.clip(root, wmin, wmax))

        w[idx] = root
        last_w = root

    return w
# --- end patch ---

