import csv

class Insurance :
    def __init__(self, age, sex, bmi, children, smoker ):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children 
        self.smoker = smoker

with open('insurance.csv') as dataset :
    names = []
    data = csv.DictReader(dataset)
    for i in data:
        names.append(i["age"])


with open('insurance.csv') as insurance_csv_file:
    pass

print(names)

