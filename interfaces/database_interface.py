from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    """Database Interface

    Args:
        ABC (_type_): _description_
    """
    
    @abstractmethod
    def select_one(self):
        pass
    