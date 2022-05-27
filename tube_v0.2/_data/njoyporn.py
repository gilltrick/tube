from flask import Flask, render_template, request, make_response, redirect
import re, math, database, analytics
from threading import Thread

cookiePattern = re.compile("{\"username\":\"(.*)\";\"password\":\"(.*)\"}")
app = Flask(__name__)

@app.route("/")
def index():
    resultCount = 0
    return render_template("home.html", resultCount=resultCount, popularCategoriesList=database.GetPopularCategoriesList(), popularPornStarList=database.GetPopularPornStarList())

@app.route("/home")
def home():
    resultCount = 0
    return render_template("home.html", resultCount=resultCount, popularCategoriesList=database.GetPopularCategoriesList(), popularPornStarList=database.GetPopularPornStarList())

@app.route("/loginUser", methods=["post"])
def loginUser():
    username = request.form["username"]
    password = request.form["password"]
    print("DEBGU: njoyporn.py >> ", username, password)
    if database.userDatabase.CheckCredentials(username, password) == True:
        resultCount = 0
        cookieValue = "{\"username\":\""+username+"\";\"password\":\""+password+"\"}"
        keyWords = "-selected"
        keyWordsList = re.split("\s+", keyWords)
        mioList = database.SearchByKeyword(keyWordsList)
        maxPageCount = math.ceil(len(mioList)/32)
        pageCounter = 1
        resultCount = 32
        if len(mioList) < 32:
            resultCount = len(mioList)  
        response = make_response(render_template("home.html", mioList=mioList, pageCounter=pageCounter, maxPageCount=maxPageCount, resultCount=resultCount, keyWords=keyWords))
        response.set_cookie("data", cookieValue)
        return response
    metaInformationObject = database.modules.MetaInformationObject()
    metaInformationObject.videoUrl = "/static/data/__/ahahah_low.mp4"
    metaInformationObject.videoTitle = "You didn't say the magic word"
    metaInformationObject.discription = "To watch the clip you want you need to be loged in"
    return render_template("videoPlayer.html", metaInformationObject=metaInformationObject)
        
@app.route("/search", methods=["post"])
def search():
    keyWords = request.form["keyWords"]
    keyWordsList = re.split("\s+", keyWords)
    mioList = database.SearchByKeyword(keyWordsList)
    Thread(target=analytics.SaveKeyWordList(keyWordsList))
    Thread(target=analytics.UpdateCategoryObject(keyWords))
    Thread(target=analytics.UpdatePornStarObject(keyWords))
    resultCount = 32
    if len(mioList) < 32:
        resultCount = len(mioList)
    pageCounter = 1
    maxPageCount = math.ceil(len(mioList)/32)
    if len(mioList) < 1:
        return render_template("home.html", resultCount=0, popularCategoriesList=database.GetPopularCategoriesList(), popularPornStarList=database.GetPopularPornStarList())
    return render_template("home.html", mioList=mioList, pageCounter=pageCounter, maxPageCount=maxPageCount, resultCount=resultCount, keyWords=keyWords)

@app.route("/redirect", methods=["post"])
def Redirect():
    url = request.form["url"]
    print("NJOYPORN: URL: " + url)
    analytics.AnalyticalObjectExits(url)
    return redirect(url)

@app.route("/page", methods=["post"])
def page():
    keyWords = request.form["keyWords"]
    pageCounter = int(request.form["pageCounter"])
    command = request.form["command"]
    keyWordsList = re.split("\s+", keyWords)
    mioList = database.SearchByKeyword(keyWordsList)
    maxPageCount = math.ceil(len(mioList)/32)
    if command == "nextPage":
        for i in range(32*pageCounter):
            mioList.remove(mioList[0])
        pageCounter += 1
    if command =="prevPage":
        pageCounter -= 1
        for i in range(32*(pageCounter-1)):
            mioList.remove(mioList[0])   
    resultCount = 32
    if len(mioList) < 32:
        resultCount = len(mioList)        
    return render_template("home.html", mioList=mioList, pageCounter=pageCounter, maxPageCount=maxPageCount, resultCount=resultCount, keyWords=keyWords)

@app.route("/playVideo", methods=["post"])
def videoPlayer():
    url = request.form["videoUrl"]
    if url == "":
        return "error"
    if "special" in url:
        metaInformationObject = database.GetMetaInfromationObjectByVideoUrl(url)
        if metaInformationObject.origin == "free":
            analytics.AnalyticalObjectExits(url)
            return render_template("videoPlayer.html", metaInformationObject=metaInformationObject)
        
        cookieValue = request.cookies.get("data")
        username, password = GetCookieData(cookieValue)
        if database.userDatabase.CheckCredentials(username, password) == True:
            if metaInformationObject == "invalid":
                return "ERROR"
            return render_template("videoPlayer.html", metaInformationObject=metaInformationObject)
        metaInformationObject = database.CreateDummyObject()
        return render_template("videoPlayer.html", metaInformationObject=metaInformationObject)
    metaInformationObject = database.GetMetaInfromationObjectByVideoUrl(url)
    analytics.AnalyticalObjectExits(url)
    if metaInformationObject == "invalid":
        metaInformationObject = database.CreateDummyObject()
        return render_template("videoPlayer.html", metaInformationObject=metaInformationObject)
    return render_template("videoPlayer.html", metaInformationObject=metaInformationObject)        

@app.route("/login")
def login():
    return render_template("login.html")

def GetCookieData(_cookieValue):
    if _cookieValue == None:
        return "",""
    result = re.search(cookiePattern, _cookieValue)
    username = result.group(1)
    password = result.group(2)
    return username, password

@app.route("/upVote", methods=["post"])
def upVote():
    id = request.form["upVote"]
    database.UpdateMetaInformationObject(id, "upVote", 1)
    return "<script>alert(\"Thanks for your vote!.\");location.href = \"/\";</script>" 

@app.route("/downVote", methods=["post"])
def downVote():
    id = request.form["upVote"]
    database.UpdateMetaInformationObject(id, "downVote", 1)
    return "<script>alert(\"Thanks for your vote!.\");location.href = \"/\";</script>" 

@app.route("/impressum")
def impressum():
    return render_template("impressum.html")    

#http://www.njoyporn.com/video_01552022_dirty-talking-cumsluts
@app.route("/video_01552022_dirty-talking-cumsluts")
def add():
    metaInformationObject = database.GetMetaInformationObjectById("eeb0f9991f46a8293558e3103ecf594e")
    analytics.AnalyticalObjectExits(metaInformationObject.videoUrl)
    return render_template("videoPlayer.html", metaInformationObject=metaInformationObject) 

@app.route("/sendComment", methods=["post"])
def sendComment():
    videoId = request.form["videoId"]
    commentContent = request.form["commentContent"]
    writerName = request.form["witerName"]
    database.AddComment(videoId, commentContent, writerName)
    metaInformationObject = database.GetMetaInformationObjectById(videoId)
    return render_template("videoPlayer.html", metaInformationObject=metaInformationObject)

if __name__ == "__main__":
    database.InitDatabase()
    app.run(debug=True, host="0.0.0.0", port=5001)