from uuid import UUID, uuid4
from typing import Optional, List
from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    firts_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    role: List[Role] = None

class Message(BaseModel):
    id: UUID = uuid4()
    sender: str
    receiver: str
    message: str
    timestamp: str = datetime.utcnow().isoformat()

class UserUpdateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Role]]
    
