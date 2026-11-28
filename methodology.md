
# Methodology — Powering the Planet

## 1. Research Objective

This project investigates the relationship between economic growth, energy sources and CO2 emissions in seven countries.

The main research question is:

**Can countries grow their economies while reducing CO2 emissions per capita, and how have their energy mixes changed?**

The analysis uses historical observations to compare economic development, emissions and energy consumption.

## 2. Country Selection

The project focuses on Italy, Germany, the United Kingdom, the United States, China, India and Brazil.

These countries were selected to provide comparisons across different geographical regions and economic contexts.

The selection includes:
- European economies: Italy, Germany and the United Kingdom.
- North American economy: United States.
- Asian economies: China and India.
- South American economy: Brazil.

The purpose is to examine whether countries with different economic and energy profiles show similar or different relationships between economic growth and emissions.

This is a selected comparison, not a statistically representative sample of all countries.

## 3. Data Sources

The project uses two datasets from Our World in Data:

1. Energy dataset:
   https://github.com/owid/energy-data

2. CO2 emissions dataset:
   https://github.com/owid/co2-data

The energy dataset provides information about GDP, population and energy sources.

The CO2 dataset provides information about total CO2 emissions and CO2 emissions per capita.

The datasets are stored locally in the project's `data` folder and loaded using functions in `data_loader.py`.

## 4. Data Preparation

The two datasets are loaded into pandas DataFrames.

The main preparation steps are:

- Inspecting the structure and columns of each dataset.
- Checking missing values.
- Checking duplicate observations.
- Selecting the seven countries.
- Restricting observations to the relevant years.
- Selecting the variables required for the analysis.
- Combining the datasets using country and year.

An inner merge is used because the economic and emissions comparisons require observations that are available in both datasets for the same country and year.

This avoids comparing values from different years.

## 5. Why GDP Per Capita?

Total GDP is influenced by the size of a country's population.

For this reason, the project calculates GDP per capita:

GDP per capita = GDP / Population

This provides an economic measure per person and makes comparisons between countries of different population sizes more meaningful.

GDP per capita is compared with CO2 emissions per capita to examine how economic development and emissions per person have changed over time.

## 6. Why Both Total and Per-Capita CO2 Emissions?

The project considers two different measures.

**CO2 emissions per capita**

This measures the average emissions associated with each person in a country. It is useful for comparing emissions levels while considering differences in population.

**Total CO2 emissions**

This measures the overall emissions produced within a country. It provides information about the country's total contribution to emissions.

Both measures are important because a country's per-capita emissions can decrease while its total emissions remain relatively stable.

For example, the United States experienced a decrease of approximately 26.92% in CO2 emissions per capita between 1990 and 2022, while total CO2 emissions decreased by approximately 1.49%.

This illustrates why the two measures should not be treated as interchangeable.

## 7. Decoupling Analysis

The project compares the percentage changes in GDP per capita and CO2 emissions per capita.

For each country, the earliest and latest valid common observations are selected.

The percentage change is calculated as:

Percentage change = ((Final value - Initial value) / Initial value) × 100

The results are interpreted using the following categories.

### Absolute Decoupling

Absolute decoupling occurs when GDP per capita increases while CO2 emissions per capita decrease.

### Relative Decoupling

Relative decoupling occurs when both GDP per capita and CO2 emissions per capita increase, but the percentage increase in emissions is smaller than the percentage increase in GDP.

### Other Trends

The analysis also allows for situations where GDP and emissions both decline or where emissions increase as fast as, or faster than, GDP.

These classifications describe changes in the selected per-capita indicators. They do not establish a causal relationship between economic growth and emissions.

## 8. Descriptive Statistics

NumPy is used to calculate three descriptive statistics for CO2 emissions per capita:

- Mean: the average value.
- Median: the middle value after sorting the observations.
- Standard deviation: a measure of variation around the mean.

The statistics summarise the available observations for each country.

Since emissions change over time, these statistics are interpreted together with the time-series charts rather than as evidence of a trend on their own.

## 9. Energy Mix Analysis

The energy mix analysis compares the shares of five energy sources:

- Coal
- Oil
- Natural gas
- Nuclear energy
- Renewables

The project uses separate panels to display the energy mix of the seven selected countries.

This makes it easier to observe differences in their energy structures and changes over time.

The analysis focuses on the share of each source in the energy mix, rather than only its absolute consumption.

## 10. Visualisation

Matplotlib is used to create three main visualisations:

1. CO2 emissions per capita over time.
2. Energy mix changes across the selected countries.
3. The relationship between GDP per-capita growth and CO2 per-capita changes.

The charts are intended to make comparisons easier and support the interpretation of the numerical results.

## 11. Time Periods

The economic comparison uses the earliest and latest valid common observations for each country. In the supplied data, the comparison covers 1990–2022.

Descriptive statistics use the available observations from 1990–2024.

The periods differ because the latest valid observations are not necessarily available for every variable in every year.

The start and end years are reported in the decoupling results.

## 12. Limitations

- The seven countries are selected for comparison and do not represent every country.
- GDP per capita and CO2 per capita are useful indicators, but they do not describe every aspect of economic or environmental development.
- The analysis uses production-based emissions and does not fully account for emissions embodied in imported goods.
- Total and per-capita emissions can show different trends.
- The analysis compares selected observations over time and does not establish causation.
- Results depend on the availability, coverage and definitions of the source datasets.
