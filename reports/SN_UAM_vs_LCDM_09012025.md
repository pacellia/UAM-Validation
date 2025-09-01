# SN Baseline — UAM vs ΛCDM (Pantheon+SH0ES)

## Summary (Δ analytically marginalized, full covariance, identical settings)
- N = 1701
- ΛCDM best-fit Ωₘ = 0.361
- χ² (n_grid=20000): UAM = 1755.11, ΛCDM = 1752.51
- Δ̂: UAM = -1.19018, ΛCDM = -1.18080
- RMS(Δ-marg): UAM = 0.172 mag, ΛCDM = 0.172 mag

## Convergence checks (differences vs n_grid=20000)
- UAM: Δχ²(15000) = 0.000, Δχ²(25000) = 0.000; Δ̂ stable within 1e-3: True
- ΛCDM: Δχ²(15000) = 0.000, Δχ²(25000) = 0.000; Δ̂ stable within 1e-3: True

## Acceptance criteria
- Row parity OK: True
- Covariance parity OK: True
- Δ̂ stability OK (≤1e-3 mag): True
- χ² stability OK (<0.1): True

## Plot paths
- /content/notebook/UAM_validations/results/sn_baseline/residuals_vs_z.png
- /content/notebook/UAM_validations/results/sn_baseline/residuals_hist.png
- /content/notebook/UAM_validations/results/sn_baseline/residuals_vs_z_delta_marg.png
- /content/notebook/UAM_validations/results/sn_baseline/residuals_hist_delta_marg.png

_Log_: /content/notebook/logs/SN_validation_09012025.json

## UAM Equation Validations (added 2025-09-01 15:37:49 UTC)

- Overall: PASS ✅
- **β(w) small-angle & even symmetry**: PASS ✅  
  - max relative error vs series \(w^2/24\): 1.25e-08 (tol 5e-08)
- **w(z) solver**: PASS ✅  
  - finite/in-bounds: PASS ✅  
  - monotone non-increasing (tol=1e-08): PASS ✅  
  - max dw/dz: -9.91e-02
- **E²(z)**: PASS ✅  
  - positive: PASS ✅, finite: PASS ✅, E²(0)=1.000000000000

_Logs_:  
- SN run & convergence: `/content/notebook/logs/SN_validation_09012025.json`  
- Equation validations: `/content/notebook/logs/UAM_equation_validations_09012025.json`

## Redshift-split robustness (full covariance, Δ-marg, n_grid=20000)

**Per-bin results** (coarse→refined Ωₘ search within each bin):

| z-bin | N | χ²ₙᵤ(UAM) | χ²ₙᵤ(ΛCDM) | Ωₘ(ΛCDM) | Δ̂(UAM) ± σΔ | Δ̂(ΛCDM) ± σΔ |
|---|---:|---:|---:|---:|---:|---:|
| 0.000-0.100 | 741 | 1.225 | 1.216 | 0.840 | -1.17423 ± 0.00747 | -1.14208 ± 0.00747 |
| 0.100-0.600 | 831 | 0.906 | 0.907 | 0.357 | -1.19581 ± 0.00709 | -1.18482 ± 0.00709 |
| 0.600-2.300 | 129 | 0.612 | 0.611 | 0.249 | -1.20302 ± 0.02071 | -1.29630 ± 0.02071 |

**Δ̂ consistency across bins (weighted):**  
- UAM : Δ̄ = -1.18659, χ² = 5.06 for 2 dof → p = 0.080  
- ΛCDM: Δ̄ = -1.17221, χ² = 55.36 for 2 dof → p = 0.000

**Interpretation:** UAM’s single Δ̂ is **consistent** across z-bins (p≈0.080), while ΛCDM’s is **inconsistent** (p≈0.000). Low-z ΛCDM prefers Ωₘ≈0.840, much higher than mid/high-z. Reduced χ² near unity in mid/high-z for both models indicates a good fit once Δ̂ is treated consistently.

**Plots:**  
- /content/notebook/UAM_validations/results/sn_baseline/zsplit_delta_hat.png  
- /content/notebook/UAM_validations/results/sn_baseline/zsplit_chi2red.png

## Redshift-split (full $C^{-1}$) with ΛCDM $\Omega_m$ fixed

**Per-bin offsets (GLS, using full $C^{-1}$):**

| model | Δ₁ (0–0.1) | Δ₂ (0.1–0.6) | Δ₃ (0.6–2.3) |
|---|---:|---:|---:|
| UAM  | -1.17595 ± 0.00711 | -1.19973 ± 0.00565 | -1.20076 ± 0.01699 |
| ΛCDM (Ωₘ=0.361) | -1.17267 ± 0.00711 | -1.18722 ± 0.00565 | -1.17782 ± 0.01699 |

**Equality of bin offsets (H₀: Δ₁=Δ₂=Δ₃; df=2):**
- UAM : Wald χ² = 5.47, p = 0.065
- ΛCDM: Wald χ² = 2.22, p = 0.329

**Low-z (0≤z≤0.1) residual slope (GLS, H₀: slope=0):**
- UAM : m = 17.95224 ± 0.33376 per unit z
- ΛCDM: m = 17.78523 ± 0.33376 per unit z

**Plot:**  /content/notebook/UAM_validations/results/sn_baseline/low_z_residual_slope_fullCinv.png


## SN + BAO (deterministic; Delta and global alpha marginalized)

Data counts: SN=1701, BAO=0 (blocks=0); total=1701.

LambdaCDM best-fit Omega_m=0.361; global BAO alpha hats — UAM=0.00000, LCDM=0.00000.

| Model | Omega_m | k | chi2_SN | chi2_BAO | chi2_tot | AIC | BIC |
|---|---:|---:|---:|---:|---:|---:|---:|
| UAM  | -   | 0 | 1755.11 | 0.00 | 1755.11 | 1755.11 | 1755.11 |
| LCDM | 0.361 | 1 | 1752.51 | 0.00 | 1752.51 | 1754.51 | 1759.95 |

_Log_: /content/notebook/logs/SNplusBAO_09012025.json


## SN + BAO (deterministic; Delta and global alpha marginalized)

Data counts: SN=1701, BAO=8 (blocks=3); total=1709.

LambdaCDM best-fit Omega_m=0.341; global BAO alpha hats — UAM=30.82512, LCDM=30.89827.

| Model | Omega_m | k | chi2_SN | chi2_BAO | chi2_tot | AIC | BIC |
|---|---:|---:|---:|---:|---:|---:|---:|
| UAM  | -   | 0 | 1755.11 | 13.93 | 1769.04 | 1769.04 | 1769.04 |
| LCDM | 0.341 | 1 | 1753.71 | 14.08 | 1767.79 | 1769.79 | 1775.23 |

_Log_: /content/notebook/logs/SNplusBAO_09012025.json
