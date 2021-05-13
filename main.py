import solver
import pygame
import board

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

square = 50
pygame.init()
screen = pygame.display.set_mode((square * 9, square * 9))
clock = pygame.time.Clock()
running = True
board = board.Board(screen, square)
solver = solver.Solver(board)

pygame.draw.rect(screen, (255, 255, 255), (0, 0, square * 9, square * 9))

for row in range(1, 9):
    pygame.draw.line(screen, (0, 0, 0), (square * row, 0), (square * row, square * 9), 5 if row % 3 == 0 else 1)
for col in range(1, 9):
    pygame.draw.line(screen, (0, 0, 0), (0, square * col), (square * 9, square * col), 5 if col % 3 == 0 else 1)

board.copy(puzzle)

while running:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            solver.start()

    pygame.display.update()
    clock.tick(60)

solver.join()