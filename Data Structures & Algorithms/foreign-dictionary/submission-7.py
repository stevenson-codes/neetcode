class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minLen = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            for j in range(minLen):
                if word1[j] != word2[j]:
                    adjList[word1[j]].add(word2[j])
                    break
        
        visited = set()
        path = set()
        res = []

        def dfs(char):
            if char in visited:
                return char not in path
            
            visited.add(char)
            path.add(char)

            for neiChar in adjList[char]:
                if not dfs(neiChar):
                    return False
            
            path.remove(char)
            res.append(char)
            return True
        
        for char in adjList:
            if not dfs(char):
                return ""
        
        res.reverse()
        return "".join(res)

