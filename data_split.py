import os

import pandas as pd
from sklearn.model_selection import train_test_split

DATA_DIR = "data"
SOURCE_CSV = os.path.join(DATA_DIR, "polymarket_markets.csv")
TRAIN_CSV = os.path.join(DATA_DIR, "train_data.csv")
REPORT_CSV = os.path.join(DATA_DIR, "report_data.csv")
REPORT_SIZE = 0.20
RANDOM_STATE = 42

if not (os.path.exists(TRAIN_CSV) and os.path.exists(REPORT_CSV)):
    df = pd.read_csv(SOURCE_CSV, low_memory=False)

    train_df, report_df = train_test_split(
        df,
        test_size=REPORT_SIZE,
        random_state=RANDOM_STATE,
    )

    if not os.path.exists(TRAIN_CSV):
        train_df.to_csv(TRAIN_CSV, index=False)
    if not os.path.exists(REPORT_CSV):
        report_df.to_csv(REPORT_CSV, index=False)
