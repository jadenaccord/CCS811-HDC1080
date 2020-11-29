import csv

rows = []

def format_raw_arduino():
    with open('file.csv') as file:
        reader = csv.reader(file, delimiter=(','), quotechar='|')
        for row in reader:
            print(row)
            line = ', '.join(row).replace(',', '').replace('[', '').replace(']', '').replace(' ', ',')
            print(line)
            rows.append(line)

def save_new_file():
    with open('formatFile.csv', 'w') as new_file:
        # new_file.write('date, time, temp, humid, eCO2, TVOC\n')
        for row in rows:
            new_file.write(row + '\n')

if __name__ == "__main__":
    format_raw_arduino()
    save_new_file()