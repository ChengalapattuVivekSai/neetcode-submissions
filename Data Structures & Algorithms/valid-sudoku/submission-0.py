class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = [set() for _ in range(9)]

        row =[set() for  _ in range(9)]

        box = [set() for _ in range(9)]

        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]==".":
                    continue
                if board[i][j] in cols[j]:
                    return False
                else:
                    cols[j].add(board[i][j])

        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]==".":
                    continue
                if board[i][j] in row[i]:
                    return False
                else:
                    row[i].add(board[i][j])

        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]==".":
                    continue
                if board[i][j] in box[i//3 * 3 + j//3]:
                    return False
                else:
                    box[i//3 * 3 + j//3].add(board[i][j])

        return True


        