class Parser:
    def __init__(self):
        self.propsTemplate = {"shape": None, "borderColour": "black", "fillColour": "white", "borderType": "solid"}
        self.commandProps = []

    def parseFile (self, path):
        with open(path) as file:
            self.loopThroughEachValue(file)

        return self.commandProps

# for shapes with solid borders and B/W fill only
class SimpleParser(Parser):
    def loopThroughEachValue(self, file):
        for line in file:
            for value in line:
                if value == "\n":
                    self.commandProps.append({"shape": "new_line"})
                elif value == " ":
                    self.commandProps.append({"shape": "blank_space"})
                else:
                    self.commandProps.append(self.setProps(value))
                  
    def setProps(self, value):
        newProps = self.propsTemplate.copy()

        match value.lower():
            case "s":
                newProps["shape"] = "square"
            case "t":
                newProps["shape"] = "triangle"
            case "c":
                newProps["shape"] = "circle"

        if value.isupper():
            newProps["fillColour"] = "black"
        else:
            newProps["fillColour"] = "white"

        return newProps


# for shapes with any border and fill colour
class ComplexParser(Parser):
    def loopThroughEachValue(self, file):
        for line in file:
            values = line.split(",")
            for value in values:
                if value == "\n":
                    self.commandProps.append({"shape": "new_line"})
                elif value == " ":
                    self.commandProps.append({"shape": "blank_space"})
                elif value == "":
                    break   
                else:
                    self.commandProps.append(self.setProps(value))
                  
    def setProps(self, value):
        newProps = self.propsTemplate.copy()

        match value[0].lower():
            case "s":
                newProps["shape"] = "square"
            case "t":
                newProps["shape"] = "triangle"
            case "c":
                newProps["shape"] = "circle"

        if value[1] == "-":
            newProps["borderType"] = "dashed"
        else:
            newProps["borderType"] = "solid"

        match value[2]:
            case "0":
                newProps["borderColour"] = "black"
            case "1":
                newProps["borderColour"] = "red"
            case "2":
                newProps["borderColour"] = "blue"
            case "3":
                newProps["borderColour"] = "green"
            case "4":
                newProps["borderColour"] = "yellow"
            case "5":
                newProps["borderColour"] = "purple"
            case "6":
                newProps["borderColour"] = "orange"
            case "7":
                newProps["borderColour"] = "pink"
            case "8":
                newProps["borderColour"] = "brown"
            case "9":
                newProps["borderColour"] = "white"

        match value[3]:
            case "0":
                newProps["fillColour"] = "black"
            case "1":
                newProps["fillColour"] = "red"
            case "2":
                newProps["fillColour"] = "blue"
            case "3":
                newProps["fillColour"] = "green"
            case "4":
                newProps["fillColour"] = "yellow"
            case "5":
                newProps["fillColour"] = "purple"
            case "6":
                newProps["fillColour"] = "orange"
            case "7":
                newProps["fillColour"] = "pink"
            case "8":
                newProps["fillColour"] = "brown"
            case "9":
                newProps["fillColour"] = "white"
            
        return newProps