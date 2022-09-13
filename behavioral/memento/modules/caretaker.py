from dataclasses import dataclass, field
from typing import List

from modules.memento import IMemento
from modules.originator import Beast

@dataclass
class BeastCaretaker:
    
    __beast: Beast 
    
    __mementos : List[IMemento] = field(default_factory=list)
    
    def backup(self) -> None:
        
        print('Creating a new Backup')
        
        memento = self.__beast.save()
        self.__mementos.append(memento)
   
   
    def undo(self) -> None:
        
        memento = self.__mementos.pop()
        
        if not memento:
            print('No backup found')
            return
        
        self.__beast.restore(memento)
        print(f'Backup {memento.get_name} restored')