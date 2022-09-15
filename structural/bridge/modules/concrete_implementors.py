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