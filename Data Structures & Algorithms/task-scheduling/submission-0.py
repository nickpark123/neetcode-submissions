class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}

        for task in tasks:
            counts[task] = 1 + counts.get(task, 0)

        maxHeap = [-count for count in counts.values()]
        heapq.heapify(maxHeap)

        q = deque()  # [remaining_count, available_time]
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                count = heapq.heappop(maxHeap)
                count += 1

                if count != 0:
                    q.append([count, time + n])

            if q and q[0][1] == time:
                count, readyTime = q.popleft()
                heapq.heappush(maxHeap, count)

        return time
