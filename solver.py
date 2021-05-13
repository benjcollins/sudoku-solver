import threading

class Solver(threading.Thread):

    def __init__(self, board):
        threading.Thread.__init__(self)
        self.board = board

    def run(self):
        self.solve(0, 0)

    def check_row(self, row):
        nums_used = {}
        for col in range(9):
            cell = self.board.get_cell(row, col)
            if cell != 0 and cell in nums_used:
                return False
            nums_used[cell] = True
        return True

    def check_col(self, col):
        nums_used = {}
        for row in range(9):
            cell = self.board.get_cell(row, col)
            if cell != 0 and cell in nums_used:
                return False
            nums_used[cell] = True
        return True

    def check_box(self, row, col):
        nums_used = {}
        for r in range(3):
            for c in range(3):
                cell = self.board.get_cell(row//3*3+r, col//3*3+c)
                if cell != 0 and cell in nums_used:
                    return False
                nums_used[cell] = True
        return True

    def check(self, row, col):
        return self.check_row(row) and self.check_col(col) and self.check_box(row, col)

    def solve_next(self, row, col):
        if col < 8:
            return self.solve(row, col + 1)
        else:
            return self.solve(row + 1, 0)
        
    def solve(self, row, col):
        if row < 9:
            if self.board.get_cell(row, col) == 0:
                for i in range(1, 10):
                    self.board.set_cell(row, col, i, "red")
                    if self.check(row, col) and self.solve_next(row, col):
                        return True
                self.board.set_cell(row, col, 0, "red")
                return False
            return self.solve_next(row, col)
        return True