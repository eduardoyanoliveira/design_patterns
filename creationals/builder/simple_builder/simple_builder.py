from dataclasses import dataclass
from typing import Optional


@dataclass
class Gun:
    
    brand: str
    elongated_clip: Optional[bool] = None
    scope: Optional[bool] = None
    elongated_stock: Optional[bool] = None
    silincer: Optional[bool] = None
    infrared_sight: Optional[bool] = None
    

@dataclass
class GunBuilder(Gun):
    
    
    def with_elongated_clip(self) -> None:
        self.elongated_clip = True
        return self
    
    def with_scope(self) -> None:
        self.scope = True
        return self

    def with_elongated_stock(self) -> None:
        self.elongated_stock = True
        return self
    
    def with_silincer(self) -> None:
        self.silincer = True
        return self

    def with_infrared_sight(self) -> None:
        self.infrared_sight = True
        return self
    
    def build(self) -> Gun:
        return Gun(
            self.brand,
            self.elongated_clip,
            self.scope,
            self.elongated_stock,
            self.silincer,
            self.infrared_sight
        )
    

if __name__ == '__main__':
    ak = GunBuilder('Ak-74').with_scope().with_silincer().build()
    glock = GunBuilder('Glock').with_infrared_sight().build()
    
    print(ak)
    print(glock)