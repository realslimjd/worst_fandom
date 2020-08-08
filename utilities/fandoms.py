import random
from typing import List

FANDOMS = [
    "Juggalos",
    "Taylor Swift",
    "Twilight",
    "Bronies",
    "Republicans",
    "Rick and Morty",
    "Logang",
    "Homestuck",
    "Anybody who listens to a Dirtbag Left podcast",
    "True crime enthusiasts",
    "Trekkies",
    "Star Wars",
]  # type: List[str]


def get_fandom() -> str:
    fandom = random.choice(FANDOMS)
    return fandom
