from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class OrderTemplate(ABC):
    
    product_amount : float
    avg_price: float
    destination_dist : float
    customer_name: str
    
    @abstractmethod
    def calc_fee(self) -> float: pass
    
    @abstractmethod
    def calc_discount(self) -> float: pass
    
    def calc_total(self) -> float:
        
        fee = self.calc_fee()
        discount = self.calc_discount()
        
        total = self.avg_price * self.product_amount + fee - discount
        return total


@dataclass
class EcommerceOrder(OrderTemplate):
    
    def calc_fee(self) -> float:
        if self.product_amount > 5:
            factor =  (self.product_amount / 5) / 50
            base_total = self.product_amount * self.avg_price
            
            return base_total * factor 
        
        return 0
    
    def calc_discount(self) -> float:
        base_total = self.avg_price + self.product_amount
        return base_total * 0.1
    

@dataclass
class StoreOrder(OrderTemplate):
    
    def calc_fee(self) -> float:
       return self.destination_dist * 0.1
    
    def calc_discount(self) -> float:
        base_total = self.avg_price + self.product_amount
        
        if self.product_amount > 10:
            return base_total * 0.2
        
        return base_total * 0.05


if __name__ == '__main__':
    
    ecommerce_order = EcommerceOrder(12, 25, 500, 'Beth')
    print(ecommerce_order.customer_name, ecommerce_order.calc_total())
    
    store_order = StoreOrder(20, 7, 40, 'John')
    print(store_order.customer_name, store_order.calc_total())