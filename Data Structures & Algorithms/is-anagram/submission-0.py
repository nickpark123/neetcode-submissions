class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        for char in s:
            if char not in my_dict:
                my_dict[char] = 1
            else:
                j = my_dict[char] + 1
                my_dict[char] = j
        your_dict = {}
        for char in t:
            if char not in your_dict:
                your_dict[char] = 1
            else:
                j = your_dict[char] + 1
                your_dict[char] = j
        return (my_dict == your_dict)
        

        
            
        

