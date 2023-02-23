# with open("weather_data.csv") as weather:
#     data = weather.readlines()
#     print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

import pandas
# import statistics
# data = pandas.read_csv("weather_data.csv")
# # print(data[data.temp == 24])
# # monday = data[data.day == "Monday"]
# # monday_temp = int(monday.temp)
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# c_data = pandas.DataFrame(data_dict)
# c_data.to_csv("new_data.csv")
#

data = pandas.read_csv("squirrel_Data.csv")

gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel, red_squirrel, black_squirrel]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")









