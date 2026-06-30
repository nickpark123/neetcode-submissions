class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = [0 for i in range(len(temperatures))]
        k = []
        for i, t in enumerate(temperatures):
            if not k:
                k.append((i, t))
                continue
            index, temp = k[-1]
            if t < temp:
                k.append((i, t))
            else:
                while k and k[-1][1] < t:
                    index, temp = k.pop()
                    s[index] = i - index
                k.append((i, t))
        return s

        