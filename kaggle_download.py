# Only run this script if the dataset (data/polymarket_markets.csv) is not
# already downloaded locally in this repo.

import shutil
from pathlib import Path

import kagglehub

KAGGLE_DATASET = "ismetsemedov/polymarket-prediction-markets"
DATA_DIR = Path(__file__).resolve().parent / "data"
SOURCE_CSV = DATA_DIR / "polymarket_markets.csv"

# Create the data folder if it does not exist
DATA_DIR.mkdir(exist_ok=True)

# Download the dataset to the kagglehub cache
download_dir = Path(kagglehub.dataset_download(KAGGLE_DATASET, force_download=True))

# Copy the markets CSV into the data folder
shutil.copy(download_dir / SOURCE_CSV.name, SOURCE_CSV)
