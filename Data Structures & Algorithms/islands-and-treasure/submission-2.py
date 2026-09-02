class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        col = len(grid[0])

        q = collections.deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            i, j = q.popleft()

            for dr, dc in directions:
                r = i + dr
                c = j + dc

                if r < 0 or r >= row or c < 0 or c >= col:
                    continue

                if grid[r][c] != 2147483647:
                    continue

                grid[r][c] = grid[i][j] + 1
                q.append((r, c))