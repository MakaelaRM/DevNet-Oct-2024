import pandas as pd


def get_value(file_name, data_type):
    df = pd.read_csv(file_name)
    last_value = df[data_type].iloc[-1]

    return last_value