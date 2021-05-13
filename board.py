import pygame

class Board:

    def __init__(self, screen, square):
        self.square = square
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.screen = screen
        self.font = pygame.font.Font(pygame.font.get_default_font(), 30)
        self.blackNumbers = [self.font.render(str(i), True, (0, 0, 0), (255, 255, 255)) for i in range(10)]
        self.redNumbers = [self.font.render(str(i), True, (255, 0, 0), (255, 255, 255)) for i in range(10)]
        self.copy(self.board)

    def copy(self, puzzle):
        for row in range(9):
            for col in range(9):
                self.set_cell(row, col, puzzle[row][col], "black")

    def set_cell(self, row, col, val, color):
        self.board[row][col] = val
        w, h = self.blackNumbers[val].get_size()
        x = (col + 0.5) * self.square - w / 2
        y = (row + 0.5) * self.square - h / 2
        pygame.draw.rect(self.screen, (255, 255, 255), (x, y, w, h))
        
        if val != 0:
            if color == "red":
                self.screen.blit(self.redNumbers[val], (x, y))
            if color == "black":
                self.screen.blit(self.blackNumbers[val], (x, y))

    def get_cell(self, row, col):
        return self.board[row][col]