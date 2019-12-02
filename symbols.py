symbols = {
    # General
    "🔜": lambda x: x,  # Lambda
    "🅰️": lambda i: argument(i),  # Return argument at index
    "🆎": lambda: arguments(),  # Return list of all arguments
    "🔁": lambda i, x: [x() for l in range(i)],  # Loop
    "🤐": lambda x: suppress(x),  # Suppress output
    "🖨": lambda p: print(p),  # Print p, return None

    # Lists
    "🧲": lambda l, i: l[i],  # Get element from list at index
    "📥": lambda x: [x],  # Return singleton list of x
    "➡️": lambda x: list(range(x)),  # Range from 0 to x,
    "↔️": lambda x, y: list(range(x, y)),  # Range from x to y
    "🗺": lambda l, f: [f(x) for x in l],  # Map each element of x to f(x)
    "🚰": lambda l, f: [x for x in l if f(x)],  # Return elements of x if f(x)

    # Comparison
    "❤️": lambda x, y: x == y,  # Return if x equals y
    "💔": lambda x, y: x != y,  # Return if x does not equal y
    "🧡": lambda x, y: x > y,  # Return if x greater than y
    "💛": lambda x, y: x < y,  # Return if y less than y
    "💚": lambda x, y: x >= y,  # Return if x greather or equal to y
    "💙": lambda x, y: x <= y,  # Return if x less or equal to y

    # Strings
    "🍏": lambda

    # Numeric constants
    "0️⃣": lambda: 0,  # Return 0
    "1️⃣": lambda: 1,  # Return 1
    "2️⃣": lambda: 2,  # Return 2
    "3️⃣": lambda: 3,  # Return 3
    "4️⃣": lambda: 4,  # Return 4
    "5️⃣": lambda: 5,  # Return 5
    "6️⃣": lambda: 6,  # Return 6
    "7️⃣": lambda: 7,  # Return 7
    "8️⃣": lambda: 8,  # Return 8
    "9️⃣": lambda: 9,  # Return 9
    "🔟": lambda: 10,  # Return 10

    # Math
    "➕": lambda a, b: a + b,
    "➖": lambda a, b: a - b,
    "✖️": lambda a, b: a * b,
    "➗": lambda a, b: a / b
}


def argument(index):
    import interp
    if index >= len(interp.arguments):
        raise Exception(
            "Tried to access an out of range argument! Index " + str(index) + ". Are you forgetting a lambda?")
    return interp.arguments[index]


def arguments():
    import interp
    return interp.arguments


def suppress(x):
    x()
    return ""
