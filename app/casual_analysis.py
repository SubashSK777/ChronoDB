from tigramite.data_processing import DataFrame
from tigramite.pcmci import PCMCI
from tigramite.independence_tests.parcorr import ParCorr
import pandas as pd

def get_causal_graph(df):
    # Keep only numeric columns
    numeric_df = df.select_dtypes(include=['number']).copy()
    # Drop rows with NaN values
    numeric_df = numeric_df.dropna()
    # Convert to float64 to avoid dtype errors in Tigramite
    dataframe = DataFrame(numeric_df.astype('float64').values, var_names=numeric_df.columns)

    pcmci = PCMCI(dataframe=dataframe, cond_ind_test=ParCorr())
    results = pcmci.run_pcmci(tau_max=3, pc_alpha=0.05)
    return results, dataframe

def run_counterfactual(df, column, old_value, new_value):
    modified = df.copy()
    modified[column] = modified[column].replace(old_value, new_value)
    return modified
