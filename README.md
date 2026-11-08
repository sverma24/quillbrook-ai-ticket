# Quillbrook Bikes: demo repo

A tiny, made-up repair-shop codebase used in the video "Tech Skills to Learn in 2027 (Before AI Takes Your Job)".
Quillbrook Bikes is fictional, and so are the orders in `data/orders.csv`.

Run the reports and the tests (Python 3.9+, standard library only, no sign-ups or keys):

    python3 -m shop.report items
    python3 -m unittest

`TICKET.md` is the ticket Claude Code works on in the video.

## Branches

- `main`: the starting point, the ticket as it was handed over.
- `solution`: what Claude Code wrote in the video, after the owner confirmed the shop closes its books on Denver time (three tests, `python3 -m shop.report monthly`).

Try the ticket yourself on `main` first, then compare with `solution`.

## License

MIT
