import pandas as pd

def scan(df: pd.DataFrame, ts_col='ts', target_col='y'):
    issues = []
    # target in features
    if target_col in [c.lower() for c in df.columns]:
        issues.append('TARGET_COLUMN_PRESENT')
    # future leakage example (placeholder): ensure all feature timestamps <= label timestamp if such exists
    # In this simplified dataset we only warn if ts is unsorted
    if not df['ts'].is_monotonic_increasing:
        issues.append('TIMESTAMP_NOT_SORTED')
    return issues
