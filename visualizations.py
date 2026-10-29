"""Functions for generating project charts."""

import matplotlib.pyplot as plt


def plot_co2_trends(data, countries, output_path=None):
    """Plot CO2 emissions per capita over time.

    Args:
        data: DataFrame containing country, year and co2_per_capita.
        countries: Countries to include in the chart.
        output_path: Optional path to save the chart.

    Returns:
        matplotlib.figure.Figure: The generated figure.
    """
    fig, ax = plt.subplots(figsize=(12, 6))

    for country in countries:
        subset = data.loc[
            data["country"] == country
        ].sort_values("year")

        ax.plot(
            subset["year"],
            subset["co2_per_capita"],
            label=country,
        )

    ax.set_title("CO2 Emissions Per Capita by Country")
    ax.set_xlabel("Year")
    ax.set_ylabel("CO2 emissions per person (tonnes)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    if output_path is not None:
        fig.savefig(output_path, dpi=300, bbox_inches="tight")

    return fig