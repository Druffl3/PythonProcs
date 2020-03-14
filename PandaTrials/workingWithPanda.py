"""
This script introduces to a basic usage of Pandas
Date: 14March_2020
Author: Goutham R
Notes:
requires pandas and xlrd.
pip3 install --user pandas
pip3 install --user xlrd -> for excel support
"""
import pandas as pd

class pandaHandler(object):
    def ReadCSVFile(self,fileName: str) -> pd.core.frame.DataFrame:
        df = pd.read_csv(fileName)
        return df

    def ReadExcelFile(self,fileName: str) -> pd.core.frame.DataFrame:
        edf = pd.read_excel(fileName)
        return edf

    def ReturnTablesFromExcel(self,*titles: list) -> pd.core.frame.DataFrame:
        """
        *titles is a tupple object.
        """
        fileName = titles[0]
        titles = list(titles[1:])
        edf = (pd.read_excel(fileName)).head() #Takes the first five elements only.
        requiredTables = edf[titles]
        return requiredTables

    def ConvertDictToDataFrame(self, modelDictionary: dict) -> pd.core.frame.DataFrame:
        return pd.DataFrame(modelDictionary)

    def ConvertListToDataFrame(self, modelList: list) -> pd.core.frame.DataFrame:
        return pd.DataFrame(modelList)


global csv_path
global xlsx_path
global songs

csv_path = "majorLazor.csv"
xlsx_path = "majorLazor.xlsx"
songs = {"album":['Thriller','Back in Black', 'The Darkside of the Moon'], "release":['2011','1980','1969'] ,"Length":['00:42:19','00:42:11','00:00:03']}
dummy_song = ['a','b',('c','d'),3,['e','f']]

pH = pandaHandler()

#print(pH.ConvertToDataFrame(songs))
#print(pH.ConvertListToDataFrame(dummy_song))
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

bonitoFrame = myDataFrame[myDataFrame['Album'] == uniqueList[4]]

bonitoFrame.to_csv('bonito.csv')

print(pH.ReadCSVFile("bonito.csv"))
