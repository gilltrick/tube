from flask import Flask, render_template, request, make_response, redirect, send_from_directory
import re, math, os, database, analytics, api, communication
from threading import Thread


cookiePattern = re.compile("{\"username\":\"(.*)\";\"password\":\"(.*)\"}")
instancePath = os.getcwd()+"/protected"
app = Flask(__name__, instance_path = instancePath)


@app.route("/")
def index():
    resultCount = 0
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:   
        return render_template("home.html", resultCount=resultCount, totalRecordsCount=database.GetTotalRecordsCount(), popularCategoriesList=database.GetPopularCategoriesList(), popularPornStarList=database.GetPopularPornStarList(), isLogedIn=True)
    return render_template("index.html", resultCount=resultCount, totalRecordsCount=database.GetTotalRecordsCount(), popularCategoriesList=database.GetPopularCategoriesList(), popularPornStarList=database.GetPopularPornStarList(), isLogedIn=False)

@app.route("/home")
def home():
    resultCount = 0
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:   
        return render_template("home.html", resultCount=resultCount, totalRecordsCount=database.GetTotalRecordsCount(), popularCategoriesList=database.GetPopularCategoriesList(), popularPornStarList=database.GetPopularPornStarList(), isLogedIn=True)
    return render_template("index.html", resultCount=resultCount, totalRecordsCount=database.GetTotalRecordsCount(), popularCategoriesList=database.GetPopularCategoriesList(), popularPornStarList=database.GetPopularPornStarList(), isLogedIn=False)

@app.route("/index")
def INDEX():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:   
        return render_template("home.html", resultCount=0, totalRecordsCount=database.GetTotalRecordsCount(), popularCategoriesList=database.GetPopularCategoriesList(), popularPornStarList=database.GetPopularPornStarList(), isLogedIn=True)
    return render_template("index.html", resultCount=0, totalRecordsCount=database.GetTotalRecordsCount(), popularCategoriesList=database.GetPopularCategoriesList(), popularPornStarList=database.GetPopularPornStarList(), isLogedIn=False)

@app.route("/loginUser", methods=["post"])
def loginUser():
    username = database.userDatabase.CreateMD5Hash(request.form["username"])
    password = database.userDatabase.CreateMD5Hash(request.form["password"])
    print("NJOYPORN: Login attempt >>\nUsername: " + request.form["username"] + "\nPassword: "  + request.form["password"])
    if database.userDatabase.CheckCredentials(username, password) == True:
        userObject = database.userDatabase.GetUserByCredentials(username, password)
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
        response = make_response(render_template("home.html", mioList=mioList, pageCounter=pageCounter, maxPageCount=maxPageCount, resultCount=resultCount, keyWords=keyWords, isLogedIn = True))
        response.set_cookie("data", cookieValue)
        return response
    metaInformationObject = database.modules.MetaInformationObject()
    metaInformationObject.videoUrl = "/static/data/__/ahahah_low.mp4"
    metaInformationObject.videoTitle = "You didn't say the magic word"
    metaInformationObject.discription = "To watch the clip you want you need to be loged in"
    return render_template("videoPlayer.html", metaInformationObject=metaInformationObject, isLogedIn = False)
        
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
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:
        if len(mioList) < 1:
            return render_template("home.html", resultCount=0, totalRecordsCount=database.GetTotalRecordsCount(), popularCategoriesList=database.GetPopularCategoriesList(), popularPornStarList=database.GetPopularPornStarList(), isLogedIn = True)
        return render_template("home.html", mioList=mioList, totalRecordsCount=database.GetTotalRecordsCount(), pageCounter=pageCounter, maxPageCount=maxPageCount, resultCount=resultCount, keyWords=keyWords, isLogedIn = True)
    if len(mioList) < 1:
        return render_template("home.html", resultCount=0, totalRecordsCount=database.GetTotalRecordsCount(), popularCategoriesList=database.GetPopularCategoriesList(), popularPornStarList=database.GetPopularPornStarList())
    return render_template("home.html", mioList=mioList, totalRecordsCount=database.GetTotalRecordsCount(), pageCounter=pageCounter, maxPageCount=maxPageCount, resultCount=resultCount, keyWords=keyWords)

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
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:        
        return render_template("home.html", mioList=mioList, pageCounter=pageCounter, maxPageCount=maxPageCount, resultCount=resultCount, keyWords=keyWords, isLogedIn = True)
    return render_template("home.html", mioList=mioList, pageCounter=pageCounter, maxPageCount=maxPageCount, resultCount=resultCount, keyWords=keyWords, isLogedIn = False)    

