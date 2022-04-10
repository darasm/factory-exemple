from interfaces import DatabaseInterface
from typing import Type, Dict, Union


class BusinessRule:
    """Business Rule
    """
    
    def __init__(self, repository: Type[DatabaseInterface]) -> None:
        self.__repository = repository
    
    def first_rule(self, data: bool) -> Union[Dict, None]:
        if data:
            return self.__repository.select_one()
        return None
            
