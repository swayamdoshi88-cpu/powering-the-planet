# Powering the Planet

## Project overview
This individual Python project investigates the relationship between
economic growth, energy sources, and CO2 emissions in seven countries:
Italy, Germany, the United Kingdom, the United States, China, India,
and Brazil.

## Research question
Can countries grow their economies while reducing CO2 emissions per capita,
and how have their energy mixes changed?

## Data sources
- Our World in Data energy dataset:
  https://github.com/owid/energy-data
- Our World in Data CO2 dataset:
  https://github.com/owid/co2-data

Download the CSV files and place them in the project root:
- owid-energy-data.csv
- owid-co2-data.csv

## Libraries
- Python
- pandas
- NumPy
- Matplotlib
- Jupyter Notebook

## How to run
1. Install Python 3.
2. Install the dependencies:
   python3 -m pip install -r requirements.txt
3. Start Jupyter:
   python3 -m notebook
4. Open Powering_the_Planet.ipynb and run the cells from top to bottom.

## Analysis
The project includes data cleaning, country comparisons, CO2-per-capita
trends, energy-mix visualizations, and percentage-change calculations.

## Limitations
The GDP comparison currently uses 1990–2022 observations because GDP
values for 2024 are missing in the merged data. Per-capita emissions
are not the same as total national emissions. The analysis describes
associations and does not establish causation.

## Author
Student project for Coding for Data Science and Data Management,
University of Milan, academic year 2026/27.
