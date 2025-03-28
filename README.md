# Cell Count Analysis Project

This repository contains Python scripts for analyzing immune cell populations from clinical sample data and a guide for managing this data within a database.

## Overview

This project includes:
- `count.py`: Processes cell count data to calculate relative frequencies of immune cell populations.
- `plot.py`: Analyzes differences in immune cell populations between responders and non-responders to treatment `tr1`.

## Scripts

### count.py

#### Description
This script calculates the relative frequency (percentage) of immune cell populations per sample.

#### Requirements
- Python 3.x
- Pandas

#### Input
- `cell-count.csv`: CSV file with sample IDs and cell counts for various populations.

#### Output
- `output_relative_frequency.csv`: CSV file with relative frequencies of cell populations per sample.

#### Usage
```bash
python count.py
