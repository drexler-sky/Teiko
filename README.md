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


## Database Design

### Schema Design

#### Projects Table
| Column | Type | Description |
|--------|------|-------------|
| project_id (PK) | SERIAL | Unique project identifier |
| project_name | VARCHAR(255) | Name of the research project |

#### Samples Table
| Column | Type | Description |
|--------|------|-------------|
| sample_id (PK) | SERIAL | Unique sample identifier |
| project_id (FK) | INTEGER | References Projects table |
| subject_id | VARCHAR(50) | Subject identifier |
| sample_type | VARCHAR(50) | Sample type (e.g. 'PBMC') |
| treatment | VARCHAR(50) | Treatment administered |
| response | BOOLEAN | Treatment response status |
| time_from_treatment_start | INTEGER | Days since treatment began |

#### CellCounts Table
| Column | Type | Description |
|--------|------|-------------|
| sample_id (FK) | INTEGER | References Samples table |
| b_cell | INTEGER | B cell count |
| cd8_t_cell | INTEGER | CD8+ T cell count |
| cd4_t_cell | INTEGER | CD4+ T cell count |
| nk_cell | INTEGER | Natural Killer cell count |
| monocyte | INTEGER | Monocyte count |

### Database Queries

#### 1. Count Subjects per Condition

    SELECT 
        condition, 
        COUNT(DISTINCT subject_id) AS num_subjects
    FROM Samples
    GROUP BY condition;

#### 2. Melanoma PBMC Samples at Baseline

    SELECT *
    FROM Samples
    WHERE condition = 'melanoma'
      AND sample_type = 'PBMC'
      AND time_from_treatment_start = 0
      AND treatment = 'tr1';

#### 3. Further Breakdowns

##### a. Samples per Project

    SELECT 
        p.project_name,
        COUNT(s.sample_id) AS num_samples
    FROM Samples s
    JOIN Projects p ON s.project_id = p.project_id
    WHERE s.condition = 'melanoma'
      AND s.sample_type = 'PBMC'
      AND s.time_from_treatment_start = 0
      AND s.treatment = 'tr1'
    GROUP BY p.project_name;

##### b. Response Status

    SELECT 
        CASE 
            WHEN response THEN 'Responder' 
            ELSE 'Non-Responder' 
        END AS response_status,
        COUNT(*) AS num_samples
    FROM Samples
    WHERE condition = 'melanoma'
      AND sample_type = 'PBMC'
      AND time_from_treatment_start = 0
      AND treatment = 'tr1'
    GROUP BY response;

##### c. Gender Distribution

    SELECT 
        su.gender,
        COUNT(s.sample_id) AS num_samples
    FROM Samples s
    JOIN Subjects su ON s.subject_id = su.subject_id
    WHERE s.condition = 'melanoma'
      AND s.sample_type = 'PBMC'
      AND s.time_from_treatment_start = 0
      AND s.treatment = 'tr1'
    GROUP BY su.gender;

##### d. Average Cell Counts

    SELECT 
        CASE 
            WHEN s.response THEN 'Responder' 
            ELSE 'Non-Responder' 
        END AS group,
        ROUND(AVG(cc.cd8_t_cell), 2) AS avg_cd8,
        ROUND(AVG(cc.cd4_t_cell), 2) AS avg_cd4,
        ROUND(AVG(cc.nk_cell), 2) AS avg_nk
    FROM Samples s
    JOIN CellCounts cc ON s.sample_id = cc.sample_id
    WHERE s.condition = 'melanoma'
      AND s.sample_type = 'PBMC'
    GROUP BY s.response;

## Analysis Scripts

### count.py

    # Script to calculate cell frequency percentages
    import pandas as pd
    
    def calculate_percentages(input_file):
        df = pd.read_csv(input_file)
        # Calculation logic here
        return df

### plot.py

    # Script to generate comparative visualizations
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    def generate_plots(data):
        # Plot generation code
        plt.show()
