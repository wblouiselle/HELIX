# HELIX

A tamper-evident data system for lab instrument output. HELIX ingests instrument files,
fingerprints and signs them, keeps an append-only audit log, and flags any record that
changes after it was captured. Built around FDA 21 CFR Part 11 electronic-records
requirements.

By Will Louiselle and Evan Young.

## Quick start

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest
```

See `CLAUDE.md` for project layout, ownership and workflow.
