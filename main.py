import sys

class Main:
    FILE = ""
    ITERATIONS = 0
    X = 0
    Y = 0
    PATTERN = [[]]

    def __init__(self, file, iterations):
        self.FILE = file
        self.ITERATIONS = iterations
        self.X = 0
        self.Y = 0
        self.PATTERN = [[]]
        
        with open(self.FILE) as file:
            lines = [line.strip() for line in file]

        for line in lines:
            # Comment
            if line[0] == "#":
                continue
            # Coords, rule
            if line[0] == "x":
                coords = line.split(",")
                self.X = int(coords[0].split("=")[-1].strip())
                self.Y = int(coords[1].split("=")[-1].strip())
                continue
            # Pattern
            i = 0
            reps = 1
            for char in line:
                if char == "!":
                    continue
                if char == "$":
                    self.PATTERN.append([])
                    i += 1
                    continue
                
                if char.isnumeric():
                    reps = int(char)
                    continue
                for j in range(reps):
                    self.PATTERN[i].append(char)
                reps = 1

    def get_width(self):
        return self.X

    def get_height(self):
        return self.Y

    def get_pattern(self):
        return self.PATTERN

if __name__ == "__main__":
    if len(sys.argv) > 1:
        iterations = sys.argv.pop()
        file = sys.argv.pop()
        Main(file, iterations).get_width()

