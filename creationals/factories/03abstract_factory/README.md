# Abstract Factory

### Type: Creational

### Prerequisites:

1. Understanding of Simple Factory and Factory Method. \
[Learn about Simple Factory](https://github.com/eduardoyanoliveira/design_patterns/blob/master/creationals/factories/01simple_factory/README.md) \
[Learn about Factory Method](https://github.com/eduardoyanoliveira/design_patterns/blob/master/creationals/factories/02factory_method/README.md)

## Introduction

The abstract factory pattern provides a way to encapsulate a group of individual factories that have a common theme without specifying their concrete classes. In normal usage, the client software creates a concrete implementation of the abstract factory and then uses the generic interface of the factory to create the concrete objects that are part of the theme. The client does not know (or care) which concrete objects it gets from each of these internal factories, since it uses only the generic interfaces of their products.This pattern separates the details of implementation of a set of objects from their general usage and relies on object composition, as object creation is implemented in methods exposed in the factory interface. 


## Advantages

1. Provides an encapsulation of a set of related objects. (They doesn't necessary need to be implementations of the same abstract product class).

## Our Python example

#### Introduction

The Nebula tech company is currently working on a helpdesk desktop app. The CTO informs the development department that this app needs to runs on both Windows and Linux platforms.You are part of the UI developement team which is responsible to creates and provides all the UI components that will be used by both windows and mac development teams.

### Problem

After creating all the UI components you notice that it's not safe to allow the teams to access the concrete classes, and to solve that you decide to use the factory method. Although it looked like a good idea at the beginning, a big error occured on the final UI template because the Mac team has used a Windows input on their version of the app.This problem happend beacuse the factory method was provinding all of the "product concrete classes" to the client code.\
After hours of thinking about the problem you decide to ask a collegue,she says the a good way tho solve the problem was using the Abstract Factory Desgin Pattern. She told you the following steps:

#### Factory Abstract Class

1. Transform the current factory class into an abstract factory class which will hava an abstract method to get each UI component. \
    e.g: get_confirm_button, get_delete_button, etc.  


#### Concrete Factory Classes

2. Creates an implemantation of the abstract factory class for each Windows and Mac. Each of the factory will return the right implementation of the abstract product class.\
    e.g: If the get_confirm_button from the Windows Factory is called, it returns a Windows Confirm Button.


#### The Program

1. Checks the OS which the code is running and returns the correct factory.
2. Each of the UI components is stored on a variable.
3. The Program calls the render methods of the UI components.

### Notes:

* Although it is usual to see books and articles that advises the use of the Abstract Factory to UI components like this example. This Design Pattern can be used in different use cases, but be careful to not overdoing it.\

#### Use cases examples:
1. File system.
2. Cryptography and decryptography system.
3. Theme system. (That is as well part of the UI).
