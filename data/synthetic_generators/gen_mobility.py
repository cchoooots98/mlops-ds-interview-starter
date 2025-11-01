#!/usr/bin/env python
import argparse, csv, random, math
from datetime import datetime, timedelta

def gen(rows=10000, seed=42):
    random.seed(seed)
    start = datetime(2025, 1, 1, 8, 0, 0)
    for i in range(rows):
        user_id = random.randint(1, 500)
        station_id = random.randint(1, 50)
        ts = start + timedelta(minutes=random.randint(0, 60*24*30))
        # simple synthetic features
        clicks_1h = max(0, int(random.gauss(2, 2)))
        clicks_24h = max(0, int(clicks_1h + random.gauss(5, 3)))
        purchases_7d = max(0, int(random.gauss(1, 1)))
        # logistic function to create label
        z = -1.0 + 0.15*clicks_1h + 0.05*clicks_24h + 0.3*purchases_7d + random.gauss(0, 0.8)
        p = 1/(1+math.exp(-z))
        y = 1 if random.random() < p else 0
        yield {
            "user_id": user_id,
            "station_id": station_id,
            "ts": ts.isoformat(),
            "clicks_1h": clicks_1h,
            "clicks_24h": clicks_24h,
            "purchases_7d": purchases_7d,
            "y": y,
        }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--rows", type=int, default=10000)
    args = ap.parse_args()
    rows = list(gen(args.rows))
    fieldnames = list(rows[0].keys())
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {len(rows)} rows to {args.out}")

if __name__ == "__main__":
    main()
