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
    
def get_selected_value(file_name, data_type, date):
 # Load the CSV file into a DataFrame
    df = pd.read_csv(file_name)
    
    # Ensure the 'date_time' column is in datetime format
    df['date_time'] = pd.to_datetime(df['date_time'])
    
    # Filter the DataFrame for rows matching the specified date
    selected_rows = df[df['date_time'].dt.date == pd.to_datetime(date).date()]
    
    # Check if any rows matched the date
    if not selected_rows.empty:
        # Retrieve the values in the data_type column for all matching rows
        specific_values = selected_rows[data_type].tolist()
        
        # If you only want the first matching value, use this:
        # specific_value = specific_values[0]
        return specific_values  # Return all matching values
    else:
        return f"No data found for date: {date}"