@app.route("/playVideo", methods=["post"])
def videoPlayer():
    url = request.form["videoUrl"]
    if url == "":
        return "error"
    if "special" in url:
        metaInformationObject = database.GetMetaInfromationObjectByVideoUrl(url)
        if metaInformationObject.origin == "free":
            cookieValue = request.cookies.get("data")
            username, password = GetCookieData(cookieValue)
            if database.userDatabase.CheckCredentials(username, password) == True:
                userObject = database.userDatabase.GetUserByCredentials(username, password)
                videoOwnerNickName = database.userDatabase.LoadUserObjectById(metaInformationObject.owner)
                analytics.AnalyticalObjectExits(url)
                return render_template("videoPlayer.html", metaInformationObject=metaInformationObject, isLogedIn = True, userId=userObject.id, videoOwnerNickName=videoOwnerNickName)
            return render_template("videoPlayer.html", metaInformationObject=metaInformationObject, isLogedIn = False)
        cookieValue = request.cookies.get("data")
        username, password = GetCookieData(cookieValue)
        if database.userDatabase.CheckCredentials(username, password) == True:
            if metaInformationObject == "invalid":
                return render_template("error.html", error=database.modules.ErrorMessage("Video not found", "Can't locate the video."))
            userObject = database.userDatabase.GetUserByCredentials(username, password)
            videoOwnerNickName = database.userDatabase.LoadUserObjectById(metaInformationObject.owner).nickName
            return render_template("videoPlayer.html", metaInformationObject=metaInformationObject, isLogedIn = True, userId = userObject.id, videoOwnerNickName=videoOwnerNickName)
        metaInformationObject = database.CreateDummyObject()
        return render_template("videoPlayer.html", metaInformationObject=metaInformationObject, isLogedIn = False, videoOwnerNickName="schroedinger")
    metaInformationObject = database.GetMetaInfromationObjectByVideoUrl(url)
    analytics.AnalyticalObjectExits(url)
    if metaInformationObject == "invalid":
        metaInformationObject = database.CreateDummyObject()
        return render_template("videoPlayer.html", metaInformationObject=metaInformationObject, isLogedIn = False)
    return render_template("videoPlayer.html", metaInformationObject=metaInformationObject, isLogedIn = False)        

@app.route("/login")
def login():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:
        return render_template("login.html", isLogedIn=True)
    return render_template("login.html", isLogedIn=False)

@app.route("/logout")
def logout():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:
        response = make_response(render_template("login.html"))
        response.set_cookie("data", '', expires=0)
        return response
    return "logoud didnt work"

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
    return "<script>alert(\"Thanks for your vote!\");location.href = \"/\";</script>" 

@app.route("/downVote", methods=["post"])
def downVote():
    id = request.form["upVote"]
    database.UpdateMetaInformationObject(id, "downVote", 1)
    return "<script>alert(\"Thanks for your vote!\");location.href = \"/\";</script>" 

@app.route("/impressum")
def impressum():
    return render_template("impressum.html")    

@app.route("/sendComment", methods=["post"])
def sendComment():
    videoId = request.form["videoId"]
    commentContent = request.form["commentContent"]
    writerName = request.form["witerName"]
    database.AddComment(videoId, commentContent, writerName)
    metaInformationObject = database.GetMetaInformationObjectById(videoId)
    return render_template("videoPlayer.html", metaInformationObject=metaInformationObject)

@app.route("/register")
def register():
    return render_template("registerUser.html")

@app.route("/registerUser", methods=["post"])
def registerUser():
    username = database.userDatabase.CreateMD5Hash(request.form["username"])
    password = database.userDatabase.CreateMD5Hash(request.form["password"])
    nickname = request.form["nickName"]
    email = request.form["email"]
    #return "currently deactivated"
    return database.userDatabase.From_GUI_AddRandomUser(username, password, email, nickname)
    

@app.route("/forgotPassword")
def forgottPassword():
    return render_template("forgotPassword.html")

@app.route("/resettPassword", methods=["post"])
def resettPassword():
    username = database.userDatabase.CreateMD5Hash(request.form["username"])
    nickName = request.form["nickName"]
    email = request.form["email"]
    return database.userDatabase.From_GUI_CheckForPossiblePasswordResett(username, nickName, email)

