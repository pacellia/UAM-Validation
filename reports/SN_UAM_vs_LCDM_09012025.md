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
