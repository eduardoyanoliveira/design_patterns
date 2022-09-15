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
         
        