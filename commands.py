class Command:
    def execute(self, turtle):
        raise NotImplementedError("Child commands need something to execute")

class SquareCommand(Command):
    def __init__(self, props):
        self.side_length = 100
        self.props = props

    def execute(self, turtle):
        turtle.selectBorderColour(self.props.borderColour)
        turtle.selectFillColour(self.props.fillColour)
        borderType = self.props.borderType

        dashed = True if borderType == "dashed" else False
            
        for i in range(4):
            turtle.drawLine(self.side_length, dashed)
            turtle.turnRight(90)

        style = "dashed" if borderType == "dashed" else "solid"
        return f"Drew a {self.props.fillColour} square with a {style} {self.props.borderColour} border"

class CircleCommand(Command):        
    def __init__(self, props):
        self.radius = 50
        self.props = props

    def execute(self, turtle):
        turtle.selectBorderColour(self.props.borderColour)
        turtle.selectFillColour(self.props.fillColour)
        borderType = props.borderType

        turtle.drawCircle(radius)

        style = "dashed" if borderType == "dashed" else "solid"
        return f"Drew a {self.props.fillColour} circle with a {style} {self.props.borderColour} border"

class TriangleCommand(Command):
    def __init__(self, props):
        self.side_length = 100
        self.props = props

    def execute(self, turtle):
        turtle.selectBorderColour(self.props.borderColour)
        turtle.selectFillColour(self.props.fillColour)
        borderType = props.borderType

        

        style = "dashed" if borderType == "dashed" else "solid"
        return f"Drew a {self.props.fillColour} triangle with a {style} {self.props.borderColour} border"
