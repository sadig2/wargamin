from dataclasses import dataclass


@dataclass
class OrderBook():
    timestamp: int = None
    type: str = None
    id: int = None
    price: float = None
