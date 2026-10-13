"""Shared data contract. Changes require agreement from both owners (see CLAUDE.md)."""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class InstrumentType(str, Enum):
    PLATE_READER = "plate_reader"
    QPCR = "qpcr"
    SPECTROPHOTOMETER = "spectrophotometer"


@dataclass(frozen=True)
class LabRecord:
    """One instrument output file, as ingested by a parser.

    `raw` is the exact file bytes; integrity checks are computed over it.
    `data` is the parsed content, for display and analysis only.
    """

    instrument_type: InstrumentType
    instrument_id: str
    operator: str
    acquired_at: datetime
    source_path: str
    raw: bytes
    data: dict[str, Any] = field(default_factory=dict)
    record_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    ingested_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __post_init__(self) -> None:
        for name in ("acquired_at", "ingested_at"):
            if getattr(self, name).tzinfo is None:
                raise ValueError(f"{name} must be timezone-aware (UTC)")
