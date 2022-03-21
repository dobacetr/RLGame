from enum import Enum, unique, auto
@unique
class Entities(Enum):
    # Paths are unbuildable
    Path = auto()
    
    # Entrance
    Entrance = auto()
    
    # Exit
    Exit = auto()
    
    # Empty tiles are buildable
    Empty = auto()
    
    # Normal Tower
    Normal0 = auto()
    
    # Cannon Tower
    Cannon0 = auto()
