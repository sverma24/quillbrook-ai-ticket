import unittest
from datetime import datetime, timezone
from decimal import Decimal

from shop.orders import Order
from shop.report import revenue_by_item


def order(oid, when, item, total, status="paid"):
    return Order(oid, when, item, Decimal(total), status)


class RevenueByItem(unittest.TestCase):
    def test_refunds_are_left_out(self):
        orders = [
            order(1, datetime(2026, 10, 3, 18, tzinfo=timezone.utc), "Brake bleed", "45.00"),
            order(2, datetime(2026, 10, 4, 18, tzinfo=timezone.utc), "Brake bleed", "45.00", "refunded"),
        ]
        self.assertEqual(revenue_by_item(orders), {"Brake bleed": Decimal("45.00")})


if __name__ == "__main__":
    unittest.main()
