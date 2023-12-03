import re

#had to search some help online as my original mapping was not working. 

class Symbol:
    def __init__(self, symbol, adjacent):
        self.symbol = symbol
        self.adjacent = adjacent

    def __str__(self):
        return f"Symbol: {self.symbol}, adjacent: {self.adjacent}"

    def is_gear(self):
        return self.symbol == '*' and len(self.adjacent) == 2

    def gear_ratio(self):
        if not self.is_gear():
            raise SyntaxError("Can't call gear ratio on non-gears")
        return self.adjacent[0] * self.adjacent[1]

def readData():
    #with open('sample.txt', "r") as read_file:
    with open('input.txt', "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData

def find_active(data, dim=3):
    active = set()
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j].isdigit:
                active.add((i, j, *([0]*(dim-2))))
    return active

def parse_schematic(input_lines):
    schematic = list()
    for line in input_lines:
        schematic.append(list(line))

    return schematic


def extract_symbols(schematic):
    part_numbers = list()
    symbols = list()
    height = len(schematic)
    width = len(schematic[0])

    check_dirs = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1]
    ]

    for y in range(height):
        for x in range(width):
            map_char = schematic[y][x]
            match = re.match("\D", map_char)
            if map_char != '.' and match:
                # we found a character, now we have to look in all directions (including diagonal) to
                # see if there are any numbers present there
                last_start_x = 0
                last_end_x = 0
                last_check_y = 0
                adjacent_to_this_symbol = []
                for direction in check_dirs:
                    check_y = y + direction[0]
                    check_x = x + direction[1]

                    # if we're on the same y as last time, make sure we're not checking a number
                    # that's already been checked. We do this by seeing if the x we're about to check
                    # is between the last_start_x and last_end x
                    if check_y == last_check_y and last_start_x <= check_x <= last_end_x:
                        continue

                    if 0 <= check_y < height and 0 <= check_x < width:
                        check_char = schematic[check_y][check_x]
                        if re.match("\d", check_char):
                            # we found a number, now we have to look in both directions in the line to see
                            # the full number. Start backwards to find the start
                            x_start_num = check_x
                            while x_start_num > 0:
                                if re.match("\d", schematic[check_y][x_start_num - 1]):
                                    x_start_num -= 1
                                else:
                                    break
                            # we found the start, now find the end of the number
                            x_end_num = check_x
                            while x_end_num < width - 1:
                                if re.match("\d", schematic[check_y][x_end_num + 1]):
                                    x_end_num += 1
                                else:
                                    break

                            last_start_x = x_start_num
                            last_end_x = x_end_num
                            last_check_y = check_y

                            found_number = int("".join(schematic[check_y][x_start_num:x_end_num + 1]))

                            part_numbers.append(found_number)
                            adjacent_to_this_symbol.append(found_number)

                symbol = Symbol(match.group(0), adjacent_to_this_symbol)
                symbols.append(symbol)

    return symbols

def find_part_numbers(schematic):
    symbols = extract_symbols(schematic)
    part_numbers = []
    for symbol in symbols:
        part_numbers.extend(symbol.adjacent)

    return part_numbers


def part1():
    data = readData()
    schematic = parse_schematic(data)
    part_numbers = find_part_numbers(schematic)
    answer = sum(part_numbers)
    print('Part 1 Answer: %d' %answer)

def part2():

    data = readData()
    schematic = parse_schematic(data)
    symbols = extract_symbols(schematic)
    gears = [symbol for symbol in symbols if symbol.is_gear()]
    part_2_answer = sum(gear.gear_ratio() for gear in gears)
    print('Part 2 Answer: %d' %part_2_answer)
    

part1()
part2()
