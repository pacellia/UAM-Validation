# Reviewer Guide

    ## What’s here
    - `GoldenMaster/` contains frozen, hashed theory and curated datasets.
    - `UAM_validations/` contains working outputs (figures_drafts, logs, mcmc_runs).
    - `docs/` contains this guide, SOURCES.md, and THEORY_NOTES.md.
    - `scripts/daily_fullpack_zip.py` creates a full-pack archive in Drive with stable paths.

    ## How to rerun (SN-only deterministic baseline)
    1) Open the Colab notebook for the session, mount Drive, and ensure the curated CSV/SPD are present.
    2) Import `GoldenMaster/theory/uam_model.py` (UAM) and a simple ΛCDM reference.
    3) Use offset-marginalized χ² for both models (UAM k=0, LCDM k=1) with **identical** data masks.
    4) Produce AIC/BIC and a one-page `SN_UAM_vs_LCDM_*.md` report.
    5) Zip the workspace using `scripts/daily_fullpack_zip.py`.

    ## What to check
    - SHA256 of curated data matches `GoldenMaster/data_curated/README_SN_curated.txt`.
    - Theory unit tests pass (β_dev symmetry, w(z) monotone on SN range, distances behave).
    - Logs contain environment versions (numpy/scipy/pandas).
    - Outputs include CSV of residuals, plots, and summary JSON with AIC/BIC.

    ## Falsification conditions (examples)
    - β_dev(w) fails even symmetry or small-angle limit.
    - w(z) non-monotone on z ∈ [0, 2.3] (with stated ε).
    - UAM SN-only fit statistically dominated by LCDM with robust, pinned inputs.
