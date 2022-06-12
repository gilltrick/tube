import os, hashlib
from pathlib import Path


rootPath = os.getcwd()
rndList = []

def Run():
    command = input("Enter command: [-install]")
    if command == "-install":
        Install()

def Install():
    #Create the folder structure
    print("Createing folders...")
    os.mkdir(rootPath+"/templates")
    os.mkdir(rootPath+"/api")
    os.mkdir(rootPath+"/static")
    os.mkdir(rootPath+"/api/_data")
    os.mkdir(rootPath+"/api/_data/__logs")
    os.mkdir(rootPath+"/static/data")
    os.mkdir(rootPath+"/static/images")
    os.mkdir(rootPath+"/static/js")
    os.mkdir(rootPath+"/static/storage")
    os.mkdir(rootPath+"/static/styles")
    os.mkdir(rootPath+"/static/userDatabase")
    os.mkdir(rootPath+"/static/data/__")
    os.mkdir(rootPath+"/static/data/__/thumbnails/")
    os.mkdir(rootPath+"/static/data/__/thumbnails/ahahah_low/")
    os.mkdir(rootPath+"/static/data/databases")
    os.mkdir(rootPath+"/static/data/default")
    os.mkdir(rootPath+"/static/data/dictionarys")
    os.mkdir(rootPath+"/static/data/analytics")
    os.mkdir(rootPath+"/static/images/icons")
    os.mkdir(rootPath+"/static/storage/specials")
    os.mkdir(rootPath+"/static/storage/specials/thumbnails")
    os.mkdir(rootPath+"/static/storage/specials/userPages")
    print("Folders created")

    #Move files to destination folder
    print("Moving files to folders...")
    Path(rootPath+"/_data/index.html").rename(rootPath+"/templates/index.html")
    Path(rootPath+"/_data/home.html").rename(rootPath+"/templates/home.html")
    Path(rootPath+"/_data/login.html").rename(rootPath+"/templates/login.html")
    Path(rootPath+"/_data/impressum.html").rename(rootPath+"/templates/impressum.html")
    Path(rootPath+"/_data/videoPlayer.html").rename(rootPath+"/templates/videoPlayer.html")
    Path(rootPath+"/_data/webgui.html").rename(rootPath+"/templates/webgui.html")
    Path(rootPath+"/_data/error.html").rename(rootPath+"/templates/error.html")
    Path(rootPath+"/_data/registerUser.html").rename(rootPath+"/templates/registerUser.html")
    Path(rootPath+"/_data/resettPassword.html").rename(rootPath+"/templates/resettPassword.html")
    Path(rootPath+"/_data/forgotPassword.html").rename(rootPath+"/templates/forgotPassword.html") 
    Path(rootPath+"/_data/userAccount.html").rename(rootPath+"/templates/userAccount.html")    
    Path(rootPath+"/_data/messaging.html").rename(rootPath+"/templates/messaging.html") 
    Path(rootPath+"/_data/checkOut.html").rename(rootPath+"/templates/checkOut.html") 
    Path(rootPath+"/_data/createUserPage.html").rename(rootPath+"/templates/createUserPage.html")     
    Path(rootPath+"/_data/editUserPage.html").rename(rootPath+"/templates/editUserPage.html") 
    Path(rootPath+"/_data/userpage.html").rename(rootPath+"/templates/userpage.html") 
    Path(rootPath+"/_data/checkOutStyle.css").rename(rootPath+"/static/styles/checkOutStyle.css")  
    Path(rootPath+"/_data/messagingStyle.css").rename(rootPath+"/static/styles/messagingStyle.css")  
    Path(rootPath+"/_data/createUserPageStyle.css").rename(rootPath+"/static/styles/createUserPageStyle.css")  
    Path(rootPath+"/_data/editUserPageStyle.css").rename(rootPath+"/static/styles/editUserPageStyle.css")
    Path(rootPath+"/_data/userPageStyle.css").rename(rootPath+"/static/stylesuserPageStyle.css")
    Path(rootPath+"/_data/loginStyle.css").rename(rootPath+"/static/styles/loginStyle.css")
    Path(rootPath+"/_data/indexStyle.css").rename(rootPath+"/static/styles/indexStyle.css")
    Path(rootPath+"/_data/homeStyle.css").rename(rootPath+"/static/styles/homeStyle.css")
    Path(rootPath+"/_data/VideoPlayerStyle.css").rename(rootPath+"/static/styles/VideoPlayerStyle.css")
    Path(rootPath+"/_data/webguiStyle.css").rename(rootPath+"/static/styles/webguiStyle.css")
    Path(rootPath+"/_data/errorStyle.css").rename(rootPath+"/static/styles/errorStyle.css")
    Path(rootPath+"/_data/resettPasswordStyle.css").rename(rootPath+"/static/styles/resettPasswordStyle.css")
    Path(rootPath+"/_data/forgotPasswordStyle.css").rename(rootPath+"/static/styles/forgotPasswordStyle.css")
    Path(rootPath+"/_data/registerUserStyle.css").rename(rootPath+"/static/styles/registerUserStyle.css")        
    Path(rootPath+"/_data/Rhiledia.ttf").rename(rootPath+"/static/styles/Rhiledia.ttf")
    Path(rootPath+"/_data/Ayrton Pight.ttf").rename(rootPath+"/static/styles/Ayrton Pight.ttf")
    Path(rootPath+"/_data/yuruy.otf").rename(rootPath+"/static/styles/yuruy.oft")
    Path(rootPath+"/_data/videoPlayer.js").rename(rootPath+"/static/js/videoPlayer.js")
    Path(rootPath+"/_data/webgui.js").rename(rootPath+"/static/js/webgui.js")
    Path(rootPath+"/_data/userwebgui.js").rename(rootPath+"/static/js/userwebgui.js")
    Path(rootPath+"/_data/userPage.js").rename(rootPath+"/static/js/userPage.js")
    Path(rootPath+"/_data/messaging.js").rename(rootPath+"/static/js/messaging.js")
    Path(rootPath+"/_data/backward.svg").rename(rootPath+"/static/images/icons/backward.svg")
    Path(rootPath+"/_data/expand.svg").rename(rootPath+"/static/images/icons/expand.svg")
    Path(rootPath+"/_data/expandd.svg").rename(rootPath+"/static/images/icons/expandd.svg")
    Path(rootPath+"/_data/forward.svg").rename(rootPath+"/static/images/icons/forward.svg")
    Path(rootPath+"/_data/LeftArrow_black.png").rename(rootPath+"/static/images/icons/LeftArrowpng_black.png")
    Path(rootPath+"/_data/pause.svg").rename(rootPath+"/static/images/icons/pause.svg")
    Path(rootPath+"/_data/play.svg").rename(rootPath+"/static/images/icons/play.svg")
    Path(rootPath+"/_data/reduce.svg").rename(rootPath+"/static/images/icons/reduce.svg")
    Path(rootPath+"/_data/RightArrow_black.png").rename(rootPath+"/static/images/icons/RightArrow_black.png")
    Path(rootPath+"/_data/silence.svg").rename(rootPath+"/static/images/icons/silence.svg")
    Path(rootPath+"/_data/searchIcon.png").rename(rootPath+"/static/images/icons/searchIcon.png")
    Path(rootPath+"/_data/thumbs-up_small.png").rename(rootPath+"/static/images/icons/thumbs-up_small.png")
    Path(rootPath+"/_data/thumbs-down_small.png").rename(rootPath+"/static/images/icons/thumbs-down_small.png")
    Path(rootPath+"/_data/thumbs-up.png").rename(rootPath+"/static/images/icons/thumbs-up.png")
    Path(rootPath+"/_data/thumbs-down.png").rename(rootPath+"/static/images/icons/thumbs-down.png")
    Path(rootPath+"/_data/volume.svg").rename(rootPath+"/static/images/icons/volume.svg")
    Path(rootPath+"/_data/background.png").rename(rootPath+"/static/images/background.png")
    Path(rootPath+"/_data/Logo_01.png").rename(rootPath+"/static/images/Logo_01.png")
    Path(rootPath+"/_data/messageIcon.png").rename(rootPath+"/static/images/icons/messageIcon.png")
    Path(rootPath+"/_data/reload.png").rename(rootPath+"/static/images/icons/reload.png")
    Path(rootPath+"/_data/heart.png").rename(rootPath+"/static/images/icons/heart.png")
    Path(rootPath+"/_data/analytics.py").rename(rootPath+"/analytics.py")
    Path(rootPath+"/_data/database.py").rename(rootPath+"/database.py")
    Path(rootPath+"/_data/fapsterScraper.py").rename(rootPath+"/fapsterScraper.py")
    Path(rootPath+"/_data/pornhubScraper.py").rename(rootPath+"/pornhubScraper.py")
    Path(rootPath+"/_data/GrabPornstars.py").rename(rootPath+"/GrabPornStars.py")
    Path(rootPath+"/_data/hotexporntoonsScraper.py").rename(rootPath+"/hotexporntoonsScraper.py")
    Path(rootPath+"/_data/modules.py").rename(rootPath+"/modules.py")
    Path(rootPath+"/_data/njoyporn.py").rename(rootPath+"/njoyporn.py")
    Path(rootPath+"/_data/userDatabase.py").rename(rootPath+"/userDatabase.py")
    Path(rootPath+"/_data/api.py").rename(rootPath+"/api.py")
    Path(rootPath+"/_data/communication.py").rename(rootPath+"/communication.py")
    Path(rootPath+"/_data/ahahah_low.mp4").rename(rootPath+"/static/data/__/ahahah_low.mp4")
    Path(rootPath+"/_data/ahahah_low.png").rename(rootPath+"/static/data/__/thumbnails/ahahah_low/0.png")
    Path(rootPath+"/_data/categorieDictionary").rename(rootPath+"/static/data/dictionarys/categorieDictionary")
    Path(rootPath+"/_data/pornStarNameDictionary").rename(rootPath+"/static/data/dictionarys/pornStarNameDictionary")
    Path(rootPath+"/_data/userPageCategorieDictionary").rename(rootPath+"/static/data/dictionarys/userPageCategorieDictionary")
    print("Files moved to folders")

    #Create files
    print("creating database files...")
    file = open(rootPath+"/static/data/analytics/analytics.db", "wb")
    file.close()
    file = open(rootPath+"/static/data/analytics/categorieAnalytics.db", "wb")
    file.close()
    file = open(rootPath+"/static/data/analytics/keyWordList.db", "wb")
    file.close()
    file = open(rootPath+"/static/data/analytics/pornStarAnalytics.db", "wb")
    file.close()
    file = open(rootPath+"/static/data/databases/fapster.db", "wb")
    file.close()
    file = open(rootPath+"/static/data/databases/pornhubdb.db", "wb")
    file.close()
    file = open(rootPath+"/static/data/databases/hotexporntoons.db", "wb")
    file.close()
    file = open(rootPath+"/static/userDatabase/userDataBase.db", "wb")
    file.close()
    file = open(rootPath+"/static/data/databases/videoDatabase.db", "wb")
    file.close()
    file = open(rootPath+"/api/_data/__logs/log", "w")
    file.close()
    file = open(rootPath+"/static/data/__/PurchaseRequests", "w")
    file.close()
    print("database files created")

    print("Installing requirements: Flask, cv2, fake_headers, bitpay...")
    os.system('pip install -r ./_data/requirements.txt')
    print("requirements: Flask, cv2, fake_headers installed")
    Path(rootPath+"/_data/requirements.txt").rename(rootPath+"/requirements.txt")
    fileList = os.listdir(rootPath+"/_data/")
    command = input("Create a admin account for the web gui? [yes / no]")
    if command == "yes":
        CreateUserAccount()
    if len(fileList) < 1:
        print("Installation complete\n Enter python njoyporn.py to start the server")     
        
def CreateUserAccount():
    username = hashlib.md5(input("Enter username: ").encode()).hexdigest()
    password = hashlib.md5(input("Enter password: ").encode()).hexdigest()
    line = "{\"username\":\"" + username + "\";\"password\":\"" + password + "\";\"email\":\"" + username + "@njoyporn.com" + "\";\"id\":\"njoyporn\";\"nickName\":\"njoyporn\";\"role\":\"admin\"}"
    file = open(os.getcwd()+"/static/userDatabase/userDatabase.db", "w")
    file.write(line + "\n")
    file.close()
    print("Admin account created!\nRun njoyporn.py to start server")
        
if __name__ == "__main__":
    Run()