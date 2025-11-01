import numpy as np, pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.utils import resample

def importance_stability(X, y, n_boot=20, random_state=42):
    rng = np.random.RandomState(random_state)
    coefs = []
    for b in range(n_boot):
        Xb, yb = resample(X, y, random_state=rng)
        clf = LogisticRegression(max_iter=200).fit(Xb, yb)
        coefs.append(clf.coef_[0])
    coefs = np.array(coefs)
    mean = coefs.mean(axis=0)
    std = coefs.std(axis=0)
    return mean, std
