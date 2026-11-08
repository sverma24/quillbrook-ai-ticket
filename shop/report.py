"""Reports for the shop owner.

    python3 -m shop.report items     revenue per service, best first
"""
import sys
from collections import defaultdict

from shop.orders import load_orders


def revenue_by_item(orders):
    totals = defaultdict(lambda: 0)
    for o in orders:
        if o.status == "paid":
            totals[o.item] += o.total
    return dict(sorted(totals.items(), key=lambda kv: kv[1], reverse=True))


def main(argv):
    if argv[:1] == ["items"]:
        for item, total in revenue_by_item(load_orders()).items():
            print(f"{item:<22} ${total:>9,.2f}")
        return 0
    print(__doc__.strip())
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
