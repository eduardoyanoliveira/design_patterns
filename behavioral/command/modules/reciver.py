from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class Message:
    author: User
    text: str
    
    def __str__(self) -> str:
        return f'From: {self.author} => {self.text}'

@dataclass
class User:
    name: str
    messages: Optional(List[Message]) =  field(default_factory=list)
    followers : Optional(List[User]) =  field(default_factory=list)
    followings: Optional(List[User]) =  field(default_factory=list)

    def __str__(self) -> str:
        return self.name