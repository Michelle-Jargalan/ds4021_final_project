# Only run this script if the dataset (polymarket_markets.csv) is not
# already downloaded locally in this repo.

import shutil
from pathlib import Path

import kagglehub

KAGGLE_DATASET = "ismetsemedov/polymarket-prediction-markets"
SOURCE_CSV = Path(__file__).resolve().parent / "polymarket_markets.csv"

# Download the dataset to the kagglehub cache
download_dir = Path(kagglehub.dataset_download(KAGGLE_DATASET, force_download=True))

# Copy the markets CSV into the repo
shutil.copy(download_dir / SOURCE_CSV.name, SOURCE_CSV)
