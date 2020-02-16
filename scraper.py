import sys
import lyricsgenius as genius
import pandas as pd
import os
import json

dataset = "Eminem_dataset.txt"
writer = "Eminem"
json_str = "Lyrics_Eminem.json"

if __name__ == "__main__":
    geniusCreds = "sTzgVYcb_lBs-WPI5q35Gf9lvZ0My3bFyzZ35-KYUp2SAHnjxjZll7rqr09HNOHV"
    api = genius.Genius(geniusCreds)
    artist = api.search_artist(writer, max_songs = 200)
    os.getcwd()
    artist.save_lyrics()
    Artist=json.load(open(json_str))

    with open(dataset, 'w') as file_:
        for song in range(len(Artist['songs'])):
            title = Artist['songs'][song]['title']
            lyrics = Artist['songs'][song]['lyrics']
            line = "{}\t{}\t{}\n".format(title, writer, lyrics.replace("\n", "\\"))
            file_.write(line)
            
        

   