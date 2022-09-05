from dataclasses import dataclass, field
from modules.command_protocol import ICommand


@dataclass
class Batch:
    commands: list[ICommand] = field(default_factory=list)

    def execute(self) -> None:
        completed_commands: list[ICommand] = []
        try:
            for command in self.commands:
                command.execute()
                completed_commands.append(command)
        except ValueError:
            for command in reversed(completed_commands):
                command.undo()
            raise

    def undo(self) -> None:
        for command in reversed(self.commands):
            command.undo()

    def redo(self) -> None:
        for command in self.commands:
            command.redo()