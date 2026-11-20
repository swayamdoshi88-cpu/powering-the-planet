# Powering the Planet 🌍

## Project Overview

**Powering the Planet** is an individual Python project developed for the *Coding for Data Science and Data Management* course at the University of Milan, academic year 2026/27.

The project investigates the relationship between economic growth, energy sources, and carbon dioxide (CO₂) emissions in seven countries: Italy, Germany, the United Kingdom, the United States, China, India, and Brazil.

## Research Question

Can countries grow their economies while reducing CO₂ emissions per capita, and how have their energy mixes changed over time?

## Objectives

- Compare CO₂ emissions per capita across seven countries.
- Examine changes in the energy mix, including coal, oil, natural gas, nuclear energy, and renewables.
- Compare changes in GDP per capita with changes in CO₂ emissions per capita.
- Identify differences between countries and discuss the implications for energy transitions.

## Data Sources

This project uses publicly available datasets from Our World in Data (OWID).

1. **Energy dataset:** https://github.com/owid/energy-data
2. **CO₂ and greenhouse gas emissions dataset:** https://github.com/owid/co2-data

### Downloading the Data

The CSV files are excluded from this GitHub repository to avoid uploading large datasets.

1. Visit the two dataset repositories linked above.
2. Download the relevant CSV files.
3. Place both files inside the project's `data/` folder using these exact filenames:

```text
data/
├── owid-energy-data.csv
└── owid-co2-data.csv
```

The `data/` folder must be located in the project root, alongside this README file and the Python modules.

## Project Structure

```text
Powering_the_Planet/
├── Powering_the_Planet.ipynb
├── data_loader.py
├── analysis.py
├── visualizations.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── (downloaded CSV datasets)
└── outputs/
    co2_emissions_per_capita.png
    energy_mix.png
    decoupling_chart.png
    decoupling_results.csv
    emissions_statistics.csv
```

## Technologies and Libraries

- **Python** — primary programming language
- **pandas** — data loading, cleaning, filtering, and analysis
- **NumPy** — numerical computing
- **Matplotlib** — data visualization
- **Jupyter Notebook** — interactive analysis and presentation

## Installation and Execution

### 1. Install Python

Install Python 3 and ensure that `python3` is available in your terminal.

### 2. Open the project directory

Open the `Powering_the_Planet` folder in VS Code.

### 3. Install the required libraries

Run the following command in the VS Code terminal from the project root:

```bash
python3 -m pip install -r requirements.txt
```

### 4. Download the datasets

Follow the instructions in the Data Sources section and place both CSV files inside the `data/` folder.

### 5. Launch Jupyter Notebook

Run:

```bash
python3 -m notebook
```

Alternatively, open `Powering_the_Planet.ipynb` directly in VS Code and select an appropriate Python kernel.

### 6. Run the analysis

Execute the notebook cells in order, from top to bottom. The notebook imports reusable functions from `data_loader.py`, `analysis.py`, and `visualizations.py`.

Generated charts and analysis results are saved in the `outputs/` folder.


## Analysis and Key Findings

The project compares GDP per capita, CO2 emissions per capita, total CO2 emissions and changes in the energy mix across seven countries.

For the economic comparison, the earliest and latest valid common observations are used. In the current datasets, the comparison period is 1990–2022.

The results show:

- **Italy:** GDP per capita increased by 38.48%, while CO2 emissions per capita decreased by 25.75%.
- **Germany:** GDP per capita increased by 83.87%, while CO2 emissions per capita decreased by 39.98%.
- **United Kingdom:** GDP per capita increased by 46.15%, while CO2 emissions per capita decreased by 56.51%.
- **United States:** GDP per capita increased by 56.33%, while CO2 emissions per capita decreased by 26.92%.
- **China:** GDP per capita increased by 544.80%, while CO2 emissions per capita increased by 281.71%.
- **India:** GDP per capita increased by 263.06%, while CO2 emissions per capita increased by 197.24%.
- **Brazil:** GDP per capita increased by 90.68%, while CO2 emissions per capita increased by 55.70%.

The results indicate absolute decoupling in the per-capita comparison for Italy, Germany, the United Kingdom and the United States. China, India and Brazil show relative decoupling because CO2 emissions per capita increased more slowly than GDP per capita.

The project also compares changes in total CO2 emissions. For example, US total CO2 emissions decreased by approximately 1.49% between 1990 and 2022, compared with a 26.92% decrease in emissions per capita.

Descriptive statistics, including the mean, median and standard deviation of CO2 emissions per capita, are calculated using NumPy.


## Limitations

- The economic comparison uses the earliest and latest valid common observations for each country. In the current data, these comparisons cover 1990–2022.
- Descriptive statistics use available observations from 1990–2024.
- GDP per capita is calculated by dividing GDP by population.
- Per-capita emissions and total national emissions measure different things.
- The analysis uses production-based emissions and does not fully account for emissions embodied in imported goods.
- Changes in GDP and emissions occurring together do not establish causation.
- Results depend on the coverage and definitions of the source datasets.


## Reproducibility

The project uses separate Python modules for data loading, analysis, and visualization. The notebook imports these modules rather than duplicating the core analysis logic.

The CSV datasets are not included in the repository. Users must download them separately and place them in the `data/` directory before running the notebook.

## Author

Individual student project  
Course: Coding for Data Science and Data Management  
University of Milan  
Academic Year: 2026/27
