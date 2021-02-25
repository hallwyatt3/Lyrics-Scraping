#this script will use the other two tools to pull all the songs for an artist and rank the songs
#to find the worst song

from grab_all_songs import getSongs
from scraping import rankLyrics

artist = 'frank ocean'

#this is hella slow. Try to find a way to make it so it doesn't have to call the website every single time
#may have to reorganize some code... let's see
gs = getSongs(artist)
total_songs = gs.get_song_list()
for i in total_songs:
    rl = rankLyrics(artist, i)
    print(rl.score_bw())