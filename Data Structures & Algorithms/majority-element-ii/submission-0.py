class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        number = defaultdict(int)
        n = len(nums) // 3
        res = []
        seen = set()

        for num in nums:
            if num in seen:
                continue
            if number[num] > n:
                res.append(num)
                seen.add(num)
            else:
                number[num] += 1
                if number[num] > n:
                    res.append(num)
                    seen.add(num)
        
        return res


        


        