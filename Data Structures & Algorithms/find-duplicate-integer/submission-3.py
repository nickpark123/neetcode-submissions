class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            index = abs(nums[i])
            if nums[index] < 0:
                return index
            else:
                nums[index] = - nums[index]
        return 0


# 4, 4, 2, 3, 5, 2
# 0, 1, 2, 3, 4, 5
            