# Cell Count Analysis Project

This repository contains Python scripts for analyzing immune cell populations from clinical sample data.

## Overview

This project includes:
- `count.py`: Processes cell count data to calculate relative frequencies
- `plot.py`: Analyzes differences between responders and non-responders to `tr1`

## Scripts

### count.py

#### Description
Calculates relative frequency (%) of immune cell populations per sample.

#### Requirements
- Python 3.x
- Pandas

#### Input
`cell-count.csv` - CSV with sample IDs and cell counts

#### Output
`output_relative_frequency.csv` - CSV with calculated frequencies

#### Usage
Run the script with:
    python count.py

### plot.py

#### Description
Generates boxplots comparing cell populations between responders and non-responders.

#### Requirements
- Python 3.x
- Pandas
- Matplotlib
- Seaborn
- SciPy

#### Input
`output_relative_frequency.csv` (from count.py)

#### Output
- Displays boxplots
- Prints statistical p-values

#### Usage
Run the script with:
    python plot.py
