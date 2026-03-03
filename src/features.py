import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def create_rfm(df):
    T = df["InvoiceDate"].max()

    rfm = df.groupby("CustomerID").agg(
        LastPurchaseDate=("InvoiceDate", "max"),
        Frequency=("Invoice", "nunique"),
        Monetary=("Revenue", "sum")
    ).reset_index()

    rfm["Recency"] = (T - rfm["LastPurchaseDate"]).dt.days

    return rfm[["CustomerID", "Recency", "Frequency", "Monetary"]]


def interpurchase_features(df):
    df = df.sort_values(["CustomerID", "InvoiceDate"])

    df["PrevDate"] = df.groupby("CustomerID")["InvoiceDate"].shift(1)
    df["Gap"] = (df["InvoiceDate"] - df["PrevDate"]).dt.days

    gap_stats = df.groupby("CustomerID")["Gap"].agg(
        GapMean="mean",
        GapStd="std"
    ).reset_index()

    return gap_stats


def basket_features(df):
    basket = df.groupby(["CustomerID", "Invoice"]).agg(
        BasketValue=("Revenue", "sum")
    ).reset_index()

    basket_stats = basket.groupby("CustomerID")["BasketValue"].agg(
        BasketMean="mean",
        BasketStd="std"
    ).reset_index()

    return basket_stats


def revenue_trend(df):
    trend_list = []

    for cust, group in df.groupby("CustomerID"):
        group = group.sort_values("InvoiceDate")

        if len(group) < 2:
            trend_list.append((cust, 0))
            continue

        X = np.arange(len(group)).reshape(-1, 1)
        y = group["Revenue"].values

        model = LinearRegression()
        model.fit(X, y)

        trend_list.append((cust, model.coef_[0]))

    trend_df = pd.DataFrame(trend_list, columns=["CustomerID", "RevenueTrend"])

    return trend_df


def category_diversity(df):
    diversity = df.groupby("CustomerID").agg(
        UniqueProducts=("StockCode", "nunique"),
        TotalPurchases=("Invoice", "nunique")
    ).reset_index()

    diversity["DiversityRatio"] = (
        diversity["UniqueProducts"] / diversity["TotalPurchases"]
    )

    return diversity[["CustomerID", "DiversityRatio"]]


def seasonality_ratio(df):
    df["Month"] = df["InvoiceDate"].dt.month

    monthly = df.groupby(["CustomerID", "Month"])["Revenue"].sum().reset_index()

    peak = monthly.groupby("CustomerID")["Revenue"].max().reset_index()
    total = df.groupby("CustomerID")["Revenue"].sum().reset_index()

    season = peak.merge(total, on="CustomerID", suffixes=("_Peak", "_Total"))

    season["SeasonalityRatio"] = (
        season["Revenue_Peak"] / season["Revenue_Total"]
    )

    return season[["CustomerID", "SeasonalityRatio"]]