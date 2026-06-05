class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        count = Counter(hand)
        hand.sort()

        for c in hand:
            if count[c]:
                for i in range(groupSize):
                    if not count[c + i]:
                        return False
                    count[c + i] -= 1
        return True