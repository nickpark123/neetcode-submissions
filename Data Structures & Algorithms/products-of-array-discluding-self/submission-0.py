class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        b = [1 for i in range(len(nums))]

        for i in range(len(nums)):
            for j in range(len(b)):
                if j != i:
                    b[j] = b[j] * nums[i]

        return b






        