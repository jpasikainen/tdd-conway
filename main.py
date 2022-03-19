import sys

class Main:
    FILE = ""
    ITERATIONS = 0

    def __init__(self, file, iterations):
        self.FILE = file
        self.ITERATIONS = iterations

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file = sys.argv.pop()
        iterations = sys.argv.pop()
        Main(file, iterations)

