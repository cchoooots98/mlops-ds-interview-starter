from ml.evaluate.calibration_brier import brier_score
import numpy as np

def test_brier_runs():
    y = np.array([0,1,0,1])
    p = np.array([0.2,0.8,0.3,0.7])
    assert 0 <= brier_score(y,p) <= 1
