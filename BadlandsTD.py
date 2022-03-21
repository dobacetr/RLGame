import numpy as np
import random

from Entities import TileTypes as TileTypes

# Define the game class
class BadlandsTDGame:
    # Public definition of board
    board = []
    # Public definition of towers
    towers = []
    
    # Constructor
    def __init__(self):
        # Define board size
        boardSz = 10
        
        # Define empty board
        self.board = np.full( (boardSz, boardSz), TileTypes.Empty)
        
        # Define path
        
            
        
    # Propagation
    def step(self, action):
        pass
        
    # Render
    def render(self):
        pass
    
    # Reset
    def reset(self):
        pass
        
