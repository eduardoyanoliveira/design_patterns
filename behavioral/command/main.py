from modules.commands import SendMessage
from modules.batch import Batch
from modules.invoker import Invoker
from modules.reciver import User
from modules.commands import Follow

if __name__ == '__main__':
    
    yan = User('Yan')
    duda = User('Duda')
    john = User('John')
    invoker = Invoker()
    
    invoker.execute(Follow(follower= yan, followed= duda))
    invoker.undo()
    
    invoker.execute( Batch ([
        Follow(follower=john, followed=yan),
        SendMessage(from_user=john, to_user=yan, text='Hello yan! I am john from HR, i just followed you can you follow me back? ')
    ])) 
    
    invoker.undo()
    invoker.redo()
    
    # Yan's Followers
    for follower in yan.followers:
        print(follower)
    
    # Yan's Followings
    for following in yan.followings:
        print(following)
        
    for message in yan.messages:
        print(message)

    