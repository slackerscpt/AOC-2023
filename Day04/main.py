def readData(fileName='input.txt'):
    with open(fileName, "r") as read_file:
        inputData = [line.rstrip() for line in read_file]

        return inputData

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def matches_values(number):
        if number == 3:
            return 4
        elif number == 4:
            return 8
        elif number == 5:
            return 16
        elif number == 6:
            return 32
        elif number == 7:
            return 64
        elif number == 8:
            return 128
        elif number == 9:
            return 256
        elif number == 10:
            return 512
        else:
            return 0

def determine_winner(card):
    card_num, numbers = card.split(':')
    winning_side, numbers_side = numbers.split('|')
    winning_numbers = winning_side.split()
    card_numbers = numbers_side.split()
    matches = intersection(winning_numbers, card_numbers)
    if (len(matches) > 2):
        value = matches_values(len(matches))
        return value
    else:
        return len(matches)
    
def determine_winner2(numbers):
    winning_side, numbers_side = numbers.split('|')
    winning_numbers = winning_side.split()
    card_numbers = numbers_side.split()
    matches = intersection(winning_numbers, card_numbers)
    return len(matches)


def setup_each_card(cards):
    cards_played = {}
    for active_card in cards:
        if active_card in cards_played:
            previous_number = cards_played[active_card]
            cards_played[active_card] = (previous_number + 1)
        else:
            cards_played[active_card] = 1
        
        
    #need to count each card and add to total of that card. 
    #is card 1 wins 3 cards 2,3,4 will have extra
    return 0

def part1():
    data = readData('input.txt')
    total = 0
    for cards in data:
        points = determine_winner(cards)
        total = total + points
    print ('Part 1 Answer: %d' %total)


def part2():
    data = readData('sample.txt')
    card_winners = {}
    total = 0
    for cards in data:
        card_num, numbers = cards.split(':')
        card, num = card_num.split()
        points = determine_winner2(numbers)
        card_winners[num] = points
    total_cards = setup_each_card(card_winners)
    print ('Part 2 Answer: %d' %total)


part1()
part2()