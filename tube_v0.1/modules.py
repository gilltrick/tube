class MetaInformationObject:
    def __init__(self):
        self.videoUrl = ""
        self.videoTitle = ""
        self.videoDuration = ""
        self.rating = 0
        self.tagList = []
        self.thumbnailPath = ""
        self.discription = ""
        self.id = ""
        self.data = ""
        
class DataBaseFile:
    def __init__(self):
        self.MetaInformationObjectList = []
        
################################## H E L P E R ####################################
#        
# class newModule:
#     def __init__(self):
#         self.videoUrl = ""
#         self.videoTitle = ""
#         self.videoDuration = ""
#         self.rating = 0
#         self.tagList = []
#         self.thumbnailPath = ""
#         self.discription = ""
#         self.id = ""
#         self.data = ""
        
# class prevModule:
#     def __init__(self):
#         self.videoUrl = ""
#         self.videoTitle = ""
#         self.videoDuration = ""
#         self.rating = 0
#         self.tagList = []
#         self.thumbnailPath = ""
#         self.discription = ""

class User:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.email = ""
        self.favouriteList = ""
        self.historyList = ""
        self.loginStampList = []
        self.ipLoginList = []
        
        
class AnaltycisObject:
    def __init__(self):
        self.metaInformationObject = MetaInformationObject()
        self.watchCounter = 0
        self.upVotes = 0
        self.downVotes = 0