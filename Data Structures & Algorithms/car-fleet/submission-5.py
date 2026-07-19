class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = list(zip(position, speed))
        combined.sort(reverse=True)
        position, speed = zip(*combined)
        time1=0
        count=1
        for i in range(len(speed)):
            temp=(target-position[i])/speed[i]
            if i==0:
                time1=temp
                continue
            if time1<temp:
                time1=temp
                count+=1
        return count