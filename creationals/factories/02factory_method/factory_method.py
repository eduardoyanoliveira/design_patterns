from abc import ABC, abstractmethod

# Abstract Class
class Discount(ABC):
    
    @abstractmethod
    def calc(self, price: float, amount: float, product_qty : int = 0) -> float:
        raise NotImplementedError()

# Concrete Classes

class ValueDiscount(Discount):
    
    
    def calc(self, price: float, amount: float, product_qty: int = 0) -> float:
        """subtract the amount of discount from the price

        Returns:
            float: price after discount has been applied
        """

        if amount > price:
            raise ValueError('The amount of discount cant not be greater than price')  
        
        return price - amount
    


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
    
    
# Abstract Factory

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
    

# Concrete Factories

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
    