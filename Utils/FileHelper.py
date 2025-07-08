import csv

def read_csv(path):
    rows = []

    with open(path, 'r') as df:
        reader = csv.reader(df)
        next(reader)

        for row in reader:
            rows.append(tuple(row))
    return rows