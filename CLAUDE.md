# HELIX — Tamper-evident lab data system

Both collaborators (Will and Evan) use Claude Code on this repo. This file is the shared
source of truth for both sessions. Change it only through a pull request.

## Goal

Ingest lab instrument output files (plate reader CSVs, qPCR exports, spectrophotometer
readings), hash and digitally sign each one, record every action in an append-only audit
log, and detect any file that changes after it was recorded. The features map to
FDA 21 CFR Part 11 (electronic records and signatures); see `docs/compliance.md`.

## Layout and ownership

| Path | Owner | Contents |
|------|-------|----------|
| `helix/models.py` | shared (PR + both approve) | `LabRecord`, the data contract between modules |
| `helix/parsers/` | Evan | One parser per instrument format, each returns `LabRecord` |
| `data/samples/` | Evan | Realistic sample instrument files (no real patient data) |
| `docs/compliance.md` | Evan | Feature → 21 CFR Part 11 mapping |
| `helix/integrity/` | Will | SHA-256 hashing, Ed25519 signing and verification, tamper detection |
| `helix/audit/` | Will | Append-only, hash-chained audit log; user roles |
| `tests/` | whoever wrote the code | pytest tests mirroring the package layout |

Do not edit a folder you don't own unless the task says so. If a change needs one,
note it in the PR description so the owner reviews it.

## The contract

`helix/models.py::LabRecord` is the only type passed between parsers, integrity and
audit. Do not add, rename or remove fields without both people agreeing. Rules:

- `raw` holds the exact bytes of the source file. Hashes and signatures are computed over
  `raw`, never over parsed data, so re-parsing can't change a hash.
- Timestamps are timezone-aware UTC (`datetime.now(timezone.utc)`).
- Records are immutable (`frozen=True`). Produce a new record instead of mutating one.

## Coding rules

- Python 3.11+, standard library first. Approved dependencies are in `requirements.txt`;
  adding one needs a PR.
- Type hints on all public functions. Keep modules small and dependency-light.
- Use `cryptography` for all crypto. Never write your own primitives, and never use MD5
  or SHA-1.
- Never commit private keys, `.env` files or real patient or experiment data. `keys/` is
  gitignored; generate keys locally.
- Every new module gets tests in `tests/`. Run `pytest` before pushing; CI runs it on
  every PR.

## Workflow

1. Every task starts as a GitHub Issue.
2. Branch from an up-to-date `main`: `feature/<issue-number>-short-name`.
3. Commit small, push, open a PR that links the issue (`Closes #N`).
4. The other person reviews before merge. Nobody pushes directly to `main`.
5. Pull `main` often.

## Commands

```
python -m venv .venv
.venv\Scripts\activate        # Windows  (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
pytest
```
