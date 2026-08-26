class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        l=len(digits)
        ans=[]
        def back(i,s):
            if i==l:
                ans.append(''.join(s))
                return
            num=digits[i]
            string=phone[num]
            for k in range(len(string)):
                s.append(string[k])
                back(i+1,s)
                s.pop()
        back(0,[])
        return ans

            
