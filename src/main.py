import requests
import rich
from rich import print,pretty
from rich.console import Console
from rich.columns import Columns
from rich.table import Table
from rich import box
from termcolor import cprint,colored
import sys
import time

def main():
    global anime_name,base_url,anime_info
    print()
    try:
        anime_name = input(str(colored("Search Anime: ","blue",attrs=["blink"])))
    except KeyboardInterrupt:
        print()
        cprint("Goodbye!","red")
        sys.exit(0)


    base_url = "https://api.jikan.moe/v4"
    
    # search with anime name
    anime_info = requests.get(f"{base_url}/anime?q={anime_name}")
    
class App(object):
    def __init__(self,title,desc,genres,figuren,anime_id,num_char,score,rank,Popularity,broadcast):
        
        self.title = title
        self.desc = desc
        self.genres = genres
        self.figuren = ','.join(figuren)
        self.anime_id = anime_id
        self.num_chars = num_char

        self.score = score
        self.rank = rank
        self.popularity = Popularity
        self.broadcast = broadcast
        
        self.show_anime_data()

    def show_anime_data(self):

        table = Table(title=f"{self.title} Table",box=box.SIMPLE_HEAD,highlight=True,title_style="bold white",show_lines=False,show_footer=False,row_styles=["dim",""],collapse_padding=True,header_style="bold blue",)

        

        anime_data = {
                "Title": f"{self.title}",
                "Genre": f"{self.genres}",
                "Desc": f"{self.desc}",
                "Characters": f"{self.figuren}"
        }

        table.add_column("Title",justify="left",style="cyan",no_wrap=True)
        table.add_column("Genres",style="magenta")

        table.add_column("Score",style="blue")
        table.add_column("Rank",style="blue")
        table.add_column("Popularity",style="blue")
        table.add_column("Broadcast",style="blue")

        table.add_column("Description",style="green",justify="left")
        table.add_column("Characters",justify="left",style="cyan")
        
        table.add_row(f"{self.title}",f"{self.genres} ",f"{self.score}",f"{self.rank}",f"{self.popularity}",f"{self.broadcast}",f"{self.desc}",f"{self.figuren}")

        console = Console()
        console.print(table)


        cprint("Scroll up!","green",attrs=["bold","blink"])




        

def anime_log(anime_id,full_data) -> None:
    console = Console()
    tasks = [f"found {n} " for n in full_data]

    with console.status("[bold green] Working on gathering data ...") as status:
        while tasks:
            task = tasks.pop(0)
            time.sleep(0.5)
            console.log(f"{task}")
        

def check_status_code() -> None:

    while True:
        try:
            main()
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
                    score = data["data"]["score"]
                    rank = data["data"]["rank"]
                    popularity = data["data"]["popularity"]
                    broadcast = data["data"]["broadcast"]["day"]
                    genres = ""+",".join([genre['name'] for genre in data['data']['genres']])



                # anime characters
                char_response = requests.get(f"{base_url}/anime/{anime_id}/characters")
                if char_response.status_code == 200:
                    char_data = char_response.json()

                    figuren = []
                    num_char = 0
                    for i,char in enumerate(char_data['data']):
                        if i < 30:
                            figuren.append(f"{char['character']['name']}")
                        num_char = i
                    
                    full_data = [
                            f"anime id: {anime_id}",
                            f"characters: {num_char}",
                            f"title: {title}",
                            f"genres: {genres}",
                            f"description",
                            f"rank: {rank}",
                            f"score: {score}",
                            f"broadcast: {broadcast}",
                            f"popularity: {popularity}"

                    ]
                    anime_log(anime_id,full_data)
                    App(title,desc,genres,figuren,anime_id,num_char,score,rank,popularity,broadcast)

            else:
                print("Error:",response.status_code)
        except Exception as e:
            print("No anime with this name or id found!",e)

check_status_code()
