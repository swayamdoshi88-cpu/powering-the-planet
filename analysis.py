"""Functions for cleaning and analyzing energy and CO2 data."""

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
    """Filter observations to selected countries and years.

    Args:
        data: Input DataFrame with country and year columns.
        start_year: First year to include.
        end_year: Last year to include.

    Returns:
        pandas.DataFrame: Filtered copy of the input data.
    """
    return data.loc[
        data["country"].isin(COUNTRIES)
        & data["year"].between(start_year, end_year)
    ].copy()


def calculate_decoupling(energy_data, co2_data):
    """Compare GDP per capita and CO2 per capita changes.

    Uses each country's earliest and latest valid observations
    within 1990–2024 and reports those years explicitly.

    Args:
        energy_data: Energy dataset containing GDP and population.
        co2_data: CO2 dataset containing CO2 per capita.

    Returns:
        pandas.DataFrame: Country-level percentage changes.
    """
    energy = filter_countries(energy_data)
    co2 = filter_countries(co2_data)

    co2 = co2[["country", "year", "co2_per_capita"]]

    merged = energy.merge(
        co2,
        on=["country", "year"],
        how="inner",
    )

    merged["gdp_per_capita"] = (
        merged["gdp"] / merged["population"]
    )

    valid = merged.loc[
        merged["gdp_per_capita"].gt(0)
        & merged["co2_per_capita"].gt(0)
    ].copy()

    results = []

    for country, group in valid.groupby("country"):
        group = group.sort_values("year")
        start = group.iloc[0]
        end = group.iloc[-1]

        gdp_change = (
            end["gdp_per_capita"]
            / start["gdp_per_capita"] - 1
        ) * 100

        co2_change = (
            end["co2_per_capita"]
            / start["co2_per_capita"] - 1
        ) * 100

        results.append({
            "Country": country,
            "Start year": int(start["year"]),
            "End year": int(end["year"]),
            "GDP per capita change (%)": round(gdp_change, 2),
            "CO2 per capita change (%)": round(co2_change, 2),
        })

    return pd.DataFrame(results)