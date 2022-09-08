from __future__ import annotations
from abc import ABC
from dataclasses import dataclass, field
from modules.program_classes import UserMessageRequest


@dataclass
class AbstractAccessHandler(ABC):
    
    _next: AbstractAccessHandler = field(init=False)
    
    def setNextHandler(self, handler: AbstractAccessHandler) -> AbstractAccessHandler:
        self._next = handler
    
    def handle(self, user_message: UserMessageRequest) -> UserMessageRequest:
        
        if self._next : return  self._next.handle(user_message)
        return user_message
        
        

    