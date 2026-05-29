class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, permutation = [], []
        visited = set()

        def bt():
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return
            
            for n in nums:
                if n not in visited:
                    permutation.append(n)
                    visited.add(n)
                    bt()
                    permutation.pop()
                    visited.remove(n)
        bt()
        return res