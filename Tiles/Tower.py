from Tiles.Entity import Entities
from Tiles.Effects import Effects

class Tower():
    # Define public tower type
    towerType = Entities.Empty
    towerDamage = 0
    towerSpeed = 0
    towerRange = 0
    towerEffect = Effects.NoEffect
    
    # Constructor
    def __init__(self, towerType):
        # Set Tower Type
        self.towerType = towerType
        
        # Set Tower specs
        if self.towerType == Entities.Normal0:
            # Normal Tower
            
            # 3 damage
            self.towerDamage = 3.0
            
            # 1 attack/s
            self.towerSpeed = 1.0
            
            # range 5 tiles
            self.towerRange = 5.0
            
            # single target
            self.towerEffect = Effects.SingleTarget
            
        elif self.towerType == Entities.Cannon0:
            # Cannon Tower
            
            # 5 damage
            self.towerDamage = 5.0
            
            # 0.5 attack/s
            self.towerSpeed = 0.5
            
            # range 3 tiles
            self.towerRange = 3.0
            
            # +1 tile splash
            self.towerEffect = Effects.SplashDamage
            
        else:
            raise NotImplemented
        
        