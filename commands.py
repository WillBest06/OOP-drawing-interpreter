import turtleAdapter  

class Command:
    def execute(self, turtle):
        raise NotImplementedError("Child commands need something to execute")

class SquareCommand(Command):
    def __init__(self, props):
        self.side_length = 100
        self.props = props

    def execute(self, turtle):
        turtle.selectBorderColour(self.props["borderColour"])
        turtle.selectFillColour(self.props["fillColour"])
        borderType = self.props["borderType"]

        dashed = True if borderType == "dashed" else False
            
        turtle.startFill()
        for i in range(4):
            turtle.drawLine(self.side_length, dashed)
            turtle.turnRight(90)
        turtle.endFill()
        turtle.enterViewMode()

        style = "dashed" if borderType == "dashed" else "solid"
        return f"Drew a {self.props["fillColour"]} square with a {style} {self.props["borderColour"]} border"

class CircleCommand(Command):        
    def __init__(self, props):
        self.radius = 50
        self.props = props

    def execute(self, turtle):
        turtle.selectBorderColour(self.props["borderColour"])
        turtle.selectFillColour(self.props["fillColour"])
        borderType = self.props["borderType"]

        turtle.drawCircle(radius)

        style = "dashed" if borderType == "dashed" else "solid"
        return f"Drew a {self.props["fillColour"]} circle with a {style} {self.props["borderColour"]} border"

class TriangleCommand(Command):
    def __init__(self, props):
        self.side_length = 100
        self.props = props

    def execute(self, turtle):
        turtle.selectBorderColour(self.props["borderColour"])
        turtle.selectFillColour(self.props["fillColour"])
        borderType = self.props["borderType"]

        dashed = True if borderType == "dashed" else False

        # [x, y] = turtle.getCurrentPos()
        # turtle.teleport(x + 50, y)

        turtle.startFill()
        for i in range(3):
            turtle.drawLine(self.side_length, dashed)
            turtle.turnRight(120)
        turtle.endFill()
        turtle.enterViewMode()


        style = "dashed" if borderType == "dashed" else "solid"
        return f"Drew a {self.props["fillColour"]} triangle with a {style} {self.props["borderColour"]} border"

# mySquare = SquareCommand({"borderColour": "black", "fillColour": "blue", "borderType": "solid"})
# myTurtle = turtleAdapter.TurtleAdapter(0, 0)

# mySquare.execute(myTurtle)

myTurtle = turtleAdapter.TurtleAdapter(0, 0)
myTriangle = TriangleCommand({"borderColour": "black", "fillColour": "blue", "borderType": "dashed"})
myTriangle.execute(myTurtle)