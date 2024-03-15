import csv
import pandas as pd
import math
import random

ward = 1
season = 1
# 1 for summer, 2 for winter, 3 for monsoon
electricity_usage = 0
no_of_people = [452, 580, 640, 320, 150, 856]
festive_week = [41,42,45,48,52]
factor=0;
demo=0
# Create a list to store the data
data = []
for year in range(2015, 2023):
    for ward in range(1, 7):
        people_count = no_of_people[ward - 1]
        for season in range(1, 4):
            if season == 1:
                for week in range(1, 17):
                    isConstruction = math.floor(random.random() * 2)
                    # Generate random temperature between 47 and 53
                    temp = math.floor(random.random() * 5) + 47
                    electricity_usage = people_count * temp * 7

                    if isConstruction == 1:
                        temp = math.floor(random.random() * 10) + 10
                        electricity_usage = electricity_usage * (temp / 100) + electricity_usage

                    electricity_usage = math.floor(electricity_usage)
                    data.append([year, ward, week, people_count, demo, isConstruction, electricity_usage])

            elif season == 3:
                for week in range(18, 35):
                    isConstruction = math.floor(random.random() * 2)
                    # Generate random temperature between 27 and 34
                    temp = math.floor(random.random() * 7) + 27
                    electricity_usage = people_count * temp * 7

                    if isConstruction == 1:
                        temp = math.floor(random.random() * 5) + 10
                        electricity_usage = electricity_usage * (temp / 100) + electricity_usage

                    electricity_usage = math.floor(electricity_usage)
                    data.append([year, ward, week, people_count, demo, isConstruction, electricity_usage])

            else:
                for week in range(35, 53):
                    if(week in festive_week):
                        factor=5
                        demo=1
                    isConstruction = math.floor(random.random() * 2)
                    # Generate random temperature between 37 and 43
                    temp = math.floor(random.random() * 6) + 37
                    electricity_usage = people_count * temp * 7
                    

                    if isConstruction == 1:
                        temp = math.floor(random.random() * 10) + 10
                        electricity_usage = electricity_usage * (temp / 100) + electricity_usage*factor
                    

                    electricity_usage = math.floor(electricity_usage)
                    data.append([year, ward, week, people_count, demo, isConstruction, electricity_usage])
                    factor=0
                    demo=0


# Define the file path
file_path = './data.csv'

# Write the data to the CSV file
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Year', 'Ward', 'Week', 'People in Ward', 'Festive Season', 'Construction', 'Electricity Usage'])
    writer.writerows(data)

print("Data saved to", file_path)
