from interfaces import IAttackStrategy, IDefenseStrategy

# Concrete implementations of the interface

# Concrete Attacks

class EmptyHandedAttackStrategy(IAttackStrategy):
    
    @staticmethod
    def execute(strength_points: float) -> None:
        power = strength_points + (strength_points / 3)
        print(f'Attacked with the arms, total power of {power}')


class SwordAttackStrategy(IAttackStrategy):
    
    @staticmethod
    def execute(strength_points: float) -> None:
        power = strength_points + (strength_points * 1.35)
        print(f'Attacked with the sword, total power of {power}')
    


class ArmsDefenseStrategy(IDefenseStrategy):
    
    @staticmethod
    def execute(defense_points: float) -> None:
        print(f'Defended {defense_points} points of the attack, using the arms')
        

class ShieldDefenseStrategy(IDefenseStrategy):
    
    @staticmethod
    def execute(defense_points: float) -> None:
        print(f'Defended {defense_points * 2 } points of the attack, using a shield')