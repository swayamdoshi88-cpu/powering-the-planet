"""Functions for loading project datasets."""

from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"


def load_energy_data():
    """Load the Our World in Data energy CSV.

    Returns:
        pandas.DataFrame: Energy observations by country and year.
    """
    path = DATA_DIR / "owid-energy-data.csv"

    if not path.exists():
        raise FileNotFoundError(
            f"Energy dataset not found: {path}"
        )

    return pd.read_csv(path)


def load_co2_data():
    """Load the Our World in Data CO2 CSV.

    Returns:
        pandas.DataFrame: CO2 emissions observations.
    """
    path = DATA_DIR / "owid-co2-data.csv"

    if not path.exists():
        raise FileNotFoundError(
            f"CO2 dataset not found: {path}"
        )

    return pd.read_csv(path)