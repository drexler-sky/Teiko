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
`cell-count.csv` 

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

### Statistical Analysis Results

The `plot.py` script conducts a statistical analysis using the Mann-Whitney U test to determine if there are significant differences in the relative frequencies of immune cell populations between responders and non-responders to treatment `tr1`. Here are the results:

#### Significant Differences in Cell Populations

- **cd4_t_cell**: This population showed a significant difference in relative frequencies between responders and non-responders, with a p-value of 0.0102. This suggests that cd4_t_cells are potentially more involved in the response mechanism to treatment `tr1`.

- **monocyte**: Similar to cd4_t_cells, monocytes also displayed significant differences, with a p-value of 0.0135. This indicates that monocytes may also play a significant role in how patients respond to treatment `tr1`.

#### Non-Significant Differences

- **b_cell**: No significant difference was observed (p-value: 0.7832), suggesting that b_cell frequencies do not vary notably between the two groups in the context of treatment `tr1`.

- **cd8_t_cell**: Also showed no significant differences (p-value: 0.6296), indicating their relative frequencies are similar across responders and non-responders.

- **nk_cell**: Similar to b_cells and cd8_t_cells, nk_cells did not show significant differences in their frequencies (p-value: 0.1156).

### Conclusion

The statistical analysis indicates that **cd4_t_cells and monocytes** are significantly associated with the response to treatment `tr1`, while **b_cells, cd8_t_cells, and nk_cells** do not show differences that are statistically significant. This information could be crucial for further research into targeted therapies and understanding the immune response in melanoma patients treated with `tr1`.


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

    SELECT condition, COUNT(DISTINCT subject_id) AS num_subjects FROM Samples GROUP BY condition;

#### 2. Melanoma PBMC Samples at Baseline

    SELECT * FROM Samples WHERE condition = 'melanoma' AND sample_type = 'PBMC' AND time_from_treatment_start = 0 AND treatment = 'tr1';

#### 3. Further Breakdowns

##### a. Samples per Project

    SELECT p.project_name, COUNT(s.sample_id) AS num_samples FROM Samples s JOIN Projects p ON s.project_id = p.project_id WHERE s.condition = 'melanoma' AND s.sample_type = 'PBMC' AND s.time_from_treatment_start = 0 AND s.treatment = 'tr1' GROUP BY p.project_name;

##### b. Response Status

    SELECT CASE WHEN response THEN 'Responder' ELSE 'Non-Responder' END AS response_status, COUNT(*) AS num_samples FROM Samples WHERE condition = 'melanoma' AND sample_type = 'PBMC' AND time_from_treatment_start = 0 AND treatment = 'tr1' GROUP BY response;

##### c. Gender Distribution

    SELECT su.gender, COUNT(s.sample_id) AS num_samples FROM Samples s JOIN Subjects su ON s.subject_id = su.subject_id WHERE s.condition = 'melanoma' AND s.sample_type = 'PBMC' AND s.time_from_treatment_start = 0 AND s.treatment = 'tr1' GROUP BY su.gender;
