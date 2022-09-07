from dataclasses import dataclass
from modules.abstract_context import AbstractInvoice
from modules.states import PendingState

@dataclass
class Invoice(AbstractInvoice):
    
    def __post_init__(self) -> None:
        self.state = PendingState(self)
    
    def pending(self) -> None:
        self.state.pending()
        print(f'Current state: {self.state.__class__.__name__}')
        print()
    
    def emit(self) -> None:
        self.state.emit()
        print(f'Current state: {self.state.__class__.__name__}')
        print()
        
    def cancel(self) -> None:
        self.state.cancel()
        print(f'Current state: {self.state.__class__.__name__}')
        print()