@app.route("/newPassword", methods=["post"])
def newPassword():
    id = request.form["id"]
    username = request.form["username"]
    password = database.userDatabase.CreateMD5Hash(request.form["password"])
    return database.userDatabase.From_GUI_ResetPassword(id, username, password)
    
@app.route("/webgui")
def webgui():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:
        if database.userDatabase.From_GUI_HasPrivileges(username, password) > 100: 
            userObject = database.userDatabase.GetUserByCredentials(username, password)
            return render_template("webgui.html", mioList = database.GetMetaInformationObjectList(), userList = database.userDatabase.GetUserList(), userObject=userObject)
    return render_template("error.html", error=database.modules.ErrorMessage("Permission denied", "You dont have the rights to access this site."))

@app.route("/userAccount")
def userAccount():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password):
        if database.userDatabase.From_GUI_HasPrivileges(username, password) > 10:
            userObject = database.userDatabase.GetUserByCredentials(username, password)
            hasUserPage = False
            if database.userDatabase.GetUserPageDataByUserId(userObject.id) != "invalid":
                hasUserPage = True
            counter = str(len(userObject.unreadConversationsList))
            print("DEBUG: counter >> " + counter)
            return render_template("userAccount.html", userObject = userObject, hasUserPage = hasUserPage, unreadMessagesCount=counter)
    return render_template("error.html", error=database.modules.ErrorMessage("Permission denied", "You are not allowed to be here"))    

@app.route("/card")
def card():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password):
        userObject = database.userDatabase.GetUserByCredentials(username, password)
        cardList = database.From_GUI_GetObjectsInUserCardList(userObject.cardList)
        if len(cardList) < 1:
            mio = database.modules.MetaInformationObject()
            mio.videoTitle = "Your card is empty"
            mio.thumbnailPath = "/static/data/__/thumbnails/ahahah_low.png"
            cardList.append(mio)
        return render_template("checkOut.html", cardList = cardList, metaInformationObject=cardList[0])
    return render_template("error.html", error=database.modules.ErrorMessage("You have to be loged in", "To see your card you have to be loged in"))    
   
@app.route("/createUserPage")
def createUserPage():
    return render_template("createUserPage.html")

@app.route("/setupUserPage", methods=["post"])
def setupUserPage():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:
        nickName = request.form["nickName"]
        userDiscription = request.form["userDiscription"]
        images = request.files.getlist("images")
        catchPharse = request.form["catchPhrase"]
        categories = request.form["categories"]
        os.mkdir(os.getcwd()+"/static/userPages/"+username)
        os.mkdir(os.getcwd()+"/static/userPages/"+username+"/images/")
        for image in images:
            fileName = database.GetFileName(str(image))
            image.save(os.getcwd()+"/static/userPages/"+username+"/images/"+fileName)
        userPageObject = database.userDatabase.SetupUserPage(nickName, username, userDiscription, catchPharse, categories)
        userPageObject = database.userDatabase.AddMetaInformationObjectsToUserPageObjectVideoList(userPageObject)
        return render_template("userPage.html", userPageObject=userPageObject)
    return "You need to be loged in to create a user page"

@app.route("/editUserPage")
def editUserPage():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:
        userPageObject = database.userDatabase.GetUserPageDataByUserId(database.userDatabase.GetUserByCredentials(username, password).id)
        if userPageObject == "invalid":
            return "file not found"
        userPageObject = database.userDatabase.AddMetaInformationObjectsToUserPageObjectVideoList(userPageObject)
        return render_template("editUserPage.html", userPageObject=userPageObject)
    
@app.route("/updateUserPageText", methods=["post"])
def updateUserPageText():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:
        userId = request.form["id"]
        nickName = request.form["nickName"]
        userDiscription = request.form["userDiscription"]
        catchPharse = request.form["catchPhrase"]
        categories = request.form["categories"] 
        print(categories)          
        userPageObject = database.userDatabase.From_GUI_EditUserPage(userId, nickName, username, userDiscription, catchPharse, categories)
        return render_template("userPage.html", userPageObject=userPageObject)

