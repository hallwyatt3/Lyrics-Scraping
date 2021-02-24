#this script will use the other two tools to pull all the songs for an artist and rank the songs
#to find the worst song

from grab_all_songs import getSongs

gs = getSongs('frank ocean')
print(gs.get_song_list())