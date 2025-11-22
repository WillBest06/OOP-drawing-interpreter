class Parser:
    def parseFile (self, path):
        linesList = []
        with open(path) as file:
            for line in file:
                linesList.append(line)

        return linesList