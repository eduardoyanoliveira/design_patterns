# Template Method

### Type: Behavioral

## Introduction

In object-oriented programming, the template method is one of the behavioral design patterns identified by Gamma et al.in the book Design Patterns. The template method is a method in a superclass, usually an abstract superclass, and defines the skeleton of an operation in terms of a number of high-level steps. These steps are themselves implemented by additional helper methods in the same class as the template method.

The helper methods may be either abstract methods, in which case subclasses are required to provide concrete implementations, or hook methods, which have empty bodies in the superclass. Subclasses can (but are not required to) customize the operation by overriding the hook methods. The intent of the template method is to define the overall structure of the operation, while allowing subclasses to refine, or redefine, certain steps.

## Advantages

1. Implements the Inversion of control principle.

2. Provide a base to generate alikely algorithms

## Disadvantages

1. Add more complexity to the code.

## Our Python example


### Introduction

The program is an order sysyem where the order total is calculated in different ways depending on the store and the order attributes.


#### Class Order Template

1. Create a template class that has the abstract methods calc_fee, calc_discount and has a final method calc_total that use the to abstract methods to calculate the order total.
The class needs to recive the average price per product on the order; the product amount; and the distance to the customer's house.

```
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

```

#### Ecommerce Order

2. Create a class Ecommerce Order that inherits from the Order Template and calcs the fee based on the product amount and applies always 1 per cent of discount

```
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

```

#### Store Order

3. Create a class Store Order that inherits from the Order Template and adds 10 cents of fee by KM of distance to the destination and applies discount by the product amount.


```
@dataclass
class StoreOrder(OrderTemplate):
    
    def calc_fee(self) -> float:
       return self.destination_dist * 0.1
    
    def calc_discount(self) -> float:
        base_total = self.avg_price + self.product_amount
        
        if self.product_amount > 10:
            return base_total * 0.2
        
        return base_total * 0.05

```


#### The Program

1. Instantiate two orders, on from Ecommerce and other from Store.
2. Prints the total of each order.

```
if __name__ == '__main__':
    
    ecommerce_order = EcommerceOrder(12, 25, 500, 'Beth')
    print(ecommerce_order.customer_name, ecommerce_order.calc_total())
    
    store_order = StoreOrder(20, 7, 40, 'John')
    print(store_order.customer_name, store_order.calc_total())

```
