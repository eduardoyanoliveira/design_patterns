from abc import ABC, abstractmethod
from enum import Enum


class Foe:
    
    """An Enemy that can be atacked with a spell
    """
    
    def __init__(self, name: str, health: int, is_elemental: bool) -> None:
        self.name = name
        self.health = health
        self.is_elemental = is_elemental

    def __str__(self) -> str:
        return f'{self.name} is with {self.health} of health.'


class Spell(ABC):
    
    """A atack that is used in a Foe. 
    It can be stronger or weaker depends on the type of spell and the type of Foe
    """
    
    def __init__(self, power: int) -> None:
        self.power = power
    
    @abstractmethod
    def cast(self, foe: Foe) -> None:
        raise NotImplementedError()


class Striker(Spell):
    
    """A physical spell
    """
    
    def __init__(self) -> None:
        super().__init__(70)
        
    def cast(self, foe: Foe) -> None:
        
        if foe.is_elemental:
            self.power *= 1.5
        
        foe.health -= self.power
                 

class Flames(Spell):
    
    """An Elemental spell
    """
    
    def __init__(self) -> None:
        super().__init__(40)
    
    
    def cast(self, foe: Foe) -> None:
            
        if foe.is_elemental:
            self.power /= 2
        else:
            self.power *= 3
        
        foe.health -= self.power

class Spells(Enum):
    Flames = 'flames'
    Striker= 'striker'


class SpellFactory:
    
    @staticmethod
    def get_spell(spell_type: Spells) -> Spell:

        if(spell_type == Spells.Striker):
            return Striker()
        
        if(spell_type == Spells.Flames):
            return Flames()
        
        assert 0, 'Error'

# The program creates two types of Foe and randomly creates a spell, then randomly pick a Foe as well to be atacked
# After the atack the program prints the two foes with their current health points 
if __name__ == '__main__':
    
    from random import choice
    
    physical_foe = Foe(name='Orc', health=700, is_elemental=False)
    elemental_foe = Foe(name='Dark elf' ,health=300, is_elemental=True)
    
    spell = SpellFactory.get_spell(choice([s for s in Spells]))
    spell.cast(choice([physical_foe, elemental_foe]))
    
    print(physical_foe)
    print(elemental_foe)