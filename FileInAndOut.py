"""
Date: 07-03-2020
Author: Goutham R(Druffl3)
Notes: Related to Files
"""
class FileHandler(object):
    def ReadFromFile(self,fileName,accessMode):
        """
        Works with both absolute and normal path(If in the same directory as the script).
        """
        fileObj = open(fileName,accessMode)
        print("Name of the File: ", fileObj.name)
        print("Content: ", fileObj.read())
        fileObj.close()

    def OptimizedReadFromFile(self,fileName,accessMode):
        """
        Works with both absolute and normal path(If in the same directory as the script).
        """
        #with is a safer way of handling files, as it automatically closes the file after its block
        #of operations are completed.
        with open(fileName, accessMode) as fileObj:
            print("Name of the File: ", fileObj.name)
            #lines = fileObj.readlines()
            i = 1
            print(fileObj.read())
            """
            for line in lines:
                self._readLine(fileObj,i)
                i = i + 1
            """
        print(fileObj.closed) #To check if file is closed.

    def _readLine(self,fileObj,index):
        print("entered",index)
        print(fileObj.readline())

    def WriteToFile(self,fileName,accessMode):
        pass

LocalFileHandler = FileHandler()

LocalFileHandler.OptimizedReadFromFile("/Users/gouthamr/Documents/PythonProjects/TaleOfTwoPumpkins.txt","r")
