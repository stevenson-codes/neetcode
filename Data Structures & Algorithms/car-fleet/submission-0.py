class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        fleet = 1
        prevTime = (target - pair[0][0]) / pair[0][1]
        for p, s in pair[1:]:
            curTime = (target - p) / s
            if prevTime < curTime:
                fleet += 1
                prevTime = curTime
        
        return fleet
