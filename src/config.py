import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

RAW_DATA_PATH = os.path.join(PROJECT_ROOT, "data", "raw", "online_retail.csv")
PROCESSED_DATA_PATH = os.path.join(PROJECT_ROOT, "data", "processed")

MODEL_PATH = os.path.join(PROJECT_ROOT, "models")