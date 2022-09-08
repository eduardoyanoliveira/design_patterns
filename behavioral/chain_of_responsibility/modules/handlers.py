from modules.abstract_handler import AbstractAccessHandler
from modules.program_classes import UserMessageRequest, Role

class TokenAccessHandler(AbstractAccessHandler):
    
    def handle(self, user_message: UserMessageRequest) -> UserMessageRequest:
        if user_message.user.token : return self._next.handle(user_message)
        
        print('Not Access token provided')
        user_message.denied = True
        return user_message
    

class RoleAccessHandler(AbstractAccessHandler):
    
    def handle(self, user_message: UserMessageRequest) -> UserMessageRequest:
        if user_message.user.role == Role.SUPER : return self._next.handle(user_message)
        
        print('User does not have permission for this operation')
        user_message.denied = True
        return user_message


class MessageAccessHandler(AbstractAccessHandler):
    
    def handle(self, user_message: UserMessageRequest) -> UserMessageRequest:
        if user_message.message:  
            print('The following message was send:')
            print(user_message.message)
            return
        
        print('No Message was provided')
        user_message.denied = True
        return user_message
    