class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1

        while(i<j):
            a=s[i].lower()
            b=s[j].lower()
            while(not(a.isalnum()) and i<j):
                i+=1
                a=s[i].lower()
            while(not(b.isalnum())and i<j):
                j-=1
                b=s[j].lower()
            if a!=b:
                return False
            i+=1
            j-=1
        return True