@app.route("/updateUserPictures", methods=["post"])
def updateUserPictures():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:
        id = request.form["id"]
        images = request.files.getlist("images")
        for image in images:
            fileName = database.GetFileName(str(image))
            image.save(os.getcwd()+"/static/userPages/"+username+"/images/"+fileName)
        userPageObject = database.userDatabase.UpdateUserPictures(id, username)
        userPageObject = database.userDatabase.AddMetaInformationObjectsToUserPageObjectVideoList(userPageObject)
        return render_template("userPage.html", userPageObject=userPageObject)
    return "You need to be loged in to create a user page"
        
@app.route("/deleteUserPagePicture", methods=["post"])
def deleteUserPagePicture():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:
        picturePath = request.form["picturePath"]
        userId = request.form["id"]
        userPageObject = database.userDatabase.RemoveUserPagePicture(picturePath, userId)
        return render_template("editUserPage.html", userPageObject=userPageObject)
                
@app.route("/userPage", methods=["post"])
def userPage():
    id = request.form["id"]
    userPageObject = database.userDatabase.GetUserPageDataByUserId(id)
    if userPageObject == "invalid":
        return "file not found"
    userPageObject = database.userDatabase.AddMetaInformationObjectsToUserPageObjectVideoList(userPageObject)
    #userPageObject = database.userDatabase.ReformatPageDiscriptionText(userPageObject)
    return render_template("userPage.html", userPageObject=userPageObject)

@app.route("/searchInUserPage", methods=["Post"])
def saearchInUserPage():
    id = request.form["id"]
    searchTerm = request.form["searchTerm"]
    userPageId = request.form["pageId"]
    userPageObject = database.userDatabase.GetUserPageDataByUserId(id)
    if userPageObject == "invalid":
        return "file not found"
    userPageObject = database.userDatabase.AddMetaInformationObjectsToUserPageObjectVideoList(userPageObject)
    userPageObject.videoList = database.userDatabase.SearchInUserVideos(userPageId, searchTerm)
    return render_template("userPage.html", userPageObject=userPageObject)

@app.route("/uploadFile", methods=["post"])
def uploadFile():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:
        if database.userDatabase.From_GUI_HasPrivileges(username, password) > 10:
            command = request.form["command"]
            if command == "forSale" and database.userDatabase.From_GUI_HasPrivileges(username, password) < 20:
                userObj = database.userDatabase.GetUserByCredentials(username, password)
                print("NJOYPORN: Unverivied user with id: " + userObj.id + " || nickName: " + userObj.nickName + " wants to sell a video")
                return "not allowed"
            file = request.files["fileToUpload"]
            videoTitle = request.form["videoTitle"]
            videoTags = request.form["videoTags"]
            discription = request.form["discription"]
            categories = request.form["categories"]
            price = request.form["price"]
            if price == "":
                price = 0
            trailerId = request.form["trailerId"]
            if command == "forSale" and trailerId == "":
                return "<script>alert(\"You need to enter a trailer video id\");location.href = \"/userAccount\";</script>"
            print("Saving File to storage: >>", file)
            fileName = database.GetFileName(str(file))
            file.save(os.getcwd()+ "/" + database.videoStoragePath + fileName)
            return database.From_GUI_AddVideo(fileName, videoTitle, videoTags, discription, categories, username, trailerId, command, price)
    return render_template("error.html", error = database.modules.ErrorMessage("Permission denied", "You are not allowed to be here"))          

@app.route("/editFile", methods=["POST"])
def editFile():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:
        #id = request.form["id"] I use the filename for both
        if database.userDatabase.From_GUI_HasPrivileges(username, password) > 10:  
            fileName = request.form["fileName"]
            videoTitle = request.form["videoTitle"]
            videoTags = request.form["videoTags"]
            discription = request.form["discription"]
            categories = request.form["categories"]
            price = request.form["price"]
            return database.From_GUI_EditVideo(fileName, videoTitle, videoTags, discription, categories, price)
    return render_template("error.html", error = database.modules.ErrorMessage("Permission denied", "You are not allowed to be here"))
        
@app.route("/removeFile", methods=["POST"])
def removeFile():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:
        if database.userDatabase.From_GUI_HasPrivileges(username, password) > 100: 
            id = request.form["id"]
            _password = database.userDatabase.CreateMD5Hash(request.form["password"])
            if _password == password:
                return database.From_GUI_RemoveVideo(id)
            return render_template("error.html", error = database.modules.ErrorMessage("Wrong password","You entered a wrong password"))
        if database.userDatabase.From_GUI_HasPrivileges(username, password) > 10: 
            videoId = request.form["id"]
            userId = request.form["userId"]
            _password = database.userDatabase.CreateMD5Hash(request.form["password"])
            if _password == password:
                return database.From_GUI_RemoveUserVideo(videoId, userId)
    return render_template("error.html", error = database.modules.ErrorMessage("Permission denied", "You are not allowed to be here"))
  

