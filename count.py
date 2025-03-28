import pandas as pd

def calculate_relative_frequency(input_file, output_file):
    data = pd.read_csv(input_file)

    populations = ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']
    data['total_count'] = data[populations].sum(axis=1)

    output_rows = []

    for idx, row in data.iterrows():
        for pop in populations:
            new_row = {
                'sample': row['sample'],
                'sample_type': row['sample_type'],
                'treatment': row['treatment'],
                'response': row['response'],
                'total_count': row['total_count'],
                'population': pop,
                'count': row[pop],
                'percentage': (row[pop] / row['total_count']) * 100
            }
            output_rows.append(new_row)

    output = pd.DataFrame(output_rows)

    output.to_csv(output_file, index=False)
    print(f"Output saved to {output_file}")

calculate_relative_frequency('cell-count.csv', 'output_relative_frequency.csv')
