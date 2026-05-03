class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subsetSum = 0
        subset = []

        def dfs(index):
            nonlocal subsetSum
            if subsetSum == target:
                res.append(subset.copy())
                return

            if index >= len(nums) or subsetSum > target:
                return
            
            subset.append(nums[index])
            subsetSum += nums[index]
            dfs(index)

            subset.pop()
            subsetSum -= nums[index]
            dfs(index + 1)
        
        dfs(0)
        return res
                
            
