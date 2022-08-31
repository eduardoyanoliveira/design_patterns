
from abc import ABC, abstractmethod
from dataclasses import dataclass


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