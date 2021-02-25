import re

import requests
from bs4 import BeautifulSoup as bs

#the purpose of this code is to grab all the songs that are available for a given artist on az lyrics

class getSongs:
    def __init__(self, artist):
        self.artist = artist

    def produce_url(self):

        def remove_special_chars(name):
            name = re.sub(r'[^A-Za-z0-9]+', '', name)
            return name.lower()

        artist = remove_special_chars(self.artist)

        # K i know this is terrible, but not sure why this is the only URL ive seen so far that's different
        if artist == 'jackjohnson':
            artist = 'johnson'
        return f'https://www.azlyrics.com/{artist[0]}/{artist}.html'

    def fetch_url(self):
        az = requests.get(self.produce_url())
        soup = bs(az.text, 'html.parser')
        return soup

    def get_song_list(self):
        #this function takes the soup fetched by the fetch_url function and 
        # returns a list of songs by the artist
        songs = self.fetch_url().find_all('a')
        songs = songs[34:-8]
        all_songs_list = []
        for i in songs:
            all_songs_list.append(str(i.get_text()))

        return all_songs_list

gs = getSongs('frank ocean')
gs.get_song_list()