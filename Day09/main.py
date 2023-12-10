def readData(fileName='input.txt'):
    with open(fileName, "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData


def determine_next_number(sequence):
    print (sequence)
    return 0

def part1():
    total = 0
    data = readData('sample.txt')
    for numbers in data:
        next_number = determine_next_number(numbers)

def part2():
    data = readData('sample.txt')

part1()
part2()