import demoji
from inspect import signature
from symbols import symbols


class Function:
    def __init__(self, symbol, action, arguments):
        assert type(arguments) == list
        assert all(type(x) == Function for x in arguments)
        self.symbol = symbol
        self.action = action
        self.arguments = arguments

    def execute(self):
        values = []
        for argument in self.arguments:
            values.append(argument.run())
        return self.action(*values)

    def run(self):
        if self.symbol == "🔜":  # Lambda expression is a special case
            return self.execute
        return self.execute()


def parse(program):
    emoji = demoji._EMOJI_PAT.findall(program)
    return visit(emoji)[0]


def visit(program):
    """
    Convert's text to an AST
    """
    if len(program) == 0:
        raise Exception("Unexpected end of program!")
    symbol = program[0]
    if symbol not in symbols:
        raise Exception("Unknown symbol in program: " + symbol)
    current = symbols[symbol]
    program = program[1:]
    arguments = []
    for _ in range(len(signature(current).parameters)):
        function, program = visit(program)
        arguments.append(function)
    return (Function(symbol, current, arguments), program)
