from modules.program_classes import SmartBand, SmartWatch
from modules.concrete_implementors import SmartBandImplementor, SmartWatchImplementor
from modules.refined_abstractions import AppDisplayScreen, DesktopDisplayScreen

if __name__ == '__main__':
    
    mi_band =  SmartBand(54, ['Test notification', 'Yan is implementing the bridge pattern'])
    
    mi_band_implementor = SmartBandImplementor(mi_band)
    
    app_display_screen = AppDisplayScreen(mi_band_implementor)
    
    app_display_screen.display_wareable_status()
    
    print()
    print('#####################################')
    print()
    
    apple_watch =  SmartWatch(90, ['new notification', 'Yan, we are looking foward to our meeting with the CEO'])
    
    apple_watch_implementor = SmartWatchImplementor(apple_watch)
    
    desktop_display_screen = DesktopDisplayScreen(apple_watch_implementor)
    
    desktop_display_screen.display_wareable_status()