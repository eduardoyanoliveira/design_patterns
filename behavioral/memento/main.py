from modules.originator import Beast
from modules.caretaker import  BeastCaretaker

if __name__ == '__main__':
    dog = Beast('dog')
    dog_caretaker = BeastCaretaker(dog)
    
    print(dog)
    
    dog_caretaker.backup()
    dog.transform('wild_dog')
    print(dog)
    
    dog_caretaker.backup()
    dog.transform('wolf')
    print(dog)
    
    dog_caretaker.backup()
    dog.transform('warewolf')
    print(dog)
    
    dog_caretaker.undo()
    print(dog)