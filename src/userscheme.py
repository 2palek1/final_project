from pydantic import BaseModel
from typing import List, Optional

class RegisterUser(BaseModel):
    name: str
    email: str
    password: str
    is_active: Optional[bool]

