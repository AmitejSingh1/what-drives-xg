"""
src/leakage.py
Leakage policy enforcement.

FORBIDDEN columns (must never appear as model features):
  - shot_outcome      : what happened after the shot
  - shot_end_location : where the ball ended up
  - statsbomb_xg      : the benchmark target — never a feature

Prefix-based rules (FORBIDDEN_PATTERNS) will be added at Checkpoint 2
once the real StatsBomb field names for the raw freeze-frame object
have been confirmed during the Checkpoint 1 data audit.

The check_no_leakage() function raises ValueError if any forbidden
column is present in a DataFrame or list of column names.
"""

from __future__ import annotations

import re
from typing import Sequence

import pandas as pd

# Exact forbidden column names
FORBIDDEN_EXACT: frozenset[str] = frozenset(
    [
        "shot_outcome",
        "shot_outcome_id",
        "shot_outcome_name",
        "shot_end_location",
        "shot_saved_to_post",
        "shot_saved_off_target",
        "statsbomb_xg",
    ]
)

# Forbidden column name prefixes (regex patterns).
# To be populated at Checkpoint 2 after the data audit confirms the
# exact name of the raw freeze-frame blob column.
FORBIDDEN_PATTERNS: list[str] = []


def _is_forbidden(col: str) -> bool:
    if col in FORBIDDEN_EXACT:
        return True
    for pattern in FORBIDDEN_PATTERNS:
        if re.match(pattern, col):
            return True
    return False


def check_no_leakage(columns: pd.DataFrame | Sequence[str]) -> None:
    """
    Raise ValueError if any forbidden column is present.

    Parameters
    ----------
    columns : DataFrame or list of column names
    """
    if isinstance(columns, pd.DataFrame):
        col_list = list(columns.columns)
    else:
        col_list = list(columns)

    violations = [c for c in col_list if _is_forbidden(c)]
    if violations:
        raise ValueError(
            f"Leakage policy violation — forbidden columns detected: {violations}"
        )


def drop_forbidden(df: pd.DataFrame) -> pd.DataFrame:
    """Return df with all forbidden columns dropped (no error if absent)."""
    to_drop = [c for c in df.columns if _is_forbidden(c)]
    return df.drop(columns=to_drop)
