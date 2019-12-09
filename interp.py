from lex import parse

arguments = []


def save(args):
    global arguments
    arguments = args


def run(program, args=[]):
    global arguments
    save(args)
    function = parse(program)
    print(function.run())
