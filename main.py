import csv

with open('data/_train.csv', 'rb') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        row_int = map(int, row)
        print(typºe(row_int[0]))