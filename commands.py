class Command:
    def execute(self, turtle):
        raise NotImplementedError("Child commands need something to execute")

class SquareCommand:
    def __init__(self):
        self.dimensions = {sideLength: 100}

    def execute(self, turtle):
        return

class CircleCommand:
    def __init__(self):
        self.dimensions = {diameter: 100}

    def execute(self, turtle):
        return

class TriangleCommand:
    def __init__(self):
        self.dimensions = {baseLength: 100, height: 100}

    def execute(self, turtle):
        return
