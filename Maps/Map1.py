from Tiles.Entity import Entities
import numpy as np

def Map1():
        # Define board size
        boardSz = 10
        
        # Define empty board
        board = np.full( (boardSz, boardSz), Entities.Empty)
        
        # Define path
        board[0, 1] = Entities.Entrance
        
        for col in range(1, 9):
            board[col, 1] = Entities.Path
            board[col, 3] = Entities.Path
            board[col, 5] = Entities.Path
            board[col, 7] = Entities.Path
        
        board[8,2] = Entities.Path
        board[1,4] = Entities.Path
        board[8,6] = Entities.Path
        board[0,7] = Entities.Path
        board[0,8] = Entities.Path
        board[0,9] = Entities.Exit
        
        return board