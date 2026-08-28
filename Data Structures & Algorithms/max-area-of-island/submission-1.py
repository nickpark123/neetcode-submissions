class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        self.mostArea = 0
        self.count = 0
        self.seen = set()
      
        def dfs(i, j):
            if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0 or (i, j) in self.seen):
                return
            elif grid[i][j] == 1:
                self.count +=1
                self.seen.add((i, j))
                for dr, dc in directions:
                    dfs(i + dr, j + dc)  

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    self.count = 0
                    dfs(row, col)
                    if self.count > self.mostArea:
                        self.mostArea = self.count

        return self.mostArea



