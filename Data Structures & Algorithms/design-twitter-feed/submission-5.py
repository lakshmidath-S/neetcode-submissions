import heapq
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
        heap=[]
        newlist=[x for x in self.following[userId]]
        newlist.append(userId)
        for i in newlist:
            for j,k in self.tweets[i]:
                heapq.heappush(heap,(j,k))
                if len(heap)>10:
                    heapq.heappop(heap)
        m=[]
        while len(heap)>0:
            a=heapq.heappop(heap)
            m.append(a[1])
        return m[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users.append(followerId)
            self.tweets[followerId]=[]
            self.following[followerId]=set()
        self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
