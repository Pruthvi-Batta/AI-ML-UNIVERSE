#claude
import pandas as pd
import numpy as np

def process_df_optimized(df, df1):
    """
    Efficiently add columns c and d to the df

    Optimizations:
    1. Use vectorized operations instead of apply
    2. Use merge with groupby for efficient min lookup
    3. Reduce redundant computations
    """
    # Vectorized column creation - faster than apply
    df['c'] = df['a'] + df['b']

    # Precompute unique c values and their minimum d values from df1
    df1_min_d = df1.groupby('c')['d'].min().reset_index()

    # Merge to add minimum d values
    df = df.merge(df1_min_d, on='c', how='left')

    return df

# Example usage
df = pd.DataFrame({'a':[1,1,2,2], 'b':[1,2,1,2]})
df1 = pd.DataFrame({'d':[1,2,4, 5, 0.5, 1, 2], 'c':[2,2,3,3,4,4,4]})
print(process_df_optimized(df, df1))