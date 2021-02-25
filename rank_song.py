#this script will use the other two tools to pull all the songs for an artist and rank the songs
#to find the worst song

from grab_all_songs import getSongs
from scraping import rankLyrics
import time
import random

artist = 'lil wayne'

#this is hella slow. Try to find a way to make it so it doesn't have to call the website every single time
#may have to reorganize some code... let's see
#nvm, i forgot it has to call the website everytime it grabs the lyrics.. so just doing a sleep function
#would make enough sense. Probably just gonna raw dog it first and see if my IP gets banned.
'''
gs = getSongs(artist)
total_songs = gs.get_song_list()
for i in total_songs[:11]:
    rl = rankLyrics(artist, i)
    print(f'{rl.score_bw()} {i}')
'''

#now I'm gonna build a script that gets all the songs, scores the lyrics, then returns the highest scoring song
# returns the average score of all songs

gs = getSongs(artist)
total_songs = gs.get_song_list()
songs_score = []

#this creates a dictionary with rows of each song with the song name artist and score
for i in total_songs[:11]:
    time.sleep(random.randrange(1,3))
    rl = rankLyrics(artist, i)
    songs_score_nested_list = {'artist':artist, 'song':i, 'score':rl.score_bw()}
    songs_score.append(songs_score_nested_list)

def get_score(song):
    return song.get('score')

songs_score.sort(key=get_score, reverse=True)

def get_avg(song_list):
    count = 0
    for i in song_list:
        count += i['score']
    return count/len(song_list)
    

print(f"The highest scoring song is {songs_score[0]['song']} with a score of {songs_score[0]['score']}")
print(f'The average score for this artist is {get_avg(songs_score)}')