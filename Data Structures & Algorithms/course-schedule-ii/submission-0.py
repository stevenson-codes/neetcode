class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {num: set() for num in range(numCourses)}
        for crs, pre in prerequisites:
            adjList[crs].add(pre)
        
        visited = set()
        path = set()
        res = []

        def dfs(crs):
            if crs in visited:
                return crs not in path

            visited.add(crs)
            path.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre):
                    return False
            
            path.remove(crs)
            res.append(crs)
            return True

        for crs in adjList:
            if not dfs(crs):
                return []
        return res
        