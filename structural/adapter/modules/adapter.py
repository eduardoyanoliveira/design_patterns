from dataclasses import dataclass
from modules.hash_token import HashToken

@dataclass
class HashTokenAdapter:
    
    @classmethod
    def get_token(cls) -> str:
        return HashToken.generate_token()
    
    @classmethod
    def verify(cls, token: str) -> bool:
        return HashToken.validate(token)