class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        buckets = defaultdict(list)
        for s in strs:
            bucket = [0 for _ in range(26)]
            for c in s:
                bucket[ord(c) - ord('a')] += 1
            buckets[tuple(bucket)].append(s)
        
        return list(buckets.values())
