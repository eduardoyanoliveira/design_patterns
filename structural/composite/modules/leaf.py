from dataclasses import dataclass
from modules.component import ProductComponent

@dataclass
class ProductLeaf(ProductComponent):
    
    name: str
    quantity: int
    
    def get_quantity(self) -> int:
        return self.quantity