from abstract_product_classes import UiButton, UiInput


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
        
        
