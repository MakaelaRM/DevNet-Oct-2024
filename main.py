import get_file
import csv_methods

file_id = '1eARZ0iioA7GDm1fb_b5Vc9gLhVxxxibf'
csv_name = 'downloaded_file.csv'

if __name__ == '__main__':
  
  csv_file = get_file.download_csv(file_id, csv_name)
  print = csv_methods.print_file(csv_name)