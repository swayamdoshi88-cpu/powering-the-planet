
"""Functions for analysing energy and CO2 emissions."""

import numpy as np
import pandas as pd


COUNTRIES = [
    "Italy",
    "Germany",
    "United Kingdom",
    "United States",
    "China",
    "India",
    "Brazil",
]


def filter_countries(data, start_year=1990, end_year=2024):
    """Select the chosen countries and years from a dataset."""
    required_columns = ["country", "year"]

    for column in required_columns:
        if column not in data.columns:
            raise ValueError(f"Missing required column: {column}")

    return data.loc[
        data["country"].isin(COUNTRIES)
        & data["year"].between(start_year, end_year)
    ].copy()


def calculate_emission_statistics(co2_data):
    """Calculate mean, median and standard deviation of CO2 per capita."""
    data = filter_countries(co2_data)

    results = []

    for country in COUNTRIES:
        values = data.loc[
            data["country"] == country, "co2_per_capita"
        ].dropna().to_numpy()

        if len(values) > 0:
            results.append({
                "Country": country,
                "Mean": np.mean(values),
                "Median": np.median(values),
                "Standard deviation": np.std(values),
                "Observations": len(values),
            })

    return pd.DataFrame(results)


def calculate_decoupling(energy_data, co2_data):
    """Compare changes in GDP per capita and CO2 emissions.

    Also reports changes in total CO2 emissions. Each country uses
    its earliest and latest valid common observations.
    """
    energy = filter_countries(energy_data)
    co2 = filter_countries(co2_data)

    required_energy = ["country", "year", "gdp", "population"]
    required_co2 = ["country", "year", "co2_per_capita", "co2"]

    for column in required_energy:
        if column not in energy.columns:
            raise ValueError(f"Missing energy column: {column}")

    for column in required_co2:
        if column not in co2.columns:
            raise ValueError(f"Missing CO2 column: {column}")

    co2 = co2[
        ["country", "year", "co2_per_capita", "co2"]
    ]

    merged = energy.merge(
        co2,
        on=["country", "year"],
        how="inner",
    )

    merged["gdp_per_capita"] = (
        merged["gdp"] / merged["population"]
    )

    valid = merged.dropna(
        subset=[
            "gdp_per_capita",
            "co2_per_capita",
            "co2",
        ]
    )

    valid = valid.loc[
        (valid["gdp_per_capita"] > 0)
        & (valid["co2_per_capita"] > 0)
        & (valid["co2"] > 0)
    ]

    results = []

    for country, group in valid.groupby("country"):
        group = group.sort_values("year")

        start = group.iloc[0]
        end = group.iloc[-1]

        gdp_change = (
            end["gdp_per_capita"] / start["gdp_per_capita"] - 1
        ) * 100

        co2_pc_change = (
            end["co2_per_capita"] / start["co2_per_capita"] - 1
        ) * 100

        total_co2_change = (
            end["co2"] / start["co2"] - 1
        ) * 100

        results.append({
            "Country": country,
            "Start year": int(start["year"]),
            "End year": int(end["year"]),
            "GDP per capita change (%)": round(gdp_change, 2),
            "CO2 per capita change (%)": round(co2_pc_change, 2),
            "Total CO2 change (%)": round(total_co2_change, 2),
        })

    return pd.DataFrame(results)


def classify_decoupling(summary):
    """Classify economic growth and CO2 per-capita changes."""
    result = summary.copy()

    gdp = result["GDP per capita change (%)"]
    co2 = result["CO2 per capita change (%)"]

    conditions = [
        (gdp > 0) & (co2 < 0),
        (gdp > 0) & (co2 > 0) & (co2 < gdp),
        (gdp > 0) & (co2 >= gdp),
        (gdp < 0) & (co2 < 0),
    ]

    labels = [
        "Absolute decoupling",
        "Relative decoupling",
        "Emissions grew as fast as or faster than GDP",
        "GDP and emissions both declined",
    ]

    result["Finding"] = np.select(
        conditions,
        labels,
        default="Other trend",
    )

    return result
