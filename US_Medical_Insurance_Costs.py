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
            with open(self.json_file,'w') as json_dataset :
                json.dump(self.data_to_dict(),json_dataset)
            return "File Created ! "
    
    class ages_insights : 

        def __init__(self, age_to_inquire):
            self.age = age_to_inquire

        def average_age(self):
            return "The average age for your dataset is {} years old.".format(round(sum(Insurance.ages)/len(Insurance.ages)))
        
        def count_inquiry(self):

            return "The dataset have {} persons of {} years old age and represent {}  percent of the total dataset.".format(Insurance.ages.count(self.age) , self.age, round((Insurance.ages.count(self.age)*100)/len(Insurance.ages),2))

    class smoker_insights:

        def smokers_inquiry(self):
            self.smokers = 0
            self.non_smokers = 0
            self.total_smoker_dataset_count = len(Insurance.smoker)
            for i in Insurance.smoker:
                if i == "yes":
                    self.smokers += 1
                else :
                    self.non_smokers +=1 
            return "Your dataset consists of {} non smokers as {} percent of the total dataset and {} smoker as {} percent of the total dataset ! ".format(self.non_smokers, round((self.non_smokers*100)/self.total_smoker_dataset_count), self.smokers, round((self.smokers*100)/self.total_smoker_dataset_count))

        def smokers_by_age(self):
            from_zero_to_ten = 0
            from_ten_to_twenty = 0
            from_twenty_to_thirty = 0
            from_thirty_to_fourty = 0
            from_fourty_to_fifty = 0
            from_fifty_to_sixty = 0
            from_sixty_to_seventy = 0
            from_seventy_to_eighty = 0
            from_eighty_to_ninethy = 0
            from_ninethy_to_hundred = 0

            for j in Insurance.main_data('insurance.csv' , 'json.json').data_to_dict()[0].values():
                if (j["Age"] <= 10) and j["Smoker"] == 'yes' :
                    from_zero_to_ten +=1 
                if (j["Age"] > 10 and j["Age"] <= 20) and j["Smoker"] == 'yes' :
                    from_ten_to_twenty +=1   
                if (j["Age"] > 20 and j["Age"] <= 30) and j["Smoker"] == 'yes' :
                    from_twenty_to_thirty +=1               
                if (j["Age"] > 30 and j["Age"] <= 40) and j["Smoker"] == 'yes' :
                    from_thirty_to_fourty +=1  
                if (j["Age"] > 40 and j["Age"] <= 50) and j["Smoker"] == 'yes' :
                    from_fourty_to_fifty +=1
                if (j["Age"] > 50 and j["Age"] <= 60) and j["Smoker"] == 'yes' :
                    from_fifty_to_sixty +=1
                if (j["Age"] > 60 and j["Age"] <= 70) and j["Smoker"] == 'yes' :
                    from_sixty_to_seventy +=1
                if (j["Age"] > 70 and j["Age"] <= 80) and j["Smoker"] == 'yes' :
                    from_seventy_to_eighty +=1
                if (j["Age"] > 80 and j["Age"] <= 90) and j["Smoker"] == 'yes' :
                    from_eighty_to_ninethy +=1
                if (j["Age"] > 90 and j["Age"] <= 100) and j["Smoker"] == 'yes' :
                    from_ninethy_to_hundred +=1

            return "Between 0 and 10 years old , you have {} smokers \nBetween 10 and 20 years old , you have {} smokers \nBetween 20 and 30 years old , you have {} smokers \nBetween 30 and 40 years old , you have {} smokers \nBetween 40 and 50 years old , you have {} smokers \nBetween 50 and 60 years old , you have {} smokers \nBetween 60 and 70 years old , you have {} smokers \nBetween 70 and 80 years old , you have {} smokers \nBetween 80 and 90 years old , you have {} smokers \nBetween 90 and 100 years old , you have {} smokers \n".format(from_zero_to_ten,from_ten_to_twenty,from_twenty_to_thirty,from_thirty_to_fourty,from_fourty_to_fifty,from_fifty_to_sixty,from_sixty_to_seventy,from_seventy_to_eighty,from_eighty_to_ninethy,from_ninethy_to_hundred)
 

for i in range(20):
    patients_ages_insights = Insurance.ages_insights(i)
    print(patients_ages_insights.count_inquiry())

json_extraction = Insurance.main_data('insurance.csv' , 'json.json')
print(json_extraction.json_file_data())

smokers_by_age1 = Insurance.smoker_insights()
print(smokers_by_age1.smokers_by_age())