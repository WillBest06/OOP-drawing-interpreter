class Parser:
    def __init__(self):
        return

    def parseFile (self, path):
        with open(path) as file:
            self.loopThroughEachValue(file)

        return self.commandProps

# for shapes with solid borders and B/W fill only
class SimpleParser(Parser):
    def __init__(self):
        self.propsTemplate = {"shape": None, "borderColour": "black", "fillColour": "white", "borderType": "solid"}
        self.commandProps = []
    
    def loopThroughEachValue(self, file):
        for line in file:
            for char in line:
                if char == "\n":
                    self.commandProps.append({"shape": "new_line"})
                elif char == " ":
                    self.commandProps.append({"shape": "blank_space"})
                else:
                    self.commandProps.append(self.setProps(char))
                  
    def setProps(self, char):
        newProps = self.propsTemplate.copy()

        match char.lower():
            case "s":
                newProps["shape"] = "square"
            case "t":
                newProps["shape"] = "triangle"
            case "c":
                newProps["shape"] = "circle"

        if char.isupper():
            newProps["fillColour"] = "black"
        else:
            newProps["fillColour"] = "white"

        return newProps

myParser = SimpleParser()
results = myParser.parseFile("text_files/file1.txt")
for result in results:
    print("\n" , result)