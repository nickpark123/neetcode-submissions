class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        k = defaultdict(int)
        res = []

        for letter in s: 
            k[letter] +=1
        
        for letter, count in k.items():
            heapq.heappush(heap, (-count, letter))

        prev_count = 0
        prev_letter = ""

        while heap:
            count, letter = heapq.heappop(heap)
            res.append(letter)

            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_letter))
            
            prev_count = count + 1
            prev_letter = letter
            
        if prev_count < 0:
            return ""
       
        return "".join(res)

