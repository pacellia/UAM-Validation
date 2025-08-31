# UAM Validation (Fresh Start)

    This repository is the public, reviewer-facing validation workspace for Unified Angular Mathematics (UAM).

    ## Layout
    - `GoldenMaster/` — frozen, reviewer-facing truth (theory, curated data, configs, reports)
    - `UAM_validations/` — working area for analyses (code, logs, figures drafts, mcmc runs)
    - `env/` — environment freeze, requirements, local backup helpers
    - `scripts/` — zipping, hashing, simple automation
    - `configs/` — run configs (templates)
    - `docs/` — reviewer docs, sources, theory notes
    - `notebooks/` — notebooks checked into source (your live Colab can be separate)

    ## Start here
    1. Open the Colab notebook named for today (e.g., `UAM_validation_notebook_08312025.ipynb`).
    2. Follow the step-by-step cells to fetch data and run the **SN-only deterministic baseline** (no MCMC).
    3. Use `scripts/daily_fullpack_zip.py` to archive the entire tree into Drive (`UAM_Public/archives/`).

    All artifacts are hashed, versioned, and documented for reproducibility and peer review.
