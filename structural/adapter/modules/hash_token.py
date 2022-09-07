from dataclasses import dataclass
from typing import ClassVar, List
import random


@dataclass
class HashToken:
    
    tokens : ClassVar[List[str]] = []
    
    @classmethod
    def generate_token(cls) -> str:
        token = random.getrandbits(128)
        
        cls.tokens.append(token)
        
        print('A Hash token was generated')
        
        return token
    
    @classmethod
    def validate(cls, token: str) -> bool:
        
        if token in cls.tokens:
            print('Hash Token is valid')
            return True
        
        print('Invalid Hash Token')
        return False
        