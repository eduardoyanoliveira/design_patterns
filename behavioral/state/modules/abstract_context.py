from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from modules.state_protocol import IInvoiceState

@dataclass
class AbstractInvoice(ABC):
    
    state: IInvoiceState = field(init=False)
    emit_date : datetime | None = None
    cancellation_date: datetime | None = None
    
    @abstractmethod
    def pending(self) -> None:pass
        
    @abstractmethod
    def emit(self) -> None: pass

    @abstractmethod    
    def cancel(self) -> None:pass
 