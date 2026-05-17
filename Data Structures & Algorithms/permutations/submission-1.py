class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        visited = set()
        def bt():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for n in nums:
                if n not in visited:
                    subset.append(n)
                    visited.add(n)
                    bt()
                    subset.pop()
                    visited.remove(n)
        bt()
        return res
            
