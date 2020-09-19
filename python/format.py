import csv

rows = []

def format_raw_arduino():
    with open('test.csv') as file:
        reader = csv.reader(file, delimiter=(','), quotechar='|')
        for row in reader:
            print(row)
            line = ', '.join(row).replace(',', '').replace('[', '').replace(']', '').replace(' ', ',')
            print(line)
            rows.append(line)

with open('newTest.csv', 'w') as new_file:
    # new_file.write('date, time, temp, humid, eCO2, TVOC\n')
    for row in rows:
        new_file.write(row + '\n')