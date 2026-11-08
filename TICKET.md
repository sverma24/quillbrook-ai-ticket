# QB-142: Monthly revenue for the accountant

From: Dana (owner, Quillbrook Bikes)

Our accountant wants total revenue for each month, so she can close the books.
Please add a `monthly` report next to the `items` one:

    python3 -m shop.report monthly

One line per month, oldest first, like `2026-09   $1,234.00`.
Refunded orders don't count. Add a test.
