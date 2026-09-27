class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph={c:set() for word in words for c in word}
        for i in range(len(words)-1):
            a=words[i]
            b=words[i+1]
            j=0
            while j<len(a) and j<len(b):
                if a[j]!=b[j]:
                    graph[a[j]].add(b[j])
                    break
                j+=1
            if j==len(b) and j<len(a):
                return ""
        state={}
        result=[]
        def dfs(node):
            if node in state :
                return state[node]==2
            state[node]=1
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False
            state[node]=2
            result.append(node)
            return True

        for node in graph:
            if node not in state:
                if not dfs(node):
                    return ""
        return "".join(result[::-1])

                