import unittest
import numpy as np
import pandas as pd
import support_indicators as support
from study_dataset import STEP


class DivergenceChecks(unittest.TestCase):
    def test_divergence_is_emitted_only_after_two_right_candles(self):
        lows=[12,11,10,11,12,11,9,10,11,12,13,14]
        frame=pd.DataFrame({'low':lows},index=np.arange(len(lows))*STEP)
        rsi=pd.Series([40,35,25,35,45,40,30,40,45,50,55,60],index=frame.index)
        rows=support.divergence(frame,rsi)
        self.assertFalse(rows.pu_active.iloc[:8].any())
        self.assertTrue(rows.pu_confirmed_now.iloc[8])
        self.assertEqual(rows.pu_confirmation_ms.iloc[8],frame.index[8]+STEP)
        self.assertEqual(rows.pu_age_bars.iloc[8],0)
        changed=frame.copy();changed.loc[frame.index[9],'low']=8
        self.assertFalse(support.divergence(changed,rsi).pu_active.iloc[9])

    def test_future_change_does_not_repaint_past_divergence_or_rsi(self):
        close=pd.Series(100+np.sin(np.arange(120)/3)*4+np.arange(120)*.01,index=np.arange(120)*STEP)
        frame=pd.DataFrame({'close':close,'low':close-.5})
        first=support.features(frame)
        changed=frame.copy();changed.iloc[80:]*=2
        pd.testing.assert_frame_equal(first.iloc[:80],support.features(changed).iloc[:80])
        pd.testing.assert_frame_equal(first.iloc[:80],support.features(frame.iloc[:80]))

    def test_rsi_flat_is_neutral_and_monotonic_prices_have_correct_limits(self):
        self.assertEqual(support.rsi_wilder(pd.Series(np.ones(30))).iloc[-1],50.)
        self.assertEqual(support.rsi_wilder(pd.Series(np.arange(1.,31.))).iloc[-1],100.)
        self.assertEqual(support.rsi_wilder(pd.Series(np.arange(30.,0.,-1))).iloc[-1],0.)


if __name__=='__main__':unittest.main()
