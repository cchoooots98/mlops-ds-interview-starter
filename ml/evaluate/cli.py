import argparse, os
import numpy as np, pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, precision_recall_curve, auc
import matplotlib.pyplot as plt
from .pr_auc_thresholds import pr_auc, best_f1_threshold
from .calibration_brier import brier_score, calibration_curve_points

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--data', required=True, help='CSV with features + y')
    ap.add_argument('--outdir', default='outputs')
    args = ap.parse_args()
    os.makedirs(args.outdir, exist_ok=True)

    df = pd.read_csv(args.data)
    X = df[['clicks_1h','clicks_24h','purchases_7d']].values
    y = df['y'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    clf = LogisticRegression(max_iter=200).fit(X_train, y_train)
    proba = clf.predict_proba(X_test)[:,1]

    # Metrics
    pra = pr_auc(y_test, proba)
    thr, f1 = best_f1_threshold(y_test, proba)
    brier = brier_score(y_test, proba)

    print(f'PR-AUC={pra:.3f}  BestF1@thr={thr:.2f} => {f1:.3f}  Brier={brier:.3f}')

    # Plots
    prec, rec, _ = precision_recall_curve(y_test, proba)
    plt.figure()
    plt.plot(rec, prec)
    plt.xlabel('Recall'); plt.ylabel('Precision'); plt.title('PR Curve')
    plt.savefig(os.path.join(args.outdir, 'pr_curve.png'), bbox_inches='tight')

    bins = calibration_curve_points(y_test, proba, n_bins=10)
    if len(bins)>0:
        plt.figure()
        plt.plot(bins[:,0], bins[:,1], marker='o')
        plt.plot([0,1],[0,1],'--')
        plt.xlabel('Predicted'); plt.ylabel('Observed'); plt.title('Calibration')
        plt.savefig(os.path.join(args.outdir, 'calibration.png'), bbox_inches='tight')

if __name__ == '__main__':
    main()
