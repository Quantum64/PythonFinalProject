from inspect import signature


def parse(program):
    """
    Convert's text to an AST
    """
    current = program[0]
    program = program[:1]
    