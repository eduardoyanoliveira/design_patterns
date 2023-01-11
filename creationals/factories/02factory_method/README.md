# Factory Method

### Type: Creational

### Prerequisites:

1. Understanding of Simple Factory. \
[Learn about Simple Factory](https://github.com/eduardoyanoliveira/design_patterns/blob/master/creationals/factories/01simple_factory/README.md)

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

```py
# Abstract Class
class Discount(ABC):
    
    @abstractmethod
    def calc(self, price: float, amount: float, product_qty : int = 0) -> float:
        raise NotImplementedError()

```

#### Concrete Classes

2. Creates the three discount types classes:

    1. ValueDiscount

    ```py
    class ValueDiscount(Discount):
    
    
    def calc(self, price: float, amount: float, product_qty: int = 0) -> float:
        """subtract the amount of discount from the price

        Returns:
            float: price after discount has been applied
        """

        if amount > price:
            raise ValueError('The amount of discount cant not be greater than price')  
        
        return price - amount
    ```

    2. ProgressiveValueDiscount

    ```py
    class ProgressiveValueDiscount(Discount):
    
    
    def calc(self, price: float, amount: float, product_qty: int = 0) -> float:
        """calculates the discount based on the product quantity.

        Returns:
            float: the price with the calculated discount
        """
       
        if amount > price:
            raise ValueError('The amount of discount can not be greater than price')
        
        
        # base to divide the product_qty
        base = 10

        # percentage to be added to the discount value
        factor = (product_qty / base) / 10
        
        # only calculates the percentage of the value if the factor is greater than zero
        if factor <= 0:
            return price
        
        # discount is equal the amount of discount plus a percentage if the product_qty is greater or equal to 10
        discount = ( amount + (amount * factor) )
        
        # limits the max amount of discount to be half of the product price
        if discount > (price / 2):
            discount = (price / 2)
        
        # applies the discount
        price -= discount
        
        return price

    ```


    3. PercentageDiscount

    ```py
    class PercentageDiscount(Discount):


    def calc(self, price: float, amount: float, product_qty: int = 0) -> float:
        """The amount is a percentage of the price to be applied as discount

        Returns:
            float: price after discount has been applied
        """

        if amount <= 0 or amount > 1:
            raise ValueError('Amount must be greater than 0 and less or equal than 1') 
        
        price += price * amount
        return price
    
    ```

### Abstract Factory Class

3. Creates the abstract factory class with a get_discount abstract method and a list_discount methods.

```py
class DiscountBaseFactory(ABC):
    
    def __init__(self, discount_types : dict) -> None:
        self.discount_types = discount_types
    
    @abstractmethod
    def get_discount(self, discount_type : str) -> Discount:
        raise NotImplementedError()
    
    def list_discounts(self):

        for discount in [*self.discount_types.keys()]:
            if(discount != None):
                print(discount)

```

### Concrete Factory classes

4. Creates two different implementations of the factory class, one with the Brazilian discount types and another for the american ones.  

```py
class BrazilianDiscountFactory(DiscountBaseFactory):
    
    def __init__(self) -> None:
        super().__init__({
        'value_discount': ValueDiscount,
        'percentage_discount': PercentageDiscount
    })
    
    def get_discount(cls, discount_type: str) -> Discount:
        return cls.discount_types[discount_type]()
    


class AmericanDiscountFactory(DiscountBaseFactory):
    
    def __init__(self) -> None:
        super().__init__({
            'progressive_discount': ProgressiveValueDiscount,
        })
    
    def get_discount(cls, discount_type: str) -> Discount:
        return cls.discount_types[discount_type]()

```

#### The Program

1. Asks the customer where is he(she) from.
2. Depending on the customer location creates a new factory (Either Brazilian or American)
3. Anounces the promotion and asks the customer to choose the type of discount. Listing only the available discounts for the customer's location.
4. Applies the choosen discount to the customer's order.

```py
if __name__ == '__main__':
    
    
    factories = {
        'b': BrazilianDiscountFactory,
        'a': AmericanDiscountFactory
    }
    
    country = input('Where are you from? (a) USA, (b) Brazil: ')
    
    if country != 'a' and country != 'b':
        raise ValueError('Please enter a valid country')
    
    factory = factories[country]()
    
    order_products = 23
    order_total = 1000
    
    print('Congrats, you are the 100th customer to buy this year!')
    print('You can choose the type of discount to be applied in your order. Here is the option(s)')
    print(factory.list_discounts())
    
    choosen_discount = input('Pick one of the above discount types: ')
    discount = factory.get_discount(choosen_discount)
    total_w_discount = discount.calcb
    (order_total, 30, order_products)
    
    print(f'Your order total is {total_w_discount}')
    
```

### Notes:

* Using the factory method, if necessary adding a new discount type for a subsidiary, it's only necessary to add it to the subsidiary's concrete factory class.

* If a new subsidiary is created in another country is only necessary to create a new concrete factory class to handle this subsidiary's discount types.
