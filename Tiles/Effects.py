from enum import Enum, unique, auto

class Effects(Enum):
    # NoEffect does nothing
    NoEffect = auto()
    
    # Single Target Damage
    SingleTarget = auto()
    
    # Splash Damage
    SplashDamage = auto()
