from abc import ABC, abstractmethod

# Interfaces

# Attack Interface
class IAttackStrategy(ABC):
    
    @staticmethod
    @abstractmethod
    def execute(strength_points: float) -> None : pass
    
# Defend Interface
class IDefenseStrategy(ABC):
    
    @staticmethod
    @abstractmethod
    def execute(defense_points: float) -> None : pass