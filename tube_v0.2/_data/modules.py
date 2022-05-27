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
        self.upVotes = 0
        self.downVotes = 0
        self.categoryList = []
        self.origin = ""
        self.owner = ""
        self.createdOn = ""
        self.sponsor = ""
        self.commentObjectList = []
        self.viewCount = 0
        
class DataBaseFile:
    def __init__(self):
        self.MetaInformationObjectList = []

class CommentObject:
    def __init__(self):
        self.text = ""
        self.writerId = ""
        self.writerNickName = ""
        self.createdOn = ""
        self.upVotes = ""
        self.downVotes = ""
        self.id = ""
        self.metaInformatinoObjectId = ""
        self.videoUrl = ""
        self.videoThumbnailUrl = ""
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
#         self.upVotes = 0
#         self.downVotes = 0
#         self.categoryList = []
#         self.origin = ""
#         self.owner = ""      
#         self.createdOn = ""
#         self.sponsor = ""
#         self.commentObjectList = []
#         self.viewCount = 0

class User:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.email = ""
        self.favouriteList = ""
        self.historyList = ""
        self.loginStampList = []
        self.ipLoginList = []
        #self.id = ""
        
class CategoryAnalyticsObject:
    def __init__(self):
        self.id = ""
        self.categorieId = ""
        self.name = ""
        self.counter = 0
        self.lastUpdate = ""
        self.createdOn = "" 
        self.searchTermCharts = CategoryAnalyticsObject.SearchTermChartList()
        
    class SearchTermChartList():
        def __init__(self):
            self.searchTerm = ""
            self.Counter = ""
            self.lastUpdate = ""
            self.createdOn = "" 
            self.id = ""
            
class PornStarAnalyticsObject:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.tagList = ""
        self.videoList = []
        self.bio = ""
        self.data = ""
        self.counter = 0
        self.lastUpdate = ""
        self.createdOn = "" 
        self.searchTermCharts = PornStarAnalyticsObject.SearchTermChartList()
        
    class SearchTermChartList():
        def __init__(self):
            self.searchTerm = ""
            self.Counter = ""
            self.lastUpdate = ""
            self.createdOn = "" 
            self.id = ""
        
class AnaltycisObject:
    def __init__(self):
        self.metaInformationObject = MetaInformationObject()
        self.watchCounter = 0
        self.upVotes = 0
        self.downVotes = 0
        self.lastUpdate = ""
        self.createdOn = "" 
        self.id = ""