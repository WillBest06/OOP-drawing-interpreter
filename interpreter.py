import commands

class Interpreter:
    def __init__ (self):
        self.listOfCommandsToExecute = []

    def interpret(self, listOfParsedShapeProps):
        for shapeProps in listOfParsedShapeProps:
            match shapeProps["shape"]:
                case "new_line":
                    command = commands.NewLineCommand()
                case "square":
                    command = commands.SquareCommand(shapeProps)
                case "circle":
                    command = commands.CircleCommand(shapeProps)
                case "triangle":
                    command = commands.TriangleCommand(shapeProps)

            self.listOfCommandsToExecute.append(command)
        
        return self.listOfCommandsToExecute