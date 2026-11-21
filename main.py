"""Write one poem about stopping to /output/entry.txt.

Python 3.13, standard library only, deterministic, no network.
The poem is a fixed string: the same bytes on every run.
"""

import os

POEM = """The kettle clicks off.
I do not pour.
The morning can wait —
the cup, the rush, the door.

I sit with the steam
as it thins to air.
My hand, unhurried,
rests on the chair.

The tea goes cold.
I drink it anyway.
"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
