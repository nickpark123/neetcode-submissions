class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            target = 0
            for p in piles:
                x = math.ceil(p/mid)
                target += x 
            if target <= h:
                ans = mid
                high = mid - 1
            elif target > h:
                low = mid + 1
        return ans
        