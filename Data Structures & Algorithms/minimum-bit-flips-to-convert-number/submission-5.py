class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count=0
        if start!=goal:
            a=bin(start)[2:]
            b=bin(goal)[2:]
            maxlen=max(len(a),len(b))
            a=a.zfill(maxlen)
            b=b.zfill(maxlen)
            for i in range(len(a)):
                if a[i]!=b[i]:
                    count+=1
        return count
