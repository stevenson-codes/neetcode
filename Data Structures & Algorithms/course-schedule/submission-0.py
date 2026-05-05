class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if not adjList[crs]:
                return True

            visited.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            adjList[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True