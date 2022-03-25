import requests


def get_api():
    url = "https://ott-details.p.rapidapi.com/search"
    movie_name = input("Write movie name: \n")
    querystring = {"title": f"{movie_name}", "page": "1"}

    headers = {
        "X-RapidAPI-Host": "ott-details.p.rapidapi.com",
        "X-RapidAPI-Key": "f77eff4adamsh4e3b081efb572fep1ed8b5jsnbac058cdf6ff"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.json()
    return result


def read_movie_data():
    response_data = get_api()
    massiv = ['title', 'genre', 'released']
    print(response_data['results'])
    print(len(response_data['results']))
    for item in response_data['results']:
        print (item['title'],item['genre'])


read_movie_data()


# class Movie():
#     def __init__(self, title, year, genre, poster, actors):
#         self.title = title
#         self.year = year
#         self.genre = genre
#         self.poster = poster
#         self.actors = actors
#
#     def get_title(self):
#         return self.title
#
#     def get_year(self):
#         return self.year
#
#     def get_genre(self):
#         return self.genre
#
#     def get_poster(self):
#         return self.poster
#
#     def get_actors(self):
#         return self.actors
#
#     def run(self):
#         title = self.get_title()
#         genre = self.get_genre()
#         year = self.get_year()
#         poster = self.get_poster()
#         actors = self.get_actors()
#         return title, genre, year, poster, actors


# m1 = Movie(titles, year, genre, actors, poster)
