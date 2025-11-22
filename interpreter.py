class Interpreter:
    def __init__ (self, shapes):
        self.shapes = shapes

    """ example params {
            shape: square,
            borderType: solid,
            borderColour: black,
            fillColour: blue,
    }"""

    def interpretLine(self, line):
        objectList = []

        for char in line:
            shapeParams = {
                "shape": None,
                "borderType": "solid",
                "borderColour": "#000000",
                "fillColour": "",
            }

            shapeParams["shape"] = self.shapes[char.lower()]
            objectList.append(shapeParams)

        return objectList

exampleLine = "ssctt "

correspondingShapes = {
    "s": "square", 
    "c": "circle",
    "t": "triangle"
}

myInterpreter = Interpreter(correspondingShapes)

print(myInterpreter.interpretLine(exampleLine))