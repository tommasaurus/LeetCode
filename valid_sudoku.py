class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        from collections import defaultdict
        grid_dict = defaultdict(set)
        for r in range(9):
            horizontal_set = set()
            vertical_set = set()            
            for c in range(9):
                if board[c][r] == ".":
                    pass
                elif board[c][r] in vertical_set:
                    return False
                else:
                    vertical_set.add(board[c][r])

                if board[r][c] == ".":
                    pass
                elif board[r][c] in horizontal_set:
                    return False
                else:
                    horizontal_set.add(board[r][c])

                grid_r = r//3
                grid_c = c//3
                key = (grid_r, grid_c)
                if key in grid_dict and board[r][c] != ".":
                    if board[r][c] in grid_dict[key]:
                        return False
                    else:
                        grid_dict[key].add(board[r][c])
                elif board[r][c] != ".":
                    grid_dict[key].add(board[r][c])

        return True

        