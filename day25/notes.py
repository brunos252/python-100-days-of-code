
# without csv and pandas
data = []
with open("weather_data.csv") as w_data:

    keys = w_data.readline().strip().split(",")

    for line in w_data.readlines():
        fields = line.strip().split(",")
        vals = {}
        for i in range(len(keys)):
            vals[keys[i]] = fields[i]

        data.append(vals)


import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)

import pandas
data = pandas.read_csv("weather_data.csv")
print(data['temp'])

print(type(data)) # Pandas DataFrame object
print(type(data['temp'])) # Pandas Series object, its like a list
# to_dict, to_excel methods for DataFrame

temps = data['temp'].to_list()
print(sum(temps) / len(temps))
# or
print(data['temp'].mean())
# also Series has mode()...

print(data['temp'].max())

print(data.temp)  # == data['temp']

# get data in row
monday = data[data.day == "Monday"]
print(monday.condition)
# get row with max temp
print(data[data.temp == data.temp.max()])

# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
