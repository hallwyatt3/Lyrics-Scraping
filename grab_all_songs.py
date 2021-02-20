import requests
from bs4 import BeautifulSoup as bs

#the purpose of this code is to grab all the songs that are available for a given artist on az lyrics

def produce_url(artist):
    
    def no_spaces(name):
        name = name.split(' ')
        new_name = ''
        for i in name:
            new_name += i.lower()
        return new_name

    def no_periods(name):
        name = name.split('.')
        new_name = ''
        for i in name:
            new_name += i.lower()
        return new_name

    artist = no_spaces(artist)
    artist = no_periods(artist)
    return f'https://www.azlyrics.com/{artist[0]}/{artist}.html'

def fetch_url(url):
    az = requests.get(url)
    soup = bs(az.text, 'html.parser')
    return soup

def get_song_list(soup):
    #this function takes the soup fetched by the fetch_url function and 
    # returns a list of songs by the artist

    songs = soup.find_all('a')
    songs = songs[33:-8]
    all_songs_list = []
    for i in songs:
        all_songs_list.append(str(i.get_text()))

    return all_songs_list

url = produce_url(input('What artist are we searching for today? '))
print(url)


print(all_songs_list)
print(len(all_songs_list))