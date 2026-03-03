import pandas as pd


def create_time_based_churn(df, cutoff_date, prediction_days=90):
    """
    Creates churn label using time-based split.
    """

    cutoff_date = pd.to_datetime(cutoff_date)
    prediction_end = cutoff_date + pd.Timedelta(days=prediction_days)

    # Historical window (for features)
    historical = df[df["InvoiceDate"] <= cutoff_date]

    # Future window (for churn definition)
    future = df[
        (df["InvoiceDate"] > cutoff_date) &
        (df["InvoiceDate"] <= prediction_end)
    ]

    # Customers active before cutoff
    customers_hist = historical["CustomerID"].unique()

    # Customers who purchased in prediction window
    customers_future = future["CustomerID"].unique()

    churn_df = pd.DataFrame({"CustomerID": customers_hist})

    churn_df["Churn"] = ~churn_df["CustomerID"].isin(customers_future)
    churn_df["Churn"] = churn_df["Churn"].astype(int)

    return historical, churn_df