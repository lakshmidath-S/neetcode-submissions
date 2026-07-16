class Solution:

    def encode(self, strs: List[str]) -> str:
        parts=[]
        for words in strs:
            parts.append(str(len(words)))
            parts.append(str('#'))
            parts.append(words)
        embeded="".join(parts)
        return embeded

    def decode(self, s: str) -> List[str]:
        if len(s)==0:
            return []
        i=0
        strings=[]
        while(i<len(s)):
            digits=''
            while i<len(s) and s[i]!='#' :
                digits+=s[i]
                i+=1
            length=int(digits)
            if s[i]=='#':
                temp=""
                for j in range(1,length+1):
                    temp+=s[i+j]
                strings.append(temp)
                i+=1
            i+=length
        return strings
