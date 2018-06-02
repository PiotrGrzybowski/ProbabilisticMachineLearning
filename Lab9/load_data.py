import os
import pandas as pd
import numpy as np


def load_data():
    files = os.listdir("data/")
    df = pd.DataFrame()
    list = np.zeros((0))
    for file in files:
        temp_df = pd.read_csv('data/' + file)
        list = np.concatenate((list, np.repeat(file[15:(15 + 4)], temp_df.shape[0])), axis=0)
        df = df.append(temp_df, ignore_index=True)
    df['rok'] = pd.Series(list)
    return df
