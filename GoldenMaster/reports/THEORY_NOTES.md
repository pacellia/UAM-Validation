# UAM Theory Notes — Core Cosmology Primitives

**Operative deviation form**
\[
\beta_{\mathrm{dev}}(w) = \left| 1 - \frac{2\sin(w/2)}{w} \right|,\quad
\beta_{\mathrm{dev}}(0)=0,\quad
\beta_{\mathrm{dev}}(w) \sim \frac{w^2}{24}\ \text{as}\ w\to 0.
\]
- Even in \(w\); used to modulate the curvature-sensitive term in \(E(z)^2\).

**w(z) solver (principal branch)**
\[
(1+z)\cos^2 w = e^{-\tan w},\quad
w \in \left(-\tfrac{\pi}{2}+\varepsilon,\ \tfrac{\pi}{2}-\varepsilon\right),\ \varepsilon=10^{-6}.
\]
- Root chosen near \(w\approx 0\) using sign-change bracketing + bisection.

**Fixed UAM matter fraction (parameter-free)**
\[
\Omega_m^{\mathrm{UAM}} = \frac{\pi^3}{100} \approx 0.3101.
\]

**Expansion**
\[
E^2(z) = \Omega_m (1+z)^3 + (1-\Omega_m)\,\sec^2 w(z)\,
\left[\frac{1}{1+\beta_{\mathrm{dev}}(w)\,\frac{z}{1+z}}\right]^2.
\]

**Numerical guardrails**
- \(\varepsilon=10^{-6}\) (documented).
- Enforce \(E^2(z)>0\) in unit tests.
- Check \(w(z)\) monotonicity on \(z\in[0,2.3]\).
