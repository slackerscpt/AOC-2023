def readData(fileName='input.txt'):
    with open(fileName, "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData

def determine_length(time, distance):
    way_to_win = 0
    for milliseconds in range(time):
        speed = milliseconds 
        covered_distance = (time - milliseconds) * speed
        if (covered_distance > distance):
            way_to_win += 1
        
    return way_to_win

def part1():
    data = readData('input.txt')
    time = data[0]
    distance = data[1]
    timing = time.split()
    distances = distance.split()
    timing.pop(0)
    distances.pop(0)
    total = 1

    for races in range(len(timing)):
        wins = determine_length(int(timing[races]), int(distances[races]))
        total = total * wins
    print ('Part 1 Answer: %d' %total)


def part2():
    data = readData('input.txt')
    time = data[0]
    distance = data[1]
    timing = time.split()
    distances = distance.split()
    timing.pop(0)
    distances.pop(0)
    full_timing = ''
    full_distance = ''
    for values in timing:
        full_timing = full_timing + values
    for values in distances:
        full_distance = full_distance + values

    wins = determine_length(int(full_timing), int(full_distance))
    print('Part 2 Answer: %d' %wins)

part1()
part2()