class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def seqChecker(seq: List[str]):
            seen = {}
            for c in seq:
                if c != "." and c in seen:
                    return False                    
                seen[c] = 1
            return True
        def squareChecker(square: List[List[str]]):
            seen_ = {}
            # print(square)
            
            for row in square:
                for s in row:
                    if s != "." and s in seen_:
                        # print("SEEN:", s)
                        return False
                    seen_[s] = 1
                    # print(seen_)
            return True
        
        # False
        for row in board:
            if not seqChecker(row):
                return False
        
        for i in range(len(board)):
            col = [row[i] for row in board]
            if not seqChecker(col):
                return False

        row_ = [0,3,6]
        col_ = [0,3,6]
        for r in row_:
            for c in col_:
                # print(r, c)
                if not squareChecker([row[c:c+3] for row in board[r:r+3]]):
                    return False


        return True