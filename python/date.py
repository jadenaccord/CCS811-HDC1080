import csv
from datetime import datetime
import pandas

dates = []
times = []

with open('test.csv') as file:
    reader = csv.reader(file, delimiter=(','), quotechar='|')
    for row in reader:
        #row_datetime = row[0] + ',' + row[1]
        #new_datetime = datetime.strptime(row_datetime, '%Y-%M-%d,%H:%m:%S.%f')
        new_date = pandas.to_datetime(row[0] + ' ' + row[1])
        print(new_date)
        