from typing import Protocol


class IInvoiceState(Protocol):
    
    def pending(self) -> None: 
        ...
    
    def emit(self) -> None: 
        ...
    
    def cancel(self) -> None:
        ...