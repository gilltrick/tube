## i use the discription varible of the metainformation object to store a preview link

import requests, re, modules, pickle, hashlib, datetime, os
from fake_headers import Headers

header = Headers(browser="chrome", os="win", headers=True)
metaInformationObjectList = []
fapsterPattern = "<a href=\"(.*)\" title=\"(.*)\">\n?<div class=\"img\">\n<img class=\"thumb_img lazyload\" data-src=\"(.*)\" alt=(.*)\" data-preview=\"(.*)\" width(.*)\n(.*)\n(.*)\n<span class=\"time\">(\d\d?:\d\d?)<\/span>\n<\/div>\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n<span class=\"atten\"><i class=\"icon-like\"><\/i>(.*)%<\/span>"
fapsterTagPattern = "<a href=\"https:\/\/fapster\.xxx\/categories(.*)\">\n<span class=\"name\">(.*)<\/span>"


def Run():
    command = input("Enter command: [-initdb, -printdb, -search, -long, -help]")
    if command == "-initdb":
        InitDB()
        print("fapsterDatabase loaded with " + str(len(metaInformationObjectList)) + " records")
        Run()
    if command == "-printdb":
        LoadMetaInformationObjectList()
        PrintMetaInformationObjectList()
    if command == "-search":
        InitDB()
        EnterKeyWords()
    if command == "-long":
        InitDB()
        LongScrape()
    if command == "-exit":
        exit()
    if command == "-help":
        print("Learn how to deal with the issue... I dont care")
        Run()
    print("Unknown Command...")
    Run()

def EnterKeyWords():
    keywords = re.split("\s+", input("Enter keywords for search: "))
    #pageCount = int(input("How many pages to search: "))
    pageCount = 1
    searchString = ""
    for word in keywords:
        if searchString != "": 
            searchString += "-"+word
        if searchString == "":
            searchString += word
    for page in range(pageCount):
        print("Extracting page: " + str(page))
        if page == 0:
            url = "https://fapster.xxx/search/"+searchString
        #if page != 0:
        #    url = "https://de.pornhub.com/video/search?search="+searchString + "&page=" + str(page)
        ExtractDataFromSite(url)
    command = input("Save Data To DB? ")
    if command == "y":
        SaveMetaInformationObjectList()
    if command != "y":
        print("Dumping data")
    Run()

def ExtractDataFromSite(_url):
    global metaInformationObjectList
    sourceCode = requests.get(_url, headers=header.generate()).text
    print(sourceCode)
    for match in re.finditer(fapsterPattern, sourceCode):
        metaInformationObject = modules.MetaInformationObject()
        videoUrl = match.group(1)
        videoTitle = match.group(2)
        videoDuration = match.group(9)
        rating = match.group(5)#da ist ein fehler mit der gruppenzuweisung
        thumbnailPath = match.group(3)
        previewLink = match.group(5)
        if MetaInformationObejctDuplication(videoUrl) == False:
            metaInformationObject.videoUrl = videoUrl
            metaInformationObject.videoTitle = videoTitle
            metaInformationObject.rating = rating
            metaInformationObject.videoDuration = videoDuration
            metaInformationObject.thumbnailPath = thumbnailPath
            metaInformationObject.discription = previewLink
            metaInformationObject.tagList = GrabTagList(videoUrl)
            metaInformationObject.id = CreateRandomId()
            metaInformationObject.data = "fapster"
            if ValidMetaInformationObject(metaInformationObject) == True:
                metaInformationObjectList.append(metaInformationObject)

def OK():
    return None

def GrabTagList(_url):
    sourceCode = requests.get(_url).text
    print("URL: " + _url + "\nVideo page source code loaded")
    tagList = []
    tag = ""
    for match in re.finditer(fapsterTagPattern, sourceCode):
        for i in range(len(match.groups())):
            if tag != "":
                try:
                    tag += " " + match.group(i+2)
                except:
                    OK()
            if tag == "":
                try:
                    tag += match.group(i+2)
                except:
                    OK()
        tagList.append(tag)
        tag = ""
    tagList = list(dict.fromkeys(tagList))
    return tagList

def LongScrape():
    lineToStart = input("Enter the line you want to start with: ")
    if lineToStart == "":
        lineToStart = 0
    pageCount = 1
    keyWordList = CreateDictionary()
    skipedItemList = []
    for i in range(int(lineToStart)):
        skipedItemList.append(keyWordList[i])
        keyWordList.remove(keyWordList[i])
    for skipedItem in skipedItemList:
        print(skipedItem + " skiped")
    keyWordsLeft = len(keyWordList) - len(skipedItemList)
    print(str(keyWordsLeft) + " key words left to scrape")
    searchString = ""
    lineCounter = int(lineToStart)
    for keyWord in keyWordList:
        print("Key word: " + keyWord + "@ line " + str(lineCounter))
        searchString = re.sub("\s", "-", keyWord)
        for page in range(pageCount):
            print("Extracting page: " + str(page))
            if page == 0:
                url = "https://fapster.xxx/search/"+searchString
            #if page != 0:
            #    url = "https://de.pornhub.com/video/search?search="+searchString + "&page=" + str(page)
            ExtractDataFromSite(url)
            SaveMetaInformationObjectList()
        lineCounter += 1
    Run()

