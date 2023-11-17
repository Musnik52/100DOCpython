# with open(r'025 - StatesGame\weather_data.csv') as file:
#     data = file.readlines()
# print(data)

# import csv

# with open(r"025 - StatesGame\weather_data.csv") as file:
#     data = csv.reader(file)
#     temps = []
#     rows = []
#     for row in data:
#         rows.append(row)
#     for i in range(1, len(rows)):
#         temps.append(int(rows[i][1]))
# print(temps)


# import pandas

# # data = pandas.read_csv(r"025 - StatesGame\weather_data.csv")
# # print(data['temp'])
# # data_temps = data['temp'].to_list()

# # # print(sum(data_temps)/len(data_temps))
# # print(data['temp'].mean())

# # print(data[data["temp"] == 14])

# school_dict = {
#     "names": ["boris", "shachar", "lior", "emil", "maxim"],
#     "grades": [77, 87, 67, 86, 97],
# }
# data = pandas.DataFrame(school_dict)
# print(data)
# '''
#      names  grades
# 0    boris      77
# 1  shachar      87
# 2     lior      67
# 3     emil      86
# 4    maxim      97
# # '''

# import pandas

# data = pandas.read_csv(r"025 - StatesGame\Squirrel_Data.csv")
# gray_sq_count = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_sq_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_sq_count = len(data[data["Primary Fur Color"] == "Black"])

# sq_dict = {
#     "fur": ["grey", "red", "black"],
#     "amount": [gray_sq_count, cinnamon_sq_count, black_sq_count],
# }

# data_csv = pandas.DataFrame(sq_dict)
# data_csv.to_csv(r"025 - StatesGame\newData.csv")
