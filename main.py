import get_file
import csv_methods

file_id = '1eARZ0iioA7GDm1fb_b5Vc9gLhVxxxibf'
csv_name = 'downloaded_file.csv'

if __name__ == '__main__':
  
  csv_file = get_file.download_csv(file_id, csv_name)
  
  date_time = csv_methods.get_value(csv_name, 'date_time')
  print(f'The date and time is: {date_time}')
  
  ph = csv_methods.get_value(csv_name, ' pH')
  print(f'The pH is: {ph}')
  
  ec = csv_methods.get_value(csv_name, 'EC')
  print(f'The EC is: {ec}')
  
  ppm = csv_methods.get_value(csv_name, 'PPM')
  print(f'The PPM is: {ppm}')
  
  temp = csv_methods.get_value(csv_name, 'Temp')
  print(f'The temprature is: {temp}')
  
  humidity = csv_methods.get_value(csv_name, 'Humidity')
  print(f'The humidity is: {humidity}')