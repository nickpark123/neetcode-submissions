class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        b = [1 for i in range(len(nums))]
        left = 1
        right = 1

        for i in range(len(nums)):
            b[i] = left
            left = left * nums[i]

        for i in range(len(nums) -1, -1, -1):
            b[i] = b[i] * right
            right = right * nums[i]

        return b







        