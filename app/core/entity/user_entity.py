from pydantic import BaseModel
import json

class UserEntity(BaseModel):
    id: int = None
    username: str = None
    age : int = None
    descriptions: str = None

    def toJSON(self):
        return {
            "id":self.id,
            "username":self.username,
            "age":self.age,
            "descriptions":self.descriptions
        }
