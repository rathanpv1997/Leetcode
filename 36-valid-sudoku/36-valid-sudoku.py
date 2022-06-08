class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isValidBlock(block: list) -> bool:
            d = {}
            for num in block:
                if num == '.':
                    continue
                if int(num) < 1 or int(num) > 9:
                    return False
                if num not in d:
                    d[num] = True
                else:
                    return False
            return True
        
        for row in board:
            if isValidBlock(row):
                continue
            else:
                return False
            
        for col in zip(*board):
            if isValidBlock(col):
                continue
            else:
                return False
            
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if isValidBlock(square):
                    continue
                else:
                    return False
        
        return True
        