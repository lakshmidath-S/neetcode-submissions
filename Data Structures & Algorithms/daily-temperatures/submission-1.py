class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temperatures)
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
                continue
            elif stack:
                while stack and  temperatures[stack[-1]]<temperatures[i]:
                    a=stack.pop()
                    result[a]=i-a
                stack.append(i) 
        return result         
