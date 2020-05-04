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
GREY = (240,240,240)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


class display:
    def __init__ (self, rows, cols, width, height, board):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.board = board
        self.selected = None
        self.solved = False
        
        copy = deepcopy(board)
        self.canSolve = sudoku.solveBoard(copy)
        self.solution = copy
        
    def updateBoard(self):
        self.board = None
    
    def placeNum(self,num):
        row,col = self.selected
               
    def draw(self,window):
        
        box_height = self.height / 9
        box_width = self.width / 9
        window.fill(WHITE)
        font = pygame.font.SysFont("comicsans", 70)

        for i in range(9):
            
            #draw the grid
            if i > 0:
                line_width = 2
                if i % 3 == 0:
                    line_width = 4
                    
                y = int(i * box_height)
                pygame.draw.line(window, BLACK, (0,y), (self.width, y), line_width)
                x = int(i * box_width)
                pygame.draw.line(window, BLACK, (x,0), (x, self.height), line_width)
            
            #draw the numbers
            for j in range(9):
                txt = str(self.board[i][j])
                if txt == '0': 
                    continue
                
                colour = BLACK
                if self.selected == (i,j):
                    colour = RED
                

                y_centre = int((i + 0.5)* box_height)
                x_centre = int((j + 0.5) * box_width)

                text_surf = font.render(txt, True, colour)
                text_rect = text_surf.get_rect()
                text_rect.center = (x_centre,y_centre)
                window.blit(text_surf, text_rect)
        pygame.display.update()



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

#initialize the window
WIDTH = 600
HEIGHT = 540
window = pygame.display.set_mode((WIDTH,HEIGHT))
window.fill(WHITE)
pygame.display.set_caption("Sudoku")

disp = display(9,9,WIDTH,HEIGHT,board)
disp.draw(window)
pygame.display.update()



# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            
pygame.quit()