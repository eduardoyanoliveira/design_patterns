# Singleton With Decorator

### Type: Creational

## Introduction

In Python is not possible to create a singleton in the same way that is presented on the GOF book, and most of the time that software engeniers try to create this patter on python is easy to spot some issues. For example, it is a common problem not to be able to use the __init__ function inside of a singleton class. A simple way to work around it is using a decorator. 


## Our Python example


#### Create the function decorator

1. Creates a function to use as a decorator. It must recive the class as a parameter, On it's body declare a varible initialized as an empty dictionary that will store the first instance of all classes that uses this decorator.

```
def singleton(this):
    
    instances = {}

```

#### Function create_instance

2. Inside teh decorator function create another function that will recive the values normaly passed on the class __init__ method ( for this use *args and **kwargs). Checks if the dictionary variable already has an instance of the class, if so return the instance, otherwise use the class passed as a parameter on the decorator to create a new instance with the *args and **kwargs. Returns the function that create the instance on the decorator function.

```
def singleton(this):
    
    instances = {}
    
    def create_instance(*args, **kwargs):
        if this not in instances:
            instances[this] = this(*args, **kwargs)
        
        return instances[this]
    
    return create_instance

```

#### The class

3. Decorate the class with the decorator funciton

```
@singleton
class DataBaseSettings:
    
    def __init__(self) -> None:
        print('__init__ function has been called')

```
### Obs

* Even if the class is called several times to instatiate a new object, it's __init__ methdo will be called only once.


#### The Program

1. Creates a new instance of the singleton and stored on the variable db_config
2. Uses the variable to add attributes to the instance.
3. Creates another instance of the class.
4. Access the attributes passed to the db_config "first instance" in the last instance.
5. The program is able to access all the attributes added to the first instance in the last one.

```
if __name__ == '__main__':
    
    db_config = DataBaseSettings()
    
    db_config.password = '12345678'
    
    new_db_config = DataBaseSettings()
    
    print(new_db_config.password)
    

```
