import pandas as pd


def clean_data(df):
    """
    Cleans raw retail transaction data.
    """

    # Standardize column names
    df.columns = df.columns.str.strip().str.replace(" ", "_")

    # Rename columns for consistency
    df = df.rename(columns={
        "Customer_ID": "CustomerID",
        "Price": "UnitPrice"
    })

    # Convert date
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Remove cancelled invoices
    df = df[~df["Invoice"].astype(str).str.startswith("C")]

    # Remove invalid quantities
    df = df[df["Quantity"] > 0]

    # Remove invalid prices
    df = df[df["UnitPrice"] > 0]

    # Drop missing customers
    df = df.dropna(subset=["CustomerID"])

    # Create revenue
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]

    return df