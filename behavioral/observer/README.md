# Observer

### Type: Behavioral

## Introduction

The Observer pattern is a behavioral design pattern meant to provide information about changes in one object state to another object of another class. The pattern consists in two interfaces, one for the observable class and other to the observer class. To follow correctly this pattern the observable class must implements the three following methods:

* subscribe or add => Add a new object to the list of subscribers.
* unsubscribe or remove => Remove the object from the list.
* notify => Notify all the objects in the subscribers' list that the observable object has changed.

While the observer class must implements only a method called update that will be executed inside the notify method from observable class.

The Observer pattern is strongly used in event driven design, and it is also part of the backbone of the Node.js's EventEmitter.


## Advantages

1. Provides an easy way to deal with events on code.

2. If not correctly implemented, the Observer can add complexity and lead to inadvertent performance issues.

## Disadvantages

1. Add coupling between the observable and observer instances, once that the observer instance must aknowladge the observable instance attributes. (Normaly the observable instance is passed as attribute to the observer class on its instantiation).

2. Breaks the single responsibility principle if the class must implements the observable interface methods and it's own.(The Observable interface methods can be added on an abstract class to avoid this problem).


## Our Python example

#### Obs

* Python does not have interfaces, to workaround it.It's possible to use abstract classes or Protocols.This example uses abstract classes. 

* The GOF books strongly reccomend the use of getters and setters in the observable class attributes, in this way is possible to call the notify method on every setter.


#### Introduction

A rocket is about to be launched into a new space mission. As it is a really important event, both the NASA scientists and some journals want to keep on track of this event.


#### Abstract Classes

1. Create the abstract classes on the "interfaces" file. 

```
class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: pass


@dataclass
class IObservable(ABC):

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def notify_observers(self) -> None: pass

```

#### Concrete observable class

2. Create a rocket ship class that implements the IObservable interface and has a boolean attribute to hold the information if the rocket has been launched.

```
class RocketShip(IObservable):

    def __init__(self, name) -> None:
        self.name: str = name
        self.__has_launched : bool = False
        self.__observers : List[IObserver] = []
    
    
    @property
    def has_launched(self) -> bool:
        return self.__has_launched


    @has_launched.setter
    def has_launched(self, value : bool) -> None:
        self.__has_launched = value
        self.notify_observers()
        
        

    def add_observer(self, observer: IObserver) -> None:
        
        if observer not in self.__observers:
            self.__observers.append(observer)


    def remove_observer(self, observer: IObserver) -> None:

        if observer in self.observers:
            self.__observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self.__observers:
            observer.update()

```



#### Concrete observers classes

3. Create a class NasaScientist and one Reporter, both of them implement the IObserver interface:

```
@dataclass
class NasaScientist(IObserver):
    
    name: str
    rocket : RocketShip
    
    def update(self) -> None:
        if(self.rocket.has_launched == True):
            print(f"This is {self.name}. Inform that {self.rocket.name} has been launched.")


@dataclass
class NewsReporter(IObserver):
    
    name: str
    journal_name: str
    rocket : RocketShip
    
    def update(self) -> None:
        if(self.rocket.has_launched == True):
            print(
                f"This is {self.name} from the {self.journal_name} journal.", 
                f"We passed the last night on the Nasa station and we are finally able that the {self.rocket.name} rocketship",
                f"has been launched at {datetime.now()}. \n The launching was a success!."
            )

```

#### The Program

1. Instatiates a rocket, a scientist and a reporter.
2. Subscribes both the scientist and the reporter to the rocket.
3. Sets the attribute has_launched on the rocket to True.
4. When the attribute has_lauched change, it notifies all of the subscribers and each reacts with a different behavior.

```
if __name__ == '__main__':
    
    rocket = RocketShip('kepler')
    
    scientist = NasaScientist('Steven Shulz', rocket)
    reporter = NewsReporter('Emmily Gray', 'The Washington Post', rocket)
    
    rocket.add_observer(scientist)
    rocket.add_observer(reporter)
    
    rocket.has_launched = True

```
