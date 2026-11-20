
"""Functions for loading the project datasets."""

from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"


def load_csv(filename, required_columns):
    """Load a CSV file and check that required columns are present."""
    path = DATA_DIR / filename

    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {path}. "
            "Please download it and place it in the data folder."
        )

    try:
        data = pd.read_csv(path)
    except pd.errors.EmptyDataError as error:
        raise ValueError(f"The file is empty: {filename}") from error
    except pd.errors.ParserError as error:
        raise ValueError(f"The CSV file is damaged or invalid: {filename}") from error

    if data.empty:
        raise ValueError(f"The dataset contains no rows: {filename}")

    missing = [
        column for column in required_columns
        if column not in data.columns
    ]

    if missing:
        raise ValueError(
            f"Missing columns in {filename}: {missing}"
        )

    return data


def load_energy_data():
    """Load the Our World in Data energy dataset."""
    return load_csv(
        "owid-energy-data.csv",
        ["country", "year", "population", "gdp"],
    )


def load_co2_data():
    """Load the Our World in Data CO2 dataset."""
    return load_csv(
        "owid-co2-data.csv",
        ["country", "year", "co2", "co2_per_capita"],
    )
