from dataclasses import dataclass
from typing import Optional
from enum import Enum, auto
from src.order.domain import OrderId

class DeliveryStatus(Enum):
    READY = auto()
    IN_TRANSIT = auto()
    DELIVERED = auto()

@dataclass(frozen=True)
class DeliveryId:
    value: int

@dataclass
class Delivery:
    id: DeliveryId
    order_id: OrderId
    address: str
    status: DeliveryStatus

class DeliveryRepository:
    def save(self, delivery: Delivery) -> None:
        raise NotImplementedError

    def find_by_id(self, delivery_id: DeliveryId) -> Optional[Delivery]:
        raise NotImplementedError
