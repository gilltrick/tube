import os, re, modules, cv2, pickle, pornhubScraper, fapsterScraper, datetime, hashlib, userDatabase, analytics

fullList = []
defaultMetaInformationList = []
metaInformationObjectList = []
videoStoragePath = "/static/storage/specials/"
dbPattern = "{\"videoTitle\":\"(.*)\"videoUrl\":\"(.*)\"videoImageUrl\":\"(.*)\"videoDuration\":\"(.*)\",\"directLink\":\"(.*)\",\"categoryName\":\"(.*)\",\"id\":\"(.*)\",\"videoLink\":\"(.*)\",\"tagList\":\[(.*)\],\"userTagList\":\[(.*)\],\"durationInSeconds\":(.*)}"
tagListPatter = "\w+|\s\w+"  

pornhubMetaInformationObjectList = []
fapsterMetaInformationObjectList = []

def GetVideoDuration(_videoUrl):
    data = cv2.VideoCapture(_videoUrl)
    frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
    seconds = int(frames / 30)
    return seconds

def InitDatabase():
    file = open(os.getcwd()+"/static/data/videoDatabase.db", "rb")
    global metaInformationObjectList
    metaInformationObjectList = pickle.load(file)
    file.close()
    LoadPornhubDB()
    LoadFapsterDB()
    userDatabase.InitDB()
    analytics.InitDB()
    

def LoadPornhubDB():
    pornhubScraper.InitDB()
    GetPornHubDataBase()
    global metaInformationObjectList
    global pornhubMetaInformationObjectList
    tempList = metaInformationObjectList.copy()
    for metaInformationObject in pornhubMetaInformationObjectList:
        tempList.append(metaInformationObject)
    global fullList
    fullList = tempList.copy()
    
def LoadFapsterDB():
    fapsterScraper.InitDB()
    GetFapsterDatabase()
    global fullList
    for metaInformationObject in fapsterMetaInformationObjectList:
        fullList.append(metaInformationObject)
    

def LoadTagList(_line):
    tagList = []
    result = re.findall(tagListPatter, _line)
    for tag in result:
        tagList.append(tag)
    return tagList
                    
def Run():
    command = input("Enter command: [--initdb, --add, --edit, --printdb, --remove, --help]")
    if command == "--initdb":
        InitDatabase()
        Run()
    if command == "--add":
        print(end="", flush=True)
        LoadMetaInformationObjectList()
        AddVideo()
    if command == "--edit":
        print(end="", flush=True)
        LoadMetaInformationObjectList()
        EditVideo()
    if command == "--printdb":
        print(end="", flush=True)
        PrintDataBaseContent()
    if command == "--remove":
        print(end="", flush=True)
        RemoveVideoFromDatabase()
    if command == "--help":
        print(end="", flush=True)
        print("This is the help page for gilltrickdb:\n You can enter these commands:\n --initdb: this initializes the database its like reloading\n --help: Prints this page")
        input("Press Enter to exit help")
        Run()

def RemoveVideoFromDatabase():
    fileName = input("Enter file name (with extension): ")
    global metaInformationObjectList
    if len(metaInformationObjectList) < 1:
        InitDatabase()
    path = "/static/storage/specials/"
    for metaInformationObject in metaInformationObjectList:
        fName = re.sub(path, "", metaInformationObject.videoUrl)
        if fName == fileName:
            command = input("Do you want to remove the file: " + fileName + "?")
            if command == "y" or "-y" or "--y" or "yes" or "-yes" or "--yes":
                path = metaInformationObject.videoUrl
                metaInformationObjectList.remove(metaInformationObject)
                print("File: " +fileName + " removed from database")
                command = input("Do you want to delete the file permanently ?")
                if command == "y" or "-y" or "--y" or "yes" or "-yes" or "--yes":
                    os.remove(os.getcwd()+path)
                    print("File " + fileName + " got deleted!")
            SaveMetaInformationObjectList()
                 
def LoadMetaInformationObjectList():
    if os.path.exists(os.getcwd()+"/static/data/videoDatabase.db"):
        file = open(os.getcwd()+"/static/data/videoDatabase.db", "rb")
        global metaInformationObjectList
        metaInformationObjectList = pickle.load(file)
        file.close()
        return
    command = input("No database file found.\nCreate a new file? ")
    if command == "y" or "-y" or "--y" or "yes" or "-yes" or "--yes":
        file = open(os.getcwd()+"/static/data/videoDatabase.db", "wb")
        file.close()

def SaveMetaInformationObjectList():
    file = open(os.getcwd()+"/static/data/videoDatabase.db", "wb")
    global metaInformationObjectList
    pickle.dump(metaInformationObjectList, file)
    file.close()
    
