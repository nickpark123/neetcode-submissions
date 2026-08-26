class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur, left):
            if not left:
                res.append(cur.copy())
                return

            for i in range(len(left)):
                cur.append(left[i])

                nxt = left.copy()
                nxt.pop(i)

                dfs(cur, nxt)

                cur.pop()

        dfs([], nums)
        return res