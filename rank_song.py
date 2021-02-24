#this script will use the other two tools to pull all the songs for an artist and rank the songs
#to find the worst song

from grab_all_songs import main as get_songs

all_songs = get_songs('frank ocean')
print(all_songs)