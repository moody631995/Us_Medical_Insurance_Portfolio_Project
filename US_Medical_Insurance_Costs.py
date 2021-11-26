import csv

with open('insurance.csv') as dataset :
    data = csv.DictReader(dataset)
    for i in data:
        print(i["age"])