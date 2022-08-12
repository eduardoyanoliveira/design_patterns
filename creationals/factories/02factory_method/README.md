# Factory Method

### Type: Creational

### Prerequisites:

1. Understanding of Simple Factory.
[Learn about](https://github.com/eduardoyanoliveira/design_patterns/blob/master/creationals/factories/01simple_factory/README.md)

## Introduction

Factory Method is a design pattern listed on the GOF Design Pattern book. The base to create a factory method is using
a simple factory.The biggest diference is that when using a factory method, the factory class is abstract, providing a new abstraction layer that allows the creation of different factories on different use cases.
Notice that here there are an abstract factory and concrete factories.

## Advantages

1. Makes the class instance creation more flexable.

2. Avoids the unnecessary implementations of the abstract class.

## Our Python example


#### Introduction

Imagine an online shop that sells products both for Brazil and USA. The CEO of the company wants to make a promotion on this year. He wants to give the 100th customer to make an order on this year a cupom that allows the customer to pick the
type of discount that he(she) wants to be applied on his(hers) order.
There is only a small problem here. By the company policies eachcountry has a certain variaty of discount types, and some discount types can be used only in one country.
    

#### Abstract Class

1. Creates the discount abstract class.

#### Concrete Classes

3. Creates the three discount types classes:
    1. ValueDiscount
    2. PercentageDiscount
    3. ProgressiveValueDiscount

### Abstract Factory Class

4. Creates the abstract factory class with a get_discount abstract method and a list_discount methods

### Concrete Factory classes

5. Creates two different implementations of the factory class, one with the Brazilian discount types and another for the american ones.  

### The Program

1. Asks the customer where is he(she) from.
2. Depending on the customer location creates a new factory (Either Brazilian or American)
3. Anounces the promotion and asks the customer to choose the type of discount. Listing only the available discounts for the customer's location.
4. Applies the choosen discount to the customer's order.

### Notes:

    * Using the factory method, if necessary adding a new discount type for a subsidiary, it's only necessary to add it to the subsidiary's concrete factory class.

    * If a new subsidiary is created in another country is only necessary to create a new concrete factory class to handle this subsidiary's discount types.