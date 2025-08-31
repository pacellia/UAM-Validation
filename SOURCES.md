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
