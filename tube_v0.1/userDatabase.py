import os, re, datetime, hashlib, database

userPattern = "{\"username\":\"(.*)\";\"password\":\"(.*)\";\"email\":\"(.*)\"}"

#userdata?
userObjectList = []

def Run():
    command = input("Enter command: ")
    if command == "-initdb":
        InitDB()
    if command == "-newUser":
        InitDB()
        username = input("Enter username: ")
        password = input("Enter password: ")
        email = input("Enter email: ")
        CreateUser(username, password, email)
    if command == "-deleteUser":
        InitDB()
        username = input("Enter username: ")
        password = input("Enter password: ")
        if CheckCredentials(username, password) == True:
            global userObjectList
            for user in userObjectList:
                if user.username == username and user.password == password:
                    userObjectList.remove(user)
                    SaveUserDatabase()
    return None

def LoadUserFromDatabase(_username):
    global userObjectList
    for user in userObjectList:
        if user.username == _username:
            return user

def LoadUserDatabase():
    InitDB()

def InitDB():
    if os.path.exists(os.getcwd()+"/static/data/userDatabase.db"):
        file = open(os.getcwd()+"/static/data/userDatabase.db" ,"r")
        lines = file.readlines()
        global userObjectList
        for line in lines:
            userObjectList.append(LineToUserObject(line))
        return
    print("You have to create a userDatabase.db file @: " + os.getcwd()+"/static/data/")
    return

def GetUserNameList():
    return os.listdir(os.getcwd()+"/static/userDatabase/")

def LineToUserObject(_line):
    userObject = database.modules.User()
    result = re.search(userPattern, _line)
    userObject.username = result.group(1)
    userObject.password = result.group(2)
    userObject.email = result.group(3)
    return userObject

def UserObjectToLine(_userObject):
    line = "{\"username\":\"" + _userObject.username + "\";\"password\":\"" + _userObject.password + "\";\"email\":\"" + _userObject.email + "\"}"
    return line

def SaveUserDatabase():
    global userObjectList
    lines = []
    for user in userObjectList:
        lines.append(UserObjectToLine(user))
    userDatabaseFile = open(os.getcwd()+"/static/data/userDatabase.db", "w")
    userDatabaseFile.writelines(lines)
        
def WriteUserToDatabase(_line):
    file = open(os.getcwd()+"/static/data/userDatabase.db", "a")
    file.write(_line)
    print("User written to database")

def CreateUser(_username, _password, _email):
    line = "{\"username\":\"" + _username + "\";\"password\":\"" + _password + "\";\"email\":\"" + _email + "\"}"
    WriteUserToDatabase(line)
    #return LineToUserObject(line)

def CheckCredentials(_username, _password):
    for user in userObjectList:
        if user.username == _username and user.password == _password:
            return True
    return False

if __name__ == "__main__":
    Run()