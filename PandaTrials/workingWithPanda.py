"""
This script introduces to a basic usage of Pandas
Date: 14March_2020
Author: Goutham R
Notes:
requires pandas and xlrd.
pip3 install --user pandas
pip3 install --user xlrd -> To read excel files
pip3 install --user openpyxl -> To write excel files
"""
import pandas as pd

class pandaHandler(object):
    def ReadCSVFile(self,fileName: str) -> pd.core.frame.DataFrame:
        df = pd.read_csv(fileName)
        return df

    def ReadExcelFile(self,fileName: str) -> pd.core.frame.DataFrame:
        edf = pd.read_excel(fileName)
        return edf

    def ReturnTablesFromExcel(self,*titles: tuple) -> pd.core.frame.DataFrame:
        fileName = titles[0]
        titles = list(titles[1:])
        edf = (pd.read_excel(fileName)).head() #Takes the first five elements only.
        requiredTables = edf[titles]
        return requiredTables

    def ConvertToDataFrame(self, collection) -> pd.core.frame.DataFrame:
        return pd.DataFrame(modelDictionary)


global csv_path
global xlsx_path
global songs

csv_path = "majorLazor.csv"
xlsx_path = "majorLazor.xlsx"
#xlsx_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx"
songs = {"album":['Thriller','Back in Black', 'The Darkside of the Moon'], "release":['2011','1980','1969'] ,"Length":['00:42:19','00:42:11','00:00:03']}
dummy_song = ['a','b',('c','d'),3,['e','f']]

pH = pandaHandler()

#print(pH.ConvertToDataFrame(songs))
#print(pH.ConvertToDataFrame(dummy_song))
#print(pH.ReturnTablesFromExcel(xlsx_path,"Title","Album"))
print(xlsx_path," opened")
myDataFrame = pH.ReadExcelFile(xlsx_path)
# print(myDataFrame.loc[0,'Year']) # Loc -> [row index, columnt title/header]
# print(myDataFrame.iloc[1,1]) # iLoc -> [row index, column index]
# print("Table from row 0 to row 3, and column Year to Title")
# print(myDataFrame.loc[0:2,'Year':'Title']) #In Loc, rowspan: index to index
# print("Table from row 3 to row 6, and column 1:2")
# print(myDataFrame.iloc[0:2,0:3]) #In iLoc row and column span: index to nth position.
uniqueList = myDataFrame['Album'].unique() #Like an intersection between sets. Displays unique elements in the specified column.
print(uniqueList)

bonitoFrame = myDataFrame[myDataFrame['Album'] == uniqueList[5]]

bonitoFrame.to_excel('bonito.xlsx') #to_csv or to_excel

print(pH.ReadExcelFile("bonito.xlsx"))
