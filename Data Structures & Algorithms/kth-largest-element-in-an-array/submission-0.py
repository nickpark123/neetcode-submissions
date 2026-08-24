class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = []
        heapq.heapify(l)
        for num in nums:
            heapq.heappush(l, num)
            if len(l) > k:
                heapq.heappop(l)
        return heapq.heappop(l)
        