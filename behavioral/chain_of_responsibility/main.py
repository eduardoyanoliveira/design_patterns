import uuid
from modules.handlers import ( 
    MessageAccessHandler, 
    RoleAccessHandler, 
    TokenAccessHandler
)
from modules.program_classes import Role, User, UserMessageRequest


if __name__ == '__main__':
    
    user = User('yan', role=Role.SUPER, token=uuid.uuid4())
    user_message = UserMessageRequest(user, 'This is just a test')
    
    token_handler = TokenAccessHandler()
    role_handler = RoleAccessHandler()
    message_handler = MessageAccessHandler()
    
    token_handler.setNextHandler(role_handler)
    role_handler.setNextHandler(message_handler)
    
    token_handler.handle(user_message)