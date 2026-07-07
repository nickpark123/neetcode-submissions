class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search for where i + 1 is not > i
        if len(nums) == 1:
            return nums[0]
        low, high = 0, len(nums) - 1
        if nums[low] <= nums[high]:
            return nums[low]

        while low <= high:
            mid = (low + high) // 2
            if nums[mid + 1] < nums[mid]:
                return nums[mid+1]
            elif nums[mid] < nums[low]:
                high = mid - 1
            else:
                low = mid + 1
                