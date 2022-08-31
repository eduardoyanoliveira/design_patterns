from dataclasses import dataclass
from datetime import datetime
from typing import List

from interfaces import IObservable, IObserver
    
    
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


if __name__ == '__main__':
    
    rocket = RocketShip('kepler')
    
    scientist = NasaScientist('Steven Shulz', rocket)
    reporter = NewsReporter('Emmily Gray', 'The Washington Post', rocket)
    
    rocket.add_observer(scientist)
    rocket.add_observer(reporter)
    
    rocket.has_launched = True
    
    