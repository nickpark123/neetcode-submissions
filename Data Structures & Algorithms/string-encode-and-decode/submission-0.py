class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += f"{len(s)}:{s}"
   
        return string

    def decode(self, s: str) -> List[str]:
        m = []
        i = 0

        while i < len(s):
            j = i
            while s[j] is not ":":
                j += 1
            leng = int(s[i:j])
            i = j + 1
            j = i + leng
            m.append(s[i:j])
            i = j
        return m




