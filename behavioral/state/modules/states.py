from dataclasses import dataclass
from datetime import datetime

from modules.abstract_context import AbstractInvoice


@dataclass
class PendingState:
    
    invoice: AbstractInvoice
    
    def pending(self) -> None:
        print(f'The invoice {self.invoice.id} is already pending')
    
    def emit(self) -> None:  
        print(f'Emitting the invoice')
        self.invoice.state = EmitState(self.invoice)
        self.invoice.emit_date = datetime.now()
        

    def cancel(self) -> None:
        print(f'The invoice has been canceled')
        self.invoice.cancellation_date = datetime.now()
        self.invoice.state = CancelState(self.invoice)

@dataclass
class CancelState:
    
    invoice: AbstractInvoice
    
    def pending(self) -> None:
        print(f'Invalid operation, The invoice is already canceled')
    
    def emit(self) -> None:  
        print(f'Invalid operation, The invoice is already canceled')

    def cancel(self) -> None:
       print(f'Invalid operation, The invoice is already canceled')


@dataclass
class EmitState:
    
    invoice: AbstractInvoice
    
    def pending(self) -> None:
        print(f'Invalid operation, The invoice is already emitted')
    
    def emit(self) -> None:  
        print(f'Invalid operation, The invoice is already emitted')
        

    def cancel(self) -> None:
        print(f'The invoice has been canceled')
        self.invoice.cancellation_date = datetime.now()
        self.invoice.state = CancelState(self.invoice)