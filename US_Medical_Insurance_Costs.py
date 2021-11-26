import csv

with open('insurance.csv') as dataset :
    names = []
    data = csv.DictReader(dataset)
    for i in data:
        names.append(i["age"])

print(names)