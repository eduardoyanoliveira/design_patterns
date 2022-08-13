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


# Product Concrete classes

# Buttons

# Windows

class WindowsConfirmButton(UiButton):
    
    def render() -> None:
        print('A Windows confirm button is rendered on screen')


class WindowsDeleteButton(UiButton):
    
    def render() -> None:
        print('A Windows delete button is rendered on screen')

# Mac

class MacConfirmButton(UiButton):
    
    def render() -> None:
        print('A Mac confirm button is rendered on screen')
                

class MacDeleteButton(UiButton):

    def render() -> None:
        print('A Mac delete is rendered on screen')

        
# Inputs

# Windows

class WindowsTextInput(UiInput):

    def render() -> None:
        print('A Windows text input is rendered on screen')


class WindowsNumberInput(UiInput):
    
    def render() -> None:
        print('A Windows number input is rendered on screen')

# Mac        

class MacTextInput(UiInput):
    
    def render() -> None:
        print('A Mac input is rendered on screen')


class MacNumberInput(UiInput):

    def render() -> None:
        print('A Mac number is rendered on screen')
        
        

# Abstract Factory

class AbstractFormFactory(ABC):
    
    @staticmethod
    @abstractmethod
    def get_confirm_button() -> UiButton:
        raise NotImplementedError
    
    @staticmethod
    @abstractmethod
    def get_delete_button() -> UiButton:
        raise NotImplementedError
    
    
    @staticmethod
    @abstractmethod
    def get_text_input() -> UiInput:
        raise NotImplementedError
    
    @staticmethod
    @abstractmethod
    def get_number_input() -> UiInput:
        raise NotImplementedError
    

# Concrete Factory Classes


class WindowsFormFactory(AbstractFormFactory):
    
    @staticmethod
    def get_confirm_button() -> UiButton:
        return WindowsConfirmButton
    
    @staticmethod
    def get_delete_button() -> UiButton:
        return WindowsDeleteButton
    
    @staticmethod
    def get_text_input() -> UiInput:
        return WindowsTextInput

    @staticmethod
    def get_number_input() -> UiInput:
        return WindowsNumberInput


class MacFormFactory(AbstractFormFactory):
    
    @staticmethod
    def get_confirm_button() -> UiButton:
        return MacConfirmButton
    
    @staticmethod
    def get_delete_button() -> UiButton:
        return MacDeleteButton
    
    @staticmethod
    def get_text_input() -> UiInput:
        return MacTextInput

    @staticmethod
    def get_number_input() -> UiInput:
        return MacNumberInput
    

# Main Program

if __name__ == '__main__':
    import platform
    
    # list the avalible concrete factories
    form_factories = {
        'Windows': WindowsFormFactory,
        'MacOs': MacFormFactory
    }
    
    # Gets the form_factory by the OS which the program is running 
    form_factory = form_factories[platform.system()]
    

    confirm_button = form_factory.get_confirm_button()
    delete_button = form_factory.get_delete_button()
    
    number_input = form_factory.get_number_input()
    text_input = form_factory.get_text_input()
    
    confirm_button.render()
    delete_button.render()
    
    text_input.render()
    number_input.render()