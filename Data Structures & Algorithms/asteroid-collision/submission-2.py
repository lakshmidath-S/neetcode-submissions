class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            sign=1 if i>0 else 0
            size=abs(i)
            alive=True
            while stack and stack[-1][1]==1 and sign==0:
                if stack[-1][0]<size:
                    stack.pop()
                elif stack[-1][0]==size:
                    stack.pop()
                    alive=False
                    break
                else:
                    alive=False
                    break
            if alive:
                stack.append([size,sign])
        return [x if y==1 else -x for x,y in stack]