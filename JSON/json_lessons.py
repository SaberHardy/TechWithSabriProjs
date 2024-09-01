import json


# with open('json_data.json', "r") as json_file:
#     loaded_data = json.load(json_file)

data = {
    "n": 12,
    "v": 34
}

# print(loaded_data)

with open('json_data.json', "r") as json_file:
    json.dump(data, json_file)

