class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.hashmap[key]
        if not values:
            return ''
        
        l, r = 0, len(values) - 1
        while l < r:
            m = (l + r + 1) >> 1
            if values[m][0] <= timestamp:
                l = m
            else:
                r = m - 1
        return values[l][1] if values[l][0] <= timestamp else ''
            
