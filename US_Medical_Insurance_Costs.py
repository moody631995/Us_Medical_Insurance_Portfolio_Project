import csv 
import json

class Insurance:
    
    ages = []
    sex = []
    bmi = []
    children = []
    smoker = []
    region = []
    charges = []
    

    with open('insurance.csv') as dataset :
        reader = csv.DictReader(dataset)
        for i in reader :
            ages.append(int(i["age"]))
            sex.append(i["sex"])
            bmi.append(float(i["bmi"]))
            children.append(int(i["children"]))
            smoker.append(i["smoker"])
            region.append(i["region"])
            charges.append(float(i["charges"]))

    class main_data:

        def __init__(self, csv, json):
            self.csv_file = csv
            self.json_file = json

        def data_to_dict(self):
            dictionary_values = []
            patients_dictionary = {}
            with open(self.csv_file ) as dataset :
                reader = csv.DictReader(dataset)
                for i in reader:
                    dictionary_values.append(i)
                for i in range(len(dictionary_values)):
                    patients_dictionary.update({"Patient_" + str(i) : {"Age":int(dictionary_values[i]["age"]), "Sex":dictionary_values[i]["sex"],"BMI":float(dictionary_values[i]["bmi"]),"Children":int(dictionary_values[i]["children"]),"Smoker":dictionary_values[i]["smoker"],"Region":dictionary_values[i]["region"],"Charges":float(dictionary_values[i]["charges"])}})
                return patients_dictionary

        def json_file_data(self):
            with open(Insurance.json_file,'w') as json_dataset :
                json.dump(Insurance.data_to_dict(),json_dataset)
            return "File Created ! "
    
    class ages_insights : 

        def __init__(self, age_to_inquire):
            self.age = age_to_inquire

        def average_age(self):
            return "The average age for your dataset is {} years old.".format(round(sum(Insurance.ages)/len(Insurance.ages)))
        
        def count_inquiry(self):

            return "The dataset have {} persons of {} years old age and represent {}  percent of the total dataset.".format(Insurance.ages.count(self.age) , self.age, round((Insurance.ages.count(self.age)*100)/len(Insurance.ages),2))

 

for i in range(20):
    patients_ages_insights = Insurance.ages_insights(i)
    print(patients_ages_insights.count_inquiry())
