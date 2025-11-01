import pandas as pd
from ml.leakage.leakage_scanner import scan

def test_scan_runs():
    df = pd.DataFrame({'ts':[1,2,3], 'y':[0,1,0]})
    issues = scan(df)
    assert isinstance(issues, list)
