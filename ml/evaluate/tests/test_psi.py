from ml.evaluate.psi_drift import psi
import numpy as np

def test_psi_runs():
    a = np.random.rand(100)
    b = np.random.rand(100)
    _ = psi(a,b)
