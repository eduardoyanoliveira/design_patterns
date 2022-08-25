# Singleton

### Type: Creational

## Introduction

Singleton design pattern is listed on the GOF book. It's main goal is to provide a class that can only be instantiated once or a class which every instance is the same.

## Advantages

1. Prevents that a class' instance changes during runtime causing problems on specific parts of the code that still need the old values.

## Our Python example

#### Introduction

Create a singleton in python is very simple, it's only need to create a class varible on the class that will be responsible store the instance and if an instance is already stored on this varible the class can not allow another one 
to be created. 


#### Create the class variable

1. On the singleton class create a class varible will be responsible store the instance and if an instance is already stored on this varible the class can not allow another one to be created. 


#### Def __new__

2. Use the  method __new__ to instantiate the class.Inside the method checks ff there is already an instance on the class variable, if so return this instance, else calls the method __new__ of the superclass to create a new instance.

### Obs

1. This class can not inherit from other class.
2. This class can not use the  method __init__.


#### The Program

1. Creates a new instance of the singleton and stored on the variable db_config
2. Uses the variable to add attributes to the instance.
3. Creates another instance of the class.
4. Access the attributes passed to the db_config "first instance" in the last instance.
5. The program is able to access all the attributes added to the first instance in the last one.

##### Program Notes

* In fact there is no two instances, when trying to instantiate the class the program will return the same object.


