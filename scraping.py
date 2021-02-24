import requests
from bs4 import BeautifulSoup
import re
from bad_words import get_bw

class rankLyrics:
    def __init__(self, artist, song):
        self.artist = artist
        self.song = song

    def produce_url(self):
        #this function takes inputted artist and song name and outputs a url to go
        #into the az = requests.get(url)

        #make sure to get rid of any spaces between names (Kanye West)

        def remove_special_chars(name):
            name = re.sub(r'[^A-Za-z0-9]+', '', name)
            return name.lower()

        artist = remove_special_chars(self.artist)
        song = remove_special_chars(self.song)

        #further considerations:
        # apostrophes
        # ampersands
        # misspellings
        # when a period is in the song name, it is removed in the url

        return f'https://www.azlyrics.com/lyrics/{artist}/{song}.html'

    def fetch_url(self):
        try:
            az = requests.get(self.produce_url())
            soup = BeautifulSoup(az.text, 'html.parser')
            return soup
        except:
            print('Couldn\'t find the song. Try again')

    def clean_lyrics(self):
        #this function gets rid of html elements and empty spaces.
        # improvements: 1. get rid of parentheses 2. get rid of \ before apostrophe 3. lower case everything

        soup_text = str(self.fetch_url())
        b4mxm = soup_text.split(' MxM banner ')
        b4mxm.pop(1)
        b4mxm = str(b4mxm)
        b4mxm = b4mxm.split('Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that.')
        b4mxm.pop(0)
        b4mxm_str = str(b4mxm)
        soup_b4mxm = BeautifulSoup(b4mxm_str, 'html.parser')


        #print(soup_b4mxm.prettify())

        ### IM GOING TO USE REGULAR EXPRESSIONS HERE WE GOOOOOOOOOOO

        def clean_text(raw_html):
            cleanr = re.compile('<.*?>')
            cleantext = re.sub(cleanr, '', raw_html)
            return cleantext

        cleantext_1 = clean_text(b4mxm_str)
        #print(cleantext_1)
        text_list = cleantext_1.split('\\\\n')
        text_list.pop(0)
        text_list.pop(-1)
        lyrics_string = ''
        for i in text_list:
            lyrics_string += (' '+i)

        lyrics_string = lyrics_string.split(' ')
        #print(lyrics_string)

        final_list = []
        for i in lyrics_string:
            if i != '':
                final_list.append(i.lower())

        #IMPROVEMENTS:
        #get rid of parentheses
        #get rid of apostrophe problem with \\

        # This is the final list of lyrics
        return final_list

    #print(clean_lyrics(url))

    def find_bw(self):
        badwordlist = get_bw()
        all_bw = []
        for i in self.clean_lyrics():
            if i in badwordlist:
                all_bw.append(i)
        return all_bw

    def score_bw(self):
        #this function scores each bad word on a scale of 1-10 for how offensive it is
        #probably just going to list the worst 10 swear words and give it a score of 10 and leave
        #all the other swear words at a one
        really_bw = ['fuck', 'cunt', 'pussy', 'bitch', 'dick', 'fucker',
        'ass', 'ballsack', 'whore', 'nigga', 'nigger']
        count = 0
        for i in self.find_bw():
            if i in really_bw:
                count += 10
            else:
                count += 1

        #also want to consider the density of swear words. So like if it's a higher percentage of swear words
        # in the song, then that should score higher. Maybe a multiplier?????
        #alright here's a multiplier
        def multiplier():
            #number of words in the song
            song_words = len(self.clean_lyrics())
            #number of swear words
            bw_words = len(self.find_bw())
            return (bw_words/song_words)

        return count*multiplier()

#commenting this function out to make a main function somewhere else in the future. The same functionality 
# is now more available now that the code is slightly more Object Oriented
'''
    def main():
        global lyric_list
        global list_bw
        try:
            #this produces the url based on inputs and saves
            lyric_url = produce_url(artist, song)

            #this fetches the url just produced and saves as soup
            soup = fetch_url(lyric_url)

            #this cleans the lyrics and saves as a list
            lyric_list = clean_lyrics(soup)

            #this finds the bad words in the song and saves as a list
            list_bw = find_bw(lyric_list)

            print(f"The number of words in this song is {len(lyric_list)}")
            print(f'The number of bad words in this song is {len(list_bw)}')
            print(f'Thus, this song scores a {score_bw(list_bw)}')
            print(list_bw)

        except:
            print('Couldn\'t find the song you wanted. Try again?')
'''

