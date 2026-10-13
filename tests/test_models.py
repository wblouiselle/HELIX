from dataclasses import FrozenInstanceError
from datetime import datetime, timezone

import pytest

from helix.integrity.hashing import fingerprint, matches
from helix.models import InstrumentType, LabRecord


def make_record(raw: bytes = b"well,od600\nA1,0.512\n") -> LabRecord:
    return LabRecord(
        instrument_type=InstrumentType.PLATE_READER,
        instrument_id="PR-01",
        operator="evan",
        acquired_at=datetime(2026, 10, 13, 14, 0, tzinfo=timezone.utc),
        source_path="data/samples/plate.csv",
        raw=raw,
    )


def test_record_is_immutable():
    with pytest.raises(FrozenInstanceError):
        make_record().operator = "mallory"


def test_naive_timestamp_rejected():
    with pytest.raises(ValueError):
        LabRecord(
            instrument_type=InstrumentType.QPCR,
            instrument_id="Q-01",
            operator="evan",
            acquired_at=datetime(2026, 10, 13, 14, 0),
            source_path="x.csv",
            raw=b"",
        )


def test_tampered_bytes_detected():
    original = make_record()
    digest = fingerprint(original)
    assert matches(original, digest)
    assert not matches(make_record(b"well,od600\nA1,0.999\n"), digest)