def AddVideo():
    global metaInformationObjectList
    print("Enter video data:")
    videoUrl = videoStoragePath + input("Enter filen name (with extension): ")
    for metaInformationObject in metaInformationObjectList:
        if metaInformationObject.videoUrl == videoUrl:
            print("Cant't add the same file name a second time to database")
            AddVideo()
    videoTitle = input("Enter video name: ")
    videoDuration = GetVideoDuration(os.getcwd()+"/"+videoUrl)
    rating = input("Enter video rating")
    tagList = re.split("\s+", input("Enter tags: "))
    discription = input("Enter video discription: ")
    command = input("Leaf empty for random id or \nAdd id: ")
    if command == "":
        id = CreateRandomId()
    metaInformationObject = modules.MetaInformationObject()
    metaInformationObject.videoUrl = videoUrl
    metaInformationObject.videoTitle = videoTitle
    metaInformationObject.videoDuration = videoDuration
    metaInformationObject.rating = rating
    metaInformationObject.tagList = tagList
    metaInformationObject.discription = discription
    metaInformationObject.id = id
    command = input("Write video data to database? (y/n)")
    if command == "y" or "-y" or "--y" or "yes" or "-yes" or "--yes":  
        metaInformationObjectList.append(metaInformationObject)
        SaveMetaInformationObjectList()
    return None

def EditVideo():
    fileName = videoStoragePath + input("Enter file name: ")
    global metaInformationObjectList
    tagString = ""
    tagList = []
    for metaInformationObject in metaInformationObjectList:
        
        if metaInformationObject.videoUrl == fileName:
            
            videoTitle = input("Enter video name: ")
            print("New VideoTitle: " + videoTitle)
            if videoTitle == "":
                print("No change on video title")
                videoTitle = metaInformationObject.videoTitle
            videoDuration = GetVideoDuration(os.getcwd()+"/"+fileName)
            
            rating = input("Enter video rating")
            if rating == "":
                rating = metaInformationObject.rating
                
            for tag in metaInformationObject.tagList:
                tagString += "," + tag
                
            print("Current tags: " + tagString)
            command = input("Enter commad for editing the tag list (--replace, --remove, --add)")
            
            if command == "":
                tagList = metaInformationObject.tagList
            
            if command == "--replace":
                replaceWhat = input("Replace: ")
                replaceWith = input("with: ")
                for tag in metaInformationObject.tagList:
                    if tag == replaceWhat:
                        metaInformationObject.tagList.remove(tag)
                        metaInformationObject.tagList.append(replaceWith)
                        tagList = metaInformationObject.tagList
                        
            if command == "--remove":
                removeWhat = input("Remove: ")
                for tag in metaInformationObject.tagList:
                    if tag == removeWhat:
                        metaInformationObject.tagList.remove(tag)
                        
            if command == "--add":     
                tempTagList = re.split("\s+", input("Enter tag(s): "))
                tagList = metaInformationObject.tagList
                for tag in tempTagList:
                    tagList.append(tag)
            
            if command == "--duration":
                videoDuration = input("Enter video duration in seconds: ")
            
            discription = input("Change discrioption: ")
            if discription == "":
                discription = metaInformationObject.discription
                
            id = input("Enter id (--rnd) for a new random id")
            if id == "--rnd":
                id = CreateRandomId()
            if id == "":
                id = metaInformationObject.id
                
            metaInformationObject.videoUrl = fileName
            metaInformationObject.videoTitle = videoTitle
            metaInformationObject.videoDuration = videoDuration
            metaInformationObject.rating = rating
            metaInformationObject.tagList = tagList
            metaInformationObject.discription = discription
            metaInformationObject.id = id
            command = input("Write video data to database? (y/n)")
            if command == "y" or "-y" or "--y" or "yes" or "-yes" or "--yes":  
                SaveMetaInformationObjectList()
                EditVideo()
        
def SearchByKeyword(_keyWords):
    global fullList
    tempList = fullList.copy()
    resultList = []
    ungready = False
    if _keyWords[0] == "":
        resultList = tempList
        return resultList
    if _keyWords[0] == "-ug":
        _keyWords.remove(_keyWords[0])
        ungready = True
    if _keyWords[0] == "-selected":
        if _keyWords[1] == "":
            global metaInformationObjectList
            return metaInformationObjectList
        if _keyWords[1] != "":
            _keyWords.remove(_keyWords[0])
            tempList = metaInformationObjectList.copy()
    gotcha = False
    if ungready == False:
        for keyWord in _keyWords:
            for metaInformationObject in tempList:
                if keyWord in metaInformationObject.videoTitle and gotcha == False:
                    gotcha = True
                    resultList.append(metaInformationObject)
                    tempList.remove(metaInformationObject)
                if gotcha == False:
                    for tag in metaInformationObject.tagList:
                        if tag == keyWord:
                            gotcha = True
                            resultList.append(metaInformationObject)
                            tempList.remove(metaInformationObject)
                gotcha = False
    if ungready == True:
        greadyMatch = False
        for metaInformationObject in tempList:
            for keyWord in _keyWords:
                if keyWord not in fullList.tagList:
                    break
                if keyWord in fullList.tagList:
                    greadyMatch = True
            if greadyMatch == True:
                resultList.append(metaInformationObject)
                tempList.remove(metaInformationObject)
                greadyMatch = False
    return resultList

