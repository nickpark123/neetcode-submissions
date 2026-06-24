class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        my_list = set()

        nums1 = sorted(nums)

        for i in range(len(nums1)):
            j = i + 1
            diff = 0 - nums1[i]
            k = len(nums1) - 1

            while j < k:
                if nums1[j] + nums1[k] == diff:
                    my_list.add((nums1[i], nums1[j], nums1[k]))
                    j += 1
                elif nums1[j] + nums1[k] < diff:
                    j += 1
                elif nums1[j] + nums1[k] > diff:
                    k -= 1
            
        return [list(t) for t in my_list]




        
        