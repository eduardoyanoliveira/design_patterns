

class DatabaseConfig:
    
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    
    # Creates a new Instance of DatabaseConfig
    db_config = DatabaseConfig()
    
    # Adds some attributes to the instance
    db_config.host = 'localhost:3000'
    db_config.password = '@pwd123'
    db_config.db_name = 'my_db'
    db_config.user = 'super'
    
    # Creates a new Instance ofthe class
    db_config_two = DatabaseConfig()
    
    # Tries to access attributes that have been seted on the first instance to be created on the second instance
    print(db_config_two.user)
    print(db_config.user)
        