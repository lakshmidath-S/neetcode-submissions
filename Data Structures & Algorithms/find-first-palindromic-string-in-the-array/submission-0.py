class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def ispalindrome(word):
            i=0
            j=len(word)-1
            while i<j:
                if word[i]!=word[j]:
                    return False
                i+=1
                j-=1
            return True
        for i in words:
            if ispalindrome(i):
                return i
        return ""
