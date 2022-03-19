import sys

class Main:
    FILE = ""
    ITERATIONS = 0
    X = 0
    Y = 0

    def __init__(self, file, iterations):
        self.FILE = file
        self.ITERATIONS = iterations
        
        with open(self.FILE) as file:
            lines = [line.strip() for line in file]

        for line in lines:
            if line[0] == "#":
                continue
            if line[0] == "x":
                coords = line.split(",")
                self.X = int(coords[0].split("=")[-1].strip())
                self.Y = int(coords[1].split("=")[-1].strip())
                
    def get_width(self):
        return self.X

    def get_height(self):
        return self.Y

if __name__ == "__main__":
    if len(sys.argv) > 1:
        iterations = sys.argv.pop()
        file = sys.argv.pop()
        Main(file, iterations).get_width()

