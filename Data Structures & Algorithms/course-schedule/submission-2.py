class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {c: set() for c in range(numCourses)}
        for crs, pre in prerequisites:
            adjList[crs].add(pre)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            
            visited.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True