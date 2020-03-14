"""
This script introduces to a basic usage of Pandas
Date: 14March_2020
Author: Goutham R
"""
import pandas as pd

csv_path = "majorLazor.csv"
xlsx_path = "majorLazor.xlsx"

songs = {"album":['Thriller','Back in Black', 'The Darkside of the Moon'], "release":['2011','1980','1969'] ,"Length":['00:42:19','00:42:11','00:00:03']}

#df stands for Data Frame
df = pd.read_csv(csv_path)
#edf stands for Excel Data Frame
edf = pd.read_excel(xlsx_path)

dummy_song = ['a','b',('c','d'),3,['e','f']]

#Converting a dictionary to a data frame
song_frame = pd.DataFrame(songs)

print(song_frame)
print(type(song_frame))
