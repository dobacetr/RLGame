from Tiles.Entity import Entities
import numpy as np

def Map1():
        # Define board size
        boardSz = 10
        
        # Define empty board
        board = np.full( (boardSz, boardSz), Entities.Empty)
        
        # Define path
        board[1, 0] = Entities.Entrance
        
        for col in range(1, 8):
            board[1, col] = Entities.Path
            board[3, col] = Entities.Path
            board[5, col] = Entities.Path
            board[7, col] = Entities.Path
        
        board[2,8] = Entities.Path
        board[4,1] = Entities.Path
        board[6,8] = Entities.Path
        board[8,0] = Entities.Path
        board[9,0] = Entities.Exit
        
        return board