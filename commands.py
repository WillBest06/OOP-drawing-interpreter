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
            
        turtle.setHeading(90)
        turtle.startFill()
        for i in range(4):
            turtle.drawLine(self.side_length, dashed)
            turtle.turnRight(90)
        turtle.endFill()

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
        self.side_length = 115
        self.props = props

    def execute(self, turtle):
        turtle.selectBorderColour(self.props["borderColour"])
        turtle.selectFillColour(self.props["fillColour"])
        borderType = self.props["borderType"]

        dashed = True if borderType == "dashed" else False

        # [x, y] = turtle.getCurrentPos()
        # turtle.teleport(x + 50, y)
        
        turtle.setHeading(150)

        turtle.startFill()
        for i in range(3):
            turtle.drawLine(self.side_length, dashed)
            turtle.turnRight(120)
        turtle.endFill()

        style = "dashed" if borderType == "dashed" else "solid"
        return f"Drew a {self.props["fillColour"]} triangle with a {style} {self.props["borderColour"]} border"

mySquare = SquareCommand({"borderColour": "black", "fillColour": "blue", "borderType": "solid"})
myTurtle = turtleAdapter.TurtleAdapter()
mySquare.execute(myTurtle)


myTriangle = TriangleCommand({"borderColour": "black", "fillColour": "blue", "borderType": "solid"})
# myTurtle = turtleAdapter.TurtleAdapter()
print(myTriangle.execute(myTurtle))

myTurtle.enterViewMode()