@app.route("/addUser", methods=["post"])
def addUser():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:
        if database.userDatabase.From_GUI_HasPrivileges(username, password) > 100:
            username = database.userDatabase.CreateMD5Hash(request.form["username"])
            nickName = request.form["nickName"]
            password = database.userDatabase.CreateMD5Hash(request.form["password"])
            email = request.form["email"]
            return database.userDatabase.From_GUI_AddUser(username, password, email, nickName)
    return render_template("error.html", error = database.modules.ErrorMessage("Permission denied", "You are not allowed to be here"))

@app.route("/editUser", methods=["post"])
def editUser():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:
        if database.userDatabase.From_GUI_HasPrivileges(username, password) > 100:
            id = request.form["id"]
            username = request.form["username"]
            if username != "":
                username = database.userDatabase.CreateMD5Hash(username)
            nickName = request.form["nickName"]
            newPassword = request.form["newPassword"]
            if username != "":    
                newPassword = database.userDatabase.CreateMD5Hash(newPassword)
            email = request.form["email"]
            role = request.form["role"]
            currentPassword = database.userDatabase.CreateMD5Hash(request.form["currentPassword"])
            return database.userDatabase.From_GUI_EditUser(id, username, password, email, nickName, currentPassword, role)
    return render_template("error.html", error = database.modules.ErrorMessage("Permission denied", "You are not allowed to be here"))

@app.route("/editAccount", methods=["post"])
def editAccount():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:
        if database.userDatabase.From_GUI_HasPrivileges(username, password) > 10:
            userId = request.form["id"]
            username = request.form["username"]
            if username != "":
                username = database.userDatabase.CreateMD5Hash(username)
            nickName = request.form["nickName"]
            newPassword = request.form["newPassword"]
            if username != "":    
                newPassword = database.userDatabase.CreateMD5Hash(newPassword)
            email = request.form["email"]    
            currentPassword = database.userDatabase.CreateMD5Hash(request.form["currentPassword"])
            return database.userDatabase.From_GUI_EditAccount(userId, username, newPassword, email, nickName, currentPassword)
        
@app.route("/removeUser", methods=["post"])
def removeUser():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:
        if database.userDatabase.From_GUI_HasPrivileges(username, password) > 100:
            id = request.form["id"]
            password = database.userDatabase.CreateMD5Hash(request.form["password"])
            return database.userDatabase.From_GUI_RemoveUser(id, password)
    return render_template("error.html", error = database.modules.ErrorMessage("Permission denied", "You are not allowed to be here"))

@app.route("/deleteAccount", methods=["post"])
def deleteAccount():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:
        id = request.form["id"]
        if database.userDatabase.From_GUI_HasPrivileges(username, password) > 10:
            password = database.userDatabase.CreateMD5Hash(request.form["password"])
            return database.userDatabase.From_GUI_RemoveUser(id, password)
    return render_template("error.html", error = database.modules.ErrorMessage("Permission denied", "You are not allowed to be here"))

@app.route("/removeVideoFromCard", methods=["post"])
def removeVideoFromCard():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password):
        userObject = database.userDatabase.GetUserByCredentials(username, password)
        videoId = request.form["id"]
        database.userDatabase.RemoveVideoFromCard(userObject.id, videoId)
        cardList = database.From_GUI_GetObjectsInUserCardList(userObject.cardList)
        if len(cardList) < 1:
            mio = database.modules.MetaInformationObject()
            mio.videoTitle = "Your card is empty"
            mio.thumbnailPath = "/static/data/__/ahahah_low.png"
            cardList.append(mio)
        return render_template("checkOut.html", cardList = cardList, metaInformationObject=cardList[0])
    return render_template("error.html", error=database.modules.ErrorMessage("Video not removed from card", "What did you do?"))            

