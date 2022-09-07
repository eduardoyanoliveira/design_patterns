from dataclasses import dataclass
from typing import ClassVar, List
import uuid

@dataclass
class JwtToken:
    
    tokens : ClassVar[List[str]] = []
    
    @classmethod
    def get_token(cls) -> str:
        token = uuid.uuid4()
        
        cls.tokens.append(token)
        
        print('A Hash token was generated')
        
        return token
    
    @classmethod
    def verify(cls, token: str) -> bool:
        
        if token in cls.tokens:
            print('Token is valid')
            return True
        
        print('Invalid Token')
        return False
        