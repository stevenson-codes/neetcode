class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res, combination = [], []
        def dfs(idx, value):
            if idx == len(nums) or value > target:
                return
            if value == target:
                res.append(combination.copy())
                return
            
            combination.append(nums[idx])
            dfs(idx, value + nums[idx])
            combination.pop()

            dfs(idx + 1, value)
        
        dfs(0, 0)
        return res
