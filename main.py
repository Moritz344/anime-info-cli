import requests

anime_name = input("Search: ")
base_url = "https://api.jikan.moe/v4"

# search with anime name
anime_info = requests.get(f"{base_url}/anime?q={anime_name}")

# TODO: termcolor für farben
# TODO: ...

class App(object):
    def __init__(self,title,desc,genres,figuren):
        
        self.title = title
        self.desc = desc
        self.genres = genres
        self.figuren = figuren
        
        print("Title:",self.title)
        print(self.genres)
        print("----------")
        print(self.desc)
        print("---------")
        print("Characters:",self.figuren)

def check_status_code():

    if anime_info.status_code == 200:
        search_data = anime_info.json()

        if search_data["data"]:
            anime_id = search_data["data"][0]["mal_id"]
            anime_title = search_data["data"][0]["title"]

        # anime details wie genre,title,beschreibung ...
        detail_response = requests.get(f"{base_url}/anime/{anime_id}")
        if detail_response.status_code == 200:
            data = detail_response.json()

            title = data["data"]["title"]
            desc = data["data"]["synopsis"]
            genres = "Genres: "+",".join([genre['name'] for genre in data['data']['genres']])

        # anime characters
        char_response = requests.get(f"{base_url}/anime/{anime_id}/characters")
        if char_response.status_code == 200:
            char_data = char_response.json()

            for char in char_data['data']:
                figuren = f"{char['character']['name']}"

            App(title,desc,genres,figuren)

    else:
        print("Error:",response.status_code)

check_status_code()
