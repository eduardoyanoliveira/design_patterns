# Simple Factory

### type: Creational

### Disclaimer:

Simple factory is not actually considere a design pattern, but it's a really good base for understanding two design patterns: "Factory Method" and "Abstract Factory".

## Introduction

Simple Factory is based on a estructure where an abstract class or interface, called the "Product Class" is implemented by other classes, "The Concrete Classes", usally using polymorphism. In this case the goal is to not share the implementations to the client code, and instead  provide a classe that will be responsible to instantiate one of the concrete classes.This class is the factory class.

## Advantages

1. Creates a system with less coupling between the classes, because the client code is not responsible to instatiate the concrete classes.

2. Make easier to add new concrete classes because the client code do not uses the implemantation of the abstract class, but only an instance.

## Our Python example

#### Base

1. Create class Foe which has health points (int) and can be elemental.

#### Abstract Class

2. Class Spell that has power (int) of the magic and an abstract method cast that recives a foe.

#### Concrete Classes

3. Class Striker a spell that when is casted inflicts the power points of damage in the foe, and it can be multiplied by 1.5 if the foe is elemental. Class Flames  that has the power points multiplied by 3 if the foe is not elemental and divided by 2 if it's.

### Enum and Factory Class

4. Creates an enum with all the concrete classes and the factory class which has only an static method get_spell who recives one of the enum options and returns the class instance according to it.

### The Program

creates a elemental Foe and a non-elemental one, then randomly creates a spell, then randomly pick a Foe as well to be atacked.
After the atack the program prints the two foes with their current health points 