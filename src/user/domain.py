from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class UserId:
    value: int

@dataclass
class User:
    id: UserId
    name: str
    email: str

class UserRepository:
    def save(self, user: User) -> None:
        raise NotImplementedError

    def find_by_id(self, user_id: UserId) -> Optional[User]:
        raise NotImplementedError
