import os, re, datetime, hashlib, database, modules

from flask import render_template

userPattern = "{\"username\":\"(.*)\";\"password\":\"(.*)\";\"email\":\"(.*)\";\"id\":\"(.*)\";\"nickName\":\"(.*)\";\"role\":\"(.*)\"}"

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
        nickName = "dummyValue"
        role = input("Enter user role: [user, admin]")
        CreateUser(username, password, email, nickName, role)
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
    if os.path.exists(os.getcwd()+"/static/data/databases/userDatabase.db"):
        file = open(os.getcwd()+"/static/data/databases/userDatabase.db" ,"r")
        lines = file.readlines()
        global userObjectList
        for line in lines:
            userObjectList.append(LineToUserObject(line))
        print("USERDATABASE: database loaded")
        return
    print("USERDATABASE: You have to create a userDatabase.db file @: " + os.getcwd()+"/static/data/databases/")
    return

def GetUserNameList():
    return os.listdir(os.getcwd()+"/static/userDatabase/")

def LineToUserObject(_line):
    userObject = database.modules.User()
    result = re.search(userPattern, _line)
    userObject.username = result.group(1)
    userObject.password = result.group(2)
    userObject.email = result.group(3)
    userObject.id = result.group(4)
    userObject.nickName = result.group(5)
    userObject.role = result.group(6)
    return userObject

def UserObjectToLine(_userObject):
    line = "{\"username\":\"" + _userObject.username + "\";\"password\":\"" + _userObject.password + "\";\"email\":\"" + _userObject.email + "\"}"
    return line

def SaveUserDatabase():
    global userObjectList
    lines = []
    for user in userObjectList:
        lines.append(UserObjectToLine(user))
    userDatabaseFile = open(os.getcwd()+"/static/data/databases/userDatabase.db", "w")
    userDatabaseFile.writelines(lines)
        
def WriteUserToDatabase(_line):
    file = open(os.getcwd()+"/static/data/databases/userDatabase.db", "a")
    file.write(_line+"\n")
    print("USERDATABASE: User written to database")
    LoadUserDatabase()
    print("USERDATABASE: User list reloaded")

def CreateUser(_username, _password, _email, _nickName, _role):
    line = "{\"username\":\"" + _username + "\";\"password\":\"" + _password + "\";\"email\":\"" + _email + "\";\"id\":\"" + CreateRandomId() + "\";\"nickName\":\"" + _nickName + "\";\"role\":\"" + _role + "\"}"
    WriteUserToDatabase(line)
    #return LineToUserObject(line)
    return True   

def RemoveUserFromListById(_id, _password):    
    global userObjectList
    userObject = GetUserById(_id)
    if userObject == "invalid":
        return False
    if userObject.password == _password:
        userObjectList.remove(userObject)
        SaveUserDatabase()
        return True
    return False
        
def CreateRandomId():
    return hashlib.md5(str(datetime.datetime.now()).encode()).hexdigest()

def CheckCredentials(_username, _password):
    global userObjectList
    for user in userObjectList:
        if user.username == _username and user.password == _password:
            return True
    return False

def GetUserList():
    return userObjectList

def GetUserById(_id):
    global userObjectList
    for userObject in userObjectList:
        if userObject.id == _id:
            return userObject
    return "invalid"
######################## W E B G U I - I M P L E M E N T A T I O N ########################
#
def From_GUI_AddUser(_username, _password, _email, _nickName):
    CreateUser(_username, _password, _email, _nickName, "user")
    return "<script>alert(\"User successfully addet to the userDatabase.\");location.href = \"webgui\";</script>"

def From_GUI_EditUser(_id, _username, _password, _email, _nickName, _currentPassword):
    userObject = GetUserById(_id)
    if userObject == "invalid":
        return render_template("error.html", error=modules.ErrorMessage("User not edited", "Please check the id or password you entered"))
    if userObject.password != _currentPassword:
        return render_template("error.html", error=modules.ErrorMessage("User not edited", "Please check the id or password you entered"))
    if _username != "":
        userObject.username = _username
    if _password != "":
        userObject.password = _password
    if _email != "":
        userObject.email = _email
    if _nickName != "":
        userObject.nickName = _nickName
    SaveUserDatabase()
    return "<script>alert(\"User successfully edited and saved to the userDatabase.\");location.href = \"webgui\";</script>"

def From_GUI_RemoveUser(_id, _password):
    if RemoveUserFromListById(_id, _password):
        return "<script>alert(\"User successfully removed from to the userDatabase.\");location.href = \"webgui\";</script>"
    #return "<script>alert(\"Wrong id or password.\");location.href = \"webgui\";</script>"
    return render_template("error.html", error=modules.ErrorMessage("User not removed", "Please check the id or password you entered"))         

def From_GUI_HasPrivileges(_username, _password):
    global userObjectList
    for user in userObjectList:
        if user.username == _username and user.password == _password:
            if user.role == "admin":
                return 112
            if user.role == "user":
                return 3
    return 0
    
if __name__ == "__main__":
    Run()