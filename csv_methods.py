import pandas as pd


def print_file(file_name):
    df = pd.read_csv(file_name)
    
    print(df.to_string())