
class Function:
    def __init__(self, exec, arguments):
        assert type(arguments) == list
        assert all(type(x) == Function for x in arguments)
        self.exec = exec
        self.arguments = arguments

    def run(self):
        values = []
        for argument in self.arguments:
            values.append(argument.run())
        return exec(*values)
