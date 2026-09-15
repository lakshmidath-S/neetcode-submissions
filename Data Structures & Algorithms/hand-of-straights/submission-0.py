class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        freq={}
        for i in hand:
            freq[i]=freq.get(i,0)+1
        hand.sort()
        for card in hand:
            if freq[card]==0:
                continue
            for j in range(groupSize):
                if freq.get(card+j,0)==0:
                    return False
                freq[card+j]-=1
        return True

