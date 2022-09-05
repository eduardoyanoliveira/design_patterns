from dataclasses import dataclass, field
from typing import List

from modules.command_protocol import ICommand


@dataclass
class Invoker:
    undo_stack : List[ICommand] = field(default_factory=list)
    redo_stack : List[ICommand] = field(default_factory=list)

    def execute(self, command: ICommand) -> None:
        command.execute()
        self.redo_stack.clear()
        self.undo_stack.append(command) 
    
    def undo(self) -> None:
        if not self.undo_stack:
            return
        
        command = self.undo_stack.pop()
        command.undo()
        self.redo_stack.append(command)
    
    def redo(self) -> None:
        if not self.redo_stack:
            return
        
        command = self.redo_stack.pop()
        command.redo()
        self.undo_stack.append(command)