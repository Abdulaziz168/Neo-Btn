import json

# Data to be written
from awesome_website.users.test_first_api import response_data

dictionary = response_data
print(dictionary.get("results"))
jsonnn = dictionary.get("results")

if type(jsonnn) is dict or list:
    with open("sample.json", "a") as outfile:
        json.dump(jsonnn, outfile, indent=4, sort_keys=True)
else:
    print(type(jsonnn))

# with open('sample.json') as json_file:
#     data = json.dumps(json_file)
#
#     print(data["Title"])
