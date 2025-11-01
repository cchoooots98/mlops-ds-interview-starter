from fe.feature_builders import rolling_counts
import pandas as pd

def test_import():
    df = pd.DataFrame({'user_id':[1,1], 'ts':['2025-01-01','2025-01-01'], 'clicks_1h':[1,2], 'clicks_24h':[3,4], 'purchases_7d':[0,1]})
    _ = rolling_counts(df)
