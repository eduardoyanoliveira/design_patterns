from dataclasses import dataclass
from modules.reciver import User, Message

@dataclass
class Follow:
    
    follower: User
    followed: User
    
    def execute(self) -> None:
        self.follower.followings.append(self.followed)
        self.followed.followers.append(self.follower)
    
    def undo(self) -> None:
        self.follower.followings.pop()
        self.followed.followers.pop()
    
    
    def redo(self) -> None:
        self.execute()
        
        
@dataclass
class SendMessage:
    
    from_user: User
    to_user: User
    text: str
    
    def execute(self) -> None:
        message = Message(self.from_user, self.text)
        self.to_user.messages.append(message)
    
    def undo(self) -> None:
        self.to_user.messages.pop()
        
    def redo(self) -> None:
        self.execute()