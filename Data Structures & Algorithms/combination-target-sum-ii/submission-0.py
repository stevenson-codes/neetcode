class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(index, count):
            if count == target:
                res.append(subset.copy())
                return
            
            if index >= len(candidates) or count > target:
                return
            
            subset.append(candidates[index])
            dfs(index + 1, count + candidates[index])
            subset.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            dfs(index + 1, count)
        
        dfs(0, 0)
        return res

            