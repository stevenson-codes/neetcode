class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, subset = [], []
        def bt(idx):
            if idx == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[idx])
            bt(idx + 1)
            subset.pop()
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            bt(idx + 1)
        bt(0)
        return res