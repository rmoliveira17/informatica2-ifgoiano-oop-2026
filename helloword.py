import pandas as pd

data = [
    {'A': 2, 'B': 5, 'C':10},
    {'A': 4, 'B': 5, 'C':10},
    {'A': 2, 'B': 6, 'C':10}]

data_df = pd.DataFrame(data)

data_df.head(5)
