from dataclasses import dataclass
from datetime import datetime
import uuid

from modules.memento import IMemento
from modules.concrete_memento import BeastMemento


@dataclass
class Beast:
    
    __state: str
    
    @property
    def state(self) -> str:
        return self.__state
    
    def transform(self, new_state: str) -> str:
        self.__state = new_state
        
    def save(self) -> IMemento:
        return BeastMemento(uuid.uuid4(), datetime.now(), self.state)
    
    def restore(self, beast_memento: BeastMemento) -> None:
        self.__state = beast_memento.state
        
    
    def __str__(self) -> str:
        return self.state
        
    
    
    