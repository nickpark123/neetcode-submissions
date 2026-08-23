class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            k = abs(heapq.heappop(maxHeap) - heapq.heappop(maxHeap))
            if k != 0:
                heapq.heappush(maxHeap, -k)
        
        if not maxHeap: 
            return 0
        else:
            return -heapq.heappop(maxHeap)
            
            