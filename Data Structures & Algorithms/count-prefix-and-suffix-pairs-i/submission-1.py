class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixandSuffix(s,t):
            if len(s)>len(t):
                return False
            for i in range(len(s)):
                if s[i]!=t[i] or s[-i-1]!=t[-1-i]:
                    return False
            print(s,t)
            return True
        count=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if isPrefixandSuffix(words[i],words[j]):
                    count+=1
        return count