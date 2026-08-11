class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def can_spell_from(r, c, k):
            
            if k == len(word):
                return True
            if not (0 <= r < rows and 0 <= c < cols):
                return False
            if (r, c) in path or board[r][c] != word[k]:
                return False

            path.add((r, c))
            ok = (can_spell_from(r + 1, c, k + 1) or
                  can_spell_from(r - 1, c, k + 1) or
                  can_spell_from(r, c + 1, k + 1) or
                  can_spell_from(r, c - 1, k + 1))
            path.discard((r, c))
            return ok

        for r in range(rows):
            for c in range(cols):
                if can_spell_from(r, c, 0):
                    return True
        return False

            
            

        