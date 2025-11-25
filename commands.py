class Command:
    def execute(self, turtle):
        raise NotImplementedError("Child commands need something to execute")

class SquareCommand(Command):
    def __init__(self, props):
        self.dimensions = {SIDELENGTH: 100}
        self.props = props

    def execute(self, turtle):
        borderColour = props.borderColour
        borderType = props.borderType
        fillColour = props.fillColour

        return

class CircleCommand(Command):        
    def __init__(self, props):
        self.dimensions = {DIAMETER: 100}
        self.props = props

    def execute(self, turtle):
        borderColour = props.borderColour
        borderType = props.borderType
        fillColour = props.fillColour

        return

class TriangleCommand(Command):
    def __init__(self, props):
        self.dimensions = {BASELENGTH: 100, HEIGHT: 100}
        self.props = props

    def execute(self, turtle):
        borderColour = props.borderColour
        borderType = props.borderType
        fillColour = props.fillColour

        return
