# Bridge

### Type: Structural

## Introduction

&nbsp;The bridge pattern is a design pattern used in software engineering that is meant to "decouple an abstraction from its implementation so that the two can vary independently".<br>
&nbsp;This pattern is often confused with the Adapter pattern, both have similar implementations and meant to provide a common interface to distint classes.But while the Adapter pattern is commonly used to solve compatibility problems on an existing code.The Bridge pattern is used when the software engenier knows that a common interface approach will be necessary.<br>
&nbsp; The implementation of this pattern consists in one abstraction that uses composition to relate with another abstraction ( the implementor ). When this pattern is adopeted the sets of implementations of two different abstraction can interchangely combined. When a new concrete implementor is created for example, there is no need to create a new abstraction.   

## Advantages

1. Avoid a cartesian product with the two abstractions.

2. Less refactoring in the future as the number of classes won’t increase as much.

3. Both sides of abstraction and implementation can be developed independently.

4. Single Responsibility Principle: Updating one component won’t affect others.

5. Apllies the Interface Segregation Principle (ISP).

## Disadvantages

1. Add more complexity to the code.

## Pattern Diagram
```mermaid
classDiagram
    class Abstraction {
        &lt;&lt;abstract&gt;&gt;
    }
    RefinedAbstraction1 --|&gt; Abstraction
    RefinedAbstraction2 --|&gt; Abstraction
    class Implementation {
        &lt;&lt;abstract&gt;&gt;
        +implementation()
    }
    Abstraction o-- Implementation : uses
    Implementation &lt;|-- ConcreteImplementation1
    Implementation &lt;|-- ConcreteImplementation2
    ConcreteImplementation1: +implementation()
    ConcreteImplementation2: +implementation()

```
## Our Python example

#### Obs

* Python does not have interfaces, to workaround it.It's possible to use abstract classes or Protocols.This example uses both. 

### Introduction

The program simulates the relationship between a wearable divice and a an application. It is common to see in nowdays wearable devices that are linked to a mobile app, where the app shows the current status of the divice, some statistics, reports, etc.

#### Implementor Protocol

1. Create the Implementor for the Weareable divice. (implementor.py) 

```
from typing import List, Protocol


class WearableDeviceImplementor(Protocol):
    
    def get_battery_charge(self) -> int: pass
    
    def get_notifications(self) -> List: pass


```

#### Program Classes

2. These classes are the normal classes that the program would have before the implementation of the pattern. They are the business logic classes and each will have a concrete_implementor that will manipulate the program class to make it match the abstraction. (program_classes.py)

```
from dataclasses import dataclass, field
from typing import List

@dataclass
class SmartBand:
    
    battery_percentage: int
    notifications: List[str] = field(default_factory=list)
    


@dataclass
class SmartWatch:
    
    battery: int
    messages: List[str] = field(default_factory=list)
    
    

```

#### Concrete Implementors

3. Create the concrete implementors for each program class.( concrete_implementors.py )

```
from typing import List
from modules.program_classes import SmartBand, SmartWatch
from dataclasses import dataclass


@dataclass
class SmartBandImplementor:
    
    smart_band: SmartBand
    
    def get_battery_charge(self) -> int: 
        return self.smart_band.battery_percentage
    
    def get_notifications(self) -> List:
        return self.smart_band.notifications
    


@dataclass
class SmartWatchImplementor:
    
    smart_watch: SmartWatch
    
    def get_battery_charge(self) -> int: 
        return self.smart_watch.battery
    
    def get_notifications(self) -> List:
        return self.smart_watch.messages

```

#### Absctraction

4. The Abstraction consumes one concrete implementor. In this case, the abstraction represents a Display screen of an application that cosumes the data from the wearable device and prints a report.

```
from abc import ABC
from dataclasses import dataclass
from modules.implementor import WearableDeviceImplementor


@dataclass
class DisplayScreenAbstraction(ABC):
    
    wearable_implementor: WearableDeviceImplementor


```

### The Refined Abstractions

5. In order to examplify that the Bridge pattern can wor with multiple implementations of both the abstraction and the implementor, here is created two classes that inherits from the abstraction. One represetns a mobile display screen and other a desktop display screen, and each provides a different report.

```
from dataclasses import dataclass
from modules.abstraction import DisplayScreenAbstraction


@dataclass
class DesktopDisplayScreen(DisplayScreenAbstraction):

    def display_wareable_status(self) -> None:
        
        display_string = f'This are the unread messages: \n'
        
        for message in self.wearable_implementor.get_notifications():
            
            display_string += f'{message} \n'
        
        display_string += f'The wareable device battery is current {self.wearable_implementor.get_battery_charge()}%'
        
        print(display_string)



@dataclass
class AppDisplayScreen(DisplayScreenAbstraction):

    def display_wareable_status(self) -> None:
        
        display_string = f'You have {len(self.wearable_implementor.get_notifications())} unread messages: \n'
        
        display_string += f'The device battery is on {self.wearable_implementor.get_battery_charge()}%'
            
        print(display_string)
         

```

#### The Program

The program show two different combinations:<br>
1. A smartband (Wearable divice program_class) is created among with its specif implementor. Then a new instance of the mobile_screen (refined abstraction) is instatiated reciving the implementor. after that the method that displays the report is called, and the report is printed on the console.

2. The second part of the program does pretty much the same thing of the first, although this time using a smartwatch (Wearable divice program_class) device and desktop display screen (refined abstraction).

* Obs:

It is possible to interchange the abstractions instances and the concrete implementors.For example:<br>
The SmartBand device can be display on the desktop display and the SmartWatch on the app display.


```
from modules.program_classes import SmartBand, SmartWatch
from modules.concrete_implementors import SmartBandImplementor, SmartWatchImplementor
from modules.refined_abstractions import AppDisplayScreen, DesktopDisplayScreen

if __name__ == '__main__':
    
    mi_band =  SmartBand(54, ['Test notification', 'Yan is implementing the bridge pattern'])
    
    mi_band_implementor = SmartBandImplementor(mi_band)
    
    app_display_screen = AppDisplayScreen(mi_band_implementor)
    
    app_display_screen.display_wareable_status()
    
    print()
    print('#####################################')
    print()
    
    apple_watch =  SmartWatch(90, ['new notification', 'Yan, we are looking foward to our meeting with the CEO'])
    
    apple_watch_implementor = SmartWatchImplementor(apple_watch)
    
    desktop_display_screen = DesktopDisplayScreen(apple_watch_implementor)
    
    desktop_display_screen.display_wareable_status()
    
```
