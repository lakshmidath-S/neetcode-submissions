class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = list(zip(position, speed))
        combined.sort(reverse=True)
        position, speed = zip(*combined)
        time=[0]*len(speed)
        for i in range(len(speed)):
            temp=(target-position[i])/speed[i]
            if i==0:
                time[i]=temp
                continue
            time[i]=max(temp,time[i-1])
        return len(set(time))
        