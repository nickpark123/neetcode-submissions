class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        heap = []
        res = []
        if a > 0:
            heapq.heappush(heap, (-a, "a"))
        if b > 0:
            heapq.heappush(heap, (-b, "b"))
        if c > 0:
            heapq.heappush(heap, (-c, "c"))
        
        while heap:
            count, letter = heapq.heappop(heap)
            if len(res) >= 2 and res[-1] == letter and res[-2] == letter:
                if not heap:
                    break
                count2, letter2 = heapq.heappop(heap)
                res.append(letter2)
                count2 += 1
                if count2 != 0:
                    heapq.heappush(heap, (count2, letter2))
                heapq.heappush(heap, (count, letter))

            else:
                res.append(letter)
                count += 1
                if count != 0:
                    heapq.heappush(heap, (count, letter))
            
        return "".join(res)
