# Simple Builder

### Type: Creational

### Disclaimer

This is not actually a design pattern, altough is the most common way that companies use the builder patter. I'm calling it of simple builder because, unlike the real builder pattern, this "pattern" does not have a builder interface and a director class.

## Introduction

The Builder design patter is meant to provide a second class that will be responsable to instatiate a complex product class that can be build in several ways, creating in each way  diferent form of the final object. In order to do so, this class must have methods that each will be responsible to add an attribute to the instance. 
The methods must return the instance because in that way the client code can chain the methods to build easly the object. The builder class must also have a build method that will be called at the end of the methods chain and will return the object.

## Our Python example

### Introduction

The program is a FPS game that let the player craft guns combining diferent parts.

#### Product Class

1. Create a dataclass for the gun that contains all the possible gun's parts.

#### Builder Class

2. Create a dataclass that will be the gun's builder class.

#### Chaining Methods

3. For each part that can be added to the gun, creates a method that will add it to the builder class instance. 
(In this case I'm only passing "true" to the parts that together creates the gun). Return the instance (self)

#### Build Method

4. Create a build method that instatiate a new Gun passing the Builder class instance attributes as the parameters to create it. Return the gun instance.


#### The Program

1. Creates a Ak-74 with scope and silincer using the Builder class and stores it on a variable 
2. Creates a Glock with infrared sight using the Builder class and stores it on a variable
3. Prints both variables on console.



