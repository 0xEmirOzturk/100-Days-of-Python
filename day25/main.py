import csv

#with open("weather_data.csv") as data_file:
    #data = csv.reader(data_file)
    #temperatures = []
    #for row in data:
        #if row[1] != "temp":
            #temperatures.append(int(row[1]))
    #print(temperatures)

import pandas

#data = pandas.read_csv("weather_data.csv")

#to_list = data["temp"].to_list()

#average = sum(to_list) / len(to_list)
#print(average)

data = pandas.read_csv("squirrel_count.csv")

gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

to_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel, cinnamon_squirrel, black_squirrel]
}

df = pandas.DataFrame(to_dict)
df.to_csv("squirrel_fur.csv")