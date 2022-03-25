import requests
import ast
var = str(input("kino nomini yoz:\n"))


url = f"https://imdb-api.com/en/API/SearchMovie/k_a5pedpr9/{var}"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
natija = response.text.encode('utf8')
byte_str = natija
dict_str = natija.decode("UTF-8")
my_data = ast.literal_eval(dict_str)

# print(repr(my_data))
lists = repr(my_data.get('results'))
if "image" in lists:
    print("Yes")
print(lists)
print(type(lists))
print(len(lists))

original_String = lists

# printing original string
print("The original string is : " + str(original_String))

# using ast.literal_eval() method
result = ast.literal_eval(original_String)

# print result
print("The converted dictionary is : " + str(result))
print(type(result[1]))
dictt = result[1]
print(dictt.get('image'))
