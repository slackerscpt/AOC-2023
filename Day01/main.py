import re

def readData():
    #with open('sample2.txt', "r") as read_file:
    with open('input.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData

def only_numerics(seq):
    seq_type= type(seq)
    return seq_type().join(filter(seq_type.isdigit, seq))

def sub_letters_to_numbers(seq):

    letter_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    new_string = seq
    for count, num in enumerate(letter_numbers):
        str_number = str(count + 1)
        temp_string = new_string.replace(num, str_number)
        new_string = temp_string
    return new_string

def part1():
    data = readData()
    count = 0
    for line in data:
        newLine = only_numerics(line)
        #if (len(newLine)) > 1:
        newNumber = int(str(newLine[0])+ str(newLine[-1]) )
        count = count + int(newNumber)
        #else:
        #    count = count + int(newLine[0])

    print('Part 1: %d' %count)

def part2():
    data = readData()
    mappings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    new_data = [[x if (x := "".join([str(idx) for idx, val in enumerate(mappings, 1) if line[i:].startswith(val)])) else line[i] for i in range(len(line))] for line in data]
    print (sum((digits := [int(i) for i in line if i.isdigit()])[0] * 10 + digits[-1] for line in new_data))
    # print (new_data)
    # count = 0
    # for line in new_data:
    # #     newLine = sub_letters_to_numbers(line)
    #     print(line)
    #     numbers = only_numerics(line)
    #     newNumber = int(str(numbers[0])+ str(numbers[-1]) )
    #     count = count + int(newNumber)
    #     print (newNumber)

    # print('Part 2: %d' %count)

#part1()
part2()