import csv 
import json

with open("insurance.csv") as insurance_csv:
    insurance_data_info = csv.DictReader(insurance_csv)
    
    region_list = []
    charge_list = []
    smoker_list = []
    for v in insurance_data_info:
        regions = v["region"]
        charge = float(v["charges"])
        smokers = v["smoker"]
        region_list.append(regions)
        charge_list.append(charge)
        smoker_list.append(smokers)
        
    
    
    
    #print(charge_list)
    sw_count = region_list.count("southwest")
    se_count = region_list.count("southeast")
    nw_count = region_list.count("northwest")
    ne_count = region_list.count("northeast")
    
    def region_count():
        return "There are {} Southwest regions, {} Southeast regions, {} Northwest regions and {} Northeast regions in this dataset.".format(sw_count, se_count, nw_count, ne_count)
    regions_in_dataset = region_count()
    
    def majority_region(sw, se, nw, ne):
        if (sw > se) and (sw > nw) and (sw > ne):
            return "Southwest has the most residents in this dataset"
        elif (se > sw) and (se > nw) and (se > ne):
            return "Southeast has the most residents in this dataset"
        elif (nw > sw) and (nw > se) and (nw > ne):
            return "Northwest has the most residents in this dataset"
        elif (ne > sw) and (ne > se) and (ne > nw):
            return "Northeast has the most residents in this dataset"
    client_region_majority = majority_region(sw_count, se_count, nw_count, ne_count)
    
    
    sum_of_charges = sum(charge_list)
    len_of_charges = len(charge_list)
    def charges_avg(lis_sum, lis_len):
        return lis_sum / lis_len
    


    #print(smokers_charges)
    average_insurance_cost = charges_avg(sum_of_charges, len_of_charges)
    print("The average insurance cost is roughly", round(average_insurance_cost, 2), ("Dollars."))
    print(client_region_majority)
    print(regions_in_dataset)
    #print(region_list)
    
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

    class children_insights:

        def average_children(self):
            self.children_summation = sum(Insurance.children)
            self.children_number = len(Insurance.children)
            return "Your dataset has average {} children".format(round(self.children_summation/self.children_number))

        def count_of_children(self, number=0):
            self.values = []
            for i in Insurance.children:
                if i == number :
                    self.values.append(1)
                else:
                    self.values.append(0)
            
            self.counts = self.values.count(1)
            return "Your dataset has {} people having {} children".format(self.counts , number)

    class charges_cost :

        def average_cost(self):
            self.average_charges = []
            self.charges_total = len(Insurance.charges)
            for i in Insurance.charges:
                self.average_charges.append(int(i))
            return "Your average charges for your total dataset is {} dollars".format(round(sum(self.average_charges)/self.charges_total))

        def average_charges_per_smoker(self):

            self.smoker_charges = []
            self.non_smoker_charges = []
            for i in Insurance.main_data('insurance.csv' , 'json.json').data_to_dict()[0].values():
                if i["Smoker"] == "yes":
                    self.smoker_charges.append(i["Charges"])
                elif i["Smoker"] == "no" :
                    self.non_smoker_charges.append(i["Charges"])
            
            self.smoker_charges_summation = sum(self.smoker_charges)
            self.non_smoker_charges_summation = sum(self.non_smoker_charges)
            self.smoker_charges_length = len(self.smoker_charges)
            self.non_smoker_charges_length = len(self.non_smoker_charges)

            return "The average charge for smokers is {} dollars while the average charge for non smokers is {} dollars".format(round(self.smoker_charges_summation/self.smoker_charges_length),round(self.non_smoker_charges_summation / self.non_smoker_charges_length))


for i in range(18,65):
    patients_ages_insights = Insurance.ages_insights(i)
    print(patients_ages_insights.count_inquiry())

patience_insurance_smokers_data = Insurance.main_data('insurance.csv' , 'json.json')
(data1,data2) = patience_insurance_smokers_data.data_to_dict()
print(data2)

printing_data_as_dictionary = Insurance.main_data('insurance.csv' , 'json.json').data_to_dict()
print(printing_data_as_dictionary)

writing_to_json = Insurance.main_data('insurance.csv' , 'dataset_dictionary.json').json_file_data()

smokers_by_age1 = Insurance.smoker_insights()
print(smokers_by_age1.smokers_by_age())

children_insights = Insurance.children_insights()
print(children_insights.average_children())
print(children_insights.count_of_children())

charges_insights = Insurance.charges_cost()
print(charges_insights.average_cost())
print(charges_insights.average_charges_per_smoker())