@app.route("/api", methods=["Post"])
def API():
    command = request.form["command"]
    data = request.form["data"]
    key = request.form["key"]
    if key != "3f2c7eb473ca5ad83f94bc1346b6cba9":
        return "Not allowed"
    if command == "paymentDone":
        result = re.search("(.*)\?\?(.*)", data)
        userId = result.group(1)
        videoId = result.group(2)
        database.userDatabase.AddVideoToPurchasedList(userId, videoId)
    return "done"

@app.route("/checkOutCard", methods=["post"])
def checkOutCard():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password):
        userObject = database.userDatabase.GetUserByCredentials(username, password)
        videoId = request.form["id"]
        cardList = database.From_GUI_GetObjectsInUserCardList(userObject.cardList)
        metaInformationObject = database.modules.MetaInformationObject()
        for mio in cardList:
            if mio.id == videoId:
                metaInformationObject = mio
        return render_template("checkOut.html", cardList = cardList, metaInformationObject=metaInformationObject)
    return ""

@app.route("/addVideoToCard", methods=["post"])
def addToCard():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password):
        videoId = request.form["id"]
        database.userDatabase.AddItemToCard(videoId, username, password)
        userObject = database.userDatabase.GetUserByCredentials(username, password)
        cardList = database.From_GUI_GetObjectsInUserCardList(userObject.cardList)
        if len(cardList) < 1:
            mio = database.modules.MetaInformationObject()
            mio.videoTitle = "Your card is empty"
            mio.thumbnailPath = "/static/data/__/ahahah_low.png"
            cardList.append(mio)
        return render_template("checkOut.html", cardList = cardList, metaInformationObject=cardList[0])
    return render_template("error.html", error=database.modules.ErrorMessage("Video not added to card", "You have to be loged in to add an item to your card"))    

@app.route("/buyVideo", methods=["post"])
def buyVideo():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password):
        videoId = request.form["id"]
        userId = database.userDatabase.GetUserByCredentials(username, password).id
        file = open(os.getcwd()+"/static/data/__/PurchaseRequests", "a")
        line = "User-Id: " + userId + " Video-Id: " + videoId
        file.write(line+"\n")
        file.close()
        return redirect(api.BtcPayment(userId, videoId)['url'])
        return "<script>alert(\"Payment in process...\");location.href = \"/userAccount\";</script>"

@app.route("/addVideoToFavoriteList", methods=["post"])
def addVideoToFavoriteList():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password):    
        videoId = request.form["id"]
        userId = database.userDatabase.GetUserByCredentials(username, password).id
        database.userDatabase.AddVideoToUserFavoriteList(videoId, userId)
        return "<script>alert(\"Video added to your favorites list.\");location.href = \"/\";</script>"  
    return render_template("error.html", error = database.modules.ErrorMessage("You need to be loged in", "Please login or register an account to add a video to favorites"))

@app.route("/removeVideoFromFavoriteList", methods=["post"])
def removeVideoFromFavoriteList():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password):
        userObject = database.userDatabase.GetUserByCredentials(username, password)     
        videoId = request.form["id"]
        database.userDatabase.RemoveFavoriteFromList(userObject.id, videoId)
        return "<script>alert(\"Video removed from your favorites list.\");location.href = \"/\";</script>"  
    return render_template("error.html", error = database.modules.ErrorMessage("You need to be loged in", "Please login or register an account to add a video to favorites"))

@app.route("/sendMessage", methods=["post"])
def sendMessage():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password):
        userObject = database.userDatabase.GetUserByCredentials(username, password)
        receiverId = request.form["id"]
        messageText = request.form["messageText"]
        senderNickName = database.userDatabase.GetUserById(userObject.id).nickName
        communication.SendMessage(userObject.id, receiverId, userObject.username, "titleText", messageText, senderNickName)
        conversationList = communication.LoadUsersConversations(username)
        receiverObject = database.userDatabase.GetUserById(receiverId)
        openConversation = communication.LoadConversationIfExisiting(username, receiverObject.username)
    return render_template("messaging.html", openConversation=openConversation, senderId=userObject.id, receiverId=receiverId, receiverNickName= receiverObject.nickName, conversationList=conversationList)
    
@app.route("/messaging", methods=["post"])
def messaging():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    receiverId = request.form["id"]
    if database.userDatabase.CheckCredentials(username, password):
        userObject = database.userDatabase.GetUserByCredentials(username, password)
        conversationList = communication.LoadUsersConversations(username)
        openConversation = communication.LoadConversationIfExisiting(username, database.userDatabase.GetUserById(receiverId).username)
        if openConversation != None and openConversation.id in userObject.unreadConversationsList:
            communication.MarkConversationAsRead(openConversation.id, userObject.id)
    return render_template("messaging.html", openConversation=openConversation, senderId=userObject.id, receiverId=receiverId, conversationList=conversationList)

