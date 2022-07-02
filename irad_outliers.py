import pandas as pd
import numpy as np

# https://towardsdatascience.com/ways-to-detect-and-remove-the-outliers-404d16608dba
# https://www.researchgate.net/post/Which-is-the-best-method-for-removing-outliers-in-a-data-set

def rm_outliers_1_percent(df, ignore_columns=None):
    '''Remove valores que estejam fora dos quantis 1% e 99%.'''
    
    for col in df.columns:
        if(col not in ignore_columns):
            if (((df[col].dtype)=='float64')):
                percentiles = df[col].quantile([0.01,0.99]).values
                query = '{} >= {} and {} <= {}'.format(col, percentiles[0], col, percentiles[1])
                df = df.query(query)

                #query = '{} <= {} or {} >= {}'.format(col, percentiles[0], col, percentiles[1])
                #df_update = df.query(query)
                #df_update[col] = np.nan

                #df.update(df_update[col])
    return df


def rm_outliers_mad(df, ignore_columns=None):
    '''Remove outliers usando método MAD'''
    
    for col in df.columns:
        if(col not in ignore_columns):
            if (df[col].dtypes == "float64"):
                mad = df[col].mad()
                median = df[col].median()
                df = df.loc[ abs(df[col] - median) / mad <= (2*mad) ]
            
    return df

def rm_outliers_irq(df, ignore_columns=None):
    '''Remove outliers usando método IRQ (Interquartile Range)'''
    
    describe = df.describe()
    
    for col in df.columns:
        if(col not in ignore_columns):
            if (df[col].dtypes == "float64"):
                q1 = describe[col]['25%']
                q3 = describe[col]['75%']
                irq = q3-q1

                query = '{} >= {} and {} <= {}'.format(col, (q1 - (1.5*irq)), col, (q1 + (1.5*irq)))
                df = df.query(query)
            
    return df

def rm_outliers_2sd(df, ignore_columns=None):
    '''Remove outliers que estão fora do intervalo de 2x desvio padrão'''
    
    describe = df.describe()
    
    for col in df.columns:
        if(col not in ignore_columns):
            if (df[col].dtypes == "float64"):
                max_val = describe[col]["mean"] + (2 * describe[col]["std"])
                min_val = describe[col]["mean"] - (2 * describe[col]["std"])

                query = '{} >= {} and {} <= {}'.format(col, min_val, col, max_val)
                df = df.query(query)
    
    return df