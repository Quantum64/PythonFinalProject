import doctest
import demoji
from interp import run
from lex import parse


def hello_world():
    """
    Prints the string "Hello World"
    >>> hello_world()
    Hello World
    """
    run("🍐➕➕➕➕➕➕➕➕➕➕🎾🥎🏸🏸🏑🛹🎽🏑♟🏸🎲")


def basic_math():
    """
    Take the mod2 of 4 + 1
    >>> basic_math()
    1
    """
    run("😁➕4️⃣1️⃣2️⃣")


if __name__ == "__main__":
    try:
        demoji.set_emoji_pattern()
    except IOError:
        demoji.download_codes()
    doctest.testmod(verbose=True)
