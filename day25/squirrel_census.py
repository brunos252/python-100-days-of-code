import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grays = len(data[data["Primary Fur Color"] == "Gray"])
reds = len(data[data["Primary Fur Color"] == "Cinnamon"])
blacks = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count": [grays, reds, blacks]
}

pandas.DataFrame(data_dict).to_csv("squirrel_census.csv")

