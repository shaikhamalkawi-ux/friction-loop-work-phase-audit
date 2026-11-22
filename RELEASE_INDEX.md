# 56H2B public derived-only reproducibility release — 2026-11-22

**Scope:** Selected author-generated analysis code, source identity registers, and derived numerical-score ledgers from the V15-EP1 scientific baseline. Raw third-party measurement files, author-review manuscript sources, and internal editorial records are excluded.

| Source archive | Files | ZIP size (bytes) | Key derived records | SHA-256 |
|---|---:|---:|---:|---|
| [Imperial/PoliTO](releases/imperial_56H2B_code_and_ledgers_20261122.zip) | 35 | 2,812,972 | 48,600 | `c65a3c4fb3a05ff6a6701a484e4df75aefaa18b4e10eaf2646639948392eba57` |
| [EUCENTRE SD21](releases/eucentre_sd21_56H2B_code_and_ledgers_20261122.zip) | 22 | 2,942,657 | 60,750 | `da4ffc51834ac9270f0eaa2be770985e810d247e9524ce2ea03ae1290b9a1ef9` |
| [EUCENTRE R5](releases/eucentre_r5_56H2B_code_and_ledgers_20261122.zip) | 15 | 1,577,985 | 12,150 | `47351e92b247f38abcf614d9237ce5bd47f8695a824529440c915fb48822f396` |
| [EUCENTRE R6](releases/eucentre_r6_56H2B_code_and_ledgers_20261122.zip) | 17 | 2,302,919 | 48,600 | `03bccf4b3ac0e5b336e7af68d410bcd4d95e951495a37c763865e8ca344fccfe` |

**Total scientific files in these archives:** 89. These counts exclude original experimental source files and publication-facing manuscript PDFs.

## Verify the published packages

With Python 3.11+ installed, run from repository root:

```bash
python tools/verify_public_release.py
```

The Python 3.11+ standard-library verifier checks each ZIP against the SHA-256 digest pinned above, then checks ZIP CRC integrity, included-file counts, the exclusion of original raw MAT/TDMS files, and four selected derived-ledger row counts. This establishes identity of the published derived archives, not independent scientific reproduction. The same command runs automatically via [GitHub Actions](.github/workflows/verify-derived-archives.yml). [Initial successful workflow run](https://github.com/shaikhamalkawi-ux/friction-loop-work-phase-audit/actions/runs/44970968458).

For scientific analysis, extract the source-scoped ZIP of interest. The archives preserve the original nested analysis scripts and source-specific instructions. Original third-party recordings must be obtained from [Imperial/PoliTO](https://doi.org/10.17632/gy587m7gx7.1) or [EUCENTRE/BED](https://doi.org/10.60756/euc-ubsy26g318), with identity/hash verification, for any full raw-data replay.

## What the verification does not show

- No fresh reprocessing of all original provider recordings was run as part of this publication.
- A verified derived-ledger identity does not establish instrument calibration, physical energy dissipation, or method superiority under untested measurement schedules.
- The public GitHub visibility is not a new blanket reuse license. Confirm underlying rights and authorship before further redistribution.
- No permanent DOI is assigned by this repository upload alone.

**Manuscript linkage:** The V16 GitHub-link update of the Lubricants Paper B manuscript references this URL separately from the historical Hannover-specific GitHub repository. Its science tables, equations, and numeric claims remain on the locked V15-EP1 baseline.
