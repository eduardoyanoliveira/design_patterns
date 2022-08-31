# Strategy

### Type: Behavioral

## Introduction

The strategy pattern (also known as the policy pattern) is a behavioral software design pattern that enables selecting an algorithm at runtime. Instead of implementing a single algorithm directly, code receives run-time instructions as to which in a family of algorithms to use.It is a very common way to use coposition and it use implements the Dependency Inversion Principle.


## Advantages

1. Provides an encapsulation of a set of algorithms that can be referenced by a common interface.

2. Follows the principle that code must not be based on implementations, but interfaces.

3. Helps on using Open closed Principle.

4. Uses Dependency injection, providing less code coupling. 

## Our Python example

#### Obs

Python does not have interfaces, to workaround it.It's possible to use abstract classes or Protocols.This example uses abstract classes. 

#### Introduction

The code is a part of a RPG game, where each warrior can use differents strategies of attack and defense. 

#### Abstract Classes

1. Create the abstract classes on the "interfaces" file with an attack abstract class and a defense abstract class.
Each has a static method called execute that does the action reciving either strength_points or defense_points. 

#### Concrete Classes

2. Create diferent concrete classes that implements one of the "interfaces":

* EmptyHandedAttackStrategy implments IAttackStrategy interface.
* SwordAttackStrategy implments IAttackStrategy interface.
* ArmsDefenseStrategy implements IDefenseStrategy interface.
* ShieldDefenseStrategy implements IDefenseStrategy interface.

#### Warrior Class

3. Create the warrior class that recives as arguments:

* name => warrior name.
* strength_points => used on the attack.
* defense_points => used on the defense.
* attack_strategy => an implementation of IAttackStrategy.
* defense_strategy => an implementation of IDefenseStrategy.

methods:

* attack => uses the reciving implementation of the IAttackStrategy interface to attack passing the strength_points.
* defense => uses the reciving implementation of the IDefenseStrategy interface to defend passing the defense_points.

#### The Program

1. Instatiate a poor_warrior that recives the EmptyHandedAttackStrategy and the ArmsDefenseStrategy.
2. Instantiate a royal_warrior that recives the SwordAttackStrategy and the ShieldDefenseStrategy.
3. Execute the functions attack and defend for both warriors

#### Use cases examples:
1. Authentication system that can recive differnt types of cryptography and decryptography implementations.
2. Shipping system.
3. Discount system.