class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range (0,9)]
        col_set = [set() for _ in range (0,9)]

        box_set = {}
        for i in range(0,3):
            for j in range(0,3):
                box_set[(i,j)]=set()

        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]==".":
                    continue
                if board[i][j] in row_set[i]:
                    return False
                else:
                    row_set[i].add(board[i][j])

                if board[i][j] in col_set[j]:
                    return False
                else:
                    col_set[j].add(board[i][j])
                key = (i//3, j//3)
                if board[i][j] in box_set[key]:
                    return False
                else:
                    box_set[key].add(board[i][j])

        return True


                
