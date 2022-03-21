from Entities import TileTypes

class Tower():
    # Define public tower type
    towerType = []
    towerSpeed = 0
    towerRange = 0
    towerEffect = 0
    
    # Constructor
    def __init__(self, towerType):
        # Set Tower Type
        self.towerType = towerType
        
        # Set Tower specs
        if self.towerType == TileTypes.Normal0:
            pass
        elif self.towerType == TileTypes.Cannon0:
            pass
        