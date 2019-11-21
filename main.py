import time
import pygame
import threading

puzzle = [
    [0, 3, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 8, 0, 9, 1, 3, 0, 0],
    [6, 0, 0, 4, 0, 0, 7, 0, 0],
    [0, 0, 3, 8, 1, 0, 0, 0, 0],
    [0, 0, 6, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 3, 4, 8, 0, 0],
    [0, 0, 1, 0, 0, 8, 0, 0, 9],
    [0, 0, 4, 1, 2, 0, 6, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 4, 0]
]

class Board:

    def __init__(self, screen):
        self.board = [[0 for i in range(9)] for i in range(9)]
        self.screen = screen
        self.font = pygame.font.Font(pygame.font.get_default_font(), 30)
        self.numbers = [self.font.render(str(i), True, (255, 255, 255), (0, 0, 0)) for i in range(0, 10)]
        self.copy(self.board)

    def copy(self, puzzle):
        for row in range(9):
            for col in range(9):
                self.set_cell(row, col, puzzle[row][col])

    def set_cell(self, row, col, val):
        self.board[row][col] = val
        w, h = self.numbers[val].get_size()
        x = (col + 0.5) * square - w / 2
        y = (row + 0.5) * square - h / 2
        pygame.draw.rect(screen, (0, 0, 0), (x, y, w, h))
        
        if val != 0:
            self.screen.blit(self.numbers[val], (x, y))

    def get_cell(self, row, col):
        return self.board[row][col]

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
                    self.board.set_cell(row, col, i)
                    if self.check(row, col) and self.solve_next(row, col):
                        return True
                self.board.set_cell(row, col, 0)
                return False
            return self.solve_next(row, col)
        return True

square = 50
pygame.init()
screen = pygame.display.set_mode((square * 9, square * 9))
clock = pygame.time.Clock()
running = True
board = Board(screen)
board.copy(puzzle)
solver = Solver(board)

for row in range(1, 9):
    pygame.draw.line(screen, (255, 255, 255), (square * row, 0), (square * row, square * 9), 5 if row % 3 == 0 else 1)
for col in range(1, 9):
    pygame.draw.line(screen, (255, 255, 255), (0, square * col), (square * 9, square * col), 5 if col % 3 == 0 else 1)

while running:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            solver.start()

    pygame.display.update()
    clock.tick(60)