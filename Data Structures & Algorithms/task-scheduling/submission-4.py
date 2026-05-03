class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]

        heapq.heapify(maxHeap)
        q = deque()

        time = 0

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][0]
            else:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    q.append([time + n, cnt])
            
            if q and time == q[0][0]:
                heapq.heappush(maxHeap, q.popleft()[1])
        

        return time
            