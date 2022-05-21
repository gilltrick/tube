from flask import Flask, render_template, request, make_response, redirect
import database, re, math, analytics

cookiePattern = re.compile("{\"username\":\"(.*)\";\"password\":\"(.*)\"}")

app = Flask(__name__)

@app.route("/")
def index():
    resultCount = 0
    return render_template("home.html", resultCount=resultCount)

@app.route("/home")
def home():
    resultCount = 0
    return render_template("home.html", resultCount=resultCount)

@app.route("/loginUser", methods=["post"])
def loginUser():
    username = request.form["username"]
    password = request.form["password"]
    if database.userDatabase.CheckCredentials(username, password) == True:
        resultCount = 0
        cookieValue = "{\"username\":\""+username+"\";\"password\":\""+password+"\"}"
        response = make_response(render_template("home.html", resultCount=resultCount))
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
    resultCount = 32
    if len(mioList) < 32:
        resultCount = len(mioList)
    pageCounter = 1
    maxPageCount = math.ceil(len(mioList)/32)
    return render_template("home.html", mioList=mioList, pageCounter=pageCounter, maxPageCount=maxPageCount, resultCount=resultCount, keyWords=keyWords)

@app.route("/redirect", methods=["post"])
def Redirect():
    url = request.form["url"]
    #at this point i can start to grab data
    print("URL: " + url)
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
        cookieValue = request.cookies.get("data")
        username, password = GetCookieData(cookieValue)
        if database.userDatabase.CheckCredentials(username, password) == True:
            metaInformationObject = database.GetMetaInfromationObjectByVideoUrl(url)
            analytics.AnalyticalObjectExits(url)
            if metaInformationObject == "invalid":
                return "ERROR"
            return render_template("videoPlayer.html", metaInformationObject=metaInformationObject)
        metaInformationObject = database.modules.MetaInformationObject()
        metaInformationObject.videoUrl = "/static/data/__/ahahah_low.mp4"
        metaInformationObject.videoTitle = "You didn't say the magic word"
        metaInformationObject.discription = "To watch the clip you want you need to be loged in"
        return render_template("videoPlayer.html", metaInformationObject=metaInformationObject)
    metaInformationObject = database.GetMetaInfromationObjectByVideoUrl(url)
    analytics.AnalyticalObjectExits(url)
    if metaInformationObject == "invalid":
        return "ERROR"
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

if __name__ == "__main__":
    database.InitDatabase()
    app.run(debug=True, host="0.0.0.0")