from dataclasses import dataclass
from modules.jwt import JwtToken
from modules.target_protocol import ITokenService
from modules.adapter import HashTokenAdapter

@dataclass
class LoginScreen:
    
    token_service: ITokenService
    token: str = None
    
    def execute(self) -> None:
        
        if self.token:
            validated_token = self.token_service.verify(self.token)
            
            if not validated_token:
                print('Acess Denied!')

            print('User is already logged, moving to home page')
            return
        
        self.token = self.token_service.get_token()
        print('User has been logged, moving to home page')


if __name__ == '__main__':
    
    # Using JwtToken
    login_screen = LoginScreen(JwtToken)
    
    login_screen.execute()
    print('####')
    login_screen.execute()
    
    print('--------------------------------')
    print()
    
    # Using HashTokenAdapter
    login_screen = LoginScreen(HashTokenAdapter)
    
    login_screen.execute()
    print('####')
    login_screen.execute()