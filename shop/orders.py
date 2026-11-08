"""Load Quillbrook Bikes orders from the CSV export of the booking system."""
import csv
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data" / "orders.csv"


@dataclass
class Order:
    order_id: int
    created_at: datetime  # timezone-aware, as stored by the booking system
    item: str
    total: Decimal
    status: str  # "paid" or "refunded"


def load_orders(path=DATA):
    with open(path, newline="") as f:
        return [
            Order(
                order_id=int(row["order_id"]),
                created_at=datetime.fromisoformat(row["created_at"].replace("Z", "+00:00")),
                item=row["item"],
                total=Decimal(row["total"]),
                status=row["status"],
            )
            for row in csv.DictReader(f)
        ]
