from lex import parse

arguments = []


def save(args):
    global arguments
    arguments = args


def run(program):
    global arguments
    arguments.clear()
    function = parse(program)
    print(function.run())
