from dataclasses import dataclass
from typing import Optional, List
from enum import Enum, auto
from src.user.domain import UserId

class OrderStatus(Enum):
    CREATED = auto()
    PAID = auto()
    SHIPPED = auto()
    DELIVERED = auto()

@dataclass(frozen=True)
class OrderId:
    value: int

@dataclass
class OrderItem:
    product_name: str
    quantity: int
    price: int

@dataclass
class Order:
    id: OrderId
    user_id: UserId
    items: List[OrderItem]
    status: OrderStatus

class OrderRepository:
    def save(self, order: Order) -> None:
        raise NotImplementedError

    def find_by_id(self, order_id: OrderId) -> Optional[Order]:
        raise NotImplementedError
