import turtleAdapter  

class Command:
    def execute(self, turtleAdapter):
        raise NotImplementedError("Child commands need something to execute")

    def colourSetup(self, turtleAdapter):
        turtleAdapter.selectShapeColours(self.props["borderColour"], self.props["fillColour"])

    def isDashed(self):
        return self.props["borderType"] == "dashed"

    def moveInsideCell(self, turtleAdapter, xOffset, yOffset):
        x, y = turtleAdapter.getCurrentPos()
        turtleAdapter.teleport(x + xOffset, y + yOffset)

    def __str__(self):
        return f"Command for a {self.props["fillColour"]} {self.shape} with a {self.props["borderType"]} {self.props["borderColour"]} border"

class NewLineCommand(Command):
    def execute(self, turtleAdapter):
        screen = turtleAdapter.screen
        screenX, screenY = screen.screensize()
        # origin is in center of screen so left
        # is negative half of screen size from origin
        screenLeft = (screenX / 2) * -1
        currentX, currentY = turtleAdapter.getCurrentPos()
        turtleAdapter.teleport(screenLeft + turtleAdapter.padding, currentY - 130)

class SquareCommand(Command):
    def __init__(self, props):
        self.side_length = 100
        self.props = props
        self.shape = "square"

    def execute(self, turtleAdapter):
        self.colourSetup(turtleAdapter)

        dashed = self.isDashed()
          
        turtleAdapter.setHeading(90)
        turtleAdapter.startFill()
        for i in range(4):
            turtleAdapter.drawLine(self.side_length, dashed)
            turtleAdapter.turnRight(90)
        turtleAdapter.endFill()

        turtleAdapter.moveToTopLeftOfNextCell()

class CircleCommand(Command):        
    def __init__(self, props):
        self.radius = 50
        self.props = props
        self.shape = "circle"

    def execute(self, turtleAdapter):
        self.colourSetup(turtleAdapter)
        dashed = self.isDashed()
        turtleAdapter.setHeading(0)

        self.moveInsideCell(turtleAdapter, 0, -50)

        turtleAdapter.startFill()
        turtleAdapter.drawCircle(-1 * self.radius, dashed)
        turtleAdapter.endFill()

        # moves turtle to top left corner of current cell
        self.moveInsideCell(turtleAdapter, 0, 50)

        turtleAdapter.moveToTopLeftOfNextCell()

class TriangleCommand(Command):
    def __init__(self, props):
        self.side_length = 115
        self.props = props
        self.shape = "triangle"

    def execute(self, turtleAdapter):
        self.colourSetup(turtleAdapter)
        dashed = self.isDashed()

        self.moveInsideCell(turtleAdapter, 50, 0)
        
        turtleAdapter.setHeading(150)

        turtleAdapter.startFill()
        for i in range(3):
            turtleAdapter.drawLine(self.side_length, dashed)
            turtleAdapter.turnRight(120)
        turtleAdapter.endFill()

        # moves turtle to top left corner of current cell
        self.moveInsideCell(turtleAdapter, -50, 0)

        turtleAdapter.moveToTopLeftOfNextCell()

mySquare = SquareCommand({"borderColour": "black", "fillColour": "blue", "borderType": "solid"})
myTurtleAdapter = turtleAdapter.TurtleAdapter()
mySquare.execute(myTurtleAdapter)

myNewLine = NewLineCommand()
myNewLine.execute(myTurtleAdapter)

myTriangle = TriangleCommand({"borderColour": "black", "fillColour": "blue", "borderType": "solid"})
myTriangle.execute(myTurtleAdapter)

myCircle = CircleCommand({"borderColour": "black", "fillColour": "blue", "borderType": "dashed"})
myCircle.execute(myTurtleAdapter)

myTurtleAdapter.enterViewMode()