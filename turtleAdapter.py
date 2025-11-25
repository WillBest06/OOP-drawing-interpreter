# CHANGE INTERPRETER TO 3.14.0 BEFORE RUNNING

import turtle

class TurtleAdapter:
    def __init__(self, x, y):
        turtle.goto(x, y)
        turtle.width(3)
        turtle.speed(8)
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
        turtle.pos()

    def selectBorderColour(self, colour):
        turtle.color(colour)

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

myTurtle = TurtleAdapter(0, 0)

for i in range(4):
    myTurtle.drawLine(100, True)
    myTurtle.turnRight(90)

myTurtle.enterViewMode()
