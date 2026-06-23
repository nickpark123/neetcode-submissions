class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i = 0
        n = len(numbers)
        t = 1
        for k in range(len(numbers)):
            if numbers[i] + numbers[n-t] == target:
                return [i +1, n-t + 1]
            if numbers[i] + numbers[n-t] < target: 
                i += 1
                continue
            if numbers[i] + numbers[n-t] > target:
                t += 1
                continue
            
