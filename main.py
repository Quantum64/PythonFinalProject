from symbols import symbols
from inspect import signature

if __name__ == "__main__":
    print(len(signature(symbols["1️⃣"]).parameters))
