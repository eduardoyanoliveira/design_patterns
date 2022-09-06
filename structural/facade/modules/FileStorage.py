from dataclasses import dataclass
from typing import ClassVar, List


@dataclass
class FileStorage:
    
    files: ClassVar[List[str]] = []
    
    @classmethod
    def add_file(cls, file) -> str:
        
        url = f'https://localhost:3000/files/{file}'
        cls.files.append(url)
        
        print(f'File {file} has been uploaded to server')
        return url

    @classmethod
    def delete_file(cls, file) -> None:
        
        if file in cls.files:
            cls.files.remove(file)
            print(f'File {file} has been removed from server')