class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            left = 0
            for c in range(cols):
                left += matrix[r][c]
                above = self.prefix[r][c+1]
                self.prefix[r+1][c+1] = above + left
            
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        topLeft = self.prefix[row1][col1]
        topRight = self.prefix[row1][col2 + 1] - topLeft
        bottomLeft = self.prefix[row2+1][col1] - topLeft
        total = self.prefix[row2+1][col2+1]
        res = total - bottomLeft - topRight - topLeft
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)