def GetMetaInfromationObjectByVideoUrl(_videoUrl):
    # global metaInformationObjectList
    # global pornhubMetaInformationObjectList
    # for metaInformationObject in metaInformationObjectList:
    #     if metaInformationObject.videoUrl == _videoUrl:
    #         return metaInformationObject
    # for metaInformationObject in pornhubMetaInformationObjectList:
    #     if metaInformationObject.videoUrl == _videoUrl:
    #         return metaInformationObject
    # return "invalid"
    global fullList
    for metaInformationObject in fullList:
        if metaInformationObject.videoUrl == _videoUrl:
            return metaInformationObject
    return "invalid"

def PrintDataBaseContent():
    if os.path.exists(os.getcwd()+"/static/data/videoDatabase.db"):
        file = open(os.getcwd()+"/static/data/videoDatabase.db", "rb")
        global metaInformationObjectList
        metaInformationObjectList = pickle.load(file)
        file.close()
        tagListLine = ""
        for metaInformationObject in metaInformationObjectList:
            for tag in metaInformationObject.tagList:
                tagListLine += " "+ tag
            print("Video Title: " + metaInformationObject.videoTitle + "\nVideoPath: " + metaInformationObject.videoUrl + "\nVideo Rating: " + metaInformationObject.rating + "\nVideoDuration: " + str(metaInformationObject.videoDuration) + " seconds \nTag-List: " + tagListLine + "\nThumbnail-Path: " + metaInformationObject.thumbnailPath + "\nDiscription: " + metaInformationObject.discription + "\nID: " + metaInformationObject.id + "\n")
            tagListLine = ""
        print("Record Count: ", len(metaInformationObjectList))
    print("No database file found")

def CreateRandomId():
    return hashlib.md5(str(datetime.datetime.now()).encode()).hexdigest()
    
def GetMetaInformationObjectList():
    global metaInformationObjectList
    return metaInformationObjectList

def GetPornHubDataBase():
    global pornhubMetaInformationObjectList
    pornhubMetaInformationObjectList = pornhubScraper.GetPornhubDatabase()

def GetFapsterDatabase():
    global fapsterMetaInformationObjectList
    fapsterMetaInformationObjectList = fapsterScraper.GetFapsterDatabase()
    
if __name__ == "__main__":
    Run()



################################## H E L P E R ####################################
#
####################### I use this function to copy data ##########################
# 
# def VideoUrlToThumbnailPath():
#     InitDatabase()
#     global metaInformationObjectList
#     for metaInformationObject in metaInformationObjectList:
#         metaInformationObject.thumbnailPath = metaInformationObject.videoUrl
#     SaveMetaInformationObjectList()
#
###################################################################################
#
###################### I use this function i update a module ######################
#
############################ L O G I C - S E C T I O N ############################
#
# create the new module call it newModule
# create a backup copy of your data
#
# function call:
#
# load all of the current data
# create a temporary list for the new modules
# loop through the current list
# create a new object of the new module
# copy the current data to the new module
# REMEMBER: If you change the varible names you brake a lot of code
#           But its quit easy to fix by using some find and replace
# let the new varibles untouched
# add the newModule object to the newModuleList
# clear the current global metaInformationObjectList
# copy new module list to global metaInformationObjectList
# Call The SaveMetaInformationObjectList function to save the updates modules list
#
# add the new varibles to the outdates MetaInformationObject class
# restart database.py
# start database.py -> --initdb -> --printdb
#
# if there is the same data then before everything worked well
# functions to update in database.py:
#   --add
#   --edit
#   --print
#
###################################################################################   
# def ModuleUpdate():
#     InitDatabase()
#     global metaInformationObjectList
#     newModuleList = []
#     for metaInformationObject in metaInformationObjectList:
#         newModule = modules.newModule()
#         newModule.videoUrl = metaInformationObject.videoUrl
#         newModule.videoTitle = metaInformationObject.videoTitle
#         newModule.videoDuration = metaInformationObject.videoDuration
#         newModule.rating = metaInformationObject.rating
#         newModule.tagList = metaInformationObject.tagList
#         newModule.thumbnailPath = metaInformationObject.thumbnailPath
#         newModule.discription = metaInformationObject.discription
#         newModule.id = ""
#         newModule.data = ""
#         newModuleList.append(newModule)
#     metaInformationObjectList.clear()
#     metaInformationObjectList = newModuleList.copy()
#     SaveMetaInformationObjectList()
#     return True
# i will use this function to add random ids to all the old data
# def Temp():
#     InitDatabase()
#     global metaInformationObjectList
#     for metaInformationObject in metaInformationObjectList:
#         metaInformationObject.id = CreateRandomId()
#     SaveMetaInformationObjectList()
#
# run the ModuleUpdate function again but replace newModule with MetaInformationObject
#
####################################################################################
