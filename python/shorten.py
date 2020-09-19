import csv

file_name = 'newFile.csv'
rows = []
counterGoal = 847
counter = counterGoal

with open(file_name) as file:
    reader = csv.reader(file, delimiter=(','), quotechar='|')
    for row in reader:
        if row[4] != '-':
            if counter == counterGoal:
                line = ','.join(row)
                print(line)
                rows.append(line)
                counter = 0
            else:
                counter = counter + 1

with open('short-' + file_name, 'w') as new_file:
    # new_file.write('date, time, temp, humid, eCO2, TVOC\n')
    for row in rows:
        new_file.write(row + '\n')