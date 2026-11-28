
"""Streamlit dashboard for Powering the Planet."""

import streamlit as st
import matplotlib.pyplot as plt

from data_loader import load_energy_data, load_co2_data
from analysis import (
    COUNTRIES,
    filter_countries,
    calculate_emission_statistics,
    calculate_decoupling,
    classify_decoupling,
)
from visualizations import (
    plot_co2_trends,
    plot_energy_mix,
    plot_decoupling_scatter,
)


st.set_page_config(
    page_title="Powering the Planet",
    page_icon="🌍",
    layout="wide",
)

st.title("🌍 Powering the Planet")
st.subheader("Energy, Economic Growth and CO2 Emissions")

st.write(
    "Explore the relationship between economic growth, "
    "energy sources and CO2 emissions across seven countries."
)

st.markdown("---")


@st.cache_data
def get_data():
    """Load the two project datasets."""
    return load_energy_data(), load_co2_data()


try:
    energy, co2 = get_data()
except (FileNotFoundError, ValueError) as error:
    st.error(str(error))
    st.info(
        "Download the two Our World in Data CSV files "
        "and place them inside the data folder."
    )
    st.stop()


# Country selection
st.sidebar.header("Dashboard Filters")

selected_countries = st.sidebar.multiselect(
    "Select countries",
    COUNTRIES,
    default=COUNTRIES,
)

if not selected_countries:
    st.warning("Please select at least one country.")
    st.stop()

start_year, end_year = st.sidebar.slider(
    "Select year range",
    min_value=1990,
    max_value=2024,
    value=(1990, 2024),
    step=1,
)

# Filter data based on selected countries and years

energy_filtered = filter_countries(
    energy,
    start_year=start_year,
    end_year=end_year,
)

co2_filtered = filter_countries(
    co2,
    start_year=start_year,
    end_year=end_year,
)

energy_filtered = energy_filtered[
    energy_filtered["country"].isin(selected_countries)
]

co2_filtered = co2_filtered[
    co2_filtered["country"].isin(selected_countries)
]



# Prepare results using the selected countries and years

summary = calculate_decoupling(
    energy_filtered,
    co2_filtered,
)

summary = classify_decoupling(summary)

summary = summary[
    summary["Country"].isin(selected_countries)
]

statistics = calculate_emission_statistics(co2_filtered)

statistics = statistics[
    statistics["Country"].isin(selected_countries)
]


# Dashboard navigation tabs

st.markdown("---")

co2_tab, energy_tab, decoupling_tab, statistics_tab, conclusion_tab = st.tabs([
    "📈 CO2 Trends",
    "⚡ Energy Mix",
    "🌍 Decoupling",
    "📊 Statistics",
    "📝 Conclusion",
])


# TAB 1: CO2 emissions

with co2_tab:

    st.header("CO2 Emissions Per Capita")

    st.write(
        f"Countries: {', '.join(selected_countries)}"
    )

    st.write(
        f"Selected period: {start_year}–{end_year}"
    )

    fig = plot_co2_trends(
        co2_filtered,
        selected_countries,
    )

    st.pyplot(fig)
    plt.close(fig)


# TAB 2: Energy mix

with energy_tab:

    st.header("Energy Mix")

    st.write(
        "Compare coal, oil, natural gas, nuclear energy "
        "and renewable energy across countries."
    )

    fig = plot_energy_mix(
        energy_filtered,
        selected_countries,
    )

    st.pyplot(fig)
    plt.close(fig)


# TAB 3: Decoupling analysis

with decoupling_tab:

    st.header("Economic Growth and CO2 Emissions")

    st.write(
        "Compare the percentage changes in GDP per capita "
        "and CO2 emissions per capita."
    )

    fig = plot_decoupling_scatter(summary)

    st.pyplot(fig)
    plt.close(fig)

    st.subheader("Country Comparison")

    st.dataframe(
        summary,
        width="stretch",
        hide_index=True,
    )

    st.download_button(
        label="⬇️ Download Decoupling Results",
        data=summary.to_csv(index=False).encode("utf-8"),
        file_name="decoupling_results.csv",
        mime="text/csv",
    )


# TAB 4: Descriptive statistics

with statistics_tab:

    st.header("Descriptive Statistics")

    st.write(
        "Statistical summary of CO2 emissions per capita "
        "for the selected countries and period."
    )

    st.dataframe(
        statistics.round(2),
        width="stretch",
        hide_index=True,
    )

    st.download_button(
        label="⬇️ Download Emissions Statistics",
        data=statistics.to_csv(index=False).encode("utf-8"),
        file_name="emissions_statistics.csv",
        mime="text/csv",
    )


# TAB 5: Conclusion

with conclusion_tab:

    st.header("Project Conclusion")

    st.write(
        "The results show that the relationship between economic "
        "growth and CO2 emissions differs across countries. "
        "The comparisons should be interpreted alongside total "
        "emissions, energy mix changes and the limitations "
        "of the datasets."
    )

    st.info(
        "These are descriptive comparisons of per-capita indicators. "
        "They do not establish a causal relationship or prove "
        "economy-wide decoupling."
    )

    st.caption(
        "Data source: Our World in Data | "
        "University of Milan | Academic Year 2026/27"
    )
