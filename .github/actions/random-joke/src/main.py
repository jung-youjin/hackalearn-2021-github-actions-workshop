import requests 
import random
import sys

api_url = "https://api.imgflip.com/get_memes"
get_joke = requests.get(api_url)
joke_obj = get_joke.json()
joke = joke_obj["data"]["memes"]

def select_random_joke(joke):
    return joke[random.randint(0,len(joke)+1)]["url"]
    
joke_url = select_random_joke(joke)

print("Hey Justin!! 이거 확인해봐  ")
print(joke_url)
print(f"::set-output name=joke::{joke_url}")