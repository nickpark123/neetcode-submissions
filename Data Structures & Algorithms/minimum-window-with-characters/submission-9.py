class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        myMap = {}
        for k in t:
            myMap[k] = myMap.get(k, 0) + 1
        window = {}
        need = len(myMap)
        have = 0

        l = 0
        shortest = float("inf")
        res = ""

        for r in range(len(s)):
            if s[r] in myMap:
                window[s[r]] = window.get(s[r], 0) + 1

                if window[s[r]] == myMap[s[r]]:
                    have += 1

            while have == need:
                if r - l + 1 < shortest:
                    shortest = r - l + 1
                    res = s[l:r + 1]

                if s[l] in myMap:
                    if window[s[l]] == myMap[s[l]]:
                        have -= 1
                    window[s[l]] -= 1

                l += 1

        return res
        





                

        