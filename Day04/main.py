import re

def readData(fileName='input.txt'):
    with open(fileName, "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData

def max_number(game_data): 
    games = game_data.split(';')
    red_max = 0
    blue_max = 0
    green_max = 0
    for game in games:
        plays = game.split(',')
        for play in plays:
            number, color = play.split()
            if (color == "red"):
                if (int(number) > red_max):
                    red_max = int(number)
            elif (color == "green"):
                if (int(number) > green_max):
                    green_max  = int(number)
            elif (color == "blue"):
                if (int(number) > blue_max):
                    blue_max = int(number)


    total = (red_max * blue_max * green_max)
    return total

def split_up(game_data):
    #only 12 red cubes, 13 green cubes, and 14 blue cubes
    games = game_data.split(';')
    for game in games:
        plays = game.split(',')
        for play in plays:
            number, color = play.split()
            if (color == "red"):
                if (int(number) > 12):
                    return False
            elif (color == "green"):
                if (int(number) > 13):
                    return False
            elif (color == "blue"):
                if (int(number) > 14):
                    return False
            else:
                print ('color not found')

    return True

def determine_legit(game):
    game_number, data = game.split(':')
    letter, number = game_number.split()
    legit = split_up(data)
    #return number as int if true. 0 if false
    if (legit):
        return int(number)
    else:
        return 0
def part1():
    data = readData()
    count = 0
    for line in data:
        value = determine_legit(line)
        count = count + value
    print('Part 1 Answer: %d' %count)
def part2():
    data = readData()
    total = 0
    for lines in data:
        game_number, data = lines.split(':')
        value = max_number(data)
        total = total + value

    print('Part 2 Answer: %d' %total)


part1()
part2()