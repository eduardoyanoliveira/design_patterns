from dataclasses import dataclass, field
from typing import List

@dataclass
class SmartBand:
    
    battery_percentage: int
    notifications: List[str] = field(default_factory=list)
    


@dataclass
class SmartWatch:
    
    battery: int
    messages: List[str] = field(default_factory=list)
    
    