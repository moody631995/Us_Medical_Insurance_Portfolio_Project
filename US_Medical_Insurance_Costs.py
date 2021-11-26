import csv

with open('insurance.csv') as dataset :
    names = []
    data = csv.DictReader(dataset)
    for i in data:
        names.append(i["age"])
with open('insurance.csv') as insurance_csv_file:
    pass
print(names)

