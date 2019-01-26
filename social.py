import praw
import winsound

class submission:
    def __init__(self,score,user,title,rank,karmaRate):
        self.score = score
        self.user = user
        self.title = title
        self.rank = rank
        self.karmaRate = karmaRate

    def getUser(self):
        return self.user
    def getScore(self):
        return self.score
    def getTitle(self):
        return self.title
    def getRank(self):
        return self.rank
    def getKarmaRate(self):
        return self.karmaRate


reddit = praw.Reddit(client_id = '7mjSfNIubxHSoA',
                     client_secret = 'UUi3w7k8a2ITZ1XleALB8waA-0g',
                     username = 'username',
                     password = 'password',
                     user_agent = 'praw')

subreddit = reddit.subreddit('askreddit')
postLimit = 200
topPosts = subreddit.top('all', limit=postLimit)

winsound.Beep(1500,200)

rank = 0
data = []


for post in topPosts:
    if not post.stickied:
        rank = rank + 1
        user = post.author

        #rank by karma
        if user != None and hasattr(user,'link_karma'):
            totalKarma = user.link_karma + user.comment_karma
            karmaRate = post.score/totalKarma
            notPlaced = True
            count = 0
            while karmaRate < data[count].getKarmaRate():
                count = count + 1
            data.insert(count,submission(post.score,user,post.title,rank,karmaRate))
            

for sub in data:
    print(sub.getRank(),":", sub.getKarmaRate(),sub.getScore(),"- ",sub.getTitle())
    winsound.Beep(2500,5)

winsound.Beep(2500,200)

    
