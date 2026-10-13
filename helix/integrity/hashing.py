"""SHA-256 fingerprints of raw record bytes."""

from __future__ import annotations

import hashlib
import hmac

from helix.models import LabRecord


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fingerprint(record: LabRecord) -> str:
    return sha256_hex(record.raw)


def matches(record: LabRecord, expected_hex: str) -> bool:
    """True if the record's bytes still hash to `expected_hex`."""
    return hmac.compare_digest(fingerprint(record), expected_hex)
