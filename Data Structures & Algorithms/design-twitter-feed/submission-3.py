class Twitter:

    def __init__(self):
        self.users=[]
        self.following={}
        self.tweets={}
        self.tc=1

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users.append(userId)
            self.tweets[userId]=[]
            self.following[userId]=set()
        self.tweets[userId].append((self.tc,tweetId))
        self.tc+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            self.users.append(userId)
            self.tweets[userId]=[]
            self.following[userId]=set()
        ts=[]
        count=0
        newlist=[x for x in self.following[userId]]
        newlist.append(userId)
        for i in newlist:
            for j in self.tweets[i]:
                ts.append(j)
        ts.sort(reverse=True)
        m=[]
        for i,j in ts:
            if count==10:
                break
            m.append(j)
            count+=1
        return m

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users.append(followerId)
            self.tweets[followerId]=[]
            self.following[followerId]=set()
        self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)