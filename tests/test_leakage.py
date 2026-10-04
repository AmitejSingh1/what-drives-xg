"""
tests/test_leakage.py
Unit tests for the leakage policy (src/leakage.py).
These tests must pass at every checkpoint.
"""

import pytest
import pandas as pd

from src.leakage import check_no_leakage, drop_forbidden, FORBIDDEN_EXACT


class TestCheckNoLeakage:
    def test_clean_columns_pass(self):
        """A DataFrame with only safe columns raises nothing."""
        df = pd.DataFrame(columns=["distance", "angle", "body_part"])
        check_no_leakage(df)  # should not raise

    def test_shot_outcome_raises(self):
        df = pd.DataFrame(columns=["distance", "shot_outcome", "angle"])
        with pytest.raises(ValueError, match="shot_outcome"):
            check_no_leakage(df)

    def test_statsbomb_xg_raises(self):
        df = pd.DataFrame(columns=["distance", "statsbomb_xg"])
        with pytest.raises(ValueError, match="statsbomb_xg"):
            check_no_leakage(df)

    def test_shot_end_location_raises(self):
        df = pd.DataFrame(columns=["distance", "shot_end_location"])
        with pytest.raises(ValueError, match="shot_end_location"):
            check_no_leakage(df)

    def test_list_of_strings_works(self):
        """check_no_leakage also accepts a plain list of column names."""
        with pytest.raises(ValueError):
            check_no_leakage(["distance", "shot_outcome"])

    def test_list_clean_passes(self):
        check_no_leakage(["distance", "angle", "body_part_foot"])


class TestDropForbidden:
    def test_drops_forbidden_keeps_safe(self):
        df = pd.DataFrame(
            columns=["distance", "angle", "statsbomb_xg", "shot_outcome", "body_part"]
        )
        result = drop_forbidden(df)
        assert "statsbomb_xg" not in result.columns
        assert "shot_outcome" not in result.columns
        assert "distance" in result.columns
        assert "body_part" in result.columns

    def test_no_forbidden_returns_unchanged_shape(self):
        df = pd.DataFrame(columns=["distance", "angle"])
        result = drop_forbidden(df)
        assert list(result.columns) == ["distance", "angle"]
