import demoji
import sys
import interp
from lex import parse


def start():
    try:
        demoji.set_emoji_pattern()
    except IOError:
        demoji.download_codes()
    if len(sys.argv) <= 1:
        print("No program to run")
        return
    with open(sys.argv[1], encoding="UTF-8") as file:
        parameters = []
        if len(sys.argv) > 2:
            parameters = sys.argv[2:]
        text = file.read()
        interp.run(text, parameters)


if __name__ == "__main__":
    start()
