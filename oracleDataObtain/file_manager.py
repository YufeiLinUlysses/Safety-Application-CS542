import os

def CreateProject(sDir):
    if not os.path.exists(sDir):
        os.makedirs(sDir)

def CreateData(sProjectName, sUrl):
    queue = sProjectName + '/queue.txt'
    crwaled = sProjectName + '/crawled.txt'
    sActualData = sProjectName + '/crimeData.txt'
    if not os.path.isfile(queue):
        WriteFile(queue, sUrl)
    if not os.path.isfile(crwaled):
        WriteFile(crwaled, "")
    if not os.path.isfile(sActualData):
        WriteFile(sActualData, "")

def WriteFile(sPath, sData):
    f = open(sPath, "w")
    f.write(sData)
    f.close()

def AppendFile(sPath, sData):
    with open(sPath, 'a') as sFile:
        sFile.write(sData + "\n")

def DeleteFile(sPath):
    with open(sPath, 'w'):
        pass

def File2Set(sFileName):
    tempResult = set()
    with open(sFileName, "rt") as f:
        for line in f:
            tempResult.add(line.replace("\n", ""))
    return tempResult

def Set2File(needSet, sFile):
    DeleteFile(sFile)
    for sContent in needSet:
        AppendFile(sFile, sContent)
