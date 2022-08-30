from dataclasses import dataclass
from concrete_classes import ArmsDefenseStrategy, EmptyHandedAttackStrategy, ShieldDefenseStrategy, SwordAttackStrategy

from interfaces import IAttackStrategy, IDefenseStrategy



# Client

@dataclass
class Warrior:
    
    name: str
    strength_points: float
    defense_points: float
    attack_strategy: IAttackStrategy
    defense_strategy: IDefenseStrategy
    
    def attack(self) -> None:
        self.attack_strategy.execute(self.strength_points)
        
    def defend(self) -> None:
        self.defense_strategy.execute(self.defense_points)
    

# Program

if __name__ == '__main__':
    
    poor_warrior = Warrior('vagabond', 75, 40, EmptyHandedAttackStrategy, ArmsDefenseStrategy)
    royal_warrior = Warrior('Lancelot', 120, 80, SwordAttackStrategy, ShieldDefenseStrategy)
    
    poor_warrior.attack()
    royal_warrior.defend()
    
    royal_warrior.attack()
    poor_warrior.defend()
    


    