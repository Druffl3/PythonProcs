"""
Date: 07-03-2020
Author: Goutham R(Druffl3)
Notes: Related to Files
"""
class FileHandler(object):
    def ReadFromFile(self,fileName,accessMode = "r"):
        """
        Works with both absolute and normal path(If in the same directory as the script).
        File access modes:
        r - read
        w - write
        a - append
        """
        fileObj = open(fileName,accessMode)
        print("Name of the File: ", fileObj.name)
        print("Content: ", fileObj.read())
        fileObj.close()

    def OptimizedReadFromFile(self,fileName,accessMode = "r"):
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
        print("Is file closed after read: ",fileObj.closed) #To check if file is closed.

    def _readLine(self,fileObj,index):
        print("entered",index)
        print(fileObj.readline())

    def WriteToFile(self,fileName,listOfTexts,accessMode = "w"):
        with open(fileName,accessMode) as fileObj:
            for line in listOfTexts:
                fileObj.write(line)
        print("Is file closed after write: ", fileObj.closed)

    def CopyFile(self,sourceFile,destinationFile):
        with open(sourceFile,"r") as readFile:
            with open(destinationFile,"w") as writeFile:
                for eachLine in readFile.readlines():
                    writeFile.write(eachLine)

LocalFileHandler = FileHandler()
#LocalFileHandler.OptimizedReadFromFile("/Users/gouthamr/Documents/PythonProjects/TaleOfTwoPumpkins.txt","r")
#LocalFileHandler.WriteToFile("LittleHearts.txt",["I wanna\n", "You wanna\n", "I don't know."])
#LocalFileHandler.WriteToFile("LittleHearts.txt",["I Jump\n", "You Jump\n", "Jumper is a good movie."],"a")
LocalFileHandler.CopyFile("LittleHearts.txt","Fractacl.txt")
LocalFileHandler.OptimizedReadFromFile("Fractacl.txt")
