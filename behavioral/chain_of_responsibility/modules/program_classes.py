from dataclasses import dataclass, field
from enum import Enum


class Role(Enum):
    
    USER = 0
    SUPER = 1
    

@dataclass
class User:
    
    username: str
    role: Role
    token: str = field(default_factory=str)


@dataclass
class UserMessageRequest:
    user : User
    message: str
    denied: bool = False
    