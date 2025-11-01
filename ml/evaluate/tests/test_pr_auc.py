from ml.evaluate.pr_auc_thresholds import pr_auc
import numpy as np

def test_pr_auc_runs():
    y = np.array([0,1,0,1])
    p = np.array([0.1,0.9,0.2,0.8])
    assert pr_auc(y,p) > 0
