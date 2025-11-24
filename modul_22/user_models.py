from pydantic import BaseModel
from typing import Optional
#class User(BaseModel):
#    id: int
#    name: str
#    email: str
#    age: int

#user1 = User(id=1, name="Xhon Do", email="xhon.do@ekzampell.kom", age=20)
class User(BaseModel):
    id: int
    name: str
    age: Optional[int] = None
    email: Optional[str] = None
user1=User(id=1, name="Xhon Do", email="xhon.do@ekzampell.kom", age=20)
print(user1)
user2=User(id=2, name="Don Xhon", email="add@fad.cam", age=None)
print(user2)
user3=User(id=3, name="Albaninabi", age=83)
print(user3)
user4=User(id=4, name="Albanina")
print(user4)