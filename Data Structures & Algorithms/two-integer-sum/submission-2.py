class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        res = {}

        for i, n in enumerate(nums):
            res[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in res and res[diff] != i:
                return [i, res[diff]]