from typing import List, Protocol


class WearableDeviceImplementor(Protocol):
    
    def get_battery_charge(self) -> int: pass
    
    def get_notifications(self) -> List: pass
