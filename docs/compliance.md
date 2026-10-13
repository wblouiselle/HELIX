# 21 CFR Part 11 mapping

Owner: Evan. Maps each HELIX feature to the Part 11 requirement it supports.

| Requirement | Section | HELIX feature | Status |
|-------------|---------|---------------|--------|
| Detect invalid or altered records | 11.10(a) | SHA-256 fingerprint of raw bytes | started |
| Secure, time-stamped audit trail | 11.10(e) | Append-only, hash-chained audit log | planned |
| Limit system access to authorized individuals | 11.10(d) | User roles | planned |
| Signatures linked to their records | 11.70 | Ed25519 signature over record hash | planned |
