def readData(fileName='input.txt'):
    with open(fileName, "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData

def get_diffs(seq):
        diffs = []
        for num in range(1, len(seq)):
            previous = num - 1
            difference = int(seq[num]) - int(seq[previous])
            diffs.append(difference)

        return diffs
def determine_next_number(sequence):
    numbers = sequence.split()
    previous = 0

    current_diffs = get_diffs(numbers)
    while (current_diffs[-1] != 0):
         previous = previous + current_diffs[-1]
         current_diffs = get_diffs(current_diffs)

    next_num = int(numbers[-1]) + previous
    return next_num

def part1():
    total = 0
    data = readData('input.txt')
    for numbers in data:
        next_number = determine_next_number(numbers)
        total = next_number + total
    print(total)

def part2():
    data = readData('sample.txt')

part1()
part2()