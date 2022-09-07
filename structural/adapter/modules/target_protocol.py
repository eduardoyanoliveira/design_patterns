from typing import Protocol

class ITokenService(Protocol):
    
    def get_token(self) -> str: pass
    
    def verify(self) -> bool: pass