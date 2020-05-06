# -*- coding: utf-8 -*-
"""
Created on Sun May  3 20:05:56 2020

@author: Cecilio
"""

import pygame
import sudoku
from copy import deepcopy


pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLUE = (65, 65, 160)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


class display:
    def __init__(self, rows, cols, width, height, board):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.board = board
        self.selected = None
        self.solved = False

        # save a copy of the original board and the solved board
        copy = deepcopy(board)
        sol = deepcopy(board)
        self.original = copy
        self.canSolve = sudoku.solveBoard(sol)
        self.solution = sol

    def placeNum(self, num):
        row, col = self.selected
        self.board[row][col] = num
               
    def draw(self, window):
        box_height = self.height / 9
        box_width = self.width / 9
        window.fill(WHITE)
        font = pygame.font.SysFont("comicsans", 70)

        for i in range(9):
            
            # draw the grid
            if i > 0:
                line_width = 2
                if i % 3 == 0:
                    line_width = 4
                    
                y = int(i * box_height)
                pygame.draw.line(window, BLACK, (0, y), (self.width, y), line_width)
                x = int(i * box_width)
                pygame.draw.line(window, BLACK, (x, 0), (x, self.height), line_width)
            
            # draw the numbers
            for j in range(9):

                colour = BLACK
                # User input spaces are displayed in a different colour
                if self.original[i][j] == 0:
                    colour = BLUE
                if self.solution[i][j] != self.board[i][j]:
                    colour = RED
                txt = str(self.board[i][j])
                # no number in the square, go to next square
                if txt == '0':
                    continue

                y_centre = int((i + 0.5) * box_height)
                x_centre = int((j + 0.5) * box_width)

                text_surf = font.render(txt, True, colour)
                text_rect = text_surf.get_rect()
                text_rect.center = (x_centre, y_centre)
                window.blit(text_surf, text_rect)

        if self.selected:
            line_width = 4
            i = self.selected[0]
            j = self.selected[1]
            # highlight the selected space with a red square
            x0 = int(j * box_width)
            x1 = int((j + 1) * box_width)
            y0 = int(i * box_height)
            y1 = int((i + 1) * box_height)
            pygame.draw.line(window, RED, (x0, y0), (x0, y1), line_width)
            pygame.draw.line(window, RED, (x0, y0), (x1, y0), line_width)
            pygame.draw.line(window, RED, (x1, y0), (x1, y1), line_width)
            pygame.draw.line(window, RED, (x0, y1), (x1, y1), line_width)

        pygame.display.update()

    def click(self, pos):
        if pos[0] > self.width or pos[1] > self.height:
            return None
        x_gap = self.width/9
        y_gap = self.height/9
        i = int(pos[1] // y_gap)
        j = int(pos[0] // x_gap)
        return i, j

    def select(self, click):
        self.selected = click


board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]

# initialize the window
WIDTH = 600
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(WHITE)
pygame.display.set_caption("Sudoku")

disp = display(9, 9, WIDTH, HEIGHT, board)
disp.draw(window)
pygame.display.update()

# game loop
running = True
key = None
while running:
    for event in pygame.event.get():
        key = None
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked = disp.click(pos)
            if clicked:
                disp.select(clicked)
                key = None
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                key = 1
            if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                key = 2
            if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                key = 3
            if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                key = 4
            if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                key = 5
            if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                key = 6
            if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                key = 7
            if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                key = 8
            if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                key = 9
            if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE or event.key == pygame.K_0:
                key = None
                i, j = disp.selected
                # Only erase the space if it came from user input
                if disp.original[i][j] == 0:
                    disp.placeNum(0)

        if key is not None:
            i, j = disp.selected
            if disp.original[i][j] == 0:
                disp.placeNum(key)

    disp.draw(window)
    pygame.display.update()

pygame.quit()
