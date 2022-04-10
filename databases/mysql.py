from typing import Dict
from interfaces import DatabaseInterface

class MysqlRepository(DatabaseInterface):
    """Mysql Repository

    Args:
        DatabaseInterface (_type_): _description_
    """
    
    def select_one(self) -> Dict:
        return {
            "success": True,
            "payload": "Mysql repository"
        }