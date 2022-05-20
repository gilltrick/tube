from flask import Flask, render_template, request
import database, re, math

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    resultCount = 0
    return render_template("home.html", resultCount=resultCount)

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

@app.route("/page", methods=["post"])
def page():
    keyWords = request.form["keyWords"]
    pageCounter = int(request.form["pageCounter"])
    command = request.form["command"]
    keyWordsList = re.split("\s+", keyWords)
    mioList = database.SearchByKeyword(keyWordsList)
    print(len(mioList))
    if command == "nextPage":
        for i in range(32*pageCounter):
            mioList.remove(mioList[0])
        pageCounter += 1
    if command =="prevPage":
        pageCounter -= 1
        for i in range(32*(pageCounter-1)):
            mioList.remove(mioList[0])   
    print(len(mioList))
    resultCount = 32
    if len(mioList) < 32:
        resultCount = len(mioList)  
    maxPageCount = math.ceil(len(mioList)/32)
    return render_template("home.html", mioList=mioList, pageCounter=pageCounter, maxPageCount=maxPageCount, resultCount=resultCount, keyWords=keyWords)

@app.route("/playVideo", methods=["post", "get"])
def videoPlayer():
    url = request.form["videoUrl"]
    metaInformationObject = database.GetMetaInfromationObjectByVideoUrl(url)
    if metaInformationObject == "invalid":
        return "ERROR"
    return render_template("videoPlayer.html", metaInformationObject=metaInformationObject)        

if __name__ == "__main__":
    database.InitDatabase()
    app.run(debug=True, host="0.0.0.0")