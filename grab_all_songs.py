import re

import requests
from bs4 import BeautifulSoup as bs

#the purpose of this code is to grab all the songs that are available for a given artist on az lyrics

def produce_url(artist):

    def remove_special_chars(name):
        name = re.sub(r'[^A-Za-z0-9]+', '', name)
        return name.lower()

    artist = remove_special_chars(artist)
    return f'https://www.azlyrics.com/{artist[0]}/{artist}.html'

def fetch_url(url):
    az = requests.get(url)
    soup = bs(az.text, 'html.parser')
    return soup

def get_song_list(soup):
    #this function takes the soup fetched by the fetch_url function and 
    # returns a list of songs by the artist
    global all_songs_list
    songs = soup.find_all('a')
    songs = songs[34:-8]
    all_songs_list = []
    for i in songs:
        all_songs_list.append(str(i.get_text()))

    return all_songs_list

def main(artist):
    url = produce_url(artist)
    soup = fetch_url(url)
    return get_song_list(soup)

main(input('What artist are we searching for today? '))

print(all_songs_list)
print(len(all_songs_list))