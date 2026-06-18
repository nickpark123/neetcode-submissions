class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for word in strs:
            sort = "".join(sorted(word))
            if sort not in my_dict.keys():
                my_dict[sort] = [word]
            else:
                my_dict.get(sort).append(word)
                    

        my_list = []
        for key in my_dict:
            my_list.append(my_dict[key])
        
        return my_list
                

        