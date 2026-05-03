class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for n in count.values():
            if n > 1:
                return True
        
        return False