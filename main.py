import demoji
from lex import parse

if __name__ == "__main__":
    try:
        demoji.set_emoji_pattern()
    except IOError:
        demoji.download_codes()
    program = parse("🔁2️⃣🔜🖨1️⃣")
    print(program.run())
