class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr=s.split(" ")
        used=set()
        if len(pattern)!=len(arr):
            return  False
        freq={}
        for i in range(len(pattern)):
            if pattern[i] in freq:
                if freq[pattern[i]]!=arr[i]:
                    return False
            else:
                if arr[i] in used:
                    return False
            freq[pattern[i]]=arr[i]
            used.add(arr[i])
        return True
