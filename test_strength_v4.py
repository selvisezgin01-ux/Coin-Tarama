"""Causal feature checks and behavioural boundaries for the experimental rules."""
from pathlib import Path
import unittest

import numpy as np
import pandas as pd

import strength_v4 as model
from study_dataset import STEP, read_json


def fixture():
    count = 240
    close = 100 + np.arange(count)*.015 + np.sin(np.arange(count))*.15
    frame = pd.DataFrame({'open':close-.05, 'high':close+.5, 'low':close-.5,
                          'close':close, 'volume':1000., 'quote_volume':100000.}, index=np.arange(count)*STEP)
    frame.iloc[210] = [103., 152., 102.5, 150., 5000., 500000.]
    for i in range(211, count):
        price = 150+(i-210)*.2
        frame.iloc[i] = [price-.1, price+.1, price-.3, price, 1000., 100000.]
    return frame


class StrengthChecks(unittest.TestCase):
    def setUp(self):
        self.config = read_json(Path(__file__).with_name('strength_v4_config.json'))

    def enrich(self, frame):
        btc = pd.Series(0., index=frame.index)
        btc.attrs['return8'] = btc.copy()
        return model.features(frame, btc, self.config)

    def test_future_changes_do_not_change_past_signals(self):
        frame = fixture()
        original = self.enrich(frame)
        changed = frame.copy()
        changed.iloc[220:, :4] *= 3
        changed.iloc[220:, 4:] *= 7
        altered = self.enrich(changed)
        pd.testing.assert_frame_equal(original.iloc[:220], altered.iloc[:220])
        pd.testing.assert_frame_equal(original.iloc[:216], self.enrich(frame.iloc[:216]))

    def test_strong_wide_breakout_is_selected_and_risk_is_visible(self):
        row = self.enrich(fixture()).iloc[210]
        self.assertGreater(row.return24_pct, 30)
        self.assertGreater(row.ema20_extension_atr, 2.5)
        self.assertTrue(row.new_breakout)
        flags = model.warnings(row, self.config)
        self.assertIn('24 saatlik yükseliş yüksek', flags)
        self.assertIn('yapı bozulma mesafesi geniş', flags)

    def test_long_upper_wick_rejected_even_with_high_volume(self):
        frame = fixture()
        frame.loc[frame.index[210], 'high'] = 210.
        row = self.enrich(frame).iloc[210]
        self.assertTrue(row.breakout_now)
        self.assertFalse(row.qualified)

    def test_continuation_has_its_own_age_window_and_expires(self):
        rows = self.enrich(fixture())
        self.assertTrue(rows.iloc[212].new_breakout)
        self.assertTrue(rows.iloc[213].continuation)
        self.assertFalse(rows.iloc[213].new_breakout)
        self.assertTrue(rows.iloc[228].continuation)
        self.assertFalse(rows.iloc[229].qualified)
        self.assertTrue(pd.isna(rows.iloc[229].breakout_level))

    def test_broken_anchor_cannot_silently_recover_without_new_breakout(self):
        frame = fixture()
        frame.loc[frame.index[214], 'low'] = 90.
        rows = self.enrich(frame)
        self.assertFalse(rows.iloc[215].gate_holds_breakout)
        self.assertFalse(rows.iloc[215].qualified)


if __name__ == '__main__':
    unittest.main()
