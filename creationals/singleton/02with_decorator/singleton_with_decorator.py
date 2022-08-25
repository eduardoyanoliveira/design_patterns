def singleton(this):
    
    instances = {}
    
    def create_instance(*args, **kwargs):
        if this not in instances:
            instances[this] = this(*args, **kwargs)
        
        return instances[this]
    
    return create_instance


@singleton
class DataBaseSettings:
    
    def __init__(self) -> None:
        print('__init__ function has been called')


if __name__ == '__main__':
    
    db_config = DataBaseSettings()
    
    db_config.password = '12345678'
    
    new_db_config = DataBaseSettings()
    
    print(new_db_config.password)
    