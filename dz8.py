import json
import csv
import random
# 1

print("---------------------------")

str_1 = "Hello Python"
str_2 = "I love you"
str_3 = "So much"
str_4 = "!!!!!"

with open('homework8.txt', "w") as file_1:
    file_1.write(f"{str_1} \n")
    file_1.write(f"{str_2} \n")
    file_1.close()

with open('homework8.txt', "a") as file_1:
    file_1.write(f"{str_3} \n")
    file_1.write(f"{str_4} \n")

with open('homework8.txt') as file_1:
    print(file_1.read())

print("---------------------------")

# 2
dict_ = {123456: ("fredo", 20),
         123455: ("pashka", 19),
         123555: ("sanya", 21),
         125555: ("gendos", 67),
         155555: ("dimulia", 23)}


with open('homework8_2.json', "w") as json_file:
    json_file.write(json.dumps(dict_))

with open('homework8_2.json') as json_file:
    print(json_file.read())

print("---------------------------")

# 3
lst = []

fields = ["ID", "Name", "Age", "Number"]

keys_ = list(dict_.keys())
values_ = list(dict_.values())

y = []

with open("homework8_3.csv", "w") as file:
    file_writer = csv.writer(file, lineterminator="\r")
    file_writer.writerow(fields)
    for key in range(len(keys_) - 1):
        list_key = str(keys_[key])
        y.append(list_key)
        for value in range(len(values_[key])):
            list_value = str(values_[key][value])
            y.append(list_value)
        number_ = random.randint(1000000, 9999999)
        y.append("+375" + str(random.randrange(29, 45, 15)) + str(number_))
        file_writer.writerow(y)
        y = []

with open("homework8_3.csv") as file:
    print(file.read())

print("---------------------------")
