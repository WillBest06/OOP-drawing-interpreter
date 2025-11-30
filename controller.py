import interpreter
import parser
import turtleAdapter

class Controller:
    def __init__(self):
        self.myTurtleAdapter = turtleAdapter.TurtleAdapter()

        # For printing red text
        self.RED = '\033[91m'
        self.RESET = '\033[0m'

    def run(self):
        parserType = None

        print("\nProvide me with a formatted text file and I will draw the shapes for you.")
        print("\nPlease select the simple parser for black & white shapes with solid borders.")
        print("\nPlease select the complex parser for RGB shapes with any border type.")

        while True:
            parserType = input("\nChoose a parser ('s' for simple | 'c' for complex): ").lower()
            
            if parserType not in ["s", "c"]:
                print(f"{self.RED}Error: Parser choice must only be simple 's' or complex 'c'{self.RESET}")
                continue
            break

        if parserType == "s":
            myParser = parser.SimpleParser()
        elif parserType == "c":
            myParser = parser.ComplexParser()

        path = input("\nPlease enter the path of the formatted text file: ")

        parsedResults = myParser.parseFile(path)

        myInterpreter = interpreter.Interpreter()
        commands = myInterpreter.interpret(parsedResults)

        for cmd in commands:
            cmd.execute(self.myTurtleAdapter)

        self.myTurtleAdapter.enterViewMode()

if __name__ == "__main__":
    myController = Controller()
    myController.run()