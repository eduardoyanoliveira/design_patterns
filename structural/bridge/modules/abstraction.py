from abc import ABC
from dataclasses import dataclass
from modules.implementor import WearableDeviceImplementor


@dataclass
class DisplayScreenAbstraction(ABC):
    
    wearable_implementor: WearableDeviceImplementor

    