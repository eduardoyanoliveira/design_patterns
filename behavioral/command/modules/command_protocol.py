from dataclasses import dataclass
from typing import Protocol


@dataclass
class ICommand(Protocol):
    
    def execute(self) -> None: pass
    
    def undo(self) -> None: pass
    
    def redo(self) -> None: pass
