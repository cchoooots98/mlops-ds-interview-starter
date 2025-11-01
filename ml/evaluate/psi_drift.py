import numpy as np

def psi(expected, actual, bins=10, eps=1e-12):
    # expected/actual are 1D np arrays in [0,1] or any continuous; we bin by quantiles of expected
    expected = np.asarray(expected)
    actual = np.asarray(actual)
    qs = np.linspace(0,1,bins+1)
    cuts = np.quantile(expected, qs)
    cuts[0] = -np.inf
    cuts[-1] = np.inf
    e_hist = np.histogram(expected, bins=cuts)[0] / max(len(expected),1)
    a_hist = np.histogram(actual, bins=cuts)[0] / max(len(actual),1)
    return float(np.sum((a_hist - e_hist) * np.log((a_hist + eps)/(e_hist + eps))))
