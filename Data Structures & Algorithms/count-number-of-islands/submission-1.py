class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        count = 0

        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if grid[a][b] == "1" and (a, b) not in seen:
                    stack = []
                    count += 1
                    seen.add((a, b))
                    stack.append((a, b))
                    while stack:
                        (i, j) = stack.pop()
                        if 0 <= i+1 < len(grid) and 0 <= j < len(grid[0]):
                            if (i+1, j) not in seen and grid[i+1][j] == "1":
                                seen.add((i+1, j))
                                stack.append((i+1, j))
                        if 0 <= i-1 < len(grid) and 0 <= j < len(grid[0]):
                            if (i-1, j) not in seen and grid[i-1][j] == "1":
                                seen.add((i-1, j)) 
                                stack.append((i-1, j))
                        if 0 <= i < len(grid) and 0 <= j+1 < len(grid[0]):
                            if (i, j+1) not in seen and grid[i][j+1] == "1":
                                seen.add((i, j+1))  
                                stack.append((i, j+1))
                        if 0 <= i < len(grid) and 0 <= j-1 < len(grid[0]):
                            if (i, j-1) not in seen and grid[i][j-1] == "1":
                                stack.append((i, j-1))
                                seen.add((i, j-1))  
                        
        return count


        