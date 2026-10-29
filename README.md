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
    ├── co2_emissions_per_capita.png
    ├── energy_mix.png
    ├── decoupling_chart.png
    └── decoupling_results.csv
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

The project includes data loading, country and year filtering, emissions trend analysis, energy-mix visualization, and comparisons of GDP per capita and CO₂ emissions per capita.

For the 1990–2022 comparison, the results indicate:

- **Italy:** GDP per capita increased by approximately 38.48%, while CO₂ emissions per capita decreased by 25.75%.
- **Germany:** GDP per capita increased by approximately 83.87%, while CO₂ emissions per capita decreased by 39.98%.
- **United Kingdom:** GDP per capita increased by approximately 46.15%, while CO₂ emissions per capita decreased by 56.51%.
- **United States:** GDP per capita increased by approximately 56.33%, while CO₂ emissions per capita decreased by 26.92%.
- **China:** GDP per capita increased substantially, alongside a 281.71% increase in CO₂ emissions per capita.
- **India:** GDP per capita increased substantially, alongside a 197.24% increase in CO₂ emissions per capita.
- **Brazil:** GDP per capita increased by approximately 90.68%, while CO₂ emissions per capita increased by 55.70%.

These results suggest that economic growth and declining per-capita emissions occurred together in Italy, Germany, the United Kingdom, and the United States during the period analyzed. In China, India, and Brazil, economic growth coincided with increasing per-capita emissions.

## Limitations

- The GDP and emissions comparison uses 1990–2022 as the common comparison period because of data availability.
- Per-capita emissions and total national emissions measure different things and should not be interpreted interchangeably.
- The analysis uses reported territorial emissions and does not fully account for emissions embodied in imported goods.
- Changes in GDP and emissions occurring together do not establish that one caused the other.
- Results depend on dataset coverage, definitions, and the years available for each country.

## Reproducibility

The project uses separate Python modules for data loading, analysis, and visualization. The notebook imports these modules rather than duplicating the core analysis logic.

The CSV datasets are not included in the repository. Users must download them separately and place them in the `data/` directory before running the notebook.

## Author

Individual student project  
Course: Coding for Data Science and Data Management  
University of Milan  
Academic Year: 2026/27
