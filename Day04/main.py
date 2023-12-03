def readData(fileName='input.txt'):
    with open(fileName, "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData

def part1():
    data = readData()

def part2():
    data = readData()


part1()
part2()