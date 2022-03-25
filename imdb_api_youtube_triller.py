import requests
import ast

# var = str(input("kino nomini yoz:\n"))

# id = get_id

# url = f"https://imdb-api.com/en/API/YouTubeTrailer/k_a5pedpr9/{id}"
url = f"https://imdb-api.com/en/API/YouTubeTrailer/k_a5pedpr9/tt0098321"
payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

result_bite = response.text.encode('utf8')
dict_str = result_bite.decode("UTF-8")
my_data = ast.literal_eval(dict_str)

print(my_data.get("videoUrl"))
