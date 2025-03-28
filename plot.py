import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu

data = pd.read_csv('output_relative_frequency.csv')

filtered_data = data[(data['sample_type'] == 'PBMC') & (data['treatment'] == 'tr1')]

responders = filtered_data[filtered_data['response'] == 'y']
non_responders = filtered_data[filtered_data['response'] == 'n']

populations = ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']
for population in populations:
    sns.boxplot(x='response', y='percentage', data=filtered_data[filtered_data['population'] == population])
    plt.title(f'Relative Frequency of {population} in Responders vs Non-responders')
    plt.ylabel('Relative Frequency (%)')
    plt.xlabel('Response')
    plt.show()
    stat, p = mannwhitneyu(responders[responders['population'] == population]['percentage'],
                           non_responders[non_responders['population'] == population]['percentage'])
    print(f"{population} - p-value: {p}")
