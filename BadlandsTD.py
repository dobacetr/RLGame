import numpy as np
import random
from Maps import Maps

from Tiles.Entity import Entities

# Define the game class
class BadlandsTDGame:
    # Public definition of board
    board = []
    # Public definition of towers
    towers = []
    
    # Constructor
    def __init__(self):
        board = Maps.InitMap(1)
            
        
    # Propagation
    def step(self, action):
        pass
        
    # Render
    def render(self):
        pass
    
    # Reset
    def reset(self):
        pass
        
