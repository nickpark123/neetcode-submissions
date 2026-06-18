class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        mini = defaultdict(set)

        
        for i in range(len(board)):
            for j in range(len(board[i])):
                a = i // 3
                b = j // 3

        
                if board[i][j] != ".": 
                    if board[i][j] in mini[a, b]:
                        return False

                    if board[i][j] in row[i]:
                        return False

                    if board[i][j] in col[j]:
                        return False

                    mini[a, b].add(board[i][j])
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])


        return True

            

            




        