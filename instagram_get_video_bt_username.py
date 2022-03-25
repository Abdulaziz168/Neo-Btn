import requests

username = input("write username:\n")

url = f"https://instagram-profile1.p.rapidapi.com/getprofile/{username}"


headers = {
	"X-RapidAPI-Host": "instagram-profile1.p.rapidapi.com",
	"X-RapidAPI-Key": "f77eff4adamsh4e3b081efb572fep1ed8b5jsnbac058cdf6ff"
}

response = requests.request("GET", url, headers=headers)

result_json = response.json()
# allinsta_data = result_json['results']
first_dict = result_json['lastVideo']
second_list = first_dict['media']
count = 0
for item in second_list:
	count +=1
	video = item['video_url']
	print(f"video num {count} {video}")