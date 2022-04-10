from usecases import BusinessRule
from databases import MysqlRepository

class Mysqlfactory:
    """Factory exemplo
     This design pattern helps to encapsulate your code, then 
     it becomes easier to mantain and create automated tests or even unit testes

    Returns:
        _type_: _description_
    """
    
    @staticmethod
    def create() -> BusinessRule:
        return BusinessRule(MysqlRepository())