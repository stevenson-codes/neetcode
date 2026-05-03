class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(perm, visited):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if not visited[i]:
                    perm.append(nums[i])
                    visited[i] = True
                    dfs(perm, visited)
                    perm.pop()
                    visited[i] = False
        
        dfs([], [False] * len(nums))
        return res
