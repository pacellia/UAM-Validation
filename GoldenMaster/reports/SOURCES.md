# Data Sources & Retrieval (Reviewer-Ready)

This document pins exactly what data are required and how to fetch them so any reviewer can reconstruct the inputs.

## 1) Pantheon+ Supernovae (SN-only baseline)

**We need**
- `pantheon_plus_mb_corr.csv` — calibrated distance-modulus–like vector used in SN-only comparisons.
- `PantheonPlus_cov_SPD.npy` — published SPD matrix; in this project we treat it as a **precision** matrix (see column map below).

**Where to get it (browse_page)**
1. In your browser, search: **Pantheon+ data release CSV SPD** (or open the official Pantheon+ data companion page referenced by the paper).
2. Download the two files named above from the official source.
3. Place them into: `notebook/GoldenMaster/data_curated/`

**Column map & semantics (pinned)**
File: `notebook/GoldenMaster/data_curated/column_map.json`
```json
{ "z_col": "zHD", "mu_col": "m_b_corr", "spd_semantics": "precision" }
```

**Quick local verify (optional)**
```python
import numpy as np, pandas as pd
from pathlib import Path
root = Path("notebook/GoldenMaster/data_curated")
df  = pd.read_csv(root/"pantheon_plus_mb_corr.csv", comment="#")
M   = np.load(root/"PantheonPlus_cov_SPD.npy")
print("[csv] shape:", df.shape, "| first cols:", list(df.columns)[:6])
print("[spd] shape:", M.shape, "| square:", M.shape[0]==M.shape[1])
```

## 2) BAO (placeholder for Phase 2)
When proceeding to SN+BAO, we will add:
- BAO compilation (source URLs/DOIs),
- exact columns used,
- covariance/precision notes,
- checksums.

## 3) Licensing & Provenance
- Datasets are the property of their authors/collaborations.
- We distribute retrieval instructions only; obtain files from official sources.
- For exact versions used here, see `GoldenMaster/reports/REVIEW_ARCHIVE_MANIFEST.md` and archive SHA256 manifests.