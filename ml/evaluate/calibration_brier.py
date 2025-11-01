import numpy as np
from sklearn import metrics

def brier_score(y_true, y_proba):
    return metrics.brier_score_loss(y_true, y_proba)

def calibration_curve_points(y_true, y_proba, n_bins=10):
    # returns (bin_pred, bin_true)
    bin_ids = np.minimum((y_proba * n_bins).astype(int), n_bins-1)
    bins = []
    for b in range(n_bins):
        mask = bin_ids == b
        if mask.any():
            bins.append((y_proba[mask].mean(), y_true[mask].mean()))
    return np.array(bins)
