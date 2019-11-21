import pygame

class Board:

    def __init__(self, screen, square):
        self.square = square
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
        x = (col + 0.5) * self.square - w / 2
        y = (row + 0.5) * self.square - h / 2
        pygame.draw.rect(self.screen, (0, 0, 0), (x, y, w, h))
        
        if val != 0:
            self.screen.blit(self.numbers[val], (x, y))

    def get_cell(self, row, col):
        return self.board[row][col]