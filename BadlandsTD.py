import numpy as np
import random
from Maps import Maps

import pygame, sys
from pygame.locals import *

from Tiles.Entity import Entities

# Define the game class
class BadlandsTDGame:
    # Public definition of board
    board = []
    # Public definition of towers
    towers = []
    
    
    DISPLAY = []
    screenHeight = 500
    screenWidth = 500
    gridHeight = []
    gridWidth = []
    
    clock = []
    
    # Constructor
    def __init__(self):
        self.board = Maps.InitMap(1)
        pygame.init()
        self.DISPLAY=pygame.display.set_mode(
            (self.screenWidth,self.screenHeight), 
            0, 
            32 
        )
        self.gridHeight = self.screenHeight/self.board.shape[1]
        self.gridWidth = self.screenWidth/self.board.shape[0]
        self.clock = pygame.time.Clock()
            
        
    # Propagation
    def step(self, action):
        pass
        
    # Render
    def render(self):
        WHITE=(255,255,255)
        BLUE=(0,0,255)
        RED=(255,0,0)
        BLACK=(0,0,0)

        #self.DISPLAY.fill(WHITE)
        
        for col in range(0,self.board.shape[0]):
            for row in range(0,self.board.shape[1]):
                color = WHITE
                if self.board[row, col] == Entities.Path:
                    color = BLACK
                elif self.board[row, col] == Entities.Entrance:
                    color = BLUE
                elif self.board[row, col] == Entities.Exit:
                    color = RED
                pygame.draw.rect(
                    self.DISPLAY,
                    color,
                    (row*self.gridHeight,
                     col*self.gridWidth,
                     self.gridWidth,
                     self.gridHeight
                    )
                )
                    
        pygame.display.update()
        self.clock.tick(60)
    
    # Reset
    def reset(self):
        pass
        
