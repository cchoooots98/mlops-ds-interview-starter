from typing import Iterable
import pandas as pd

def rolling_counts(df: pd.DataFrame, by: str = "user_id") -> pd.DataFrame:
    """Example rolling aggregations (skeleton). Assumes ts is sortable.
    """
    df = df.copy()
    df['ts'] = pd.to_datetime(df['ts'])
    df = df.sort_values(['user_id','ts'])
    # Example: rolling 1h clicks if you had an 'event' column; here we reuse provided columns.
    return df
