# Data Sources & Acquisition

    ## Pantheon+ Supernovae (SN)
    - **Browse page**: Search for “Pantheon+ supernova dataset arXiv 2023 supplementary” (or use the Scolnic group release page).
    - **What to download**:
      - Corrected SN table (CSV/ASCII) that includes either distance modulus μ or m_b_corr.
      - Full SPD matrix (either covariance or precision). The curated copy will pin its interpretation.
    - **Curation step**:
      - Place the CSV as: `GoldenMaster/data_curated/pantheon_plus_mb_corr.csv`
      - Place the SPD as:  `GoldenMaster/data_curated/PantheonPlus_cov_SPD.npy`
      - Record SHA256 hashes in `GoldenMaster/data_curated/README_SN_curated.txt`
      - Pin column indices in `configs/run_config.json` (copy from `.template` and edit).

    ## BAO (Phase 2)
    - Add compilation source links (e.g., BOSS/eBOSS DR releases).
    - Pin column meaning and units.

    ## Notes
    - Do not rely on autodetection; always pin exact columns and SPD semantics in the curated README and run config.

# SOURCES

[updated 2025-08-31 12:47:43Z UTC]

## Pantheon+ (arXiv 2023)
- **Description**: Pantheon+ supernova compilation with corrected magnitudes and SPD (precision or covariance) matrix.
- **Download Instructions**:
  1. Visit the Pantheon+ project page or arXiv (2023 release).
  2. Download the corrected magnitudes CSV (commonly named `pantheon_plus_mb_corr.csv`).
  3. Download the SPD matrix file (commonly `PantheonPlus_cov_SPD.npy`).
  4. Place both files anywhere under Google Drive; the pipeline will copy them into:
     `GoldenMaster/data_curated/`.
- **Pinned Columns**: Redshift (`z_col`) and data (`data_col`) are recorded in
  `GoldenMaster/configs/run_config.json` generated from the template.
- **Semantics**: SPD is treated as **precision** by default; change to `covariance`
  in `run_config.json` if needed.
