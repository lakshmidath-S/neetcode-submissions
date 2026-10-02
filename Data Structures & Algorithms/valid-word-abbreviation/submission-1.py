class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i=0
        j=0
        n=len(word)
        m=len(abbr)
        while i<n and j<m:
            if abbr[j].isalpha():
                if abbr[j]!=word[i]:
                    return False
                j+=1
                i+=1
            else:
                if abbr[j]=='0':
                    return False
                num=0
                while j<m and abbr[j].isdigit():
                    num=(num*10)+int(abbr[j])
                    j+=1
                i+=num
        return i==n and j==m