from dataclasses import dataclass, field
from functools import reduce
from modules.component import ProductComponent
from typing import List

@dataclass
class ProductComposite(ProductComponent):
    
    __parents : List[ProductComponent] = field(default_factory=list)
    
    def add(self, *products: List[ProductComponent]) -> None:  
        for product in products:
            self.__parents.append(product)


    def remove(self, product: ProductComponent) -> None:
        self.__parents.remove(product)
        
        
    def get_quantity(self) -> int:  
        return reduce(lambda sum, parent: sum + parent.get_quantity(), self.__parents, 0)
