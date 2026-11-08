import unittest
from datetime import datetime, timezone
from decimal import Decimal

from shop.orders import Order
from shop.report import revenue_by_item, revenue_by_month


def order(oid, when, item, total, status="paid"):
    return Order(oid, when, item, Decimal(total), status)


class RevenueByItem(unittest.TestCase):
    def test_refunds_are_left_out(self):
        orders = [
            order(1, datetime(2026, 10, 3, 18, tzinfo=timezone.utc), "Brake bleed", "45.00"),
            order(2, datetime(2026, 10, 4, 18, tzinfo=timezone.utc), "Brake bleed", "45.00", "refunded"),
        ]
        self.assertEqual(revenue_by_item(orders), {"Brake bleed": Decimal("45.00")})


class RevenueByMonth(unittest.TestCase):
    def test_sums_per_month_oldest_first_without_refunds(self):
        orders = [
            order(1, datetime(2026, 10, 3, 18, tzinfo=timezone.utc), "Brake bleed", "45.00"),
            order(2, datetime(2026, 9, 30, 18, tzinfo=timezone.utc), "Wheel true", "35.00"),
            order(3, datetime(2026, 10, 4, 18, tzinfo=timezone.utc), "Brake bleed", "45.00", "refunded"),
            order(4, datetime(2026, 10, 9, 18, tzinfo=timezone.utc), "Wheel true", "35.50"),
        ]
        result = revenue_by_month(orders)
        self.assertEqual(list(result), ["2026-09", "2026-10"])
        self.assertEqual(result, {"2026-09": Decimal("35.00"), "2026-10": Decimal("80.50")})

    def test_months_follow_denver_time(self):
        # 2026-11-01 01:12 UTC is Oct 31, 7:12 pm in Denver (MDT)
        orders = [order(1034, datetime(2026, 11, 1, 1, 12, tzinfo=timezone.utc), "Full overhaul", "249.00")]
        self.assertEqual(revenue_by_month(orders), {"2026-10": Decimal("249.00")})


if __name__ == "__main__":
    unittest.main()
