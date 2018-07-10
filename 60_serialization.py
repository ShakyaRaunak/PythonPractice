# https://www.learnpython.org/en/Serialization
import json

json_string = """{
    "president": {
        "name": "Donald Trump",
        "political party": "Republican"
    }
}"""

# json.loads method decodes json string to json object; it takes a string and converts to json object.
print(json.loads(json_string))

# read from a json file
from pprint import pprint

with open('stock_data.json') as f:
    data = json.load(f)

# pprint prints the formatted representation of object on stream, followed by a newline.
pprint(data)

# To encode a data structure to JSON, use the "dumps" method. This method takes an object and returns a String :
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)  # [1, 2, 3, "a", "b", "c"]

# Python supports a Python proprietary data serialization method called pickle (and a faster alternative called cPickle).
import pickle

pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))  # [1, 2, 3, "a", "b", "c"]


# Example : this function adds the given name and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    salaries[name] = salary

    return json.dumps(salaries)


# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])  # 300
print(decoded_salaries["Jane"])  # 400
print(decoded_salaries["Me"])  # 800

# write json object to a json file
with open("data_file.json", "w") as write_file:
    json.dump(json.loads(json_string), write_file)