def MetaInformationObejctDuplication(_vidoeUrl):
    global metaInformationObjectList
    for metaInformationobject in metaInformationObjectList:
        if _vidoeUrl == metaInformationobject.videoUrl:
            print("Duplication for: " + _vidoeUrl + " dumping data")
            return True
    return False    
    
def ValidMetaInformationObject(_metaInformationObject):
    if _metaInformationObject.videoUrl == "":
        print("no video url")
        return False
    if _metaInformationObject.videoTitle == "":
        print("no video title")
        return False
    if _metaInformationObject.videoDuration == "":
        print("no video duration")
        return False
    if len(_metaInformationObject.tagList) < 1:
        print("no tags")
        return False
    if _metaInformationObject.thumbnailPath == "":
        print("no thumbnail path")
        return False
    if _metaInformationObject.id == "":
        print("no id")
        return False
    return True

def SaveMetaInformationObjectList():
    global metaInformationObjectList
    file = open(os.getcwd()+"/static/data/fapster.db", "wb")
    pickle.dump(metaInformationObjectList, file)
    file.close()
    print("Database saved")

def InitDB():
    if os.path.exists(os.getcwd()+"/static/data/fapster.db"):
        LoadMetaInformationObjectList()
        return
    print("No database file found")
    command = input("Create a new file? ")
    if command == "yes":
        file = open(os.getcwd()+"/static/data/fapster.db", "wb")
        file.close()
        Run()

def LoadMetaInformationObjectList():
    if os.path.exists(os.getcwd()+"/static/data/fapster.db"):
        global metaInformationObjectList
        file = open(os.getcwd()+"/static/data/fapster.db", "rb")
        try:
            metaInformationObjectList = pickle.load(file)
        except:
            print("No data in db or data is corrupted")
        file.close()
        return
    print("Cant load database file")

def PrintMetaInformationObjectList():
    global metaInformationObjectList
    tagString = ""
    for metaInformationObject in metaInformationObjectList:
        for tag in metaInformationObject.tagList:
            if tagString != "":
                tagString += " " + tag
            if tagString == "":
                tagString += tag
        print("Video-Title: " + metaInformationObject.videoTitle + "\nRating: " + metaInformationObject.rating + "\nVideo-Url: " + metaInformationObject.videoUrl + "\nVideo-Duration: " + metaInformationObject.videoDuration + "\nVideo-Thumbnail: " + metaInformationObject.thumbnailPath + "\nTag-List: " + tagString + "\nDiscription: " + metaInformationObject.discription + "\nID: " + metaInformationObject.id + "\nData: " + metaInformationObject.data + "\n")  
        tagString = ""
    print("Record count: " + str(len(metaInformationObjectList)))
    Run() 

def CreateDictionary():
    keyWordDictionary = open(os.getcwd()+ "/static/data/keyWordDictionary" , "r")
    lines = keyWordDictionary.readlines()
    return lines

def CreateRandomId():
    return hashlib.md5(str(datetime.datetime.now()).encode()).hexdigest()

def GetFapsterDatabase():
    global metaInformationObjectList
    return metaInformationObjectList  
    
def RemoveRatingFromAllObjects():
    global metaInformationObjectList
    for metaInformationObject in metaInformationObjectList:
        metaInformationObject.rating = ""
    SaveMetaInformationObjectList()    


if __name__ == "__main__":
    InitDB()
    RemoveRatingFromAllObjects()
    Run()
    

    
############################# H E L P E R ##############################
#
# payload = {
#    
#             "mode": "async",
#             "function": "get_html",
#             "block_id": "list_videos_videos_list_search_result",
#             "q": "sperma schlucken",
#             "category_ids": "" ,
#             "sort_by": "",
#             "from_videos": "1",
#             "from_albums": "1",
#             "_": "11321685468"
#           }
########################################################################            
#
# keyWords = "sperma schlucken"
# nextPageNumber = "3"
# string = "{\"mode\":\"async\",\"function\":\"get_html\",\"block_id\":\"list_videos_videos_list_search_result\",\"q\":\""+keyWords+"\",\"category_ids\":\"\",\"sort_by\":\"\",\"form_videos\":\""+nextPageNumber+"\",\"form_albums\":\""+ nextPageNumber+"\",\"_\";\"\"}"
########################################################################
#
# def CreatePayload():
#     return None
#
########################################################################