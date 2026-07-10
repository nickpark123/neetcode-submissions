class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        m = 0
        

        while l <= r:
            m = (l + r) // 2
        # so at least 2 of the 3 will be ordered
        # such as 8, 2, 6
            if nums[m] == target:
                return m
            elif nums[m] <= nums[r]:
                if nums[r] >= target > nums[m]:
                    l = m + 1
                else: 
                    r = m - 1
            else: 
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else: 
                    l = m + 1
                

        return -1


            

        