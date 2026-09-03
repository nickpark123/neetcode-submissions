class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r, b, g = 0, 0, 0

        for num in nums:
            if num == 0:
                r +=1
            elif num == 2:
                g +=1
            else: 
                b += 1

        for i in range(len(nums)):
            if r != 0:
                nums[i] = 0
                r -=1
                continue
            if b != 0:
                nums[i] = 1
                b-=1
                continue
            else:
                nums[i] = 2
                


        
                
        