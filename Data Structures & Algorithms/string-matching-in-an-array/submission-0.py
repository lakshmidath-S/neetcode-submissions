class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=set()
        for i in range(len(words)):
            for j in range(i,len(words)):
                if i==j:
                    continue
                if words[i] in words[j]:
                    ans.add(words[i])
                elif words[j] in words[i]:
                    ans.add(words[j])
        return [x for x in ans ]