symbols = {
    # General
    "🔜": lambda x: x,  # Lambda
    "🔁": lambda i, x: [x() for l in range(i)],  # Loop
    "🖨": lambda p: print(p),

    # Numeric constants
    "1️⃣": lambda: 1,
    "2️⃣": lambda: 2,
    "😀": lambda: 3,

    # Math
    "➕": lambda a, b: a + b,
    "➖": lambda a, b: a - b,
    "✖️": lambda a, b: a * b,
    "➗": lambda a, b: a / b
}
