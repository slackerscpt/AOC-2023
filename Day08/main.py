def readData(fileName='input.txt'):
    with open(fileName, "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData

def map_list(list):
    steps = dict()
    for step in list:
        
        step_value, LR_value = step.split(' = ')
        left_temp, right_temp = LR_value.split(', ')
        left = left_temp.replace('(', '')
        right = right_temp.replace(')', '')
        steps[step_value] = dict([
            ('L', left), 
            ('R', right) 
        ]);

    return steps
        
def take_steps(instructions, step_map):
    count = 0
    current_step ='AAA'
    # for step in instructions:
    #     landed = step_map[current_step][step]
    #     current_step = landed
    #     count +=1
    #     print (current_step)
    #     if (current_step) == 'ZZZ':
    #         return count
    #If we get here we didn't hit ZZZ
    #It goes RL until found
    while( current_step != 'ZZZ'):
        for step in instructions:
            count +=1
            current_step = step_map[current_step][step]
            # print (landed)
            # current_step = landed
        
        #count +=1
        #current_step = step_map[current_step]['R']
        # print (landed)
        #count +=1
        # current_step = landed
        #current_step = step_map[current_step]['L']
        # print (landed)
        # count +=1
        # current_step = landed


    print('Missing')
    return count

def part1():
    data = readData('input.txt')
    instructions = data.pop(0)
    data.pop(0) #remove blank line
    step_map = map_list(data)
    steps_taken = take_steps(instructions, step_map)
    print('Answer Part1: %s' %steps_taken)

def part2():
    data = readData('sample.txt')

part1()
part2()