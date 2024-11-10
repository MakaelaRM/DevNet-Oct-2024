import pandas as pd

#gets last value
def get_value(file_name, data_type):
    df = pd.read_csv(file_name)
    last_value = df[data_type].iloc[-1]

    return last_value

#gets value before the last
def get_value_before(file_name, data_type):
    df = pd.read_csv(file_name)
    before_value = df[data_type].iloc[-2]

    return before_value

#gets the difference between last and second to last
def get_value_diff(file_name, data_type):
    df = pd.read_csv(file_name)
    
    last_value = df[data_type].iloc[-1]
    before_value = df[data_type].iloc[-2]
    
    diff = round(last_value - before_value, 1)
    
    return diff

#gets column of data
def get_column(file_name, data_type):
        df = pd.read_csv(file_name)
        values = df[data_type]
        
        return values

#gets all file data
def get_data(file_name):
        df = pd.read_csv(file_name)
        
        return df