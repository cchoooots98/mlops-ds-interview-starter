import numpy as np
from sklearn import metrics

def pr_auc(y_true, y_proba):
    precision, recall, _ = metrics.precision_recall_curve(y_true, y_proba)
    return metrics.auc(recall, precision)

def best_f1_threshold(y_true, y_proba, grid=None):
    if grid is None:
        grid = np.linspace(0.0, 1.0, 101)
    best = (0.0, 0.0)
    for t in grid:
        y_pred = (y_proba >= t).astype(int)
        f1 = metrics.f1_score(y_true, y_pred, zero_division=0)
        if f1 > best[1]:
            best = (t, f1)
    return best  # (threshold, f1)
