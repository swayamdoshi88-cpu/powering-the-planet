
"""Functions for creating project visualizations."""

import matplotlib.pyplot as plt


ENERGY_SOURCES = [
    "coal_share_energy",
    "oil_share_energy",
    "gas_share_energy",
    "nuclear_share_energy",
    "renewables_share_energy",
]

ENERGY_LABELS = [
    "Coal",
    "Oil",
    "Natural gas",
    "Nuclear",
    "Renewables",
]


def plot_co2_trends(data, countries, output_path=None):
    """Plot CO2 emissions per capita over time."""
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


def plot_energy_mix(data, countries, output_path=None):
    """Plot the energy mix for each selected country."""
    fig, axes = plt.subplots(
        4, 2,
        figsize=(14, 15),
        sharex=True,
    )

    axes = axes.flatten()

    for ax, country in zip(axes, countries):
        country_data = data.loc[
            data["country"] == country
        ].sort_values("year").copy()

        country_data = country_data.dropna(
            subset=ENERGY_SOURCES
        )

        if country_data.empty:
            ax.set_title(country)
            ax.text(0.5, 0.5, "No complete data",
                    ha="center", va="center",
                    transform=ax.transAxes)
            continue

        ax.stackplot(
            country_data["year"],
            *[country_data[col] for col in ENERGY_SOURCES],
            labels=ENERGY_LABELS,
            alpha=0.85,
        )

        ax.set_title(country)
        ax.set_ylabel("Energy share (%)")
        ax.grid(alpha=0.2)

    for ax in axes[len(countries):]:
        ax.set_visible(False)

    for ax in axes[:len(countries)]:
        ax.set_xlabel("Year")

    handles, labels = axes[0].get_legend_handles_labels()

    fig.legend(
        handles,
        labels,
        loc="upper center",
        ncol=5,
    )

    fig.suptitle("Energy Mix Across Selected Countries", y=1.01)
    fig.tight_layout(rect=[0, 0, 1, 0.96])

    if output_path is not None:
        fig.savefig(output_path, dpi=300, bbox_inches="tight")

    return fig


def plot_decoupling_scatter(summary, output_path=None):
    """Plot GDP per-capita changes against CO2 per-capita changes."""
    fig, ax = plt.subplots(figsize=(11, 7))

    for _, row in summary.iterrows():
        x = row["GDP per capita change (%)"]
        y = row["CO2 per capita change (%)"]

        ax.scatter(x, y, s=90)

        ax.annotate(
            row["Country"],
            (x, y),
            xytext=(6, 6),
            textcoords="offset points",
            fontsize=9,
        )

    ax.axhline(0, linestyle="--", alpha=0.6)
    ax.axvline(0, linestyle="--", alpha=0.6)

    ax.set_title("Economic Growth and CO2 Emissions")
    ax.set_xlabel("GDP per capita change (%)")
    ax.set_ylabel("CO2 per capita change (%)")
    ax.grid(alpha=0.3)

    fig.tight_layout()

    if output_path is not None:
        fig.savefig(output_path, dpi=300, bbox_inches="tight")

    return fig
