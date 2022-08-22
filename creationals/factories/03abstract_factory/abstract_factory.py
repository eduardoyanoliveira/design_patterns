from abc import ABC, abstractmethod
from abstract_product_classes import UiButton, UiInput
from concrete_product_classes import (
    WindowsConfirmButton,
    WindowsDeleteButton,
    WindowsNumberInput,
    WindowsTextInput,
    MacConfirmButton,
    MacDeleteButton,
    MacNumberInput,
    MacTextInput
)

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