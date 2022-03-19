import sys

class Main:
    FILE = ""
    ITERATIONS = 0
    X = 0
    Y = 0
    PATTERN = []

    def __init__(self, file, iterations):
        self.FILE = file
        self.ITERATIONS = iterations
        self.X = 0
        self.Y = 0
        self.PATTERN = []
        
        with open(self.FILE) as file:
            lines = [line.strip() for line in file]

        line_string = ""
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
            reps = 0
            for char in line:
                if char == "!":
                    self.PATTERN.append(line_string)
                    continue
                if char == "$":
                    self.PATTERN.append(line_string)
                    line_string = ""
                    continue
                
                if char.isnumeric():
                    if reps != 0:
                        reps += char
                    else:
                        reps = char
                    continue

                if reps != 0:
                    for _ in range(int(reps)):
                        line_string += char
                else:
                    line_string += char

                reps = 0
        
        # Fix last line length
        diff = self.X - len(self.PATTERN[-1])
        if diff != 0:
            for _ in range(diff):
                self.PATTERN[-1] += "b"
        
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

