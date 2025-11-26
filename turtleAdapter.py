# CHANGE INTERPRETER TO 3.14.0 BEFORE RUNNING

import turtle

class TurtleAdapter:
    def __init__(self):
        turtle.mode("logo")
        turtle.width(3)
        turtle.speed(10)
        turtle.setup(1.0, 1.0)
        turtle.screensize(turtle.window_width(), turtle.window_height())
        self.screen = turtle.getscreen()
        self.padding = 50
        self.moveTurtleToStartingPoint()
        
        
    # record turtle starting point before drawing

    def moveTurtleToStartingPoint(self):
        screen = self.screen
        screenSize = screen.screensize()
        x = ((screenSize[0] // 2) * -1) + self.padding
        y = ((screenSize[1] // 2) - self.padding)
        turtle.teleport(x, y)

    def teleport(self, x, y):
        turtle.teleport(x, y)

    def getCurrentPos(self):
        return turtle.pos()

    def setHeading(self, heading):
        turtle.setheading(heading)

    def selectShapeColours(self, borderColour, fillColour):
        turtle.color(borderColour, fillColour)

    def drawLine(self, length, dashed):
        if dashed:
            step = int(length * 0.1)
            for i in range(0, length, step * 2):
                turtle.pendown()
                turtle.forward(step)
                turtle.penup()
                turtle.forward(step)
        else:
            turtle.pendown()
            turtle.forward(length)
            turtle.penup()

    def drawCircle(self, radius):
        turtle.circle(radius)

    def turnRight(self, degrees):
        turtle.right(degrees)

    def turnLeft(self, degrees):
        turtle.left(degrees)

    def startFill(self):
        turtle.begin_fill()

    def endFill(self):
        turtle.end_fill()

    def enterViewMode(self):
        turtle.done()