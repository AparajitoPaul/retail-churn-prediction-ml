import numpy as np
from sklearn.metrics import roc_auc_score, f1_score, precision_score, recall_score


def evaluate_model(model, X_test, y_test, top_k=0.15):

    # Predicted probabilities
    probs = model.predict_proba(X_test)[:, 1]
    preds = (probs > 0.5).astype(int)

    # ROC-AUC
    roc = roc_auc_score(y_test, probs)

    # F1
    f1 = f1_score(y_test, preds)

    # Sort by probability (for Top-K metrics)
    sorted_indices = np.argsort(probs)[::-1]
    top_n = int(len(probs) * top_k)

    top_k_indices = sorted_indices[:top_n]

    precision_top_k = y_test.iloc[top_k_indices].mean()

    recall_top_k = y_test.iloc[top_k_indices].sum() / y_test.sum()

    return {
        "ROC-AUC": roc,
        "F1 Score": f1,
        f"Precision@Top{int(top_k*100)}%": precision_top_k,
        f"Recall@Top{int(top_k*100)}%": recall_top_k
    }