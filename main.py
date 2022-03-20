import sys
from itertools import groupby

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
        
        for _ in range(self.ITERATIONS):
            self.simulate()
        
    def get_width(self, pattern = None):
        if pattern == None:
            return self.X
        return len(pattern[0])

    def get_height(self, pattern = None):
        if pattern == None:
            return self.Y
        return len(pattern)

    def get_pattern(self):
        return self.PATTERN

    def get_neighbors(self, x, y, pattern = None):
        if pattern == None: pattern = self.PATTERN

        if x < 0 or x >= self.get_width(pattern) or y < 0 or y >= self.get_height(pattern):
            return 0
        
        count = 0
        if x-1 >= 0 and pattern[y][x-1] == "o":
            count += 1
        if x+1 < self.get_width(pattern) and pattern[y][x+1] == "o":
            count += 1
        if y-1 >= 0 and pattern[y-1][x] == "o":
            count += 1
        if y+1 < self.get_height(pattern) and pattern[y+1][x] == "o":
            count += 1

        # Diagonals
        if x-1 >= 0 and y-1 >= 0 and pattern[y-1][x-1] == "o":
            count += 1
        if x+1 < self.get_width(pattern) and y-1 >= 0 and pattern[y-1][x+1] == "o":
            count += 1
        if x-1 >= 0 and y+1 < self.get_height(pattern) and pattern[y+1][x-1] == "o":
            count += 1
        if x+1 < self.get_width(pattern) and y+1 < self.get_height(pattern) and pattern[y+1][x+1] == "o":
            count += 1
        
        return count

    def get_cell(self, x, y, pattern = None):
        if pattern == None: pattern = self.PATTERN
        if x < 0 or x >= self.get_width(pattern) or y < 0 or y >= self.get_height(pattern):
            return "b"
        
        return pattern[y][x]
    
    def simulate(self):
        self.X += 2
        self.Y += 2
        # Add frame to the pattern
        i = 0
        for row in self.PATTERN:
            self.PATTERN[i] = "b" + row + "b"
            i += 1
        empty_row = ["".join(["b" for _ in range(self.get_width())])]
        self.PATTERN = empty_row + self.PATTERN + empty_row
        original = self.PATTERN.copy()

        for y in range(self.get_height()):
            for x in range(self.get_width()):
                nbs = self.get_neighbors(x, y, original)
                if nbs < 2 or nbs > 3:
                    line = self.PATTERN[y]
                    self.PATTERN[y] = line[:x] + "b" + line[x+1:]
                    continue
                if self.get_cell(x, y, original) == "b" and nbs == 3:
                    line = self.PATTERN[y]
                    self.PATTERN[y] = line[:x] + "o" + line[x+1:]
        
       
        # Clean up frame if no changes
        if len(set(self.PATTERN[0])) == 1:
            self.PATTERN = self.PATTERN[1:]
            self.Y -= 1
        if len(set(self.PATTERN[-1])) == 1:
            self.PATTERN = self.PATTERN[:-1]
            self.Y -= 1
        if len(set([i[0] for i in self.PATTERN])) == 1:
            self.PATTERN = [i[1:] for i in self.PATTERN]
            self.X -= 1
        if len(set([i[-1] for i in self.PATTERN])) == 1:
            self.PATTERN = [i[:-1] for i in self.PATTERN]
            self.X -= 1
    
    def reformat(self):
        xyr = "x = %d, y = %d, rule = B3/S23" % (self.get_width(), self.get_height())
        pattern = ""

        for line in self.PATTERN:
            code = ["".join(v) for k, v in groupby(line)]
            for x in code:
                count = len(x)
                if count == 1:
                    pattern += x
                else:
                    pattern += "%d%s" % (count, x[0])
            pattern += "$"
        return xyr + "\n" + pattern[:-1] + "!"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        iterations = int(sys.argv.pop())
        file = sys.argv.pop()
        print(Main(file, iterations).reformat())

