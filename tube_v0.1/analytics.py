import os, re, datetime, hashlib, pickle, database

analyticalObjectList = []

def InitDB():
    if os.path.exists(os.getcwd()+"/static/data/analytics.db"):
        global analyticalObjectList
        file = open(os.getcwd()+"/static/data/analytics.db", "rb")
        try:
            analyticalObjectList = pickle.load(file)
            file.close()
        except:
            print("Can't load analytics database")
            file.close()
            return
    print("Can't load analytics database")
        
def NewAnalyticalObject(_url):
    newAnalyticalObject = database.modules.AnaltycisObject()
    metaInformationObject = database.GetMetaInfromationObjectByVideoUrl(_url)
    newAnalyticalObject.metaInformationObject = metaInformationObject
    newAnalyticalObject.watchCounter = 1
    analyticalObjectList.append(newAnalyticalObject)
    SaveAnalyticalObjectList()
    
def SaveAnalyticalObjectList():
    global analyticalObjectList
    file = open(os.getcwd()+"/static/data/analytics.db", "wb")
    pickle.dump(analyticalObjectList, file)
    file.close()
    
def AnalyticalObjectExits(_url):
    global analyticalObjectList
    for analyticalObject in analyticalObjectList:
        if analyticalObject.metaInformationObject.videoUrl == _url:
            analyticalObject.watchCounter += 1
            SaveAnalyticalObjectList()
            #append data
            return
    NewAnalyticalObject(_url)
    
def PrintData():
    global analyticalObjectList
    for analyticalObject in analyticalObjectList:
        print("Video-Title: " + analyticalObject.metaInformationObject.videoTitle + "\nWatch-Counter: " + str(analyticalObject.watchCounter)+"\n")
        
if __name__ == "__main__":
    InitDB()
    PrintData()