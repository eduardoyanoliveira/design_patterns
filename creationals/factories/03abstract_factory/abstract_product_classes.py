from abc import ABC, abstractmethod

# Product abstract classes

class UiButton(ABC):
    """Represents an ui button that will be render on screen
    """
    @abstractmethod
    def render() -> None:
        raise NotImplementedError()
    

class UiInput(ABC):
    """Represents an ui input that will be render on screen
    """
    @abstractmethod
    def render() -> None:
        raise NotImplementedError()
