from enum import Enum, unique, auto
@unique
class TileTypes(Enum):
    # Paths are unbuildable
    Path = 0
    
    # Empty tiles are buildable
    Empty = auto()
    
    # Normal Tower
    # 1 attack/s
    # range 5 tiles
    # single target
    Normal0 = auto()
    
    # Cannon Tower
    # 0.5 attack/s
    # range 3 tiles
    # +1 tile aoe
    Cannon0 = auto()
