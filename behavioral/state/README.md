# State

### Type: Behavioral

## Introduction

The state pattern is a behavioral software design pattern that allows an object to alter its behavior when its internal state changes. This pattern is close to the concept of finite-state machines. The state pattern can be interpreted as a strategy pattern, which is able to switch a strategy through invocations of methods defined in the pattern's interface.<br>
The state pattern is used in computer programming to encapsulate varying behavior for the same object, based on its internal state. This can be a cleaner way for an object to change its behavior at runtime without resorting to conditional statements and thus improve maintainability.<br>
The class that has a state behavior is called context and recives the state object as an attribute. Whenever a state behavior or a method that can change the context state is called, the context class delegates the execution of the method to the state object.<br>
In order to create both the context and state a state interface is create to describe all the state methods that both the context and states will have.


## Advantages

1. Implementing state-specific behavior directly within a class is inflexible because it commits the class to a particular behavior and makes it impossible to add a new state or change the behavior of an existing state later, independently from the class, without changing the class.

2. Defines separate (state) objects that encapsulate state-specific behavior for each state. That is, define an interface (state) for performing state-specific behavior, and define classes that implement the interface for each state.

3. implements polymorphic behavior.

## Disadvantages

1. The Context and State objects are circular related, and because of that. there is an increasing in coupling.

## Our Python example

* Python does not have interfaces, to workaround it.It's possible to use abstract classes or Protocols.This example uses Protocols. 

### Introduction

The program simulates an invoice system where the invoice can be emitted or canceled.(the invoice is created as pending).

* When the invoice is pending, it can be emitted or canceled.
* When the invoice is emitted, it can only be canceled.
* When the invoice is canceled, it can not be changed.


#### State Protocol

1. Create the protocol that every concrete class will follow. (state_protocol.py)

```
from typing import Protocol


class IInvoiceState(Protocol):
    
    def pending(self) -> None: 
        ...
    
    def emit(self) -> None: 
        ...
    
    def cancel(self) -> None:
        ...

```

#### Abstract Context (Optional)

2. Create an abstract context class in order to avoid circular imports on python files.  (abstract_context.py)

```
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

```

#### Concrete Context

3. Create the context that will inhiret from the abstract context and delegate the methods to the state classes.

```
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

```

#### The States

4. Create a file with every state that the context needs. (states.py)

```
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

```

#### The Program

1. Instantiate an invoice.
2. Emits the invoice.
3. Cancel the invoice.


```
from modules.context import Invoice

    
if __name__ == '__main__':
    invoice = Invoice()
    
    invoice.emit()
    print('Emit date:',invoice.emit_date)
    print('#######')
    
    invoice.pending()
    print('#####')
    
    invoice.cancel()
    print('Cancelation date:',invoice.emit_date)

```

#### Obs:

In this case the context class works also as a Façade class encapsulating all the complex implementations from the client code.
