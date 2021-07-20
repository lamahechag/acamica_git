import pandas as pd

df = pd.read_csv("combined_data_2.txt", nrows=100)
print(f'rows number {df.shape[0]}')
print(f'rows columns {df.shape[1]}')