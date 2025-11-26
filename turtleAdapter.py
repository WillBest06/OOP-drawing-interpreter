# CHANGE INTERPRETER TO 3.14.0 BEFORE RUNNING

import turtle

class TurtleAdapter:
    def __init__(self):
        turtle.mode("logo")
        turtle.width(3)
        turtle.speed(10)
        self.screen = turtle.getscreen()
        self.moveTurtleToStartingPoint()
        
    # record turtle starting point before drawing

    def moveTurtleToStartingPoint(self):
        screen = self.screen
        screenSize = screen.screensize()
        x = ((screenSize[0] // 2) * -1) + 10
        y = ((screenSize[1] // 2) - 10)
        turtle.teleport(x, y)

    def teleport(self, x, y):
        turtle.teleport(x, y)

    def getCurrentPos(self):
        return turtle.pos()

    def setHeading(self, heading):
        turtle.setheading(heading)

    def selectBorderColour(self, colour):
        turtle.pencolor(colour)

    def selectFillColour(self, colour):
        turtle.fillcolor(colour)

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