@app.route("/messages")
def messages():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:
        userObject = database.userDatabase.GetUserByCredentials(username, password)
        conversationList = communication.LoadUsersConversations(username)
        if len(conversationList) > 0:
            openConversation = conversationList[len(conversationList)-1]
        if len(conversationList) < 1:
            #openConversation = communication.CreateDummyConversation()
            openConversation = communication.CreateSupportConversation(userObject.id)
            conversationList.append(openConversation)
        return render_template("messaging.html", openConversation=openConversation, receiverId=openConversation.participentId, senderId=userObject.id, conversationList=conversationList) 
    
@app.route("/sendOfferMessage", methods=["post"])
def sendOffer():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:
        #sellerId = request.form["sellerId"]
        userObject = database.userDatabase.GetUserByCredentials(username,password)
        sellerId = userObject.id
        buyerId = request.form["buyerId"]
        #offerTitle = request.form["offerTitle"]
        offerTitle = "offerMessage"
        offerText = request.form["offerText"]
        offerPrice = request.form["offerPrice"]
        if offerTitle == "":
            offerTitle = "offerMessage"
        communication.CreateOffer(sellerId, buyerId, offerTitle, offerText, offerPrice)
        conversationList = communication.LoadUsersConversations(username)
        if len(conversationList) > 0:
            openConversation = conversationList[len(conversationList)-1]
        if len(conversationList) < 1:
            openConversation = communication.CreateDummyConversation()
            conversationList.append(openConversation)
    return render_template("messaging.html", openConversation=openConversation, receiverId=openConversation.participentId, senderId=userObject.id, conversationList=conversationList) 

@app.route("/sendVideoMessage" , methods=["post"])
def sendVideoMessage():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:    
        videoId = request.form["videoId"]
        receiverId = request.form["id"]
        database.userDatabase.AddVideoToPurchasedList(receiverId, videoId)
        return "<script>alert(\"Video sendet successfully.\");location.href = \"/messages\";</script>"

@app.route("/payOffer", methods=["post"])
def payOffer():
    #stuff i need to make an invoice
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password):
        offerId = request.form["offerId"]
        sellerId = request.form["sellerId"]
        userId = database.userDatabase.GetUserByCredentials(username, password).id
        return redirect(api.CustomInvoice(userId, sellerId, offerId)['url'])


@app.route("/followUser", methods=["post"])
def followUser():
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:      
        userToFollowId = request.form["id"]
        newFollowerId = database.userDatabase.GetUserByCredentials(username, password).id
        database.userDatabase.From_GUI_FollowUser(userToFollowId, newFollowerId)
        print("DEBUG: userToFollowID >> ",userToFollowId)
        print("DEBUG: newFollowerId >> ",newFollowerId)        
        return "<script>alert(\"Video sendet successfully.\");location.href = \""+userToFollowId+"\";</script>"
    return render_template("error.html", error=database.modules.ErrorMessage("Something went wrong", "Upsi, your following didn't work out :/"))

@app.route("/<path:userId>")
def directPage(userId):
    userPageObject = database.userDatabase.GetUserPageDataByUserId(userId)
    if userPageObject == "invalid":
        return "file not found"
    userPageObject = database.userDatabase.AddMetaInformationObjectsToUserPageObjectVideoList(userPageObject)
    return render_template("userPage.html", userPageObject=userPageObject)
    
@app.route("/protected/<path:fileId>")
def protected(fileId):
    cookieValue = request.cookies.get("data")
    username, password = GetCookieData(cookieValue)
    if database.userDatabase.CheckCredentials(username, password) == True:
        userObject = database.userDatabase.GetUserByCredentials(username, password)
        if database.userDatabase.UserHasPurchasedVideo(userObject.id, fileId):
            print(fileId)
            fileName = "videos/" + database.GetMetaInformationObjectById(fileId).fileName
            print(fileName)
            return send_from_directory(os.path.join(app.instance_path, ""),fileName)
    return "<h1>Please log in to access the file</h1>"

if __name__ == "__main__":
    database.InitDatabase()
    app.run(debug=True, host="0.0.0.0", port=7676)
