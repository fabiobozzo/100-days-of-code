# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data)) # <class 'pandas.core.frame.DataFrame'>

# print(data["temp"])
# print(type(data["temp"]))  # <class 'pandas.core.series.Series'>

# print(data.to_dict())

# temp_list = data["temp"].to_list()
# print(temp_list)

# average = sum(temp_list) / len(temp_list)
# print(average)
# print(data["temp"].mean())
# print(data["temp"].max())

# get data in columns
# print(data.condition)
# print(data["condition"])  # same

# get data in rows
# print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# ---

