import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
import webbrowser
import sys


def randomizer():
    num_of_letters = random.randint(1,6)
    #track_option = random.randint(0,39)
    search_seed = ""
    for x in range(num_of_letters):
        letter = random.choice("abcdefghijklmnopqrstuvwxyz")
        search_seed += letter
    return [search_seed]

def ArgumentReader():
    #Description:   Read and validets Arguments and assign to variable
    global state

    if len(sys.argv) > 1:
        if sys.argv[1] == "-app" and len(sys.argv) <= 2:
            state = 1
        elif sys.argv[1] == "-online" and len(sys.argv) <= 2:
            state = 2
        elif len(sys.argv) <= 2:
            print("this is not an option you can ran the app with")
            print("Options: \n1. -online \n2. -app")
            exit(1)
        else:
            print("this app accept only 1 option flag")
            print("Please enter only one of the following options")
            print("Options: \n1. -online \n2. -app")
            exit(2)


state = 0
ArgumentReader()



 #Run state thingy
while (state != 1 and state != 2) and len(sys.argv) < 2:
    state = int(input(" Please select a spotify player type \n Press 1 for application.  Press 2 for online Player \n"))
    if state == 1 or state == 2:
        break
    else:
        print(" you can enter only 1 or 2  \n Press 1 for application.  Press 2 for online Player \n")


#Crerating Sesion for all queris and Souch
Spotify_Session = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=<your client ID>,client_secret=<Your Client Secret>))

track_Search = randomizer()

Number_of_available_Tracks = 0

#results check for preventing app fails
while Number_of_available_Tracks == 0:

    #the track Search itself  data come as dict{dict{list[dict{}]}}
    Search = Spotify_Session.search(q=track_Search[0],limit=40)

    #randimzation of track
    Number_of_available_Tracks = len(Search["tracks"]["items"])

    if Number_of_available_Tracks < 2:
        track_Search = randomizer()
    else:
        break
track_Search.append(random.randint(0, Number_of_available_Tracks - 1))

# print(Search["tracks"]["items"][track_Search[1]].keys())#

if state == 2:
#opening track in spotify online
    track_id = Search["tracks"]["items"][track_Search[1]]["id"]
    webbrowser.open("https://open.spotify.com/track/" + track_id)


elif state == 1:

    track_id = Search["tracks"]["items"][track_Search[1]]["uri"]
    webbrowser.open(track_id)

#exit 42 is good remember 42 is Everything :-)
exit(42)

