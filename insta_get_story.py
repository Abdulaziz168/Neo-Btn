import requests

username = input("write username:\n")

url = f"https://instagram-profile1.p.rapidapi.com/getstory/{username}"

headers = {
	"X-RapidAPI-Host": "instagram-profile1.p.rapidapi.com",
	"X-RapidAPI-Key": "f77eff4adamsh4e3b081efb572fep1ed8b5jsnbac058cdf6ff"
}

response = requests.request("GET", url, headers=headers)

result_json = response.json()
print(result_json)

count = 0

for item in result_json['story']:
	count +=1
	a = item['video_src']
	print(f"video{count} {a}")