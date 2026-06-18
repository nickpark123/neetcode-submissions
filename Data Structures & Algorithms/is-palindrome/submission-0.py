class Solution:
    def isPalindrome(self, s: str) -> bool:
        my_str = [ch for ch in s if ch.isalnum()]
        k = len(my_str) // 2
        i =-1
        j = 0

        for m in range(k):
            if my_str[j].lower() != my_str[i].lower():
                return False
            else:
                i -= 1
                j += 1

        return True
            


            

        